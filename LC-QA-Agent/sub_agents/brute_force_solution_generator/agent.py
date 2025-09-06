import os
import sys
import io
import traceback
import subprocess
import tempfile
from typing import Optional, List, Tuple

from google.adk.agents import LlmAgent
from ...utils.logging_utils import log_message
from google.adk.code_executors import BaseCodeExecutor
from google.adk.code_executors.code_execution_utils import (
    CodeExecutionInput,
    CodeExecutionResult,
)
from google.adk.agents.invocation_context import InvocationContext


class CodeExecutor(BaseCodeExecutor):
    code_block_delimiters: List[Tuple[str, str]] = [
        ("```python\n", "\n```"),
        ("```tool_code\n", "\n```"),
        ("```java\n", "\n```"),
        ("```cpp\n", "\n```"),
        ("```javascript\n", "\n```"),
    ]

    def _extract_code_and_lang(self, raw_code: str) -> Tuple[str, str]:
        """Extract code snippet and detect language."""
        for start, end in self.code_block_delimiters:
            if raw_code.startswith(start) and raw_code.endswith(end):
                lang = start.strip("`\n")
                lang = lang.replace("```", "").strip()
                return raw_code[len(start):-len(end)], lang
        return raw_code.strip(), "python"  # default fallback

    def _run_subprocess(self, cmd: List[str], input_file: Optional[str] = None) -> Tuple[str, str, bool]:
        """Run subprocess command and capture output."""
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                cwd=tempfile.gettempdir(),
                timeout=10,
            )
            return result.stdout.strip(), result.stderr.strip(), result.returncode == 0
        except Exception as e:
            return "", str(e), False

    def execute_code(
        self,
        invocation_context: InvocationContext,
        code_execution_input: CodeExecutionInput,
    ) -> CodeExecutionResult:
        """Executes code in Python/Java/C++/JS and captures output/errors."""

        raw_code = code_execution_input.code
        code, lang = self._extract_code_and_lang(raw_code)

        stdout, stderr, success = "", "", True

        if lang == "python":
            # Run inline Python code
            stdout_capture = io.StringIO()
            stderr_capture = io.StringIO()
            original_stdout, original_stderr = sys.stdout, sys.stderr
            sys.stdout, sys.stderr = stdout_capture, stderr_capture

            try:
                exec_globals, exec_locals = {}, {}
                exec(code, exec_globals, exec_locals)
            except Exception:
                success = False
                stderr = traceback.format_exc()
            finally:
                sys.stdout, sys.stderr = original_stdout, original_stderr
                stdout = stdout_capture.getvalue().strip()
                if not stderr:
                    stderr = stderr_capture.getvalue().strip()

        elif lang == "java":
            with tempfile.TemporaryDirectory() as tmpdir:
                file_path = os.path.join(tmpdir, "Main.java")
                with open(file_path, "w") as f:
                    f.write(code)

                # Compile
                _, compile_err, ok = self._run_subprocess(["javac", file_path])
                if not ok:
                    return CodeExecutionResult(False, "", compile_err)

                # Run
                stdout, stderr, success = self._run_subprocess(
                    ["java", "-cp", tmpdir, "Main"]
                )

        elif lang == "cpp":
            with tempfile.TemporaryDirectory() as tmpdir:
                file_path = os.path.join(tmpdir, "main.cpp")
                exe_path = os.path.join(tmpdir, "main.exe" if os.name == "nt" else "main")
                with open(file_path, "w") as f:
                    f.write(code)

                # Compile
                _, compile_err, ok = self._run_subprocess(["g++", file_path, "-o", exe_path])
                if not ok:
                    return CodeExecutionResult(False, "", compile_err)

                # Run
                stdout, stderr, success = self._run_subprocess([exe_path])

        elif lang == "javascript":
            with tempfile.NamedTemporaryFile(delete=False, suffix=".js", mode="w") as f:
                file_path = f.name
                f.write(code)

            stdout, stderr, success = self._run_subprocess(["node", file_path])
            os.remove(file_path)

        else:
            return CodeExecutionResult(
                success=False,
                output="",
                error=f"Unsupported language: {lang}",
            )

        return CodeExecutionResult(
            success=success,
            output=stdout,
            error=stderr or None,
        )


# Agent definition
brute_force_solution_generator_agent = LlmAgent(
    name="brute_force_solution_generator_agent",
    model=os.getenv("MODEL_NAME"),
    description="Generates and validates brute force solutions for LeetCode problems",
    instruction="""Generate brute force solution. 
    Format:
    **Heading** Brute Force Solution
- **Approach**: [strategy]
- **Code**:```[lang]
[code]```
- **Topic**: [topic]
- **Time**: O([n])
- **Space**: O([n])
- **Results**: [pass/fail]
Include test results.""",
    after_agent_callback=log_message,
)

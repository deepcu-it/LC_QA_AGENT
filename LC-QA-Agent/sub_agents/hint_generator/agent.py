
from google.adk.agents import LlmAgent
from ...utils.logging_utils import log_message
import os

hint_generator_agent = LlmAgent(
    name="hint_generator_agent",
    model=os.getenv("MODEL_NAME"),
    description="Generate strategic hints for problem-solving approach.",
    instruction="""Generate 3 strategic hints for solving the LeetCode problem.

Focus on problem-solving approach, not programming syntax.

Output format (bullet points only):
    **Heading**: Hints for [Problem Title]
- **Hint 1**: [Strategic approach hint]
- **Hint 2**: [Data structure or algorithm hint]  
- **Hint 3**: [Edge case or optimization hint]

Keep hints concise and actionable.""",
    after_agent_callback=log_message
)
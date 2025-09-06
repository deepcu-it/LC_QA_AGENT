from google.adk.agents import LlmAgent
import os
from ...utils.logging_utils import TestCaseLogger

class TestCaseCheckerAgent:
    def __init__(self):
        self.logger = TestCaseLogger()
        self.agent = LlmAgent(
            name="test_case_checker_agent",
            model=os.getenv("MODEL_NAME"),
            description="Validate any solution against test cases using pass@k.",
            instruction="""Validate the provided solution against test cases.

Output format (bullet points only):
• **Solution Validation**:
  - Test Case 1: ✅/❌ [Input: X, Expected: Y, Got: Z]
  - Test Case 2: ✅/❌ [Input: X, Expected: Y, Got: Z]
  - Test Case 3: ✅/❌ [Input: X, Expected: Y, Got: Z]
  - Test Case 4: ✅/❌ [Input: X, Expected: Y, Got: Z]
  - Test Case 5: ✅/❌ [Input: X, Expected: Y, Got: Z]
• **Pass@K Score**: [X/5] test cases passed
• **Status**: [PASS/FAIL]
• **Issues**: [List any failed test cases and reasons]
• **Performance Notes**: [Any observations about solution efficiency]

Show individual test case results with input/output comparison.""",
        )

    def validate_solution(self, question_id, solution_code, test_cases):
        # Execute test cases and get results
        test_results = self.agent.execute(solution_code=solution_code, test_cases=test_cases)
        
        # Log the results
        self.logger.create_log_entry(
            question_id=question_id,
            test_results=test_results,
            solution_code=solution_code
        )
        
        return test_results
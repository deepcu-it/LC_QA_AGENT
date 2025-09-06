from google.adk.agents import LlmAgent
from ...utils.logging_utils import log_message
import os

test_case_generater_agent = LlmAgent(
    name="test_case_generator_agent",
    model=os.getenv("MODEL_NAME"),
    description="Generate comprehensive test cases for LeetCode problem validation.",
    instruction="""Generate 5 diverse test cases covering edge cases and constraints.

Output format (bullet points only):
+    **Heading**: Test Cases for [Problem Title]
- **Test Case 1**: 
  - Input: [input values]
  - Expected Output: [expected result]
- **Test Case 2**: 
  - Input: [input values]
  - Expected Output: [expected result]
- **Test Case 3**: 
  - Input: [input values]
  - Expected Output: [expected result]
- **Test Case 4**: 
  - Input: [input values]
  - Expected Output: [expected result]
- **Test Case 5**: 
  - Input: [input values]
  - Expected Output: [expected result]

Include edge cases like empty inputs, single elements, and boundary values.""",
    output_key="test_cases",
    after_agent_callback=log_message
)
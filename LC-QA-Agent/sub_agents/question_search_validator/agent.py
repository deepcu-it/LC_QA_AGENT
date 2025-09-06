from google.adk.agents import LlmAgent
from ...utils.logging_utils import log_message
import os


question_search_validator_agent = LlmAgent(
    name="question_search_validator_agent",
    model=os.getenv("MODEL_NAME"),
    description="Search and validate LeetCode question number or title.",
    instruction="""Search Google for the LeetCode question and validate it exists.

Output format (bullet points only):
- **Question Found**: [Yes/No]
- **Question Title**: [Title if found]
- **Question Description**: [Brief description if found]
- **Difficulty**: [Easy/Medium/Hard if found]
- **Error**: [Error message if not found]

Keep response concise and structured as bullet points.""",
    output_key="question",
    after_agent_callback=log_message
)
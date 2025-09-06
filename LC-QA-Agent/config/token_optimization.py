"""
Token optimization configuration for LC-QA Agent.

This module contains configurations to minimize token usage while maintaining
functionality and readability.
"""

# Agent instruction templates optimized for minimal token usage
AGENT_INSTRUCTIONS = {
    "question_validator": """Search Google for LeetCode question and validate existence.

Output (bullet points only):
• **Question Found**: [Yes/No]
• **Question Title**: [Title if found]
• **Question Description**: [Brief description if found]
• **Difficulty**: [Easy/Medium/Hard if found]
• **Error**: [Error message if not found]

Keep response concise and structured as bullet points.""",

    "hint_generator": """Generate 3 strategic hints for solving the LeetCode problem.

Focus on problem-solving approach, not programming syntax.

Output (bullet points only):
• **Hint 1**: [Strategic approach hint]
• **Hint 2**: [Data structure or algorithm hint]  
• **Hint 3**: [Edge case or optimization hint]

Keep hints concise and actionable.""",

    "test_case_generator": """Generate 5 diverse test cases covering edge cases and constraints.

Output (bullet points only):
• **Test Case 1**: 
  - Input: [input values]
  - Expected Output: [expected result]
• **Test Case 2**: 
  - Input: [input values]
  - Expected Output: [expected result]
• **Test Case 3**: 
  - Input: [input values]
  - Expected Output: [expected result]
• **Test Case 4**: 
  - Input: [input values]
  - Expected Output: [expected result]
• **Test Case 5**: 
  - Input: [input values]
  - Expected Output: [expected result]

Include edge cases like empty inputs, single elements, and boundary values.""",

    "syntax_checker": """Analyze the provided code for syntax errors and potential issues.

Output (bullet points only):
• **Syntax Status**: [VALID/INVALID]
• **Language**: [Detected programming language]
• **Error Analysis**:
  - Line X: [Error description if any]
  - Line Y: [Warning description if any]
• **Code Quality**:
  - Indentation: ✅/❌
  - Brackets/Parentheses: ✅/❌
  - Semicolons: ✅/❌ (if applicable)
  - Variable Declaration: ✅/❌
• **Recommendations**: [Suggestions for fixing issues]

Provide detailed syntax analysis with specific line numbers and error descriptions.""",

    "solution_generator": """Generate a solution for the LeetCode problem.

If no language specified, ask user for preferred language (Python, Java, C++, etc.).

Output (bullet points only):
• **Solution Approach**: [Brief explanation of strategy]
• **Code**:
```[language]
[complete solution code]
```
• **Topic**: [Algorithm/data structure topic]
• **Time Complexity**: O([complexity])
• **Space Complexity**: O([complexity])
• **Pass@K Results**:
  - Test Case 1: ✅/❌
  - Test Case 2: ✅/❌
  - Test Case 3: ✅/❌
  - Test Case 4: ✅/❌
  - Test Case 5: ✅/❌
• **Pass Rate**: [X/5] test cases passed

Validate solution against provided test cases and show individual results.""",

    "test_case_checker": """Validate the solution against provided test cases.

Output (bullet points only):
• **Solution Validation**:
  - Test Case 1: ✅/❌ [Input: X, Expected: Y, Got: Z]
  - Test Case 2: ✅/❌ [Input: X, Expected: Y, Got: Z]
  - Test Case 3: ✅/❌ [Input: X, Expected: Y, Got: Z]
  - Test Case 4: ✅/❌ [Input: X, Expected: Y, Got: Z]
  - Test Case 5: ✅/❌ [Input: X, Expected: Y, Got: Z]
• **Pass@K Score**: [X/5] test cases passed
• **Status**: [PASS/FAIL]
• **Issues**: [List any failed test cases and reasons]

Show individual test case results with input/output comparison."""
}

# Token usage optimization settings
TOKEN_OPTIMIZATION = {
    "max_instruction_length": 500,  # Maximum characters for agent instructions
    "use_abbreviations": True,      # Use abbreviations where appropriate
    "minimize_examples": True,      # Minimize example usage in instructions
    "bullet_point_format": True,    # Enforce bullet point format
    "remove_redundancy": True,      # Remove redundant text
}

# Pass@K configuration
PASS_AT_K_CONFIG = {
    "default_k": 5,                 # Default number of test cases to consider
    "show_individual_results": True, # Show individual test case results
    "calculate_pass_rate": True,    # Calculate and display pass rate
    "use_visual_indicators": True,  # Use ✅/❌ for visual clarity
}

# Output formatting for Google embedded chatbot
CHATBOT_FORMATTING = {
    "use_bullet_points": True,      # Use bullet points for all outputs
    "use_emojis": True,            # Use emojis for visual appeal
    "max_line_length": 80,         # Maximum line length for readability
    "indent_sub_items": True,      # Indent sub-items in bullet lists
    "use_code_blocks": True,       # Use code blocks for code snippets
}

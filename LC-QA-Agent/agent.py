import os
from dotenv import load_dotenv
load_dotenv()

from google.adk.agents import SequentialAgent
from .sub_agents.question_search_validator.agent import question_search_validator_agent
from .sub_agents.hint_generator.agent import hint_generator_agent
from .sub_agents.test_case_generater.agent import test_case_generater_agent
from .sub_agents.brute_force_solution_generator.agent import brute_force_solution_generator_agent
from .sub_agents.solution_optimizer.agent import solution_optimizer_agent
from .utils.logging_utils import log_message


root_agent = SequentialAgent(
    name="leetcode_flow_agent",
    sub_agents=[
        question_search_validator_agent,
        hint_generator_agent,
        test_case_generater_agent,
        brute_force_solution_generator_agent,
        solution_optimizer_agent
    ],
    after_agent_callback=log_message
)
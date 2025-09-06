import os
from datetime import datetime
from google.adk.agents.callback_context import CallbackContext
from google.genai import types
from typing import Optional

def log_message(callback_context: CallbackContext,log_dir: str="logs") -> Optional[types.Content]:
    """
    Logs a message to a file named with the current date and timestamp.
    Args:
        message (str): The message to log.
        log_dir (str): Directory where log files are stored.
    """
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    log_filename = f"{timestamp}.log"
    log_path = os.path.join(log_dir, log_filename)
    agent_name = callback_context.agent_name
    invocation_id = callback_context.invocation_id
    message = f"{agent_name} Completed task with invocation ID {invocation_id}."
    file_path = os.getcwd() + "/" + log_path
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(f"{datetime.now().isoformat()} - {message}\n")
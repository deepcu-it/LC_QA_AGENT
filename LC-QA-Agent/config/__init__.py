"""
Configuration module for Universal Programming Q&A Agent.

This module exports model configurations and environment variable settings.
"""

from .model_config import (
    AGENT_MODELS,
    MODEL_CONFIG,
    get_model_name,
    get_alternative_model,
    get_default_k,
    get_max_instruction_length
)

__all__ = [
    "AGENT_MODELS",
    "MODEL_CONFIG", 
    "get_model_name",
    "get_alternative_model",
    "get_default_k",
    "get_max_instruction_length"
]

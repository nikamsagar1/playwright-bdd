# tests/test_runner.py

from pytest_bdd import scenarios

# -----------------------------
# Import all step definitions
# -----------------------------
# This ensures that pytest-bdd can find all step implementations
from step_definitions.test_add_user_steps import *  # noqa: F401, F403

# -----------------------------
# Load all scenarios from the feature file(s)
# -----------------------------
# You can add more feature files as needed
scenarios("../features/add_user.feature")

# agents/error_agent.py
from crewai import Agent
from llm import get_llm

error_agent = Agent(
    role="System Monitor (Mid-Level Agent)",
    goal="Detect errors, log them, and trigger fallbacks or recoveries.",
    backstory="You monitor the system for API failures, invalid data, or ethical issues in medical queries, providing logs and suggesting alternatives.",
    llm=get_llm(),
    tools=[],  # Could add a logging tool later
    verbose=True,
    memory=True,
)
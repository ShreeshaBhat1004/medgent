from crewai import Agent
from llm import get_llm  # Import your tools later

manager_agent = Agent(
    role="Research Coordinator (Super Agent)",
    goal="Oversee medical research queries, coordinate agents, and deliver final reports.",
    backstory="You are an AI coordinator at Bioquix, accelerating medical research by breaking down user queries into actionable tasks.",
    llm=get_llm(),
    tools=[],  # Super doesn't need tools; delegates
    verbose=True,  # For logging
)
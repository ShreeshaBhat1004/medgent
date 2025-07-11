# agents/intent_agent.py
from crewai import Agent
from llm import get_llm

intent_agent = Agent(
    role="Intent Interpreter (Mid-Level Agent)",
    goal="Parse user requests, map to task agents, and handle ambiguity by clarifying.",
    backstory="You specialize in understanding natural language queries in medical research contexts, routing them to appropriate task agents like literature retrieval or drug info.",
    llm=get_llm(),
    tools=[],  # Uses LLM for intent
    verbose=True,
    memory=True,
)
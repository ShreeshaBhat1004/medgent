# main.py
from crewai import Crew, Process, Task
from agents.manager_agent import super_agent
from agents.intent_agent import intent_agent
from agents.error_agent import error_agent
from agents.task_agents import literature_agent, drug_agent, translation_agent, summarization_agent

# Define Tasks (hierarchical flow: Super -> Intent/Error -> Tasks)
super_task = Task(
    description="Coordinate the user query: {user_query}. Delegate to intent and monitor for errors.",
    expected_output="Final coordinated response with disclaimer.",
    agent=super_agent,
)

intent_task = Task(
    description="Analyze intent of {user_query} and route to appropriate task agents.",
    expected_output="Routed tasks and sub-queries.",
    agent=intent_agent,
)

error_task = Task(
    description="Monitor for errors in the process and handle recoveries.",
    expected_output="Error logs and fallbacks if needed.",
    agent=error_agent,
)

# Task-specific tasks (these will be triggered based on intent)
literature_task = Task(
    description="Fetch literature for sub-query: {sub_query}",
    expected_output="Literature summaries.",
    agent=literature_agent,
)

drug_task = Task(
    description="Get drug info for: {sub_query}",
    expected_output="Drug details.",
    agent=drug_agent,
)

translation_task = Task(
    description="Translate: {sub_query}",
    expected_output="Translated text.",
    agent=translation_agent,
)

summarization_task = Task(
    description="Summarize: {sub_query}",
    expected_output="Summary.",
    agent=summarization_agent,
)

# Create Crew
crew = Crew(
    agents=[super_agent, intent_agent, error_agent, literature_agent, drug_agent, translation_agent, summarization_agent],
    tasks=[super_task, intent_task, error_task],  # Core tasks; others dynamically called
    process=Process.hierarchical,  # Hierarchical coordination
    verbose=2,  # Detailed logging
    memory=True,  # Shared memory
)

# Example run
if __name__ == "__main__":
    user_query = input("Enter your medical research query: ")
    result = crew.kickoff(inputs={"user_query": user_query, "sub_query": user_query})  # Simplify for demo
    print(result)
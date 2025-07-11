# app.py - Simple Streamlit Interface for the Multi-Agent System
import streamlit as st
from crewai import Crew, Process, Task
from agents.manager_agent import manager_agent
from agents.intent_agent import intent_agent
from agents.error_agent import error_agent
from agents.task_agents import literature_agent, drug_agent, translation_agent, summarization_agent
from llm import get_llm

# Define Tasks (same as main.py)
super_task = Task(
    description="Coordinate the user query: {user_query}. Delegate to intent and monitor for errors.",
    expected_output="Final coordinated response with disclaimer.",
    agent=manager_agent,
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
    agents=[manager_agent, intent_agent, error_agent, literature_agent, drug_agent, translation_agent, summarization_agent],
    tasks=[super_task, intent_task, error_task],
    process=Process.hierarchical,
    verbose=True,
    memory=False,
    manager_llm = get_llm(),
)

# Streamlit UI
st.title("Medgent Multi-Agent Medical Research Assistant")

user_query = st.text_input("Enter your medical research query:", placeholder="e.g., Summarize recent studies on Alzheimer's treatments")

if st.button("Process Query"):
    if user_query:
        with st.spinner("Processing..."):
            try:
                result = crew.kickoff(inputs={"user_query": user_query, "sub_query": user_query})
                st.success("Query Processed!")
                st.markdown("### Result:")
                st.write(result)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a query.")

# Optional: Display logs or additional info
if st.checkbox("Show System Logs"):
    # You can add logging capture here if needed, but for simplicity, rely on verbose output in console
    st.info("Check console for detailed logs.")

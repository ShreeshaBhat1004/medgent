# agents/task_agents.py (updated imports and instances)
from crewai import Agent
from llm import get_llm
from tools.pubmed_tool import PubMedSearchTool
from tools.pubchem_tool import PubChemInfoTool
from tools.translation_tool import TranslationTool
from tools.summarization_tool import SummarizationTool

# Literature Retrieval Agent
literature_agent = Agent(
    role="Literature Retrieval Agent (Task Agent)",
    goal="Fetch medical literature abstracts from PubMed.",
    backstory="You query PubMed for research papers and return relevant summaries.",
    llm=get_llm(),
    tools=[PubMedSearchTool()],
    verbose=True,
    memory=True,
)

# Drug Information Agent
drug_agent = Agent(
    role="Drug Information Agent (Task Agent)",
    goal="Retrieve drug details and properties from PubChem.",
    backstory="You fetch information on compounds, including names, properties, and basic interactions.",
    llm=get_llm(),
    tools=[PubChemInfoTool()],
    verbose=True,
    memory=True,
)

# Translation Agent
translation_agent = Agent(
    role="Translation Agent (Task Agent)",
    goal="Translate medical texts between languages.",
    backstory="You handle translations for global research accessibility, focusing on accuracy in medical terms.",
    llm=get_llm(),
    tools=[TranslationTool()],
    verbose=True,
    memory=True,
)

# Summarization Agent
summarization_agent = Agent(
    role="Summarization Agent (Task Agent)",
    goal="Condense medical content into key points.",
    backstory="You summarize research papers, highlighting findings, methods, and conclusions.",
    llm=get_llm(),
    tools=[SummarizationTool()],
    verbose=True,
    memory=True,
)
# MedGent: Multi-Agent AI System for Medical Research

## Overview

MedGent is a hierarchical multi-agent AI orchestration system designed to accelerate medical research. It demonstrates a three-level agent architecture for processing natural language queries related to medical literature, drug information, translation, and summarization. The system integrates with APIs like PubMed and PubChem, uses Groq for fast LLM inference, and features a Streamlit-based web interface for user interaction.

Key highlights:
- **Hierarchical Structure**: Super Agent (coordinator), Mid-Level Agents (intent analysis and error monitoring), Task Agents (specific operations).
- **Medical Focus**: Tailored for tasks like fetching research papers, drug details, and ethical handling with disclaimers.
- **Expansions**: Includes memory for context retention, guardrails for ethics, and robust error handling.

This project showcases multi-agent design skills, aligning with Bioquix's mission to speed up medical advancements.

## Features

- **Natural Language Query Processing**: Interpret user requests (e.g., "Summarize recent Alzheimer's studies") and route to appropriate agents.
- **API Integrations**:
  - PubMed for literature retrieval.
  - PubChem for drug properties.
  - LLM-based translation and summarization.
- **Error Handling**: Dedicated agent for logging, retries, and fallbacks (e.g., mock data on API failure).
- **Guardrails**: Ethical disclaimers (e.g., "Not medical advice") to prevent misuse.
- **Memory and Goal Management**: Retains session context for multi-step queries.
- **User Interface**: Streamlit app for easy querying and result display.
- **Demo Queries**:
  - Literature: "Summarize recent studies on Alzheimer's treatments."
  - Drug Info: "What is the molecular formula of ibuprofen?"
  - Translation: "Translate this abstract to Spanish: [text]."
  - Complex: "Fetch diabetes papers and summarize in French."

## Architecture

The system follows a three-level hierarchy:

1. **Level 1: Super Agent** - Oversees coordination, delegates tasks, and compiles responses.
2. **Level 2: Mid-Level Agents**
   - Intent Analysis Agent: Parses queries and routes to tasks.
   - Error Monitoring Agent: Tracks issues and handles recoveries.
3. **Level 3: Task Agents**
   - Literature Retrieval (PubMed).
   - Drug Information (PubChem).
   - Translation (LLM).
   - Summarization (LLM).

Communication uses CrewAI's protocols for agent-to-agent messaging. Shared memory ensures context persistence.

## Requirements

- Python 3.10+
- Dependencies
  - crewai
  - langchain
  - langchain_groq
  - streamlit
  - requests
  - python-dotenv.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/shreeshabhat1004/medgent.git
   cd medgent
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   # Or on Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables in `.env`:
   ```
   GROQ_API_KEY=your_groq_api_key_here  # Get from https://console.groq.com
   NCBI_API_KEY=your_ncbi_api_key_here  # Optional for PubMed/PubChem rate limits; from https://account.ncbi.nlm.nih.gov/
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```
   - Open the provided URL (e.g., http://localhost:8501) in your browser.
   - Enter a medical research query and click "Process Query".
   - View results, with options to show logs.

2. Alternatively, run via console (main.py):
   ```
   python main.py
   ```
   - Input queries when prompted.

For testing errors: Simulate API failures by modifying tool URLs temporarily.

## Development and Expansion

- **Code Structure**:
  - `agents/`: Agent definitions (super, intent, error, tasks).
  - `tools/`: API wrappers (PubMed, PubChem, etc.).
  - `utils/`: LLM setup.
  - `app.py`: Streamlit UI.
  - `main.py`: Console entry point.

- **To Expand**:
  - Add more Task Agents (e.g., Hypothesis Generator using ML).
  - Integrate additional APIs (e.g., NIH for images).
  - Enhance guardrails for HIPAA compliance.

- **Notes**:
  - Uses free-tier APIs; monitor quotas.
  - AI assistance (e.g., Grok) was used for development, as encouraged in the assignment.
  - For production, add authentication and scaling.


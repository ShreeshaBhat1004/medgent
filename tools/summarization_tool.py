# tools/summarization_tool.py
from crewai.tools import BaseTool
from llm import get_llm

class SummarizationTool(BaseTool):
    name: str = "SummarizeMedicalContent"
    description: str = "Summarizes medical texts or research."

    def _run(self, content: str):
        llm = get_llm()
        prompt = f"Summarize this medical content, highlighting key findings, methods, and conclusions: {content}"
        try:
            response = llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Error: {str(e)}"
# tools/translation_tool.py
from crewai.tools import BaseTool
from llm import get_llm

class TranslationTool(BaseTool):
    name: str = "TranslateMedicalText"
    description: str = "Translates medical text to a specified language."

    def _run(self, text: str, target_language: str = "Spanish"):
        llm = get_llm()
        prompt = f"Translate this medical text to {target_language}: {text}"
        try:
            response = llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Error: {str(e)}"
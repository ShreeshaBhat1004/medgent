# llm.py (remove the model_config line)
import os
from dotenv import load_dotenv
from langchain_litellm import ChatLiteLLM  # Assuming you migrated as per previous guidance

load_dotenv()

def get_llm(model="groq/llama3-8b-8192"):
    return ChatLiteLLM(
        model=model,
        temperature=0.7,
    )

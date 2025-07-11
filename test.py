# Test script: test_llm.py
from llm import get_llm

llm = get_llm()
response = llm.invoke("Hello, world!")
print(response.content if response else "Empty response")

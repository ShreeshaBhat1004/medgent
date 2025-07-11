# tools/pubmed_tool.py
from crewai.tools import BaseTool
import requests
import os
from dotenv import load_dotenv

load_dotenv()
NCBI_API_KEY = os.getenv("NCBI_API_KEY")

class PubMedSearchTool(BaseTool):
    name: str = "PubMedSearch"
    description: str = "Searches PubMed for medical literature summaries."

    def _run(self, query: str):
        try:
            # ESearch to get IDs
            esearch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
            esearch_params = {
                "db": "pubmed",
                "term": query.replace(" ", "+"),
                "retmax": 5,
                "retmode": "json",
                "api_key": NCBI_API_KEY,
            }
            response = requests.get(esearch_url, params=esearch_params)
            response.raise_for_status()
            data = response.json()
            pmids = data["esearchresult"]["idlist"]

            if not pmids:
                return "No results found."

            # ESummary to get summaries
            esummary_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
            esummary_params = {
                "db": "pubmed",
                "id": ",".join(pmids),
                "retmode": "json",
                "api_key": NCBI_API_KEY,
            }
            summary_response = requests.get(esummary_url, params=esummary_params)
            summary_response.raise_for_status()
            summaries = summary_response.json()["result"]

            results = []
            for pmid in pmids:
                if pmid in summaries:
                    doc = summaries[pmid]
                    results.append({
                        "title": doc.get("title", "N/A"),
                        "authors": ", ".join([author["name"] for author in doc.get("authors", [])]),
                        "pubdate": doc.get("pubdate", "N/A"),
                        "source": doc.get("source", "N/A"),
                    })

            return results
        except Exception as e:
            return f"Error: {str(e)} - Fallback to mock data or retry."
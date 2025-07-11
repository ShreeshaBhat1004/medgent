# tools/pubchem_tool.py
from crewai.tools import BaseTool
import requests

class PubChemInfoTool(BaseTool):
    name: str = "PubChemInfo"
    description: str = "Fetches drug compound information from PubChem."

    def _run(self, drug_name: str):
        try:
            # Get CID
            cid_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{drug_name}/cids/JSON"
            cid_response = requests.get(cid_url)
            cid_response.raise_for_status()
            cids = cid_response.json().get("IdentifierList", {}).get("CID", [])
            if not cids:
                return "No compound found."

            cid = cids[0]

            # Get properties
            prop_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/property/IUPACName,MolecularFormula,MolecularWeight/JSON"
            prop_response = requests.get(prop_url)
            prop_response.raise_for_status()
            props = prop_response.json()["PropertyTable"]["Properties"][0]

            # Note: PubChem doesn't have direct interactions; suggest basic info
            return {
                "IUPACName": props.get("IUPACName", "N/A"),
                "MolecularFormula": props.get("MolecularFormula", "N/A"),
                "MolecularWeight": props.get("MolecularWeight", "N/A"),
                "Note": "For interactions, consult reliable sources like DrugBank."
            }
        except Exception as e:
            return f"Error: {str(e)} - Fallback to mock data."
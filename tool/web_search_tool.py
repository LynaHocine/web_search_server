import os
from serpapi import GoogleSearch
from dotenv import load_dotenv

# Load variables from .env into environment
load_dotenv()

def web_search_tool(query) -> dict:
    """It takes the user query (text) as input.
    Outputs result of the search 
    """

    q = query.strip()
    if not q: 
        return {"query": q, "result": "The query is empty"}
    
    api_key = os.getenv("SERPAPI_KEY")

    if not api_key:
        return {"query": q, "result": "SerpAPI key not configured."}
    
    params = {
        "engine": "google",
        "q": q,
        "api_key": api_key,
        "num": 1
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()
    except Exception as e:
        return {"query": q, "result": f"Request failed: {str(e)}"}
    
    organic_results = results.get("organic_results")

    if not organic_results: 
        return {"query":q, "result": "No results found"}
    
    top = organic_results[0]

    title = top.get("title", "No title")
    snippet = top.get("snippet", "no snippet")

    result = f"{title}\n{snippet}"


    return {"query":q, "result":result}
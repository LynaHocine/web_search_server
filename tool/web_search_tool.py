import requests
from bs4 import BeautifulSoup
import urllib.parse

def web_search_tool(query) -> dict:
    """It takes the user query (text) as input.
    Outputs result of the search 
    """

    q = query.strip()
    if not q: 
        return {"query": q, "result": "The query is empty"}
    
    #web tool does search with DuckDuckGo

    encoded_q = urllib.parse.quote(q)
    url = f"https://html.duckduckgo.com/html/?q={encoded_q}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status()
    except Exception as e:
        return {"query": q, "result": f"Request failed: {str(e)}"}
    
    #extract the data from the html
    soup = BeautifulSoup(res.text, "html.parser")

    #get the top result 
    results = soup.find_all("a", class_="result__a")

    if not results: 
        return {"query":q, "result": "No results found (possibly blocked)"}
    
    top = results[0].get_text()
    title = (top.find("a", class_="result__a")).get_text()

    snippet_tag = top.find_next("a", class_="result__snippet") or top.find("div", class_="result__snippet")
    snippet = snippet_tag.get_text() if snippet_tag else "No snippet available"

    result = f"{title}\n{snippet}"


    return {"query":q, "result":result}
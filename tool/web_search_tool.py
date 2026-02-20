def web_search_tool(query):
    """It takes the user query (text) as input.
    Outputs result of the search 
    """

    q = query.strip()
    if not q: 
        return {"query": q, "result": "The query is empty"}
    else: 
        result = "web search"

        return {"query":q, "result":result}
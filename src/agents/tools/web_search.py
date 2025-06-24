from typing import List

def web_search(query: str, k: int = 3) -> List[str]:
    # Placeholder for a real tool (SerpAPI/Tavily/etc.)
    return [f"Result {i+1} for '{query}'" for i in range(k)]

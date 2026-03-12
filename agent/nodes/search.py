from tavily import TavilyClient
from agent.state import ResearchState

tavily = TavilyClient(api_key="")

def search_node(state: ResearchState):
    all_results = []
    
    for question in state['sub_questions']:
        results = tavily.search(question, max_results=3)
        all_results.extend(results['results'])
    
    return {"search_results": all_results}
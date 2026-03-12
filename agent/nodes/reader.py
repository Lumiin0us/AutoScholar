import httpx
from bs4 import BeautifulSoup
from agent.state import ResearchState

def reader_node(state: ResearchState):
    scraped = []
    
    for result in state['search_results'][:3]:  # top 3 only
        try:
            response = httpx.get(result['url'], timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            text = ' '.join(p.text for p in soup.find_all('p'))
            scraped.append(text[:2000])  
        except:
            continue
    
    return {"scraped_content": scraped}
from agent.state import ResearchState
from agent.config import llm

def synthesizer_node(state: ResearchState):
    content = "\n\n".join(state['scraped_content'])
    prompt = f"""
    You are a research analyst. Using the content below,
    write a comprehensive structured report on:
    
    Topic: {state['topic']}
    
    Content: {content}
    
    Format: Introduction, Key Findings, Conclusion, Sources
    """
    response = llm.invoke(prompt)
    return {"report": response.content}
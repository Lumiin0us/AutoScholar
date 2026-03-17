from agent.state import ResearchState
from agent.config import llm

def reflection_node(state: ResearchState):
    prompt = f"""
    Original question: {state['topic']}
    
    Generated report: {state['report']}
    
    Does this report fully and accurately answer the 
    original question? Reply with only YES or NO, 
    then one sentence explanation.
    """
    response = llm.invoke(prompt)
    passed = response.content.strip().upper().startswith("YES")
    return {
        "reflection_passed": passed,
        "loop_count": state['loop_count'] + 1
    }

def should_continue(state: ResearchState):
    if state['reflection_passed'] or state['loop_count'] >= 2:
        return "END"
    else:
        return "search"
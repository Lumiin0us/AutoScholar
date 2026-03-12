from agent.state import ResearchState
from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.3-70b-versatile", api_key="")

def parse_questions(text: str) -> list:
    lines = text.strip().split("\n")
    questions = []
    
    for line in lines:
        line = line.strip()
        if line:  # skip empty lines
            cleaned = line.lstrip("0123456789.-) ").strip()
            if cleaned:
                questions.append(cleaned)
    
    return questions

def planner_node(state: ResearchState):
    prompt = f"""
    You are a research planner. Break this topic into 
    3-4 specific search queries:
    
    Topic: {state['topic']}
    
    Return only a numbered list of search queries.
    """
    response = llm.invoke(prompt)
    # parse response into a list
    sub_questions = parse_questions(response.content)
    
    return {"sub_questions": sub_questions}
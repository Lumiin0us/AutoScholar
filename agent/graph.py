from langgraph.graph import StateGraph, END
from agent.state import ResearchState
from agent.nodes.reader import reader_node
from agent.nodes.search import search_node
from agent.nodes.planner import planner_node
from agent.nodes.synthesizer import synthesizer_node
from agent.nodes.reflection import reflection_node, should_continue

# Create the graph
graph = StateGraph(ResearchState)

# Add all nodes
graph.add_node("planner", planner_node)
graph.add_node("search", search_node)
graph.add_node("reader", reader_node)
graph.add_node("synthesizer", synthesizer_node)
graph.add_node("reflection", reflection_node)

# Add edges (flow between nodes)
graph.set_entry_point("planner")
graph.add_edge("planner", "search")
graph.add_edge("search", "reader")
graph.add_edge("reader", "synthesizer")
graph.add_edge("synthesizer", "reflection")

# Conditional edge - reflection either ends or loops back
graph.add_conditional_edges(
    "reflection",
    should_continue,
    {
        "search": "search",  # loop back
        "END": END           # finish
    }
)

app = graph.compile()
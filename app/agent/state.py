from typing import TypedDict, List

class ResearchState(TypedDict):
    topic: str                  # user's original question
    sub_questions: List[str]    # broken down by planner node
    search_results: List[dict]  # raw results from Tavily
    scraped_content: List[str]  # full page text
    report: str                 # final synthesized report
    reflection_passed: bool     # did reflection approve?
    loop_count: int             # prevent infinite loops
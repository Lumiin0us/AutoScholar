import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import streamlit as st
from agent.graph import app

st.title("AI Research Assistant")
topic = st.text_input("Enter research topic:")

if st.button("Research"):
    with st.spinner("Agent is researching..."):
        result = app.invoke({
            "topic": topic,
            "sub_questions": [],
            "search_results": [],
            "scraped_content": [],
            "report": "",
            "reflection_passed": False,
            "loop_count": 0
        })
    st.markdown(result['report'])
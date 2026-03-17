import streamlit as st
from agent.graph import app

st.title("AutoScholar")
st.caption("Autonomous AI research agent — enter a topic and get a structured report")

topic = st.text_input("Enter research topic:")

if st.button("Research"):
    if not topic.strip():
        st.warning("Please enter a topic first")
    else:
        with st.spinner("Agent is researching... this may take a minute"):
            result = app.invoke({
                "topic": topic,
                "sub_questions": [],
                "search_results": [],
                "scraped_content": [],
                "report": "",
                "reflection_passed": False,
                "loop_count": 0
            })

        st.success("Research complete")
        st.markdown(result['report'])
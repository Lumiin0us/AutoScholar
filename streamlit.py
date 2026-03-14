import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import streamlit as st
from agent.graph import app
from agent.state import ResearchState
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy
from datasets import Dataset
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings

evaluator_llm = LangchainLLMWrapper(
    ChatGroq(model="llama-3.3-70b-versatile", api_key="", n=1)
)
evaluator_embeddings = LangchainEmbeddingsWrapper(
    HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
)


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

    dataset = Dataset.from_dict({
            "question": [result['topic']],
            "answer": [result['report']],
            "contexts": [result['scraped_content']],
    })

    scores = evaluate(
            dataset=dataset,
            metrics=[faithfulness, answer_relevancy],
            llm=evaluator_llm,
            embeddings=evaluator_embeddings)

    st.subheader("Report Quality Scores")
    st.metric("Faithfulness", round(scores['faithfulness'][0], 2))
    st.metric("Answer Relevancy", round(scores['answer_relevancy'][0], 2))

    st.markdown(result['report'])

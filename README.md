# AutoScholar

AutoScholar is an autonomous multi-step research agent/assistant built with LangGraph. Given any research topic, it plans a search strategy, queries the web, reads and extracts content from sources, and formulates a structured, cited report — without any manual intervention.
It uses a self-reflection loop to evaluate the quality of its output and automatically re-searches if the report doesn't fully answer the original question.

---

## Live Demo
[Try AutoScholar on HuggingFace Spaces](https://huggingface.co/spaces/luminoria/AutoScholar)

---

## How It Works

When a user submits a research topic, the agent runs through a graph of nodes — each responsible for one stage of the research process:
  1. Planner — The LLM breaks the topic into 3-4 specific sub-questions worth searching for independently.
  2. Search — Each sub-question is sent to the Tavily Search API, which returns clean, LLM-ready results including URLs and content snippets.
  3. Reader — The top URLs are fetched and parsed with BeautifulSoup, extracting the main body text and stripping unwanted data.
  4. Synthesizer — All gathered content is assembled into a prompt and sent to the LLM, which writes a structured report with an introduction, key findings, and conclusion.
  5. Reflection — The LLM evaluates whether the report fully answers the original question. If not, the agent loops back to the Search node with refined queries. The loop is capped at 2 iterations to prevent infinite cycles.

---

## Agent Graph

```
[Planner] → [Search] → [Reader] → [Synthesizer] → [Reflection]
                ↑                                        ↓
                └──────────── re-search if needed ───────┘
                                                         ↓
                                                        END
```

---

## Project Structure

```

AutoScholar/
├── app/
│   ├── agent/
│   │   ├── nodes/
│   │   │   ├── planner.py
│   │   │   ├── search.py
│   │   │   ├── reader.py
│   │   │   ├── synthesizer.py
│   │   │   └── reflection.py
│   │   ├── graph.py
│   │   └── state.py
│   └── streamlit.py
└── README.md

```
  
---

## Workflow

User Topic  
     ↓  
Planner (LLM)  
     ↓  
Tavily Web Search × N sub-questions  
     ↓  
BeautifulSoup Page Reader  
     ↓  
Synthesizer (LLM)  
     ↓  
Reflection (LLM)  
     ↓  
Structured Report  

---

## AutoScholar UI

<img width="388" height="642" alt="Screenshot 2026-03-12 at 11 15 39 AM" src="https://github.com/user-attachments/assets/8dce02eb-03e2-46f5-9ab6-5310cec131f6" />


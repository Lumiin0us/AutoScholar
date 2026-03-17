from langchain_groq import ChatGroq
from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile")
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
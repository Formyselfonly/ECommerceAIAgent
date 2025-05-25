from langchain.tools import tool
from rag.retriever import get_faq_retriever

faq_retriever = get_faq_retriever()

@tool
def customer_support_tool(question: str) -> str:
    """Answer customer support questions using a FAQ knowledge base."""
    docs = faq_retriever.invoke(question)
    if not docs:
        return "Sorry, I couldn't find an answer to your question."
    return "\n".join([f"- {doc.page_content}" for doc in docs])
from langchain.tools import tool
from rag.retriever import get_product_retriever

retriever = get_product_retriever()

@tool
def product_search_tool(query: str) -> str:
    """Search for products related to a user query."""
    docs = retriever.invoke(query)
    if not docs:
        return "No relevant products found."
    return "\n".join([f"- {doc.page_content}" for doc in docs])
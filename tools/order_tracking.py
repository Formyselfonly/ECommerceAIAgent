from langchain_openai import ChatOpenAI
from langchain.tools import tool
import json
import os

llm = ChatOpenAI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ORDERS_FILE = os.path.normpath(os.path.join(BASE_DIR, "..", "data", "orders.json"))

@tool
def order_tracking_tool(order_input: str) -> str:
    """Check the status of an order by ID, allowing flexible input like 'order1' or 'my order three'."""
    try:
        with open(ORDERS_FILE, "r") as f:
            orders = json.load(f)
        order_ids = list(orders.keys())

        # Build simple prompt directly
        prompt = f"""
        A user asked about an order: "{order_input}".
        From this list of Order IDs: {', '.join(order_ids)}
        What is the best matching Order ID? Reply with only the ID.
        """
        response = llm.invoke(prompt).content.strip()

        order = orders.get(response)
        if order:
            return f"Order {response} status: {order['status']}"
        else:
            return f"Order ID {response} not found."

    except Exception as e:
        return f"Error accessing order database: {e}"

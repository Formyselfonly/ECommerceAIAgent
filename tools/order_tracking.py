from langchain.tools import tool
import json
import os

ORDERS_FILE = os.path.join("data", "orders.json")

@tool
def order_tracking_tool(order_id: str) -> str:
    """Check the status of an order by ID."""
    try:
        with open(ORDERS_FILE, "r") as f:
            orders = json.load(f)
        order = orders.get(order_id)
        if order:
            return f"Order {order_id} status: {order['status']}"
        else:
            return f"Order ID {order_id} not found."
    except Exception as e:
        return f"Error accessing order database: {e}"

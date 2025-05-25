from langchain.tools import tool
import pandas as pd
import os

PRODUCTS_FILE = os.path.join("data", "products.csv")

@tool
def recommendation_tool(preference: str) -> str:
    """Recommend a product based on user preference keywords."""
    try:
        df = pd.read_csv(PRODUCTS_FILE)
        filtered = df[df['description'].str.contains(preference, case=False, na=False)]
        if filtered.empty:
            return "No recommendations found for that preference."
        results = filtered.sort_values(by="sales", ascending=False).head(3)
        return "\n".join([f"{row['name']} - ${row['price']}" for _, row in results.iterrows()])
    except Exception as e:
        return f"Error generating recommendation: {e}"
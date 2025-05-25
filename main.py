from langchain.agents import initialize_agent, Tool
from langchain_openai  import ChatOpenAI
from langchain.memory import ConversationBufferMemory

from tools.product_search import product_search_tool
from tools.order_tracking import order_tracking_tool
from tools.customer_support import customer_support_tool
from tools.recommendation import recommendation_tool
import dotenv
import os
dotenv.load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
# Define your tools list
TOOLS = [
    product_search_tool,
    order_tracking_tool,
    customer_support_tool,
    recommendation_tool
]

# Load language model (use OpenAI or replace with your LLM)
llm = ChatOpenAI(
    temperature=0.2,
    api_key=OPENAI_API_KEY
)

# Add memory to support multi-turn dialogue
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Initialize the agent
agent = initialize_agent(
    tools=TOOLS,
    llm=llm,
    memory=memory,
    agent="chat-conversational-react-description",
    verbose=True,
)

if __name__ == "__main__":
    print("🛒 E-Commerce AI Agent is ready!")
    while True:
        query = input("User: ")
        if query.lower() in ["exit", "quit"]:
            break
        response = agent.invoke(query)
        print(f"Agent: {response}")
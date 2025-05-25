# 🛒 ECommerce AI Agent Framework

A multi-tool, LLM-powered E-Commerce Agent built with LangChain.  
Designed for intelligent product search, order tracking, FAQ support, and personalized recommendations — all using local data files (no external database needed).

---

## 💡 Features

| Function            | Tool Name             | Description                                               |
| ------------------- | --------------------- | --------------------------------------------------------- |
| 🔍 Product Search    | `ProductSearchTool`   | Vector-based semantic retrieval over product descriptions |
| 🧾 Order Tracking    | `OrderTrackingTool`   | Order status lookup via JSON file                         |
| ❓ Customer Support  | `CustomerSupportTool` | FAQ question answering using RAG + LLM                    |
| 🎯 Recommendation    | `RecommendationTool`  | Recommend products based on user queries or categories    |
| 🧠 Multi-Turn Memory | `ConversationMemory`  | Supports follow-up questions and session tracking         |

---

## 🚀 Tech Stack

- **LangChain v0.3+**
- **OpenAI GPT-3.5 / ChatGLM**
- **FAISS for Vector Search**
- **Local CSV / JSON / TXT as simulated databases**

---

## 🗂️ Project Structure

```python
ECommerceAIAgent/
├── main.py # Agent entry point
├── tools/
│ ├── product_search.py # Product retrieval
│ ├── order_tracking.py # Order status check
│ ├── customer_support.py # FAQ tool
│ └── recommendation.py # Recommendation logic
├── data/
│ ├── products.csv # Product database
│ ├── orders.json # Simulated order data
│ └── faq.txt # FAQ corpus
├── rag/
│ ├── embedder.py
│ └── retriever.py
└── utils/
└── prompts.py # Prompt templates
```

## 💬 Sample Prompts

> "Find me a budget-friendly wireless mouse."  
> "What’s the return policy?"  
> "Track my order ID ORD002."  
> "Recommend something suitable for office use."

---

## 🔹 Next Step: Feature Enhancements (Lightweight)

| Enhancement                       | Purpose                                                      | How to Implement                                             |
| --------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 🧾 Add “Place Order” feature       | Simulate placing an order to complete the shopping flow      | Create an `OrderSubmissionTool` that writes to `my_orders.json` |
| 🎯 Improve recommendation accuracy | Make recommendations more relevant by matching keyword + category | Add simple category filtering inside `recommendation_tool`   |
| ❓ Enable multi-turn FAQ memory    | Allow follow-up questions like “How long?” → “Is it free?”   | Use `memory` and context-aware logic to track follow-ups     |
| 📢 Format output responses better  | Make replies more readable with line breaks or symbols       | Use `f-strings` + markdown-style formatting                  |

## 🎯 Designed For

- Interview showcase for AI Backend/LLM Engineer roles
- Demonstrating LangChain multi-tool orchestration
- Realistic e-commerce workflow simulation without external services

---

## ✨ Author

Built by [Shijie Zheng](https://github.com/Formyselfonly?tab=repositories) for technical interviews at  

---

## 📎 License

MIT License
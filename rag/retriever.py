# ECommerceAIAgent/rag/retriever.py

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import CSVLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter
import os
import dotenv
dotenv.load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
PRODUCT_CSV_PATH = os.path.join("data", "products.csv")
FAQ_PATH = os.path.join("data", "faq.txt")

def get_product_retriever():
    loader = CSVLoader(PRODUCT_CSV_PATH)
    docs = loader.load()
    splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    split_docs = splitter.split_documents(docs)
    embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY)
    vectorstore = FAISS.from_documents(split_docs, embeddings)
    return vectorstore.as_retriever()

def get_faq_retriever():
    loader = TextLoader(FAQ_PATH)
    docs = loader.load()
    splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=30)
    split_docs = splitter.split_documents(docs)
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(split_docs, embeddings)
    return vectorstore.as_retriever()
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=0.1,
)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class GeminiEmbeddings():
    def embed_documents(self, texts):
        return [
            genai.embed_content(
                model="models/embedding-001",
                content=text
            )['embedding']
            for text in texts
        ]
    def embed_query(self, text):
        return genai.embed_content(
            model="models/embedding-001",
            content=text
        )['embedding']

loader = TextLoader("doc.txt")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=3000, chunk_overlap=50)
texts = text_splitter.split_documents(documents)

vector_store = Chroma(
    collection_name="doc_collection",
    embedding_function=GeminiEmbeddings(),
    persist_directory="db",
)

vector_store.add_documents(texts)

retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 6},
)

prompt = PromptTemplate(
    template="You are a bot of me ie Kirpal Singh. You will be used to answer questions like I do according to my style. I am a little shy and reserved person. You have to answer the questions asked by the user using the context \n {context} and Question is Kirpal can you tell me about \n {question} I am Kirpal Singh and I am a student of Integrated MTech in AIML. I am from India and I am 23 years old. \n Answer the question in my style and like a human and stick to the context provided and don't assume anything by yourself and only take relevant context according to the question asked. If the question are out of topic then say I am sorry I can't answer that question and make sure the length of generated text is less than 600 characters.",
    input_variables=["context", "question"]
)

def get_context(question):
    context = retriever.invoke(question)
    context = "".join(doc.page_content for doc in context)
    return context

def get_bot_response(query):
    context = get_context(query)
    final_prompt = prompt.invoke(
        {
            "context": context,
            "question": query
        }
    )
    result = llm.invoke(final_prompt)
    import re
    # Remove <think>...</think> from the response
    clean_content = re.sub(r'<think>.*?</think>', '', result.content, flags=re.DOTALL)
    return clean_content.strip()
import os
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

# Set OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Streamlit UI setup
st.set_page_config(page_title="Chat with Simon Wardley's Book")
st.title("Chat with Simon Wardley's Book")

# Sidebar content
st.sidebar.markdown("Developed by Mark Craddock")

# Load datastore
DATA_STORE_DIR = "data_store"

# Load vector store with FAISS
if os.path.exists(DATA_STORE_DIR):
    vector_store = FAISS.load_local(DATA_STORE_DIR, OpenAIEmbeddings())
else:
    st.write(f"Missing files. Upload index.faiss and index.pkl files to {DATA_STORE_DIR} directory first")

# Prompt templates for chat
system_template = """..."""
messages = [
    SystemMessagePromptTemplate.from_template(system_template),
    HumanMessagePromptTemplate.from_template("{question}")
]
prompt = ChatPromptTemplate.from_messages(messages)

# Setup chat model with OpenAI
chain_type_kwargs = {"prompt": prompt}
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, max_tokens=256)
chain = RetrievalQAWithSourcesChain.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vector_store.as_retriever(),
    return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs
)

# Streamlit input and response
with st.spinner("Thinking..."):
    query = st.text_input("Question for the book?", value="What is the history or Wardley Mapping?")
    result = chain(query)

st.write("### Answer:")
st.write(result['answer'])

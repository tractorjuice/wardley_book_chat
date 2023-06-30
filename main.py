import os
import re
import openai
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

# Set OpenAI Model and API key
openai.api_key = st.secrets["OPENAI_API_KEY"]
#MODEL = "gpt-3"
#MODEL = "gpt-3.5-turbo"
#MODEL = "gpt-3.5-turbo-0613"
#MODEL = "gpt-3.5-turbo-16k"
#MODEL = "gpt-3.5-turbo-16k-0613"
#MODEL = "gpt-4"
MODEL = "gpt-4-0613"
#MODEL = "gpt-4-32k-0613"

st.set_page_config(page_title="Chat with Simon Wardley's Book")
st.title("Chat with Simon Wardley's Book")
st.sidebar.markdown("# Query this book using AI")
st.sidebar.divider()
st.sidebar.markdown("Developed by Mark Craddock](https://twitter.com/mcraddock)", unsafe_allow_html=True)
st.sidebar.markdown("Current Version: 0.2.0")
st.sidebar.divider()
st.sidebar.markdown("Using GPT-4 API")
st.sidebar.markdown("Not optimised")
st.sidebar.markdown("May run out of OpenAI credits")
st.sidebar.divider()
st.sidebar.markdown("Wardley Mapping is provided courtesy of Simon Wardley and licensed Creative Commons Attribution Share-Alike.")

# Get datastore
DATA_STORE_DIR = "data_store"

if "messages" not in st.session_state:
    st.session_state.messages = []

    if os.path.exists(DATA_STORE_DIR):
        vector_store = FAISS.load_local(
            DATA_STORE_DIR,
            OpenAIEmbeddings()
        )
    else:
        st.write(f"Missing files. Upload index.faiss and index.pkl files to {DATA_STORE_DIR} directory first")
  
    system_template="""Use the following pieces of context to answer the users question.
    If you don't know the answer, just say that "I don't know", don't try to make up an answer.
    ----------------
    {summaries}"""
    prompt_messages = [
        SystemMessagePromptTemplate.from_template(system_template),
        HumanMessagePromptTemplate.from_template("{question}")
        ]
    prompt = ChatPromptTemplate.from_messages(prompt_messages)
    
    chain_type_kwargs = {"prompt": prompt}
    llm = ChatOpenAI(model_name=MODEL, temperature=0, max_tokens=300)  # Modify model_name if you have access to GPT-4
    print("done chain stuff")
    chain = RetrievalQAWithSourcesChain.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever(),
        return_source_documents=True,
        chain_type_kwargs=chain_type_kwargs
    )

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if query := st.chat_input("What question do you have for the book?"):
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)
      
    with st.spinner():
        with st.chat_message("assistant"):
            response = chain(query)
            st.markdown(response['answer'])
        st.session_state.messages.append({"role": "assistant", "content": response['answer']})

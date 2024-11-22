import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import GPT4All
import streamlit as st

# Paths
PDF_PATH = "D:/ContentEngine/data"
VECTOR_DB_PATH = "D:/ContentEngine/chromadb"
MODEL_PATH = "D:/ContentEngine/gpt4all-model.bin"

# Initialize the Local LLM
def initialize_gpt4all(model_path):
    return GPT4All(model_path, model_type="llama")

# Load and Process PDFs
def load_and_process_pdfs(pdf_dir):
    all_docs = []
    for pdf_file in os.listdir(pdf_dir):
        if pdf_file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(pdf_dir, pdf_file))
            all_docs.extend(loader.load_and_split())
    return all_docs

# Build Vector Store
def build_vector_store(docs, db_path):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    split_texts = text_splitter.split_documents(docs)
    embeddings = HuggingFaceEmbeddings()
    vector_store = Chroma.from_documents(split_texts, embedding=embeddings, persist_directory=db_path)
    vector_store.persist()
    return vector_store

# Set up Retrieval Chain
def setup_retrieval_chain(db_path, llm):
    vector_store = Chroma(persist_directory=db_path, embedding_function=HuggingFaceEmbeddings())
    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)

# Streamlit Interface
def main():
    st.title("Content Engine: Analyze and Compare PDFs")
    st.sidebar.header("Options")
    
    # Inputs
    user_query = st.text_area("Enter your query:")
    if st.sidebar.button("Process PDFs"):
        with st.spinner("Processing PDFs..."):
            documents = load_and_process_pdfs(PDF_PATH)
            build_vector_store(documents, VECTOR_DB_PATH)
        st.success("PDFs processed and vector store updated!")
    
    if user_query:
        with st.spinner("Fetching insights..."):
            local_llm = initialize_gpt4all(MODEL_PATH)
            qa_chain = setup_retrieval_chain(VECTOR_DB_PATH, local_llm)
            response = qa_chain.run(user_query)
        st.write("### Response:")
        st.write(response)

if __name__ == "__main__":
    main()

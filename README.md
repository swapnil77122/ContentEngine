# **Content Engine: Analyze and Compare PDFs**

## **Overview**
Content Engine is a Python-based application that allows users to upload and analyze PDF documents. Using advanced natural language processing (NLP) and retrieval-based question-answering, the tool can answer user queries based on the contents of the uploaded PDFs. It leverages LangChain for document processing and chaining, GPT4All as a local large language model (LLM), and Chroma for vector storage and retrieval.

## **Features**
- **PDF Parsing**: Automatically extracts and processes text content from PDFs.
- **Chunking and Embedding**: Splits documents into manageable chunks and creates vector embeddings for efficient search.
- **Question Answering**: Allows users to query the documents for insights, returning precise answers along with source documents.
- **Streamlit Interface**: A user-friendly web interface for interacting with the application.

---

## **Prerequisites**
1. Python 3.8 or higher installed.
2. Required Python libraries (install using `pip install -r requirements.txt`).
3. Pre-trained GPT4All model downloaded and saved to the specified path.
4. PDFs to analyze stored in the `D:/ContentEngine/data` directory.

---

## **Installation**

1. **Clone or Download the Repository**:
   ```bash
   git clone https://github.com/your-repo/content-engine.git
   cd content-engine
   ```

2. **Install Dependencies**:
   Create a virtual environment and install the required packages:
   ```bash
   python -m venv env
   source env/bin/activate        # For Linux/MacOS
   .\env\Scripts\activate         # For Windows

   pip install -r requirements.txt
   ```

3. **Download the GPT4All Model**:
   - Download the model file from the [GPT4All website](https://gpt4all.io/).
   - Save it as `gpt4all-model.bin` in `D:/ContentEngine/`.

4. **Set Up Directory Structure**:
   Ensure the following directory structure exists:
   ```
   D:/ContentEngine/
       ├── data/              # Folder for storing PDFs
       ├── chromadb/          # Folder for storing the vector database
       ├── gpt4all-model.bin  # GPT4All model file
   ```

---

## **How to Use**

1. **Start the Application**:
   Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. **Interface**:
   - The main page will display options to **process PDFs** and enter a query.
   - Use the **sidebar** to process PDFs stored in `D:/ContentEngine/data/`.
   - Enter your query in the text box to retrieve insights based on the PDFs.

3. **Workflow**:
   - Click **Process PDFs** to load and embed documents into the vector database.
   - Enter a query in the text box and wait for the response to be displayed.

---

## **Code Overview**

### **Key Components**
1. **PDF Loading and Processing**:
   - The `load_and_process_pdfs()` function reads all PDFs from the specified directory and splits their content into chunks.

2. **Vector Store**:
   - Built using Chroma and HuggingFace embeddings. 
   - Persistent storage ensures that embeddings don't need to be recreated unless new PDFs are added.

3. **Retrieval-Based QA**:
   - GPT4All serves as the LLM for query-answering.
   - Uses similarity search to retrieve the most relevant chunks from the vector store.

4. **Streamlit UI**:
   - Provides an interactive interface for processing PDFs and querying the content.

---

## **Configuration**
- **Paths**:
   - `PDF_PATH`: Directory to store PDFs (`D:/ContentEngine/data`).
   - `VECTOR_DB_PATH`: Directory for the vector database (`D:/ContentEngine/chromadb`).
   - `MODEL_PATH`: Path to the GPT4All model file (`D:/ContentEngine/gpt4all-model.bin`).

- **Chunk Size**:
   - Documents are split into chunks of size 1000 characters with an overlap of 200 characters for improved retrieval.

- **Query Parameters**:
   - Retrieves the top 3 most similar document chunks for each query.

---

## **Requirements File**
Below is the `requirements.txt` for the application:
```
langchain==0.0.267
chromadb==0.3.25
huggingface-hub==0.17.1
streamlit==1.27.0
pypdf==3.14.0
gpt4all==0.3.5
```

---

## **Troubleshooting**
- **No Response to Query**:
  Ensure that the PDFs are processed before querying and the `gpt4all-model.bin` file is correctly placed.
  
- **Slow Response**:
  Depending on the size of the PDFs and your system's hardware, responses may take time. Consider reducing the chunk size or query parameters.

- **Error in Loading PDFs**:
  Verify that all files in `PDF_PATH` are valid PDF documents.

---

## **Future Improvements**
- Add support for dynamic PDF uploads through the Streamlit interface.
- Enhance response accuracy by fine-tuning the embeddings or LLM.
- Integrate other pre-trained models for extended functionality.

---

## **Credits**
- **LangChain**: Framework for chaining language models and retrieval systems.
- **GPT4All**: Local LLM for question-answering.
- **Streamlit**: Web interface for user interaction. 

---


import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_split_pdf(file_path):
    """Loads a PDF and splits it into manageable text chunks."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Could not find the PDF at: {file_path}")

    print(f"--- Loading Document: {os.path.basename(file_path)} ---")
    loader = PyPDFLoader(file_path)
    pages = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=150
    )
    chunks = text_splitter.split_documents(pages)

    print(f"Successfully split into {len(chunks)} chunks.")
    return chunks

if __name__ == "__main__":
    # --- BULLETPROOF PATH LOGIC ---
    # 1. Get the directory where THIS loader.py file lives
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 2. Go up one level to 'Statement-1-Insurance-Decoder', then into 'docs'
    pdf_path = os.path.abspath(os.path.join(current_dir, "..", "docs", "TITAN SECURE.pdf"))
    
    print(f"Searching for PDF at: {pdf_path}")
    
    try:
        data_chunks = load_and_split_pdf(pdf_path)
        print(f"\nSample content from Page 1:\n{data_chunks[0].page_content[:200]}...")
    except Exception as e:
        print(f"Error: {e}")
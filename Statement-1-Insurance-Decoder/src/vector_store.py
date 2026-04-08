import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
# Import the function from your previous file
from loader import load_and_split_pdf

# 1. Load API Key
# Assuming .env is in the 'Statement-1-Insurance-Decoder' folder
current_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(current_dir, "..", ".env"))

def create_vector_db(pdf_path):
    chunks = load_and_split_pdf(pdf_path)
    
    if not os.getenv("GOOGLE_API_KEY"):
        raise ValueError("GOOGLE_API_KEY not found! Check your .env file.")
        
    # --- USE THE EXACT ID FROM YOUR DIAGNOSTIC ---
    # The 'models/' prefix is required for gemini-embedding-001
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        task_type="retrieval_document"
    )
    
    print("--- Creating Embeddings (This will work now!) ---")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    persist_dir = os.path.join(current_dir, "..", "chroma_db")
    
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_dir
    )
    
    print(f"Success! Vector database created at: {persist_dir}")
    return vector_db
    

if __name__ == "__main__":
    pdf_path = os.path.abspath(os.path.join(current_dir, "..", "docs", "TITAN SECURE.pdf"))
    try:
        create_vector_db(pdf_path)
    except Exception as e:
        print(f"Error: {e}")
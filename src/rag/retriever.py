from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

def get_interviews(profile):
    # Load vector DB
    db = Chroma(
        persist_directory="db",
        embedding_function=HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )
    )

    # Create query from skills
    query = " ".join(profile["skills"])

    # Search top 3 matches
    docs = db.similarity_search(query, k=3)

    # Return text
    return [doc.page_content for doc in docs]
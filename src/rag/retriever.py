from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

def get_interviews(profile):
    db = Chroma(
        persist_directory="db",
        embedding_function=OpenAIEmbeddings()
    )

    query = " ".join(profile["skills"])
    docs = db.similarity_search(query, k=3)

    return [doc.page_content for doc in docs]
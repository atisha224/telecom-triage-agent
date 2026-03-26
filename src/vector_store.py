from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


class VectorStore:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        self.db = None

    def create_store(self, documents):
        self.db = FAISS.from_texts(documents, self.embeddings)

    def search(self, query):
        if not self.db:
            return []
        return self.db.similarity_search(query, k=2)
    
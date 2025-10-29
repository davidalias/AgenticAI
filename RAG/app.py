from src.data_loader import load_all_documents
from src.embedding import EmbeddingPipeline
from src.vectorstore import FaissVectorStore


#Example usage

if __name__ == "__main__":
    """
    Once vector store is created, this part of the code is not required for further querying

    docs = load_all_documents("data")

    #embedding working
    chunks = EmbeddingPipeline().chunk_documents(docs)
    chunkvectors = EmbeddingPipeline().embed_chunks(chunks)
    print(chunkvectors)

    #vectorstore working
    store = FaissVectorStore("faiss_store")
    store.build_from_documents(docs)"""

    store = FaissVectorStore("faiss_store")
    store.load()
    print(store.query("What is RAG?", top_k =3))

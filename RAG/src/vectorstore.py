import os
import faiss
import numpy as np
import pickle
from typing import List, Any
from sentence_transformers import SentenceTransformer
from src.embedding import EmbeddingPipeline

class FaissVectorStore:
    def __init__(self, persist_dir:str = "faiss_store", embedding_model:str = "all-MiniLM-L6-v2", chunk_size: int =1000, chunk_overlap: int = 200):
        self.persist_dir = persist_dir
        os.makedirs(self.persist_dir, exist_ok=True)
        self.index = None
        self.metadata = []
        self.embedding_model = embedding_model
        self.model = SentenceTransformer(embedding_model)
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        print(f"[INFO] Loaded embedding model: {embedding_model}")

    #convert input data to docs to chunks to embeddings, and add embeddings to faiss vectordb and save faiss index file and metadata pickle file in local 
    def build_from_documents(self, documents: List[Any]):
        print(f"[INFO] Building vector store from {len(documents)} raw documents...")
        emb_pipe = EmbeddingPipeline(model_name=self.embedding_model, chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)
        chunks = emb_pipe.chunk_documents(documents)
        embeddings = emb_pipe.embed_chunks(chunks)
        metadatas = [{"text": chunk.page_content} for chunk in chunks]
        self.add_embeddings(np.array(embeddings).astype('float32'), metadatas)
        self.save()
        print(f"[INFO] Vector store built and saved to {self.persist_dir}")

    #add embeddings to faiss vectorstore
    def add_embeddings(self, embeddings: np.ndarray, metadatas: List[Any]=None):
        dim = embeddings.shape[1]
        if self.index is None:
            self.index = faiss.IndexFlatL2(dim) #This index uses L2 (Euclidean) distance for similarity search.IndexFlatL2 is simple and fast but doesn't scale well for huge datasets.
            #A FAISS index is a data structure used for fast similarity search on high-dimensional vectors, like those generated from text, images, or other data using machine learning models.
        self.index.add(embeddings)#This method adds the given embeddings (a NumPy array of shape (n_vectors, dim)) to the index.This is a FAISS index object, such as IndexFlatL2, which stores and allows fast similarity search over vectors.
        if metadatas:
            self.metadata.extend(metadatas)
        print(f"[INFO] Added {embeddings.shape[0]} vectors to Faiss index")

    #save faiss index file and metadata pickle file in the local folder
    def save(self):
        faiss_path = os.path.join(self.persist_dir, "faiss.index")#"faiss.index" is the binary file for the FAISS index.
        meta_path = os.path.join(self.persist_dir, "metadata.pkl")#"metadata.pkl" is a pickle file for storing metadata (e.g., document info).
        faiss.write_index(self.index, faiss_path)#Saves the FAISS index to disk in binary format
        with open(meta_path, "wb") as f:  #Opens the file at meta_path in write-binary mode ("wb").
            pickle.dump(self.metadata, f)# Serializes the self.metadata object and writes it to the file f.
        print(f"[INFO] Saved Faiss Index and metadata to {self.persist_dir}")

    #load faiss index file and metadata pickle file from the local folder
    def load(self):
        faiss_path = os.path.join(self.persist_dir, "faiss.index") #Joins multiple path components into one complete path using the correct separator for the operating system (/ for Unix-like systems, \ for Windows).
        meta_path = os.path.join(self.persist_dir, "metadata.pkl")
        self.index = faiss.read_index(faiss_path)
        with open(meta_path, "rb") as f:
            self.metadata = pickle.load(f)
        print(f"[INFO] Loaded Faiss index and metadata from {self.persist_dir}")

    #search for similar top_k similar embeddings
    def search(self, query_embedding: np.ndarray, top_k: int = 5):
        D, I = self.index.search(query_embedding, top_k)
        results = []
        for idx, dist in zip(I[0], D[0]):
            meta = self.metadata[idx] if idx < len(self.metadata) else None
            results.append({"index": idx, "distance": dist, "metadata": meta})
        return results

    #encode query text into embeddings and call search function to find similar embeddings 
    def query(self, query_text: str, top_k: int = 5):
        print(f"[INFO] Querying vector store for: '{query_text}'")
        query_emb = self.model.encode([query_text]).astype('float32')
        return self.search(query_emb, top_k = top_k)

    

    
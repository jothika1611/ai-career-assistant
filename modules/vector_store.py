from config import MODEL_PROVIDER
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
import numpy as np

if MODEL_PROVIDER == "openai":
    from langchain.embeddings.openai import OpenAIEmbeddings
else:
    from langchain.embeddings.base import Embeddings

    class LocalEmbeddings(Embeddings):
        def embed_documents(self, texts):

            return [np.random.rand(1536).tolist() for _ in texts]

        def embed_query(self, text):
            return np.random.rand(1536).tolist()

class VectorStore:
    def __init__(self, text):
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        docs = [Document(page_content=chunk) for chunk in splitter.split_text(text)]

        if MODEL_PROVIDER == "openai":
            self.embeddings = OpenAIEmbeddings()
        else:
            self.embeddings = LocalEmbeddings()


        self.store = FAISS.from_documents(docs, self.embeddings)

    def similarity_search(self, query, k=3):
        return self.store.similarity_search(query, k=k)

def create_vector_store(text):
    return VectorStore(text)
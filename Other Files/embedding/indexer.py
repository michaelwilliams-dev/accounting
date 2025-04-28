from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

embedding_model = OpenAIEmbeddings()

def index_chunks(chunks, metadata_list, index_path="faiss_index"):
    faiss_index = FAISS.from_texts(texts=chunks, embedding=embedding_model, metadatas=metadata_list)
    faiss_index.save_local(index_path)
    return faiss_index

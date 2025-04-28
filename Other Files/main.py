from fastapi import FastAPI
from pydantic import BaseModel
from ingestion.ingest import chunk_text
from tagging.tagger import tag_chunk
from embedding.indexer import index_chunks

app = FastAPI()

class Document(BaseModel):
    text: str

@app.post("/process")
def process_document(doc: Document):
    chunks = chunk_text(doc.text)
    tagged_metadata = []
    for chunk in chunks:
        tag = tag_chunk(chunk)
        category, doc_type = tag.split("\n")
        tagged_metadata.append({
            "category": category.replace("Category: ", "").strip(),
            "document_type": doc_type.replace("Document Type: ", "").strip()
        })
    index_chunks(chunks, tagged_metadata)
    return {"message": "Document processed and indexed successfully."}

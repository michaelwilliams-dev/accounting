from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-4", temperature=0)

def tag_chunk(chunk):
    prompt = f"Categorize this accounting text. Respond with Category and Document Type only:\n\n{chunk}"
    response = llm.predict(prompt)
    return response

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/flan-t5-large",
    task="text2text-generation",
    temperature=0.7,
    max_new_tokens=100
)

model = ChatHuggingFace(llm=llm)

res = model.invoke("What is the capital of India?")
print(res.content)
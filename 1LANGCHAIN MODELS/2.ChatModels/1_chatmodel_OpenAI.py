from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model='gpt-4o-mini', temperature=0.7,max_completion_tokens=10)

res=model.invoke("what is the capital of India")

print(res)
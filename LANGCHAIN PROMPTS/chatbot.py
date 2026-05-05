from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()

chat_history=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content="Tell me about Langchain")
]
while True:
    user_input=input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input=='exit':
        break
    res=model.invoke(chat_history)
    chat_history.append(AIMessage(res.content))
    print("AI: ",res.content)   
    
print(chat_history) 
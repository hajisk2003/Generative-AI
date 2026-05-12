from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

template1=PromptTemplate(
    template='write a detail report on {topic}',
    input_variables=['topic']
)
template2=PromptTemplate(
    template='write a 5 line summary on text. /n report on {text}',
    input_variables=['text']
)

prompt1=template1.invoke({'topic':'Black hole'})

res1=model.invoke(prompt1)

prompt2=template2.invoke({'text':res1.content})

res2=model.invoke(prompt2)

print(res1.content)
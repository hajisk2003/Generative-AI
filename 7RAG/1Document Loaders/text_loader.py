from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
model=ChatOpenAI()

prompt=PromptTemplate(
    template='write a summary on the following poem \n {poem}',
    input_variables=['poem']
)

parser=StrOutputParser()

chain=prompt | model | parser



loader = TextLoader('cricket.txt', encoding='utf-8')


docs = loader.load()

print(chain.invoke({'poem':docs[0].page_content}))

print(docs)
print(docs[0])

print(docs[0].page_content)
print(docs[0].metadata)
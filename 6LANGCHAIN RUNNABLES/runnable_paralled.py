from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schemas.runnable import RunnableParallel,Runnablesequence

load_dotenv()

prompt1=PromptTemplate(
    template='generate a twit about {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='generate a linkdin post about {topic}',
    input_variables=['topic']
)

parser=StrOutputParser()

parallechain=RunnableParallel({
    'tweet':Runnablesequence(prompt1,model,parser),
    'linkdin':Runnablesequence(prompt2,model,parser)
})

res=parallechain.invoke({'topic':'AI'})

print(res['tweet'])
print(res['linkdin'])
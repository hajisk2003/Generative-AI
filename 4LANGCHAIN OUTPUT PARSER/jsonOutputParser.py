from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser=JsonOutputParser()
template=PromptTemplate(
    template='Give me the name,age and city of fictional person \n {format_instuction}',
    input_variabe=[],
    partial_variable={'format_instruction':parser.get_fromat_instructions()}
)

chain=template | model | parser

res=chain.invoke()
print(res)



# prompt=template.format()
# print(prompt)

# res=model.invoke(prompt)
# print(res)

# final_res=parser.parse(res.content)
# print(final_res['name'])
# print(final_res)
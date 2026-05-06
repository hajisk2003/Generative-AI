from pydantic import BaseModel
class Student(BaseModel):
    name:str
    
new_student={'name':'Haji'}
student=Student(**new_student)
print(student)
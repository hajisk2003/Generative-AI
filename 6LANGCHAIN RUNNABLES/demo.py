class llm:
    def __init__(self):
        print('llm created')
        
    def predict(self,prompt):
        respomse_list=[
            'delhi is the capital of india',
            'ipl is a cricket leagur',
            'ai stands for artificial intelligence'
            
        ]
        return {'response':random.choice(respose_list)}

    
llm1=llm()
llm1.predict('What is the capital of india')
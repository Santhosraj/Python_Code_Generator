# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 10:22:25 2023

@author: SanthosRaj
"""
def execute():
    import os 
    import langchain
    from langchain_experimental.pal_chain import PALChain
    from langchain import OpenAI
    from langchain.chains.llm import LLMChain
    
    os.environ["OPENAI_API_KEY"] = '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'
    
    llm = OpenAI(model_name = 'text-davinci-002' ,
                 temperature=0,
                 max_tokens=512)
    
    pal_chain =PALChain.from_math_prompt(llm,verbose=True)
    
    
    question = "Raja has 5 chocolates , he gave 3 chocolates to his friends , how many chocolates are left with Raja"
    
    pal_chain.run(question)
execute()
from langchain_openai import ChatOpenAI

#from helper_functions import get_api_key

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

response = llm.invoke("What is the capital of France?")
print(response.content) 
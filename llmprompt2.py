from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

response = llm.invoke(" The song what a beautiful name it is by hillsong")
print(response.content) 
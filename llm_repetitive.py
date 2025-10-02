from langchain_openai import ChatOpenAI

name = "Peter"

prompt = f"""write a poem for {name} birthday, inspired by the name Andreas """

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
response = llm.invoke(prompt)
print(response.content)

# %%    
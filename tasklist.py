
from langchain_openai import ChatOpenAI
literature_list = ['poem', 'story', 'song', 'play', 'poem']
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

for literature in literature_list:
    prompt = f"""Write a {literature}"""
response = llm.invoke(prompt)
print(response.content)
print('--------------------------------\n')
print(type(literature_list))

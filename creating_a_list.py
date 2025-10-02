from tasklist import prompt
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

friends_lists = ["Peter", "John", "Mary", "Jane", "Jim", "Jill", "Jack"]
print(friends_lists)
print(friends_lists[2])
friends_lists.append('Mutinda')
friends_lists.remove('Jim')
friends_lists.sort()
friends_lists.reverse()
friends_lists.pop()
friends_lists.insert(2, 'Mutinda')
friends_lists.clear()
friends_lists.copy()



print(len(friends_lists))
type(friends_lists)

prompt = f"The list of friends is {friends_lists}"
response = llm.invoke(prompt)
print(response.content)


# %%    



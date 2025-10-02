from tasklist import prompt
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

friends_lists = ["Peter", "John", "Mary", "Jane", "Jim", "Jill", "Jack"]
print(friends_lists)
print(friends_lists[2])
friends_lists.append('Mutinda')
print(f' the  lists after appending Mutinda is {friends_lists}')
friends_lists.remove('Jim')
print(f' the  lists after removing Jim is {friends_lists}')
friends_lists.sort()
print(f' the  lists after sorting is {friends_lists}')
friends_lists.reverse()
print(f' the  lists after reversing is {friends_lists}')
friends_lists.pop()
print(f' the  lists after popping is {friends_lists}')
friends_lists.insert(2, 'Mutinda')
print(f' the  lists after inserting Mutinda is {friends_lists}')
friends_lists.clear()
print(f' the  lists after clearing is {friends_lists}')
friends_lists.copy()
print(f' the  lists after copying is {friends_lists}')



print(len(friends_lists))
type(friends_lists)

prompt = f"The list of friends is {friends_lists}"
response = llm.invoke(prompt)
print(response.content)


# %%    



from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

to_do_tasks= ['clean the house', 'wash the car', 'buy groceries', 'do the laundry', 'mow the lawn']

for task in to_do_tasks:
    print(f'the task is to {task}')
    response = llm.invoke(f'the task is to {task}')
    print(response.content)


to_do_tasks.append('fix the bike')
for task in to_do_tasks:
    print(f'the task is to {task}')
    response = llm.invoke(f'the task is to {task}')
    print(response.content)


    
# %%    
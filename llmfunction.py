from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

print('~\_("/)_/~')
print(len('Hello, World!'))
print(round(45.639))
print('--------------------------------\n')


string_length = len('Global Warming!')
print(f'The length of the string is {string_length}')
print('--------------------------------\n')
name = 'John'
potatoes = 5

prompt = f'{name} has {potatoes} potatoes'
response = llm.invoke(prompt) 
print(response.content)
print('--------------------------------\n')

# Use print_llm_response() to print a poem with the specified number of lines. Use the 
# prompt variable to save your prompt before calling print_llm_response()

number_of_lines = 25
prompt = f""" Write the {number_of_lines} lines from a poem"""
response = llm.invoke(prompt)
print(response.content)
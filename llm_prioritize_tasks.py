from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# keys are the flavor names, values are the flavor descriptions
# values are the flavor descriptions
ice_cream_flavors = {
    "Vanilla": "Classic and creamy with a rich, smooth flavor from real vanilla beans.",
    "Chocolate": "Deep and indulgent, made with rich cocoa for a satisfying chocolate experience.",
    "Strawberry": "Sweet and fruity, bursting with the fresh taste of ripe strawberries.",
    "Mint Chocolate Chip": "Refreshing mint ice cream studded with decadent chocolate chips.",
    "Cookie Dough": "Vanilla ice cream loaded with chunks of chocolate chip cookie dough.",
    "Salted Caramel": "Sweet and salty with a smooth caramel swirl and a hint of sea salt.",
    "Pistachio": "Nutty and creamy, featuring the distinct taste of real pistachios.",
    "Cookies and Cream": "Vanilla ice cream packed with chunks of chocolate sandwich cookies.",
    "Mango": "Tropical and tangy, made with juicy mangoes for a refreshing treat.",
    "Rocky Road": "Chocolate ice cream mixed with marshmallows, nuts, and chocolate chunks."
}

cookie_dough_description = ice_cream_flavors["Cookie Dough"]
print(cookie_dough_description)

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

food_preferences = {
    "spicy": ["spicy", "hot", "sauce", "chili", "pepper"],
    "sweet": ["sweet", "sugar", "honey", "jam", "syrup"],
    "salty": ["salty", "salt", "sodium", "soup", "broth"],
    "savory": ["savory", "umami", "broth", "soup", "sauce"],
    "sour": ["sour", "acid", "vinegar", "lemon", "lime"],
    "bitter": ["bitter", "piquant", "tangy", "astringent", "umami"],
    "savory": ["savory", "umami", "broth", "soup", "sauce"],
    "sour": ["sour", "acid", "vinegar", "lemon", "lime"],
    "bitter": ["bitter", "piquant", "tangy", "astringent", "umami"],
}
print(food_preferences)
print("--------------------------------")
print(food_preferences.keys())
import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the API key from the environment variable
API_KEY = os.getenv('API_KEY')  # Fetch API key from .env
BASE_URL = 'https://api.spoonacular.com/recipes/findByIngredients'

def get_recipes(ingredients):
    url = f'{BASE_URL}?ingredients={ingredients}&number=5&apiKey={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Add a `run()` function to encapsulate the logic for this page
def run():
    # Title and Introduction with Emojis
    st.title('🍽️ Recipe Finder 🍳')
    st.write('🔍 Enter ingredients you have at home, and we will suggest some delicious recipes for you!')

    # User input for ingredients
    ingredients = st.text_input('🔑 Enter ingredients (comma separated):')

    if ingredients:
        # Show loading spinner while fetching recipes
        with st.spinner('Searching for recipes...'):
            recipes = get_recipes(ingredients)
        
        # If recipes are found
        if recipes:
            st.write(f"🍴 Here are some recipes you can make with the ingredients: {ingredients}:")
            
            # Display recipes in a grid-like format
            for recipe in recipes:
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.image(f"https://spoonacular.com/recipeImages/{recipe['id']}-312x231.jpg", width=200)
                with col2:
                    st.subheader(f"🍲 {recipe['title']}")
                    st.write(f"### Used ingredients: {', '.join([ingredient['name'] for ingredient in recipe['usedIngredients']])}")
                    st.write(f"### Missing ingredients: {', '.join([ingredient['name'] for ingredient in recipe['missedIngredients']])}")
                    st.write(f"🔗 [Link to Recipe](https://spoonacular.com/recipes/{recipe['id']})")
                    
        else:
            st.error('❌ Sorry, no recipes found. Please try different ingredients!')
    else:
        st.warning('⚠️ Please enter some ingredients to get started.')

# Call the run function
if __name__ == '__main__':
    run()

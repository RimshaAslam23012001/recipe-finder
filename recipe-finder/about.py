import streamlit as st

# Add a `run()` function to encapsulate the logic for this page
def run():
    st.title("ℹ️ About Recipe Finder App 🍽️")
    
    st.write("""
        🍳 **Welcome to the Recipe Finder App!** 🍳
        
        This app helps you find **delicious recipes** based on ingredients you already have at home. 
        Simply enter a list of ingredients (comma-separated), and the app will suggest recipes that include those ingredients.

        🌟 **Features:**
        - **Quick Recipe Search**: Enter ingredients and find related recipes instantly.
        - **Recipe Details**: See images, ingredients used, and missing ingredients.
        - **External Links**: Direct links to the full recipe instructions on Spoonacular.

        🥘 **How It Works:**
        1. Enter your ingredients in the input box (e.g., "chicken, tomato, onion").
        2. The app fetches matching recipes and displays them with pictures, ingredients, and links.
        3. Click on the recipe link to view the full details.

        🔗 The app uses the **Spoonacular API** to fetch recipes. You can explore their official [Spoonacular API documentation](https://spoonacular.com/food-api).

        👨‍🍳 **Happy Cooking!** 🎉
    """)

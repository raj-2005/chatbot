import os
import openai
import streamlit as st

# Fetch the OpenAI API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

# Function to get response from OpenAI ChatGPT model
def get_gpt_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the appropriate model
            messages=[{"role": "user", "content": user_input}],
            max_tokens=100,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit App Layout
st.title("Skin Cancer Detection Chatbot")

# Input box for user's query
user_query = st.text_input("Enter your question about skin cancer:", key="user_input")

if st.button("Submit"):
    if user_query:
        # Fetch response from OpenAI
        gpt_response = get_gpt_response(user_query)
        
        # Display the response
        st.write("**Chatbot Response:**")
        st.write(gpt_response)
    else:
        st.error("Please enter a question!")




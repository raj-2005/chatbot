#!/usr/bin/env python
# coding: utf-8

# In[6]:


pip install --upgrade openai


# In[7]:


import os
import openai
import streamlit as st

# Fetch the OpenAI API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

# Function to get response from OpenAI GPT model using the new API
def get_gpt_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You can use other models too, e.g., gpt-4
        messages=[{"role": "user", "content": user_input}],
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()

# Streamlit App Layout
st.title("Skin Cancer Detection Chatbot")

# Input box for user's query
user_query = st.text_input("Enter your question about skin cancer:")

if st.button("Submit"):
    if user_query:
        # Fetch response from OpenAI
        gpt_response = get_gpt_response(user_query)
        
        # Display the response
        st.write("**Chatbot Response:**")
        st.write(gpt_response)
    else:
        st.error("Please enter a question!")




# In[ ]:





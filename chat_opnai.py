import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = "OPEN_API_KEY"

SKIN_CANCER_CONTEXT = """
Skin cancer is the abnormal growth of skin cells, most often developing on skin exposed to the sun. 
There are three major types of skin cancer: basal cell carcinoma, squamous cell carcinoma, and melanoma. 
Melanoma is the most dangerous form of skin cancer. Possible signs of skin cancer include changes in the skin 
such as a new growth, a sore that doesn't heal, or a change in an existing mole. 
The ABCDE rule can help identify potential melanomas: Asymmetry, Border irregularity, Color changes, 
Diameter larger than 6mm, and Evolving size, shape, or color. Early detection and treatment are crucial 
for the best possible outcome. Regular skin checks and protecting your skin from UV radiation can help 
prevent skin cancer.
"""

def get_chatgpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": f"You are a helpful assistant that answers questions about skin cancer. Use this context for your answers: {SKIN_CANCER_CONTEXT}"},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    st.set_page_config(page_title="Skin Cancer Q&A Chatbot", page_icon="🏥", layout="wide")

    st.title("Skin Cancer Q&A Chatbot")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What is your question about skin cancer?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = get_chatgpt_response(prompt)
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()


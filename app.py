import streamlit as st

st.title("The Identity Echo Interface")
st.write("Welcome to the interface! Please provide your name and a message below to transmit to the system.")

user_name = st.text_input("Name")
user_message = st.text_input("Message")

if st.button("Transmit"):
    if not user_name.strip():
        st.error("Please provide your name.")
    elif not user_message.strip():
        st.warning("Please type a message to transmit.")
    else:
        st.success(f"Transmission successful! Greetings, {user_name}. We received your message: {user_message}")
        
        total_characters = len(user_message)
        token_count = total_characters / 4
        
        st.info(f"System Check: Your message will consume approximately {token_count:.2f} tokens from our context window.")

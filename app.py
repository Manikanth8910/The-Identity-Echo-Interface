import streamlit as st

def calculate_estimated_tokens(text: str) -> float:
    return len(text) / 4

def main() -> None:
    st.set_page_config(page_title="Identity Echo", page_icon="📡")
    
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
            
            token_count = calculate_estimated_tokens(user_message)
            st.info(f"System Check: Your message will consume approximately {token_count:.2f} tokens from our context window.")

if __name__ == "__main__":
    main()

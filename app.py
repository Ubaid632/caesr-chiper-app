

import streamlit as st

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]

    return encrypted_text

# Streamlit app layout
st.title("Ubaid's Cipher App")
st.write("The Caesar cipher encrypts any message by moving each letter depending on the shift value.")
st.write("Encrypt your text using the Caesar cipher.")

# Input for plain text
text = st.text_input("Enter the text to be encrypted/decrypted:")

# Input for shift value
shift = st.number_input("Enter the shift value (1-25):", min_value=1, max_value=25, value=5)

# Button to encrypt
if st.button("Encrypt Now!"):
    if text:
        encrypted_text = caesar(text, shift)
        st.write('**Plain text:**', text)
        st.write('**Encrypted text:**', encrypted_text)
    else:
        st.warning("Please enter a text to encrypt.")

# Button to decrypt
if st.button("Decrypt Now!"):
    if text:
        decrypted_text = caesar(text, -shift)  # Use negative shift for decryption
        st.write('**Input text:**', text)
        st.write('**Decrypted text:**', decrypted_text)
    else:
        st.warning("Please enter a text to decrypt.")

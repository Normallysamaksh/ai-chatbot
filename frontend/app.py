import streamlit as st
import requests

st.title("Samaksh's AI")
message= st.text_input("Enter your prompt...")

if st.button("Send"):
    response= requests.post(
        "http://127.0.0.1:8000/chat",
        json={
            "message": message
            }
        )
    data= response.json()
    st.write(data["response"])
        
    

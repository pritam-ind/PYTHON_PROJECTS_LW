import streamlit as st
import google.generativeai as genai

# import speech_recognition as sr
# import pyttsx3

import time as t

st.set_page_config(page_title="Public AI Interface", page_icon="🤖")
st.title("PUBLIC AI INTERFACE")


if "messages" not in st.session_state:
    st.session_state.messages = []


st_home, st_select, st_about = st.tabs(["Home", "Select Model", "About"])


with st_home:
    st.write("Welcome Friends, This is Our Own Home Dashboard!")
    st.info("Head over to the 'Select Model' tab to start chatting!")

with st_select:
    st.header("Please select")
    
    selection_model = ["Gemini", "ChatGPT", "Grok", "Deepseek"]
    
    user_selection = st.selectbox(
        "Choose your prefered AI Model",
        selection_model
    )

    
    if user_selection.lower() == "gemini":
        st.success("You are now chatting with Gemini!")
        
        
        api_key = st.text_input("Enter Google API Key:", type="password")
        
        
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

       
        if prompt := st.chat_input("Ask Gemini something..."):
            if not api_key:
                st.error("Please enter an API Key first!")
            else:
                
                with st.chat_message("user"):
                    st.markdown(prompt)
                
                st.session_state.messages.append({"role": "user", "content": prompt})

                
                try:
                    genai.configure(api_key=api_key)
                    
                    model = genai.GenerativeModel("gemini-2.5-flash")
                    
                    with st.chat_message("assistant"):
                        with st.spinner("Thinking..."):
                            response = model.generate_content(prompt)
                            st.markdown(response.text)
                    
                    
                    st.session_state.messages.append({"role": "assistant", "content": response.text})
                
                except Exception as e:
                    st.error(f"Error: {e}")

   
    elif user_selection.lower() == "chatgpt":
        st.warning("Sorry for the Inconvenience, ChatGPT model is not available now!\nWe will come in touch with you very soon!")
    elif user_selection.lower() == "grok":
        st.warning("Sorry for the Inconvenience, Grok model is not available now!\nWe will come in touch with you very soon!")
    elif user_selection.lower() == "deepseek":
        st.warning("Sorry for the Inconvenience, Deepseek model is not available now!\nWe will come in touch with you very soon!")


with st_about:
    st.header("This is Pritam's About Section!")
    st.write("""Hi, I am a student at Vivekananda Global University (VGU). This application was developed as part of my AI Internship Project. My goal was to create a user-friendly interface that integrates powerful LLMs like Gemini to help students and users interact with AI easily.

    Tech Stack: Python, Streamlit, Google Gemini API.""")

    
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("GitHub", "https://github.com/pritam-ind")
    with col2:
        st.link_button("LinkedIn", "https://github.com/pritam-ind")

    
    st.markdown("---")
    st.header("LinuxWorld & the Team")
    st.subheader("Internship Program!")
    
    try:
        st.image("LinuxWorldILinkedIn.png", width=300)
    except:
        st.info("Placeholder for Internship Image")
        
    st.write("""Created with ❤️ during the LinuxWorld Informatics Internship. This tool showcases the power of Python in building rapid AI prototypes. It demonstrates how modern AI can be made accessible to everyone through simple, effective web interfaces.""")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("Organization")
        st.link_button("LinuxWorld", "https://www.linkedin.com/company/linuxworld-informatics-pvt-ltd")

    with col2:
        st.write("Mentor")
        st.link_button("Mr. Vimal Daga", "https://www.linkedin.com/in/vimaldaga")

    with col3:
        st.write("Tech Head")
        st.link_button("Mr. Jibbran Ali", "https://www.linkedin.com/in/jibbran-ali")

    st.caption("© VGU Internship Project, All Rights Reserved 2025")
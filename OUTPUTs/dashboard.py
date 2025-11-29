import streamlit as st

st.set_page_config(page_title="Pritam Dashboard", page_icon="👁️")

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Home", "Calculator", "Unit Converter", "Contact"])

if page == "Home":
    st.title("Welcome To My Dashboard")
    st.header("Hi, I am Pritam, an Intern at LinuxWorld Informatics")
    
    st.write("I am a B.Tech student at Vivekananda Global University.")
    st.write("This dashboard shows my journey as an Intern at LinuxWorld Informatics.")
    st.write("Here are some demos of my projects")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("My Skills")
        st.write(" Python Programming")
        st.write(" Streamlit & Flask")
        st.write(" Linux Administration")
        st.write(" Machine Learning Basics")
        
    with col2:
        st.subheader("My Projects")
        st.write("* CALCULATOR")
        st.write("*  ATM LOGIC")
        st.write("* UNIT CONVERTER")
        st.write("* MOVIE TICKET BOOKING SYSTEM ")
        st.write("* POSITIVE-NEGATIVE CHECKER")
        st.write("* FILE TRANSFER")
        st.write("* PRITAM'S STREAMLIT DASHBOARD")
        st.write("* CHATBOT- AI ASSISTANT")
        st.write("* TEXT-TO-SPEECH CONVERTER ")
        st.write("* TIC-TAC-TOE GAME")
        st.write("* FLASK APP")
        st.write("* Email Automation")
        st.write("* SMS Automation  ")

elif page == "Calculator":
    st.title("My Python Calculator")
    st.write("This is a simple tool I built to practice logic.")
    n1 = st.number_input("Enter the first number")
    n2 = st.number_input("Enter the second number")
    op = st.selectbox("Select Operation", ["Add","Subtract", "Multiply","Divide"])
    if st.button("Calculate Result"):
        if op == "Add":
            ans = n1 + n2
            st.success(f"The sum is: {ans}")
        elif op == "Subtract":
            ans = n1 - n2
            st.success(f"The difference is: {ans}")
        elif op == "Multiply":
            an = n1*n2
            st.success(f"The multiplication is: {ans}")
        elif op== "Divide":
            if n2 != 0:
                ans = n1 /n2
                st.success(f"The division is: {ans}")
            else:
                st.error("Cannot divide by zero")

elif page== "Unit Converter":
    st.title("Unit Converter Tool")
    
    type = st.radio("Select Type", ["Temperature", "Currency"])
    if type == "Temperature":
        st.subheader("Celsius to Fahrenheit")
        c = st.number_input("Enter Celsius Value")
        if st.button("Convert Temp"):
            f = (c * 1.8) + 32
            st.info(f"{c} Celsius is equal to {f} Fahrenheit")
    elif type == "Currency":
        st.subheader("Rupee to Dollar")
        inr = st.number_input("Enter Amount in INR")
        if st.button("Convert Currency"):
            usd = inr / 86
            st.info(f"{inr} INR is approx {usd} USD")
            
elif page == "Contact":
    st.snow()
    st.title("Get in Touch")
    
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        msg = st.text_area("Your Message")
        
        submitted = st.form_submit_button("Send Message")
        if submitted:
            if name and email:
                st.success("Thanks for contacting me! I will reply soon.")
            else:
                st.warning("Please fill all details.")
    
    # st.write("LinkedIn: [Pritam's Profile](https://www.linkedin.com/in/pritam-ind)")
    st.write("Student at VGU, Jaipur")
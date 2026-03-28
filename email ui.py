import streamlit as st
import smtplib

st.set_page_config(page_title="Email Sender 📧")

# 🌈 Colorful background
st.markdown("""
<style>
.stApp {
    background: linear-gradient(270deg, 
        #ff9a9e, #fad0c4, #fbc2eb, #a6c1ee, #84fab0);
    background-size: 1000% 1000%;
    animation: gradient 12s ease infinite;
}

@keyframes gradient {
    0% {background-position: 0%}
    50% {background-position: 100%}
    100% {background-position: 0%}
}

.title {
    text-align: center;
    font-size: 35px;
    color: white;
    font-weight: bold;
}

.box {
    background: rgba(255,255,255,0.2);
    padding: 20px;
    border-radius: 15px;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">📧 Email Sender</p>', unsafe_allow_html=True)

st.markdown('<div class="box">', unsafe_allow_html=True)

# Input fields
sender_email = st.text_input("Your Email")
password = st.text_input("Password", type="password")
receiver_email = st.text_input("Receiver Email")
subject = st.text_input("Subject")
message = st.text_area("Message")


if st.button("Send Email 🚀"):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)

        email_message = f"Subject: {subject}\n\n{message}"
        server.sendmail(sender_email, receiver_email, email_message)

        server.quit()
        st.success("Email sent successfully ✅")

    except Exception as e:
        st.error("Error sending email ❌")

st.markdown('</div>', unsafe_allow_html=True)
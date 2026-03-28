import streamlit as st
import random
st.title("!!!!GUESS ME GAME!!!!!")
if"number"not in st.session_state:
    st.session_state.number=random.randint(1,100)
if"attempts" not in st.session_state:
    st.session_state.attempts=0
max_attempts=5
guess=st.number_input("Enter your guess",min_value=1,max_value=100)
if st.button("Submit guess"):
    st.session_state.attempts+=1
    if guess<st.session_state.number:
        st.warning("guess high!")
    elif guess>st.session_state.number:
        st.warning("guess low!")
    else:
        st.success(f"Congratualations! you guessed the number {st.session_state.number} in {st.session_state.attempts} attempts!")
        st.balloons()
        st.snow()
    if st.session_state.attempts>=max_attempts and guess != st.session_state.number:
        st.error(f"Game over! you've used all{max_attempts} attempts. The number was {st.session_state.number}.")
    st.write(f"Attempts remaining: {max_attempts - st.session_state.attempts}")
    if st.button("Restart"):
       st.session_state.number = random.randint(1, 100)
       st.session_state.attempts = 0
import streamlit as st

st.set_page_config(page_title="Happy Birthday Malu 🎉")

st.title("🎉 Happy 13th Birthday, Malu! 💛")

st.write("Welcome to your very own Inheritance Games 😉")

st.markdown("### 🧩 Your First Clue")
st.code("13 – 1 – 12 – 21")

answer = st.text_input("Enter your answer:")

if answer.lower() == "malu":
    st.success("Correct 😄")
    st.write("📖 Start at the beginning... Chapter 1")
    st.balloons()
else:
    st.info("Hint: A=1, B=2 😉")

st.markdown("---")
st.write("Hope your teenage years are full of mystery, fun, and amazing adventures ✨")

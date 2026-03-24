import streamlit as st
import base64
import os

st.set_page_config(page_title="The 13th Game 🎉", layout="centered")

# ---- Debug (remove later if you want) ----
st.write("Files in directory:", os.listdir())

# ---- Title ----
st.title("🎉 The 13th Game 🎉")
st.subheader("Happy 13th Birthday, Malu 💛")

# ---- Photo (IMPORTANT PART) ----
if os.path.exists("photo.jpeg"):
    st.image("photo.jpeg", use_container_width=True)
else:
    st.error("photo.jpeg not found ❌")

# ---- Message ----
st.markdown("""
### ✨ A Message for You

You’re officially a teenager now—and this is where things start getting interesting.

Stay curious. Stay confident. And enjoy every moment.

Because just like in *The Inheritance Games*… every clue leads to something bigger 😉
""")

# ---- Puzzle ----
st.markdown("### 🧩 Your First Clue")
st.code("13 – 1 – 12 – 21")

answer = st.text_input("Enter your answer:")

def play_music():
    with open("music.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()

    audio_html = f"""
    <audio autoplay>
    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

if answer.lower() == "malu":
    st.success("Correct 😄")
    play_music()
    st.balloons()

    st.markdown("""
    ## 🔓 You solved the first clue

    The game begins now.

    📖 Start at Chapter 1

    Good luck, Malu 😉
    """)
else:
    st.info("Hint: A = 1 😉")

# ---- Footer ----
st.markdown("---")
st.write("You solved the first clue. The real game begins now. 🔐✨")

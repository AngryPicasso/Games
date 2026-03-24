import streamlit as st
import base64

st.set_page_config(page_title="The 13th Game 🎉", layout="centered")

# ---- Helper to load local files ----
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ---- Background Image ----
bg_img = get_base64("photo.jpg")  # her photo
page_bg = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/jpg;base64,{bg_img}");
    background-size: cover;
    background-position: center;
}}
.block-container {{
    background-color: rgba(0,0,0,0.6);
    padding: 2rem;
    border-radius: 15px;
}}
h1, h2, h3, p {{
    color: white;
    text-align: center;
}}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ---- Background Music ----
audio_file = open("music.mp3", "rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mp3", autoplay=True)

# ---- Title ----
st.title("🎉 The 13th Game 🎉")

st.write("Happy 13th Birthday, Malu 💛")

# ---- Long Message ----
st.markdown("""
You’re officially a teenager now—and this is where things get exciting.

Not everything will always be easy, but that’s what makes it interesting.
You’ll discover new things, learn more about yourself, and create memories that actually matter.

Stay curious. Stay confident. And most importantly—enjoy the game.

Because just like in *The Inheritance Games*… every clue leads to something bigger 😉
""")

# ---- Puzzle ----
st.markdown("### 🧩 Your First Clue")
st.code("13 – 1 – 12 – 21")

answer = st.text_input("Enter your answer:")

if answer.lower() == "malu":
    st.success("Correct 😄")
    st.write("📖 Start at the beginning... Chapter 1")
    st.balloons()
else:
    st.info("Hint: A=1 😉")

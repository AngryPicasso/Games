import streamlit as st
import base64

st.set_page_config(page_title="The 13th Game 🎉", layout="centered")

# ---- Helper: Show Photo ----
def show_image():
    try:
        with open("photo.jpeg", "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()

        img_html = f"""
        <div style="text-align:center;">
            <img src="data:image/jpeg;base64,{b64}" 
            style="width:100%; max-width:500px; border-radius:15px;">
        </div>
        """
        st.markdown(img_html, unsafe_allow_html=True)

    except:
        st.error("photo.jpeg not found ❌")

# ---- Helper: Play Music ----
def play_music():
    try:
        with open("music.mp3", "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()

        audio_html = f"""
        <audio autoplay>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)

    except:
        st.warning("Music file not found 🎵")

# ---- Title ----
st.title("🎉 The 13th Game 🎉")
st.subheader("Happy 13th Birthday, Malu 💛")

# ---- Intro ----
st.markdown("""
You’ve been given a clue.

Solve it… and something special will be revealed 🔐
""")

# ---- Puzzle ----
st.markdown("### 🧩 Your First Clue")
st.code("13 – 1 – 12 – 21")

answer = st.text_input("Enter your answer:")

# ---- SUCCESS FLOW ----
if answer.lower() == "malu":
    st.success("Correct 😄")

    # 🎵 Play music
    play_music()

    # 🎉 Animation
    st.balloons()

    # 🖼️ Reveal photo
    show_image()

    # 💬 Message
    st.markdown("""
    ## 🔓 You unlocked it

    Happy 13th Birthday, Malu 💛

    This is just the beginning of something amazing.

    Keep smiling, keep dreaming, and enjoy every moment of your teenage years.

    📖 And now… your story begins.

    Start with Chapter 1 😉
    """)

else:
    st.info("Hint: A = 1 😉")

# ---- Footer ----
st.markdown("---")
st.write("The game has just begun 🔐✨")

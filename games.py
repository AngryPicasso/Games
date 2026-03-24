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
        st.error("Image not found ❌")

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
        pass

# ---- Title ----
st.title("🔐 The 13th Game")

# ---- Anonymous Intro ----
st.markdown("""
You’ve already taken the first step.

Most don’t make it this far.

Let’s see if you can solve what comes next.
""")

# ---- Transition (connects with A clue before link) ----
st.markdown("""
You already found where the story begins…

Now find who it’s about.
""")

# ---- Puzzle ----
st.markdown("### 🧩 Your First Clue")
st.code("13 – 1 – 12 – 21")

answer = st.text_input("Enter your answer:")

# ---- SUCCESS FLOW ----
if answer.lower() == "malu":
    st.success("Access Granted 🔓")

    # 🎵 Music
    play_music()

    # 🎈 Effect
    st.balloons()

    # 🖼️ Photo reveal
    show_image()

    # 🎭 Dramatic reveal first
    st.markdown("""
    ## You solved it.

    Not bad.

    Every game has a reason.
    Every clue leads somewhere.

    And this one… was always meant for you.
    """)

    # 🎉 Final birthday reveal
    st.markdown("""
    ---

    ### 🎉 Happy 13th Birthday, Malu 💛

    This was all for you.

    Welcome to your teenage era—  
    full of surprises, memories, and moments that matter.

    And just like this game…

    **this is only the beginning.**
    """)

else:
    st.info("Hint: A = 1 😉")

# ---- Footer ----
st.markdown("---")
st.write("The game has just begun 🔐")

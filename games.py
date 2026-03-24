import streamlit as st
import base64

st.set_page_config(page_title="The 13th Game 🎉", layout="centered")

# ---- Helper: Show Photo (base64) ----
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

# ---- Photo ----
show_image()

# ---- Message ----
st.markdown("""
### ✨ A Message for You

You’re officially a teenager now—and this is where things start getting interesting.

There will be new experiences, new challenges, and moments that shape who you become.

Stay curious. Stay confident. And enjoy every step of the journey.

Because just like in *The Inheritance Games*… every clue leads to something bigger 😉
""")

# ---- Puzzle ----
st.markdown("### 🧩 Your First Clue")
st.code("13 – 1 – 12 – 21")

answer = st.text_input("Enter your answer:")

if answer.lower() == "malu":
    st.success("Correct 😄")

    # 🎵 Play music
    play_music()

    # 🎉 Effects
    st.balloons()

    # 🔐 Reveal
    st.markdown("""
    ## 🔓 You solved the first clue

    And just like that… the game begins.

    Every mystery has a starting point.  
    Every story has a first page.

    📖 **Start at the beginning — Chapter 1**

    Good luck, Malu 😉
    """)

else:
    st.info("Hint: A = 1 😉")

# ---- Footer ----
st.markdown("---")
st.write("You solved the first clue. The real game begins now. 🔐✨")

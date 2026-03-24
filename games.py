import streamlit as st

st.set_page_config(page_title="The 13th Game 🎉", layout="centered")

# ---- Title ----
st.title("🎉 The 13th Game 🎉")
st.subheader("Happy 13th Birthday, Malu 💛")

# ---- Photo ----
st.image("photo.jpeg", use_container_width=True)

# ---- Background Music ----
try:
    with open("music.mp3", "rb") as audio_file:
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")
except:
    st.warning("Music file not found 🎵")

# ---- Message ----
st.markdown("""
### ✨ A Message for You

You’re officially a teenager now—and this is where things start getting interesting.

There will be new experiences, new challenges, and a lot of moments that shape who you become.  
But don’t overthink it—just enjoy it.

Stay curious. Stay confident. And always be yourself.

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
    st.info("Hint: A = 1 😉")

# ---- Footer ----
st.markdown("---")
st.write("You solved the first clue. The real game begins now. 🔐✨")

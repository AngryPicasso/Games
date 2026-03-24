import streamlit as st
import base64

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
    
    # 🎵 Play music on success
    play_music()
    
    # 🎉 Effects
    st.balloons()
    
    # 🔐 Reveal message
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

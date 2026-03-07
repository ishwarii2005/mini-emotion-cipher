import streamlit as st
import matplotlib.pyplot as plt

from emotion_model import detect_emotions
from emotion_encoder import encode_emotions
from encryption import encrypt_message, decrypt_message
from language_utils import process_text
from cache import get_cached_result, store_result
from timeline import update_emotion_history, get_emotion_history
from user_profile import learn_user_patterns, adjust_emotions


# Emotion code → name mapping
emotion_decode = {
    "01": "Joy",
    "02": "Sadness",
    "03": "Anger",
    "04": "Fear",
    "05": "Surprise",
    "06": "Disgust",
    "07": "Neutral"
}


st.title("Mini Emotion Cipher")
st.caption("Emotion-aware encryption system that preserves emotional insight without exposing the message.")

user_input = st.text_area("Enter your message")


# ANALYZE & ENCRYPT
if st.button("Analyze & Encrypt"):

    text = user_input.strip()

    if text == "":
        st.warning("Please enter a message.")
    else:

        cached = get_cached_result(text)

        if cached:
            emotions = cached
        else:

            processed = process_text(text)

            emotions = detect_emotions(processed)

            emotions = adjust_emotions(text, emotions)

            store_result(text, emotions)

            learn_user_patterns(text, emotions)

        update_emotion_history(emotions)

        emotion_code = encode_emotions(emotions)

        st.session_state.packet = encrypt_message(text, emotion_code)
        st.session_state.emotions = emotions
        st.session_state.decrypted = False

        st.success("Message encrypted successfully.")


# SHOW EMOTION CONFIDENCE
if "emotions" in st.session_state:

    st.subheader("Emotion Confidence")

    emotions = st.session_state.emotions

    for emotion, score in emotions.items():

        # clamp score to valid range
        score = max(0, min(score, 1))

        percent = min(round(score * 100, 1), 100)

        bar_value = percent / 100

        st.write(f"{emotion.capitalize()} — {percent}%")

        st.progress(bar_value)


# SHOW ENCRYPTED PACKET
if "packet" in st.session_state and not st.session_state.get("decrypted", False):

    st.subheader("Encrypted Packet")

    st.code(st.session_state.packet, language="json")

    if st.button("Decrypt Message"):

        message, code = decrypt_message(st.session_state.packet)

        st.session_state.decrypted = True
        st.session_state.decrypted_message = message
        st.session_state.decrypted_code = code


# SHOW DECRYPTED OUTPUT
if st.session_state.get("decrypted", False):

    st.subheader("Decrypted Output")

    message = st.session_state.decrypted_message
    code = st.session_state.decrypted_code

    decoded = [emotion_decode.get(c, "Unknown") for c in code.split("|")]

    st.write("Message:", message)
    st.write("Detected Emotions:", ", ".join(decoded))


# EMOTION DISTRIBUTION CHART
st.subheader("Emotion Distribution")

history = get_emotion_history()

if history:

    emotions = list(history.keys())
    counts = list(history.values())

    fig, ax = plt.subplots()

    ax.bar(emotions, counts)

    ax.set_xlabel("Emotion")
    ax.set_ylabel("Frequency")
    ax.set_title("Emotion Distribution")

    st.pyplot(fig)
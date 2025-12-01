import streamlit as st
from googletrans import Translator

# Initialize translator
translator = Translator()

# Streamlit app
st.title("🌐 English to Odia Translator")

st.write("Type any English text below and get the Odia translation instantly.")

# Input text
english_text = st.text_area("Enter English text:")

# Translate button
if st.button("Translate"):
    if english_text.strip() != "":
        try:
            # Perform translation
            translation = translator.translate(english_text, src="en", dest="or")
            st.success("✅ Translation:")
            st.text_area("Odia Translation:", translation.text, height=150)
        except Exception as e:
            st.error(f"Translation failed: {e}")
    else:
        st.warning("Please enter some text to translate.")


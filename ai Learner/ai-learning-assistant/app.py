import streamlit as st
from pdf_parser import extract_text_from_pdf
from summarizer import summarize_text

st.set_page_config(page_title="📚 AI Learning Assistant", page_icon="🤖")

st.title("🤖 AI Learning Assistant")
st.subheader("Upload your notes, type content, or get instant quizzes!")

uploaded_file = st.file_uploader("📤 Upload PDF", type="pdf")

if uploaded_file is not None:
    try:
        with st.spinner("Extracting text from PDF..."):
            raw_text = extract_text_from_pdf(uploaded_file)
            st.success("Text extracted successfully!")
    except Exception as e:
        st.error(f"Error extracting text: {e}")
        raw_text = ""

    if raw_text and st.button("🧠 Generate Summary"):
        with st.spinner("Generating summary using AI..."):
            try:
                summary = summarize_text(raw_text)
                st.text_area("📑 Summary", summary, height=300)
            except Exception as e:
                st.error(f"Error generating summary: {e}")

user_input = st.text_area("🎤 Type your text here")
if st.button("✅ Submit Text") and user_input.strip():
    with st.spinner("Processing your input..."):
        try:
            summary = summarize_text(user_input)
            st.text_area("📑 Summary", summary, height=300)
        except Exception as e:
            st.error(f"Error generating summary: {e}")

if 'show_quiz' not in st.session_state:
    st.session_state.show_quiz = False

if st.button("❓ Generate Quiz"):
    st.session_state.show_quiz = True

if st.session_state.show_quiz:
    st.subheader("📚 Quiz Time!")
    st.write("Q1: What are the key ideas of the uploaded text?")
    st.text_input("Answer 1")
    st.write("Q2: List two important details.")
    st.text_input("Answer 2")
    st.write("Q3: Summarize the text in one sentence.")
    st.text_input("Answer 3")

st.markdown("---")
st.caption("by Pradhyumn")

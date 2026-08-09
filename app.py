import streamlit as st
from Modules.llm import ask_gemini

st.title("LLM RAG Chat")

uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

if uploaded_file is not None:
    with st.spinner("Processing file..."):


        st.success("File processed successfully! You can now ask questions about the PDF.")

        question = st.text_input("Ask a question:")

        if st.button("Answer"):
            if question:
                context = "your retrieved context here"  # مؤقت
                answer = ask_gemini(question, context)

                st.subheader("Answer")
                st.write(answer)
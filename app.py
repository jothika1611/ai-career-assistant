import streamlit as st
from modules.pdf_loader import load_pdf
from modules.vector_store import create_vector_store
from modules.rag_pipeline import chat_with_pdf
from modules.resume_analyzer import analyze_resume


st.set_page_config(
    page_title="AI Career Assistant",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1100px;
    }
    h1 { color: #1e40af; font-size: 2.7rem !important; }
    h2, h3 { color: #1e3a8a; margin-top: 1.6rem; }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        background-color: #f8fafc;
        border-radius: 10px;
        padding: 0.5rem 1.2rem;
        margin-bottom: 1.8rem;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        color: #475569;
        font-weight: 600;
        font-size: 1.05rem;
        border-radius: 8px;
        padding: 0 24px !important;
    }
    .stTabs [aria-selected="true"] {
        background-color: #3b82f6 !important;
        color: white !important;
    }
    .stButton > button {
        background: #2563eb;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.7rem 1.5rem;
        font-weight: 600;
    }
    .stButton > button:hover {
        background: #1d4ed8;
    }
    hr {
        border-color: #e2e8f0;
        margin: 2rem 0 1.4rem 0;
    }
    </style>
""", unsafe_allow_html=True)


st.title("💼 AI Career Assistant")
st.markdown("Analyze your resume or chat with any PDF document — powered by AI.")
st.markdown("---")


tab1, tab2 = st.tabs(["📄 Resume Analyzer", "📚 PDF Chatbot"])

# ────────────────────────────────────────────────
# Tab 1: Resume Analyzer
# ────────────────────────────────────────────────
with tab1:
    st.subheader("Resume Analysis")
    st.markdown("Upload your resume PDF and get AI-powered insights and suggestions.")

    resume_file = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"],
        key="resume_uploader"
    )

    if resume_file:
        if st.button("Analyze Resume", type="primary"):
            with st.spinner("Processing resume..."):
                try:
                    resume_text = load_pdf(resume_file)
                    result = analyze_resume(resume_text)
                    st.success("Analysis complete!")
                    st.markdown("### Result")
                    st.markdown(result)
                except Exception as e:
                    st.error(f"Error during analysis: {str(e)}")

# ────────────────────────────────────────────────
# Tab 2: PDF Chatbot
# ────────────────────────────────────────────────
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with tab2:
    st.subheader("Chat with PDF")
    st.markdown("Ask questions about your uploaded document.")

    pdf_file = st.file_uploader(
        "Upload PDF document",
        type=["pdf"],
        key="pdf_uploader"
    )

    if pdf_file:
        if "current_pdf_name" not in st.session_state or st.session_state.current_pdf_name != pdf_file.name:
            with st.spinner("Reading PDF and building vector store..."):
                try:
                    text = load_pdf(pdf_file)
                    st.session_state.vector_db = create_vector_store(text)
                    st.session_state.current_pdf_name = pdf_file.name
                    st.success("Document is ready! You can now ask questions.")
                except Exception as e:
                    st.error(f"Error processing document: {str(e)}")
                    st.session_state.vector_db = None
        else:
            st.success("Document already loaded. Ask anything!")

    else:
        st.info("Please upload a PDF document first.")
        st.session_state.vector_db = None

    if "vector_db" in st.session_state and st.session_state.vector_db is not None:
        with st.form(key="pdf_chat_form", clear_on_submit=True):
            col1, col2 = st.columns([7, 2])

            with col1:
                question = st.text_input(
                    "Your question about the document",
                    placeholder="Ask something... (press Enter or click Send)",
                    label_visibility="collapsed",
                    key="question_input_form"
                )

            with col2:
                submit_button = st.form_submit_button(
                    "Send",
                    type="primary",
                    use_container_width=True
                )

        if submit_button and question.strip():
            with st.spinner("Generating answer..."):
                try:
                    answer = chat_with_pdf(
                        question,
                        st.session_state.vector_db,
                        st.session_state.chat_history
                    )
                    st.session_state.chat_history.append((question, answer))
                except Exception as e:
                    st.error(f"Error generating answer: {str(e)}")
                    answer = None

            if 'answer' in locals() and answer:
                st.markdown("**Answer:**")
                st.markdown(answer)

        
        if st.session_state.chat_history:
            st.markdown("### Conversation")
            for idx, entry in enumerate(st.session_state.chat_history, 1):
                if isinstance(entry, tuple) and len(entry) == 2:
                    q, a = entry
                    st.markdown(f"**Q{idx}:** {q}")
                    st.markdown(f"**A{idx}:** {a}")
                else:
                    st.markdown(f"**Entry {idx}:** (invalid format)")
                st.markdown("---")


        if st.button("🗑️ Clear chat history", use_container_width=False):
            st.session_state.chat_history = []
            st.rerun()


# Footer

st.markdown("---")
st.caption(f"AI Career Assistant • Streamlit {st.__version__} • 2025")
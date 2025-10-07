"""
YouTube RAG Question Answering App
A Streamlit web application for asking questions about YouTube videos using RAG.
"""

import streamlit as st
import re
from src.utils.transcript_fetcher import TranscriptFetcher
from src.utils.vector_store import VectorStoreManager
from src.utils.rag_chain import RAGChain

# Page config
st.set_page_config(
    page_title="YouTube RAG Q&A",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #ff6b6b;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 2rem;
    }
    .success-message {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        padding: 1rem;
        border-radius: 0.375rem;
        margin: 1rem 0;
    }
    .error-message {
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
        padding: 1rem;
        border-radius: 0.375rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def extract_video_id(url):
    """Extract video ID from YouTube URL"""
    patterns = [
        r'(?:v=|\/)([0-9A-Za-z_-]{11}).*',
        r'(?:youtu\.be\/)([0-9A-Za-z_-]{11})',
        r'(?:embed\/)([0-9A-Za-z_-]{11})'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def initialize_session_state():
    """Initialize session state variables"""
    if 'transcript_fetched' not in st.session_state:
        st.session_state.transcript_fetched = False
    if 'vector_store' not in st.session_state:
        st.session_state.vector_store = None
    if 'rag_chain' not in st.session_state:
        st.session_state.rag_chain = None
    if 'current_video_id' not in st.session_state:
        st.session_state.current_video_id = None
    if 'selected_question' not in st.session_state:
        st.session_state.selected_question = ""
    if 'answer' not in st.session_state:
        st.session_state.answer = ""

def main():
    initialize_session_state()
    
    # Header
    st.markdown('<h1 class="main-header">🎥 YouTube RAG Q&A</h1>', unsafe_allow_html=True)
    st.markdown("### Ask questions about any YouTube video using AI-powered retrieval!")
    
    # Sidebar
    with st.sidebar:
        st.header("📹 Video Setup")
        
        # YouTube URL input
        youtube_url = st.text_input(
            "Enter YouTube URL:",
            placeholder="https://www.youtube.com/watch?v=...",
            help="Paste any YouTube video URL here"
        )
        
        # Extract video ID
        video_id = None
        if youtube_url:
            video_id = extract_video_id(youtube_url)
            if video_id:
                st.success(f"✅ Video ID detected: {video_id}")
            else:
                st.error("❌ Invalid YouTube URL")
        
        # Process video button
        if st.button("🔄 Process Video", disabled=not video_id):
            if video_id != st.session_state.current_video_id:
                with st.spinner("Fetching transcript and setting up RAG..."):
                    try:
                        # Fetch transcript
                        fetcher = TranscriptFetcher()
                        transcript = fetcher.get_transcript(video_id)
                        
                        if transcript:
                            # Create vector store
                            vector_manager = VectorStoreManager()
                            vector_store = vector_manager.create_vector_store(transcript)
                            
                            # Initialize RAG chain
                            rag_chain = RAGChain(vector_store)
                            
                            # Update session state
                            st.session_state.transcript_fetched = True
                            st.session_state.vector_store = vector_store
                            st.session_state.rag_chain = rag_chain
                            st.session_state.current_video_id = video_id
                            
                            st.success("✅ Video processed successfully!")
                        else:
                            st.error("❌ Failed to fetch transcript")
                            
                    except Exception as e:
                        st.error(f"❌ Error processing video: {str(e)}")
        
        # Video info
        if st.session_state.transcript_fetched:
            st.success("🎯 Ready for Q&A!")
            if st.button("🗑️ Clear Session"):
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                st.rerun()
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("💬 Ask Questions")
        
        if not st.session_state.transcript_fetched:
            st.info("👈 Please enter a YouTube URL and process the video first!")
        else:
            # Question input
            question = st.text_input(
                "Your question:",
                value=st.session_state.selected_question,
                placeholder="What is this video about?",
                help="Ask any question about the video content",
                key="question_input"
            )
            
            # Answer button
            if st.button("🔍 Get Answer", disabled=not question):
                if st.session_state.rag_chain:
                    with st.spinner("Generating answer..."):
                        try:
                            answer = st.session_state.rag_chain.get_answer(question)
                            st.session_state.answer = answer
                            
                        except Exception as e:
                            st.session_state.answer = f"❌ Error generating answer: {str(e)}"
            
            # Display answer in main area
            if st.session_state.answer:
                st.subheader("📝 Answer:")
                st.write(st.session_state.answer)
    
    with col2:
        st.header("ℹ️ How it works")
        st.markdown("""
        1. **Enter URL**: Paste any YouTube video URL
        2. **Process**: Click 'Process Video' to fetch transcript
        3. **Ask**: Type your question about the video
        4. **Get Answer**: AI will answer based on video content
        
        ### ⚡ Features:
        - 🎯 RAG-powered Q&A
        - 🔍 Semantic search
        - 🧠 Context-aware answers
        - 🌐 Multi-language support
        """)
        
        # Example questions
        if st.session_state.transcript_fetched:
            st.subheader("💡 Example Questions:")
            example_questions = [
                "What is the main topic of this video?",
                "Can you summarize the key points?",
                "What are the important concepts discussed?",
                "Who are the people mentioned in the video?"
            ]
            
            for i, eq in enumerate(example_questions):
                if st.button(f"📌 {eq}", key=f"example_{i}"):
                    # Set the selected question in session state
                    st.session_state.selected_question = eq
                    # Clear previous answer
                    st.session_state.answer = ""
                    # Trigger a rerun to update the input field
                    st.rerun()

if __name__ == "__main__":
    main()
"""
Vector Store Manager Module
Handles text chunking, embedding generation, and vector store creation.
"""

import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from typing import Optional


class VectorStoreManager:
    """Manages text splitting and vector store creation"""
    
    def __init__(self, 
                 chunk_size: int = 1000, 
                 chunk_overlap: int = 200,
                 model_name: str = "sentence-transformers/all-mpnet-base-v2"):
        """
        Initialize vector store manager
        
        Args:
            chunk_size (int): Size of text chunks
            chunk_overlap (int): Overlap between chunks
            model_name (str): HuggingFace embedding model name
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.model_name = model_name
        
        # Initialize text splitter
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )
        
        # Initialize embeddings (cached)
        self.embeddings = self._get_embeddings()
    
    @st.cache_resource
    def _get_embeddings(_self):
        """Get cached embeddings model"""
        return HuggingFaceEmbeddings(model_name=_self.model_name)
    
    def create_vector_store(self, transcript: str) -> Optional[FAISS]:
        """
        Create FAISS vector store from transcript
        
        Args:
            transcript (str): Video transcript text
            
        Returns:
            FAISS: Vector store object or None if failed
        """
        try:
            # Split text into chunks
            chunks = self.text_splitter.create_documents([transcript])
            
            st.sidebar.info(f"📊 Created {len(chunks)} text chunks")
            
            # Create vector store
            vector_store = FAISS.from_documents(chunks, self.embeddings)
            
            st.sidebar.success("✅ Vector store created successfully!")
            
            return vector_store
            
        except Exception as e:
            st.sidebar.error(f"❌ Error creating vector store: {str(e)}")
            return None
    
    def get_chunk_info(self, transcript: str) -> dict:
        """
        Get information about how text will be chunked
        
        Args:
            transcript (str): Text to analyze
            
        Returns:
            dict: Information about chunking
        """
        chunks = self.text_splitter.create_documents([transcript])
        
        return {
            "total_chunks": len(chunks),
            "avg_chunk_size": sum(len(chunk.page_content) for chunk in chunks) / len(chunks),
            "total_chars": len(transcript),
            "chunk_size": self.chunk_size,
            "chunk_overlap": self.chunk_overlap
        }
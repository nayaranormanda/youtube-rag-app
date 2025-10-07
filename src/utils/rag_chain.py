"""
RAG Chain Module
Handles the retrieval-augmented generation chain for question answering.
"""

import streamlit as st
import os
from langchain_perplexity import ChatPerplexity
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda, RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import FAISS
from typing import Optional
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


class RAGChain:
    """Handles RAG-based question answering"""
    
    def __init__(self, vector_store: FAISS, model: str = "sonar", temperature: float = 0):
        """
        Initialize RAG chain
        
        Args:
            vector_store (FAISS): Vector store for retrieval
            model (str): Perplexity model name
            temperature (float): Model temperature
        """
        self.vector_store = vector_store
        self.model = model
        self.temperature = temperature
        
        # Initialize components
        self.llm = self._get_llm()
        self.retriever = self._get_retriever()
        self.prompt = self._get_prompt()
        self.chain = self._create_chain()
    
    def _get_llm(self):
        """Initialize language model"""
        try:
            return ChatPerplexity(model=self.model, temperature=self.temperature)
        except Exception as e:
            st.error(f"❌ Error initializing LLM: {str(e)}")
            st.error("Make sure you have set your PPLX_API_KEY in the .env file")
            return None
    
    def _get_retriever(self):
        """Create retriever from vector store"""
        return self.vector_store.as_retriever(
            search_type="similarity", 
            search_kwargs={"k": 4}
        )
    
    def _get_prompt(self):
        """Create prompt template"""
        return PromptTemplate(
            template="""You are a helpful AI assistant analyzing a YouTube video transcript. 
            Use the following pieces of context to answer the question at the end.
            
            If you don't know the answer based on the provided context, just say that you don't know, 
            don't try to make up an answer.
            
            Context:
            {context}
            
            Question: {question}
            
            Answer: """,
            input_variables=["context", "question"],
        )
    
    def _format_context(self, docs):
        """Format retrieved documents into context string"""
        return "\n\n".join([doc.page_content for doc in docs])
    
    def _create_chain(self):
        """Create the complete RAG chain"""
        if not self.llm:
            return None
            
        # Create parallel chain for context and question
        parallel_chain = RunnableParallel({
            'context': self.retriever | RunnableLambda(self._format_context),
            'question': RunnablePassthrough(),
        })
        
        # Create complete chain
        parser = StrOutputParser()
        return parallel_chain | self.prompt | self.llm | parser
    
    def get_answer(self, question: str) -> Optional[str]:
        """
        Get answer for a question using RAG
        
        Args:
            question (str): User question
            
        Returns:
            str: Generated answer or None if failed
        """
        if not self.chain:
            return "❌ RAG chain not properly initialized. Please check your API key."
        
        try:
            answer = self.chain.invoke(question)
            return answer
            
        except Exception as e:
            st.error(f"❌ Error generating answer: {str(e)}")
            return f"Sorry, I encountered an error while processing your question: {str(e)}"
    
    def get_relevant_context(self, question: str) -> list:
        """
        Get relevant context chunks for a question
        
        Args:
            question (str): User question
            
        Returns:
            list: List of relevant document chunks
        """
        try:
            docs = self.retriever.invoke(question)
            return [{"content": doc.page_content, "metadata": doc.metadata} for doc in docs]
        except Exception as e:
            st.error(f"❌ Error retrieving context: {str(e)}")
            return []
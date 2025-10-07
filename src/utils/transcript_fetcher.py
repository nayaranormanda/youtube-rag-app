"""
Transcript Fetcher Module
Handles YouTube transcript fetching with error handling and language support.
"""

import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from typing import Optional


class TranscriptFetcher:
    """Handles fetching transcripts from YouTube videos"""
    
    def __init__(self):
        self.api = YouTubeTranscriptApi()
    
    def get_transcript(self, video_id: str, languages: list = None) -> Optional[str]:
        """
        Fetch transcript for a YouTube video
        
        Args:
            video_id (str): YouTube video ID
            languages (list): List of language codes to try (default: ['en', 'hi'])
            
        Returns:
            str: Combined transcript text or None if failed
        """
        if languages is None:
            languages = ['en', 'hi']
            
        try:
            # Fetch transcript
            transcript_list = self.api.fetch(video_id, languages=languages)
            
            # Combine all transcript snippets
            transcript = " ".join([snippet.text for snippet in transcript_list])
            
            # Display success info
            st.sidebar.success(f"📄 Transcript fetched: {len(transcript)} characters")
            
            return transcript
            
        except TranscriptsDisabled:
            st.sidebar.error("❌ Transcripts are disabled for this video")
            return None
            
        except NoTranscriptFound:
            st.sidebar.error("❌ No transcript found for this video")
            return None
            
        except Exception as e:
            st.sidebar.error(f"❌ Error fetching transcript: {str(e)}")
            return None
    
    def get_available_languages(self, video_id: str) -> list:
        """
        Get list of available transcript languages for a video
        
        Args:
            video_id (str): YouTube video ID
            
        Returns:
            list: List of available language codes
        """
        try:
            transcript_list = self.api.list(video_id)
            return [transcript.language_code for transcript in transcript_list]
        except Exception:
            return []
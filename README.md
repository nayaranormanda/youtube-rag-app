# 🎥 YouTube RAG Question Answering App

A Streamlit web application that enables users to ask questions about YouTube videos using Retrieval-Augmented Generation (RAG). The app fetches video transcripts, creates embeddings, and uses AI to answer questions based on the video content.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

- 🎯 **RAG-powered Q&A**: Ask natural language questions about any YouTube video
- 🔍 **Semantic Search**: Advanced retrieval using vector embeddings
- 🧠 **Context-aware Answers**: AI generates answers based on actual video content
- 🌐 **Multi-language Support**: Supports videos with English and Hindi transcripts
- 🎨 **Clean UI**: Beautiful Streamlit interface with intuitive design
- ⚡ **Fast Processing**: Efficient vector storage and retrieval

## 🚀 Demo

1. Enter a YouTube URL
2. Click "Process Video" to fetch transcript and create embeddings
3. Ask any question about the video content
4. Get AI-powered answers based on the actual transcript

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- Perplexity API key (get it from [Perplexity AI](https://www.perplexity.ai/settings/api))

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/youtube-rag-app.git
   cd youtube-rag-app
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.template .env
   # Edit .env and add your PPLX_API_KEY
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 📝 Environment Variables

Create a `.env` file with the following variables:

```env
# Required
PPLX_API_KEY=your_perplexity_api_key_here

# Optional
HUGGINGFACE_API_TOKEN=your_huggingface_token_here
```

## 🏗️ Project Structure

```
youtube-rag-app/
├── app.py                      # Main Streamlit application
├── src/
│   ├── __init__.py
│   └── utils/
│       ├── __init__.py
│       ├── transcript_fetcher.py   # YouTube transcript handling
│       ├── vector_store.py         # Text chunking and embeddings
│       └── rag_chain.py           # RAG chain implementation
├── requirements.txt            # Python dependencies
├── .env.template              # Environment variables template
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

## 🔧 How It Works

1. **Transcript Fetching**: Uses `youtube-transcript-api` to extract video transcripts
2. **Text Processing**: Splits transcript into manageable chunks using LangChain's text splitter
3. **Embeddings**: Creates vector embeddings using HuggingFace's `all-mpnet-base-v2` model
4. **Vector Storage**: Stores embeddings in FAISS for efficient similarity search
5. **Question Answering**: Uses Perplexity AI with retrieved context to generate answers

## 🎯 Usage Examples

### Example Questions:
- "What is the main topic of this video?"
- "Can you summarize the key points discussed?"
- "Who are the people mentioned in the video?"
- "What are the important concepts explained?"

### Supported Video Types:
- Educational content
- Tutorials and how-to videos
- Lectures and presentations
- Interviews and discussions
- Any video with available transcripts

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LangChain](https://python.langchain.com/) for the RAG framework
- [Streamlit](https://streamlit.io/) for the web app framework
- [Perplexity AI](https://www.perplexity.ai/) for the language model
- [HuggingFace](https://huggingface.co/) for embeddings models
- [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) for transcript extraction

## ⚠️ Limitations

- Requires videos to have available transcripts
- Transcript availability depends on YouTube's auto-generation or manual upload
- API rate limits may apply based on your Perplexity AI plan
- Processing time depends on video length and transcript size

## 🔮 Future Enhancements

- [ ] Support for multiple video URLs
- [ ] Transcript translation capabilities
- [ ] Chat history and conversation context
- [ ] Video timestamp references in answers
- [ ] Export Q&A sessions
- [ ] Support for additional language models

## 📧 Contact

For questions or suggestions, please open an issue on GitHub or contact [your-email@example.com](mailto:your-email@example.com).

---

Made with ❤️ and AI
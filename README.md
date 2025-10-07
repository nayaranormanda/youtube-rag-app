# 🎥 YouTube RAG Question Answering App

A Streamlit web application that enables users to ask questions about YouTube videos using Retrieval-Augmented Generation (RAG). The app fetches video transcripts, creates embeddings, and uses AI to answer questions based on the video content.

**Main Purpose**: This project was created to understand and utilize different LangChain components in a practical, real-world application. It demonstrates the integration of various LangChain modules including text splitters, vector stores, embeddings, retrievers, prompts, and chains to build a complete RAG system.

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
- 🔗 **LangChain Integration**: Demonstrates practical usage of multiple LangChain components
- 📚 **Educational**: Perfect for learning how to build RAG systems with LangChain

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

This project demonstrates the practical implementation of various LangChain components:

1. **Transcript Fetching**: Uses `youtube-transcript-api` to extract video transcripts
2. **Text Processing**: Implements LangChain's `RecursiveCharacterTextSplitter` for optimal text chunking
3. **Embeddings**: Utilizes LangChain's `HuggingFaceEmbeddings` with `sentence-transformers/all-mpnet-base-v2` model
4. **Vector Storage**: Leverages LangChain's `FAISS` integration for efficient similarity search
5. **Retrieval**: Creates a retriever using LangChain's vector store interface
6. **Prompt Engineering**: Uses LangChain's `PromptTemplate` for structured prompt creation
7. **Chain Construction**: Implements LangChain's `RunnableParallel` and `RunnableLambda` for complex workflows
8. **Question Answering**: Integrates everything into a complete RAG pipeline using LangChain's chain paradigm

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

For questions or suggestions, please open an issue on GitHub or contact [harshvirani.91@gmail.com](mailto:harshvirani.91@gmail.com).

---

Made with ❤️ and AI
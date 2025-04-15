React Docs Chatbot - Context-Aware Support Assistant

This project is a context-aware chatbot built using FastAPI, ChromaDB, Sentence Transformers, and the Gemini LLM API. It is designed to help users get precise and relevant answers from documentation-based sources like React.js or JavaScript.

The chatbot uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from documentation pages and leverages Gemini to provide detailed responses. It can be adapted to build a contextual assistant for any documentation-based website.

✨ Features

✏️ Web Crawler: Automatically scrapes content from a documentation site.

🔗 ChromaDB Integration: Stores the scraped content as embeddings for semantic search.

✨ Sentence Transformers: Encodes questions and documents for similarity search.

⚙️ RAG-powered Responses: Retrieves relevant documents from ChromaDB and uses Gemini API to generate focused, context-aware answers.

💬 FastAPI Backend: RESTful API endpoints for chatbot interaction.

⚖️ Session Management: Uses Redis to manage chat history and sessions.

📊 Easy Customization: Simply change the base documentation URL to create a chatbot for any product.

🚀 How It Works

Scraping Documentation:

The built-in web scraper visits all pages of a documentation site starting from a base URL.

Extracts and stores the text content from each page.

Embedding the Data:

The scraped content is passed through a SentenceTransformer model to generate embeddings.

These embeddings, along with source metadata, are stored in ChromaDB for semantic search.

Query Flow:

A user submits a question via FastAPI endpoint.

The question is embedded and matched against the most relevant documents in ChromaDB.

The retrieved context is sent to the Gemini API, which generates a precise and on-topic answer.

Session Handling (Optional):

Supports multi-turn conversations with contextual continuity.

Redis is used to store chat history per session.

🚀 Build Your Own Chatbot

To adapt this chatbot for any other product documentation:

Update the base_url in the main() function to point to the new documentation site.

Run the script to scrape and ingest the new documentation into ChromaDB.

Start the FastAPI server and begin asking questions.

🤝 Why Use ChromaDB?

ChromaDB is used for efficient vector similarity search. It allows:

Fast retrieval of relevant documents using embeddings.

Persistent storage and metadata support.

Easy integration with models like Sentence Transformers.

🚀 Why Gemini for Response Generation?

Gemini LLM is used to:

Summarize and respond using only the most relevant context.

Avoid hallucinations by sticking to the retrieved data.

Generate helpful and actionable responses for developers.

⚡ Dependencies

This project uses the following Python packages:

fastapi

uvicorn

requests

beautifulsoup4

sentence-transformers

chromadb

transformers

pydantic

accelerate

redis

🚀 Use Cases

Developer support bots for frameworks like React, Vue, Angular, etc.

Internal documentation assistants.

Product support chatbots for SaaS tools.

Personal AI assistants for custom knowledge bases.

🙏 Contribution & Feedback

Feel free to contribute or raise issues. You can extend this to support multiple collections, UI integration, or multilingual responses.

📅 Future Improvements

Add authentication for APIs

Integrate front-end UI

Improve scraping with JS-rendering (Selenium or Playwright)

Support for multiple document sources or languages

🚫 Disclaimer

Please make sure not to expose your Gemini API key publicly. Replace it with environment variables for production use.

📍 Credits

Built with ❤️ using FastAPI, ChromaDB, and Gemini LLM.

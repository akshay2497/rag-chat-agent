# React Docs Chatbot - Context-Aware Support Assistant

This project is a context-aware chatbot built using FastAPI, ChromaDB, Sentence Transformers, and the Gemini LLM API. It is designed to help users get precise and relevant answers from documentation-based sources like React.js or JavaScript.

The chatbot uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from documentation pages and leverages Gemini to provide detailed responses. It can be adapted to build a contextual assistant for any documentation-based website.

---

## ✨ Features

- ✏️ **Web Crawler**: Automatically scrapes content from a documentation site.
- 🔗 **ChromaDB Integration**: Stores the scraped content as embeddings for semantic search.
- ✨ **Sentence Transformers**: Encodes questions and documents for similarity search.
- ⚙️ **RAG-powered Responses**: Retrieves relevant documents from ChromaDB and uses Gemini API to generate focused, context-aware answers.
- 💬 **FastAPI Backend**: RESTful API endpoints for chatbot interaction.
- ⚖️ **Session Management**: Uses Redis to manage chat history and sessions.
- 📊 **Easy Customization**: Simply change the base documentation URL to create a chatbot for any product.

---

## 🚀 How It Works

1. **Scraping Documentation**:
   - The built-in web scraper visits all pages of a documentation site starting from a base URL.
   - Extracts and stores the text content from each page.

2. **Embedding the Data**:
   - The scraped content is passed through a `SentenceTransformer` model to generate embeddings.
   - These embeddings, along with source metadata, are stored in ChromaDB for semantic search.

3. **Query Flow**:
   - A user submits a question via FastAPI endpoint.
   - The question is embedded and matched against the most relevant documents in ChromaDB.
   - The retrieved context is sent to the Gemini API, which generates a precise and on-topic answer.

4. **Session Handling (Optional)**:
   - Supports multi-turn conversations with contextual continuity.
   - Redis is used to store chat history per session.

---

## 🚀 Build Your Own Chatbot

To adapt this chatbot for any other product documentation:

1. **Clone the Project**  
   Clone the repository and open it in PyCharm or any IDE you choose.

2. **Install Dependencies**  
   Install all dependencies listed in `requirements.txt` and configure all necessary directory paths.

3. **Set Up Gemini API key**  
   Create your Gemini API key in [https://aistudio.google.com/welcome](googleAIstudio)

4. **Start Redis Server**  
   Install and start the Redis server on your machine. It's required for managing user sessions.

5. **Configure the Scraper**  
   In `crawl_pages.py`, update the base URL of your product documentation.  
   You may also need to modify `scraper.py` depending on how anchor tags are defined in your site's HTML.

6. **Run the Crawler**  
   Execute `crawl_pages.py` from the terminal. It will scrape the documentation, convert it to embeddings, and store it in ChromaDB.

7. **Start the API Server**  
   Navigate to the `app` directory and run the following command:  
   ```
   uvicorn main:app --reload
   ```

8. **Test the API**  
   Once the app is running, use the included Postman collection (available in this repo) to test your chatbot's endpoints.

---

## 🤝 Why Use ChromaDB?

ChromaDB is used for efficient vector similarity search. It allows:

- Fast retrieval of relevant documents using embeddings.
- Persistent storage and metadata support.
- Easy integration with models like Sentence Transformers.

---

## 🚀 Why Gemini for Response Generation?

Gemini LLM is used to:

- Summarize and respond using only the most relevant context.
- Avoid hallucinations by sticking to the retrieved data.
- Generate helpful and actionable responses for developers.

---

## ⚡ Dependencies

This project uses the following Python packages:

- `fastapi`
- `uvicorn`
- `requests`
- `beautifulsoup4`
- `sentence-transformers`
- `chromadb`
- `transformers`
- `pydantic`
- `accelerate`
- `redis`

---

## 🚀 Use Cases

- Developer support bots for frameworks like React, Vue, Angular, etc.
- Internal documentation assistants.
- Product support chatbots for SaaS tools.
- Personal AI assistants for custom knowledge bases.

---

## 🙏 Contribution & Feedback

Feel free to contribute or raise issues. You can extend this to support multiple collections, UI integration, or multilingual responses.

---

## 📅 Future Improvements

- Add authentication for APIs
- Integrate front-end UI
- Improve scraping with JS-rendering (Selenium or Playwright)
- Support for multiple document sources or languages

---

## 🚫 Disclaimer

Please make sure not to expose your Gemini API key publicly. Replace it with environment variables for production use.

---

## 📍 Credits

Built with ❤️ using FastAPI, ChromaDB, and Gemini LLM.

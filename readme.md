# Smart Seek - Revolutionizing File Search with Vector Databases

## Overview

Smart Seek leverages advanced AI models and TiDB’s vector database to enable accurate file retrieval through descriptive queries. By simply providing the path to the folders you want to be searchable, Smart Seek indexes them in the background, allowing you to search via natural language descriptions.

## Features

- **File Indexing:** Select folders to index, and Smart Seek processes the files using captioning, embedding, and OCR models.
- **Vector Database:** Uses TiDB’s vector database to store embeddings and perform fast, scalable searches.
- **Search Capability:** Retrieve files using natural language queries, with results ranked by semantic similarity.
- **Future Scope:** Integration with cloud storage providers, and an extension for enhanced search capabilities using an LLM interface.

## Prerequisites

- Python 3.10+
- Node.js and npm
- Ensure you have TiDB and any required credentials set up.

## Setup Instructions

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/smart-seek.git
    cd smart-seek
    ```

2. **Install Dependencies:**
    ```bash
    cd Backend && pip install -r requirements.txt
    ```

3. **Environment Variables:**
   Set up any required environment variables for TiDB, file paths, etc.

4. **Running the Backend:**
   Navigate to the `Backend` folder and run the following commands:
    ```bash
    cd Backend
    uvicorn Backend:app --reload --host 0.0.0.0 --port 8001
    uvicorn TiDb_Hack_Backend:app --reload --host 0.0.0.0 --port 8000
    python3 processFolder.py
    python3 searchSimilar.py
    ```

5. **Running the Frontend:**
   Navigate to the `frontend` folder and start the frontend server:
    ```bash
    cd ../frontend
    npm start
    ```

## CORS Issues

If you encounter CORS issues, you can bypass them by launching your browser with web security disabled. Follow the steps below based on your operating system:

- **Windows:**
  1. Open Start window
  2. Search Run and open it or press Window + R
  3. Paste `chrome.exe --user-data-dir="C://Chrome dev session" --disable-web-security` and execute it
  4. This will open a new browser with web security disabled. You can now access your project in this browser without worrying about CORS errors.

- **OSX:**
  Run the following command in the terminal:
  ```bash
  open -n -a /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --args --user-data-dir="/tmp/chrome_dev_test" --disable-web-security
  ```


  - **Linux:**
  Run the following command in the terminal:
  ```
  google-chrome --disable-web-security
  ```

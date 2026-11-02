# Continuum

Continuum is a Python-based personal AI assistant that combines Google's Gemini AI with persistent memory stored using SQLite.

The aim of the project is to explore how AI assistants can maintain useful information across conversations rather than starting from scratch every time.

## Features

- **AI conversations:** Interact with Google's Gemini model.
- **Persistent memory:** Save information in a local SQLite database.
- **Recall memories:** Retrieve previously stored information.
- **Memory management:** Add, update and delete stored memories.
- **Command-line interface:** Interact with Continuum directly through the terminal.

## Technologies

- Python
- Google Gemini API
- SQLite
- Google Gen AI SDK
- python-dotenv

## Project Structure

- `main.py` – Main application and command-line interface.
- `ai.py` – Handles communication with the Gemini API.
- `memory.py` – Handles saving, retrieving and deleting memories.
- `continuum.db` – Local SQLite database, generated when the application runs.
- `.env` – Stores the Gemini API key.

## Setup

1. Clone the repository.
2. Install the required dependencies:

   `pip install -r requirements.txt`

3. Create a `.env` file in the project folder.
4. Add your Gemini API key:

   `GEMINI_API_KEY=your_api_key_here`

5. Start the application:

   `python main.py`

## Available Commands

| Command | Description |
|---|---|
| `/remember key=value` | Save or update a memory |
| `/recall key` | Retrieve a memory |
| `/forget key` | Delete a memory |
| `exit` | Close Continuum |

## Current Limitations

- Memories are retrieved using exact keys rather than semantic search.
- Conversations are not currently stored as chat history.
- The assistant relies on an external Gemini API connection.

## Future Improvements

- Semantic memory retrieval.
- Conversation history.
- Improved memory extraction and management.
- Additional assistant capabilities.
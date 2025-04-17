from mcp.server.fastmcp import FastMCP
import os
import json
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# Create MCP server
mcp = FastMCP("AIAssistant")

# File configurations
NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes.txt")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_URL = "https://newsapi.org/v2/everything"
ARTICLES_FILE = os.path.join(os.path.dirname(__file__), "news_articles.json")

def ensure_notes_file():
    """Ensure the notes file exists, creating an empty file if it doesn't."""
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            f.write("")

def ensure_articles_file():
    """Ensure the articles file exists, creating an empty JSON array if it doesn't."""
    if not os.path.exists(ARTICLES_FILE):
        with open(ARTICLES_FILE, "w") as f:
            json.dump([], f)

# Sticky Notes Tools
@mcp.tool()
def add_note(message: str) -> str:
    """
    Append a new note to the sticky note file.
    """
    ensure_notes_file()
    with open(NOTES_FILE, "a") as f:
        f.write(message + "\n")
    logging.info(f"Added note: {message}")
    return "Note saved!"

@mcp.tool()
def read_notes() -> str:
    """
    Read and return all notes from the sticky note file.
    """
    ensure_notes_file()
    with open(NOTES_FILE, "r") as f:
        content = f.read().strip()
    logging.info("Read all notes")
    return content or "No notes yet."

# News API Tools
@mcp.tool()
def fetch_news(query: str) -> str:
    """
    Fetch news articles from the News API based on a query.
    """
    ensure_articles_file()
    try:
        params = {
            "q": query,
            "apiKey": NEWS_API_KEY,
            "pageSize": 5,
            "sortBy": "publishedAt",
            "language": "en"
        }
        response = requests.get(NEWS_API_URL, params=params)
        response.raise_for_status()
        articles = response.json().get("articles", [])

        if not articles:
            logging.warning(f"No articles found for query: {query}")
            return "No articles found for the query."

        with open(ARTICLES_FILE, "r") as f:
            stored_articles = json.load(f)

        new_articles = [
            {
                "title": article["title"],
                "description": article.get("description", ""),
                "url": article["url"],
                "publishedAt": article["publishedAt"]
            }
            for article in articles
        ]
        stored_articles.extend(new_articles)

        with open(ARTICLES_FILE, "w") as f:
            json.dump(stored_articles, f, indent=2)

        logging.info(f"Fetched {len(new_articles)} articles for query: {query}")
        return f"Fetched {len(new_articles)} articles for query '{query}'."
    except requests.RequestException as e:
        logging.error(f"Error fetching news: {str(e)}")
        return f"Error fetching news: {str(e)}"

@mcp.tool()
def read_articles() -> str:
    """
    Read and return all stored news articles.
    """
    ensure_articles_file()
    with open(ARTICLES_FILE, "r") as f:
        articles = json.load(f)

    if not articles:
        logging.info("No articles stored yet")
        return "No articles stored yet."

    output = []
    for i, article in enumerate(articles, 1):
        output.append(
            f"Article {i}:\n"
            f"Title: {article['title']}\n"
            f"Description: {article['description']}\n"
            f"URL: {article['url']}\n"
            f"Published: {article['publishedAt']}\n"
        )
    logging.info("Read all articles")
    return "\n".join(output)

if __name__ == "__main__":
    logging.info("Starting MCP server")
    mcp.run()
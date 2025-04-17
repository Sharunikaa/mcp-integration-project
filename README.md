# Model Context Protocol (MCP) Integration Suite

## What is MCP?

Model Context Protocol (MCP) is a framework that enables AI assistants to interact with external tools, services, and data sources through standardized interfaces. By using MCP, AI models can perform real-world actions and access up-to-date information beyond their training data, expanding their capabilities significantly.

This project demonstrates how to integrate various services using MCP, allowing AI assistants to perform tasks like fetching news, managing GitHub repositories, sending Slack messages, accessing location data, automating browsers, and managing notes.

## 🌟 Key Integrations

This repository showcases the following MCP integrations:

- **GitHub**: Repository, issue, and pull request management
- **Slack**: Channel messaging and thread interactions
- **File System**: Secure file and directory operations
- **Google Maps**: Location services and directions
- **Playwright**: Browser automation
- **News API**: Article retrieval and management
- **Notes System**: Custom note-taking functionality

## 📋 Prerequisites

- Python 3.13+
- Node.js 16+ (for npx commands)
- API keys for respective services

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/Sharunikaa/mcp-integration-project.git
cd mcp-integration-project
```

2. Install Python dependencies:
```bash
pip install fastmcp mcp[cli] requests
```

3. Configure environment variables in a `.env` file:
```env
NEWS_API_KEY=your_news_api_key
GITHUB_PERSONAL_ACCESS_TOKEN=your_github_token
SLACK_BOT_TOKEN=your_slack_token
SLACK_TEAM_ID=your_team_id
SLACK_CHANNEL_IDS=channel1,channel2
GOOGLE_MAPS_API_KEY=your_google_maps_key
```

## 🔧 MCP Configuration

### Complete MCP Server Configuration Example

Create a `claude_desktop_config.json` file with your MCP server definitions:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-github"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your_github_token"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "C:\\Users\\your_username",
        "D:\\your_project_directory"
      ]
    },
    "slack": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-slack"
      ],
      "env": {
        "SLACK_BOT_TOKEN": "xoxb-your-token",
        "SLACK_TEAM_ID": "your_team_id",
        "SLACK_CHANNEL_IDS": "channel1,channel2"
      }
    },
    "google-maps": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-google-maps"
      ],
      "env": {
        "GOOGLE_MAPS_API_KEY": "your_google_maps_key"
      }
    },
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest"
      ]
    },
    "custom-server": {
      "command": "python",
      "args": [
        "main.py"
      ],
      "env": {
        "NEWS_API_KEY": "your_news_api_key"
      }
    }
  }
}
```

## 📝 Custom Functions

### Creating Your Own MCP Server

This project demonstrates how to create a custom MCP server with Python using the FastMCP library:

```python
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("AI Assistant")

# Register custom tools
@mcp.tool()
def fetch_news(query: str) -> str:
    """Fetch news articles based on a query."""
    # Implementation
    
@mcp.tool()
def add_note(message: str) -> str:
    """Add a note to the system."""
    # Implementation
    
# Start the server
if __name__ == "__main__":
    mcp.run()
```

## 🚀 Usage Examples

### Starting Your MCP Server

```bash
python main.py
```

### GitHub Operations

```python
# Create a repository
github_create_repository(name="new-repo", description="A new repository")

# Create an issue
github_create_issue(owner="username", repo="repo-name", title="Issue title", body="Issue description")
```

### Google Maps Operations

```python
# Get directions
maps_directions(origin="New York", destination="Boston", mode="driving")

# Search for places
maps_search_places(query="restaurants near me", location={"latitude": 40.7128, "longitude": -74.0060})
```

### Playwright Browser Automation

```python
# Navigate to a website
browser_navigate(url="https://example.com")

# Take a screenshot
browser_take_screenshot()
```

### News and Notes Operations

```python
# Fetch news on a topic
fetch_news(query="artificial intelligence")

# Add a note
add_note(message="Important meeting tomorrow")
```

## 🔐 Security Considerations

- Store all API keys and tokens in environment variables, not directly in code
- Limit file system access to necessary directories only
- Implement proper error handling and logging
- Use restricted scopes for API tokens when possible

## 📚 Documentation Resources

For more information about MCP and related technologies:

- [Model Context Protocol Documentation](https://github.com/microsoft/semantic-kernel/tree/main/samples/mcp)
- [FastMCP Documentation](https://pypi.org/project/fastmcp/)
- [GitHub API Documentation](https://docs.github.com/en/rest)
- [Slack API Documentation](https://api.slack.com/web)
- [Google Maps Platform Documentation](https://developers.google.com/maps/documentation)
- [Playwright Documentation](https://playwright.dev/docs/intro)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Made with ❤️ by [Sharunikaa](https://github.com/Sharunikaa)
# MCP Notes Management System

## What is MCP?

Model Context Protocol (MCP) is a framework that enables AI assistants to interact with external tools, services, and data sources through standardized interfaces. By using MCP, AI models can perform real-world actions and access up-to-date information beyond their training data, expanding their capabilities significantly.

This project demonstrates a practical implementation of MCP, focusing on notes management, while also showing how to integrate with GitHub, Slack, file system operations, Google Maps, and browser automation.

## 📊 Project Structure

```
.
├── main.py                # MCP server implementation
├── notes.txt              # Sample notes file containing information about GenAI
├── pyproject.toml         # Python project configuration
├── README.md              # This documentation
└── .env                   # Environment variables (create this file)
```

## 🌟 Features

This project showcases note management functionality with several possible integrations:

### 1. Notes Management
- Add notes with timestamps
- Read all existing notes
- Access the latest note
- Generate note summary prompts

### 2. External Service Integrations
- **GitHub**: Repository and issue management
- **Slack**: Channel messaging
- **File System**: Secure file operations
- **Google Maps**: Location services
- **Playwright**: Browser automation

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

## 🔧 MCP Configuration

### Claude Desktop Configuration

Create or update your `claude_desktop_config.json` file with the following MCP server definitions:

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
        "D:\\news_custom"
      ]
    },
    "slack": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-slack"
      ],
      "env": {
        "SLACK_BOT_TOKEN": "your_slack_token",
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
    "notes-assistant": {
      "command": "python",
      "args": [
        "main.py"
      ]
    }
  }
}
```

## 📝 Implementation Details

### Notes Management

The project includes tools for managing notes:

```python
@mcp.tool()
def add_note(message: str) -> str:
    """
    Append a new note to the sticky note file.
    """
    # Adds a note to notes.txt
    
@mcp.tool()
def read_notes() -> str:
    """
    Read and return all notes from the sticky note file.
    """
    # Returns all stored notes
    
@mcp.resource("notes://latest")
def get_latest_note() -> str:
    """
    Get the most recently added note.
    """
    # Returns the last note
```

## 🚀 Usage Examples

### Starting Your MCP Server

```bash
python main.py
```

### Notes Operations

```python
# Add a note
add_note(message="Important meeting tomorrow")

# Read all notes
read_notes()

# Get the latest note
get_latest_note()
```

## 🔍 Troubleshooting

Common issues and solutions:

1. **MCP Server Not Starting**: Check if the correct version of Python is installed (3.13+)
2. **Tool Not Found Errors**: Ensure your Claude configuration points to the correct file paths
3. **Empty Results**: Make sure your notes.txt file exists and is writable

## 📚 Documentation Resources

For more information about MCP and related technologies:

- [Model Context Protocol Documentation](https://github.com/microsoft/semantic-kernel/tree/main/samples/mcp)
- [FastMCP Documentation](https://pypi.org/project/fastmcp/)
- [GitHub API Documentation](https://docs.github.com/en/rest)
- [Slack API Documentation](https://api.slack.com/web)
- [Google Maps Platform Documentation](https://developers.google.com/maps/documentation)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Last updated: April 17, 2025  
Made by [Sharunikaa](https://github.com/Sharunikaa)
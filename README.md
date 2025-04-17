# Multi-Service Integration with Model Context Protocol (MCP)

A comprehensive project that demonstrates integration with various services using Model Context Protocol (MCP). This project includes integrations with GitHub, Slack, file system operations, Google Maps, Playwright for browser automation, and custom note-taking functionality.

## 🌟 Features

- **GitHub Integration**: Manage repositories, issues, and pull requests
- **Slack Communication**: Send messages and interact with Slack channels
- **File System Operations**: Handle file and directory operations securely
- **Google Maps Integration**: Access location-based services and directions
- **Playwright Browser Automation**: Automate web browser interactions
- **Custom Notes System**: Create and manage notes with rich functionality
- **News API Integration**: Fetch and manage news articles

## 📋 Prerequisites

- Python 3.13 or higher
- Node.js (for npx commands)
- Required API keys for various services

## 🛠️ Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd mcp-integration-project
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables by copying `.env.example` to `.env` and filling in your API keys.

## 🚀 Usage

### Starting the MCP Server

```bash
python main.py
```

### Available Tools

- GitHub Operations (create repos, issues, PRs)
- Slack Communication
- Google Maps Services
- File System Management
- Custom Notes System
- News API Integration

See the documentation of each tool in the code comments for detailed usage.

## 📝 Configuration

Copy `.env.example` to `.env` and configure your API keys:

```env
NEWS_API_KEY=your_news_api_key
GITHUB_PERSONAL_ACCESS_TOKEN=your_github_token
SLACK_BOT_TOKEN=your_slack_token
SLACK_TEAM_ID=your_team_id
SLACK_CHANNEL_IDS=channel1,channel2
GOOGLE_MAPS_API_KEY=your_google_maps_key
```

## 🔐 Security

- All API keys and tokens should be stored in `.env`
- File system access is restricted to specified directories
- Proper error handling and logging implemented

## 📚 Documentation

For more details, see:
- [Model Context Protocol Documentation](https://github.com/microsoft/semantic-kernel/tree/main/samples/mcp)
- Individual service documentation in code comments

## 📄 License

MIT License - See LICENSE file for details.

---
For questions and support, please open an issue in the repository.
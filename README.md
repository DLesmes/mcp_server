# 🚀 MCP Server Demo

## 📋 Overview

A simple and fast introduction to **Model Context Protocol (MCP)** servers! This project demonstrates how to create a basic MCP server with a simple math tool, perfect for learning MCP concepts without the complexity of inspector tools or npm dependencies.

This demo server provides a basic `add` function that can be called through the MCP protocol, showcasing the fundamental concepts of MCP server development.

## ✨ Features

- 🧮 **Simple Math Tool**: Basic addition functionality via MCP
- 🐍 **Python-based**: Built with FastMCP for easy development
- 🚀 **UV Support**: Modern Python package management with UV
- 🔧 **CLI Testing**: Test tools directly with mcp-tools-cli
- 🖥️ **Claude Desktop Integration**: Ready-to-use configs for both Windows and WSL
- 📦 **Minimal Dependencies**: Only essential packages required

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.12+** 🐍
- **UV** (recommended) or **pip** 📦
- **Claude Desktop** (for GUI testing) 🖥️
- **mcp-tools-cli** (for CLI testing) 🔧

### Installing UV (Recommended)
```bash
# Windows (PowerShell)
irm https://astral.sh/uv/install.ps1 | iex

# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Installing mcp-tools-cli
```bash
# Using UV
uvx mcp-tools-cli --help

# Using pip
pip install mcp-tools-cli
```

## 🚀 Quick Start

### Option 1: Using UV (Recommended) ⚡

1. **Clone and navigate to the project:**
```bash
git clone <your-repo-url>
cd mcp_server
```

2. **Create virtual environment:**
```bash
uv venv
```

3. **Activate virtual environment:**
```bash
# Windows
.venv\Scripts\activate
```

```bash
# macOS/Linux
source .venv/bin/activate
```

4. **Install dependencies:**
```bash
uv pip install -r requirements.txt
```

5. **Run the server:**
```bash
uv run python server.py
```

### Option 2: Using Pure Python 🐍

1. **Clone and navigate to the project:**
```bash
git clone <your-repo-url>
cd mcp_server
```

2. **Create virtual environment:**
```bash
python -m venv .venv
```

3. **Activate virtual environment:**
```bash
# Windows
.venv\Scripts\activate
```

```bash
# macOS/Linux
source .venv/bin/activate
```

4. **Install dependencies:**
```bash
pip install -r requirements.txt
```

5. **Run the server:**
```bash
python server.py
```

## 🧪 Testing

### CLI Testing with mcp-tools-cli 🔧

Test your MCP server using the command line interface. Use these commands to verify the `add` tool works correctly:

#### Proper JSON Format
```bash
uvx mcp-tools-cli call-tool --% --mcp-name local_demo --tool-name add --tool-args {"a":1,"b":2} --config-path .\mcp_config.json
```

#### Tolerant Fallback Formats
```bash
# Key-value pairs
uvx mcp-tools-cli call-tool --mcp-name local_demo --tool-name add --tool-args a=1,b=2 --config-path .\mcp_config.json

# Simplified JSON
uvx mcp-tools-cli call-tool --% --mcp-name local_demo --tool-name add --tool-args {a:1,b:2} --config-path .\mcp_config.json
```

### Claude Desktop Testing 🖥️

For a more interactive experience, test your MCP server with Claude Desktop:

1. **Configure Claude Desktop:**
   - Copy the contents of `claude_desktop_config_wd.json` (Windows) or `claude_desktop_config_wsl.json` (WSL)
   - Update the file paths and API keys in the config
   - Add the config to your Claude Desktop settings

2. **Start Claude Desktop** and you'll see your MCP server available as a tool

3. **Test the tool** by asking Claude to use the `add` function:
   ```
   "Can you add 5 and 3 using the add tool?"
   ```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository** 🍴
2. **Create a feature branch** 🌿
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes** ✏️
4. **Test your changes** 🧪
5. **Commit your changes** 💾
   ```bash
   git commit -m "Add amazing feature"
   ```
6. **Push to the branch** 🚀
   ```bash
   git push origin feature/amazing-feature
   ```
7. **Open a Pull Request** 📝

### Development Guidelines
- Keep it simple and educational 📚
- Add clear comments to code 💬
- Test all changes thoroughly ✅
- Update documentation as needed 📖

## 📞 Contact

- **Issues**: [GitHub Issues](https://github.com/DLesmes/mcp_server/issues) 🐛
- **Discussions**: [GitHub Discussions](https://github.com/DLesmes/mcp_server/projects?query=is%3Aopen) 💬
- **Email**: your-email@example.com 📧

---

**Happy MCP Development!** 🎉 

*This project is designed to be a quick and easy introduction to MCP servers. Perfect for beginners who want to understand the basics without getting overwhelmed by complex tooling.*

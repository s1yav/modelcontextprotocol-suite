# mcp-server-weather-nws

An MCP (Model Context Protocol) server that integrates with the US National Weather Service (NWS) API to retrieve active weather alerts and feed them to LLM assistants.

This server is built using the official Python MCP SDK with the high-level `FastMCP` wrapper.

## Features

*   **Asynchronous API Requests**: Uses `httpx` for non-blocking GET requests to the NWS API.
*   **Safe Error Handling**: Robust try/except blocks to ensure server stability during network or API downtimes.
*   **Human-Readable Alert Formatting**: Formats complex GeoJSON alert schemas into clean, readable text summaries containing:
    *   Event type
    *   Affected area description
    *   Severity level
    *   Detailed description
    *   Recommended safety instructions

## Installation

Ensure you have `uv` installed (Astral's fast Python package manager).

1.  Navigate to this directory:
    ```bash
    cd mcp-server-weather-nws
    ```

2.  Sync the dependencies and build the virtual environment:
    ```bash
    uv sync
    ```

## Usage

### Running Locally

You can run the server directly using `uv`:

```bash
uv run weather.py
```

### Configuring Claude Desktop (or other MCP Clients)

To use this server with your LLM client, add it to your client's configuration file (e.g., `claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "weather-nws": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/mcp-server-weather-nws",
        "run",
        "weather.py"
      ]
    }
  }
}
```

*Note: Replace `/absolute/path/to/mcp-server-weather-nws` with the actual path to this directory on your machine.*

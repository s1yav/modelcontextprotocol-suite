# mcp_server_weather_nws

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
    cd mcp_server_weather_nws
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
        "/absolute/path/to/mcp_server_weather_nws",
        "run",
        "weather.py"
      ]
    }
  }
}
```

*Note: Replace `/absolute/path/to/mcp_server_weather_nws` with the actual path to this directory on your machine.*

## Hosting on a Mac Mini (Remote SSE Transport)

If you have a Mac Mini acting as a home server, you can host this MCP server on it and connect to it remotely from your MacBook or other devices on your local network using **Server-Sent Events (SSE) Transport**.

### 1. Configure the Server for SSE
In your package's `__init__.py` file, ensure the `mcp.run` call is configured to use the `"sse"` transport:

```python
def main():
    mcp.run(transport="sse")
```

### 2. Set Up a Local Hostname
To connect without memorizing IP addresses, assign a friendly local hostname to your Mac Mini:
1. On the Mac Mini, go to **System Settings** -> **General** -> **Sharing**.
2. Scroll to the bottom to **Local Hostname**, click **Edit**, and set it (e.g. `mac-mini` or `weather-server`).
3. Your Mac Mini is now reachable on your home Wi-Fi at `http://mac-mini.local:8000/sse`.

### 3. Run the Server on the Mac Mini
Start the server process on your Mac Mini. It will begin listening on port `8000`:
```bash
uv run mcp_server_weather_nws
```

### 4. Configure the Client on your MacBook
In your client configuration (e.g. `claude_desktop_config.json` on your MacBook), connect to the server using the `url` property:
```json
{
  "mcpServers": {
    "weather-nws": {
      "url": "http://mac-mini.local:8000/sse"
    }
  }
}
```
Now your MacBook client will make real-time network queries to your Mac Mini when executing weather tools.

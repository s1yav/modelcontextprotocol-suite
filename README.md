# MCP Suite

A unified monorepo hosting a collection of Model Context Protocol (MCP) servers and clients. This suite is designed to extend Large Language Model (LLM) capabilities by providing them with secure, local access to data, external APIs, and custom system tools.

## Repository Structure

The suite is divided into two primary directories:

*   **`servers/`**: A collection of custom MCP servers that expose tools, resources, and prompts to LLM clients.
    *   [mcp-server-weather-nws/](./mcp-server-weather-nws): An asynchronous Python server built with `FastMCP` that integrates with the National Weather Service (NWS) API to retrieve active weather alerts. (See the [MCP Build Server Guide](https://modelcontextprotocol.io/docs/develop/build-server) for development details).
*   **`clients/`**: Custom client applications, web dashboards, or editor integrations that consume the MCP servers.

## Quick Start

### Prerequisites

*   **Python 3.10+** (Python 3.13 recommended)
*   **`uv`**: A fast, Rust-based Python package installer and resolver.
    *   To install: `curl -LsSf https://astral.sh/uv/install.sh | sh`
*   **GitHub CLI (`gh`)**: Used for remote repository operations.

### Running a Server Locally

Navigate to the specific server's directory and run it with `uv`:

```bash
cd mcp-server-weather-nws
uv run weather.py
```

## References

*   **Official MCP Documentation**: For detailed architecture guides, SDK references, and quickstarts, see the [Model Context Protocol Introduction](https://modelcontextprotocol.io/docs/getting-started/intro).

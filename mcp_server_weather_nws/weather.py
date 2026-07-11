from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP

# initialize fast MCP server
# initialize the FastMCP class with a custom name
mcp = FastMCP("weather")

NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app" # NWS requires a custom user agent to identify the client

async def make_nws_request(endpoint: str) -> dict[str, Any] | None:
    """Make a GET request to the NWS API and return the JSON response."""
    headers = {"User-Agent": USER_AGENT, "Accept": "application/geo+json"}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url=endpoint, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None
    
def format_alert(feature: dict) -> str:
    """Format the alert feature into readable strings"""
    props = feature["properties"]
    return f"""
    Event: {props.get("event", "Unknown")}
    Area: {props.get("areaDesc", "Unknown")}
    Severity: {props.get("severity", "Unknown")}
    Description: {props.get("description", "Description not available")}
    Instructions: {props.get("instructions", "Instructions not available")}
    """
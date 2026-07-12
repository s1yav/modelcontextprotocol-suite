from mcp_server_weather_nws.weather import mcp

def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()

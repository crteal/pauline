"""
Creates a Pauline FastMCP server, runs it directly with main
"""

import os

from pauline.mcp import MCP

mcp = MCP()

if __name__ == "__main__":
    mcp_transport = os.environ.get("MCP_TRANSPORT", "stdio").lower()
    mcp.run(transport=mcp_transport)

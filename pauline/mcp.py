"""
A FastMCP server providing Pauline via Model Context Protocol
"""

from typing import Optional

from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession
import sqlglot
from sqlglot.errors import ParseError

def MCP(**config) -> FastMCP:
    mcp = FastMCP("Pauline", **config)

    @mcp.tool()
    async def validate_query(
        query: str,
        ctx: Context[ServerSession, None]
    ) -> str:
        await ctx.info(f"Attempting to parse query as SQL: {query}")
        try:
            ast = sqlglot.parse_one(query)
            await ctx.info(f"Successfully parsed query as SQL with AST: {ast}")
            return ast
        except ParseError as e:
            await ctx.error(f"Failed to parse query as SQL with exception: {e}")
            return str(e)

    return mcp

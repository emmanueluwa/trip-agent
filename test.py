import asyncio
from mcp_client_test import get_all_tools


async def main():
    await get_all_tools()


if __name__ == "__main__":
    asyncio.run(get_all_tools())

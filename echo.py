import asyncio
import websockets
from urllib.parse import urlparse, parse_qs


async def echo(websocket, path):
    # 解析URL和查询参数
    query_params = parse_qs(urlparse(websocket.path).query)
    print(f"Query parameters: {query_params}")

    async for message in websocket:
        print(f"Received message: {message}")
        await websocket.send(f"Echo: {message}")


async def main():
    async with websockets.serve(echo, "localhost", 8765):
        print("WebSocket server started on ws://localhost:8765")
        await asyncio.Future()  # Run forever


# Run the server
asyncio.run(main())

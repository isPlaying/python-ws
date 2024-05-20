import asyncio
import websockets


async def connect_to_websocket():
    # 定义 WebSocket 服务器的 URI 并附加查询参数
    params = {"param1": "value1", "param2": "value2"}
    uri = "ws://localhost:8765"
    query_string = "&".join([f"{key}={value}" for key, value in params.items()])
    uri_with_params = f"{uri}?{query_string}"
    try:
        async with websockets.connect(uri_with_params) as websocket:
            # 发送消息
            await websocket.send("Hello, WebSocket!")
            print(f"> Sent: Hello, WebSocket!")
            # 接收响应
            response = await websocket.recv()
            print(f"< Received: {response}")
    except websockets.exceptions.ConnectionClosed as e:
        print(f"Connection closed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    asyncio.run(connect_to_websocket())

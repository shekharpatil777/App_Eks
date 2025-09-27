from fastapi import FastAPI, WebSocket, WebSocketDisconnect



@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # Wait for a client to connect
    await websocket.accept()
    try:
        while True:
            # Wait for data from the client
            data = await websocket.receive_text()
            # Send the received data back to the client
            await websocket.send_text(f"Message text was: {data}")
    except WebSocketDisconnect:
        print("Client disconnected")
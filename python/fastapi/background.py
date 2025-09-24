# main.py
from fastapi import FastAPI, BackgroundTasks
import time

def write_notification(email: str, message=""):
    """A slow task, like writing to a log file or sending an email."""
    print(f"Preparing notification for {email}...")
    time.sleep(5) # Simulate a slow I/O operation
    with open("log.txt", mode="a") as email_file:
        content = f"notification for {email}: {message}\n"
        email_file.write(content)
    print("Notification sent.")


app = FastAPI()

@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    """
    The response is returned immediately.
    The 'write_notification' function runs in the background.
    """
    
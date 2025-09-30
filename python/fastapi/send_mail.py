from fastapi import BackgroundTasks, FastAPI

app = FastAPI()

def write_notification(email: str, message=""):
    """A dummy function to simulate sending an email."""
    with open("log.txt", mode="a") as email_log:
        content = f"notification for {email}: {message}\n"
        email_log.write(content)
        print(f"Sent: {content.strip()}")

@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    # Add the task to be run in the background.
    # The response will be sent to the user immediately.
    background_tasks.add_task(write_notification, email, message="some notification")
    
    return {"message": "Notification sent in the background"}

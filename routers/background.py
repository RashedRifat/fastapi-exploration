from fastapi import APIRouter, BackgroundTasks
from pathlib import Path

router = APIRouter(prefix='/background')

def send_email(email: str, message : str = ''):
    with open(Path("logs/email.txt"), 'a+') as fp:
        fp.write(f'notification for {email} : {message}')

@router.get("/send-email/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, email, message="some notification")
    return {"message": "Notification sent in the background"}
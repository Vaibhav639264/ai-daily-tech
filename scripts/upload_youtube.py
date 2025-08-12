import os
import pickle
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def upload(video_file, title, description, tags, config):
    creds = None
    token_path = config['youtube']['token_file']
    
    if os.path.exists(token_path):
        with open(token_path, 'rb') as f:
            creds = pickle.load(f)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                config['youtube']['credentials_file'], SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open(token_path, 'wb') as f:
            pickle.dump(creds, f)

    youtube = build("youtube", "v3", credentials=creds)

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": tags,
                "categoryId": "27"
            },
            "status": {
                "privacyStatus": "public"
            }
        },
        media_body=MediaFileUpload(video_file)
    )
    response = request.execute()
    print("✅ Uploaded:", response["id"])

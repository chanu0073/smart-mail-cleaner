from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
import os
import json

SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]

def main():
    creds = None
    if os.path.exists('token.json'):
        with open('token.json','r') as token:
            creds = Credentials.from_authorized_user_file(
                "token.json",
                SCOPES
            )
        
    if not creds:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json',
            SCOPES
        )
        creds = flow.run_local_server(port=0)
        with open("token.json",'w') as token:
            token.write(creds.to_json())
        
        print("Authentication successful. Token saved")
    else:
        print("Already authenticated. Token loaded")

if __name__ == "__main__":
    main()
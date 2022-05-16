'''
send email with mailgun
'''
from mailjet_rest import Client
import base64

def send_email(email: str,name: str):
    data = open("data.csv", "r").read()

    api_key = '98d09d61b387e6aee0f618be8450af96'
    api_secret = 'd5c4eb5c882bc5d6a76c7d49a3a83ca3'
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
    'Messages': [
        {
        "From": {
            "Email": "thiernoibrahimalo@esp.sn",
            "Name": "thierno ibrahima"
        },
        "To": [
            {
            "Email": email,
            "Name": name
            }
        ],
        "Subject": "List de presence LGLSIA",
        "TextPart": "Bonjour veuillez trouver ci-joint la liste de presence",
        "Attachments": [
                    {
                    "ContentType": "text/csv",
                    "Filename": "Liste.csv",
                    "Base64Content": base64.b64encode(data.encode()).decode()
                }
                ],
        "CustomID": "AppGettingStartedTest",
        }
    ],

    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())

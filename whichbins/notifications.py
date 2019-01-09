from twilio.rest import Client

def send_sms(message, recipient):
    # Your Account Sid and Auth Token from twilio.com/console
    account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    auth_token = 'your_auth_token'
    # Your messaging service Sid
    service_sid = 'MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        messaging_service_sid=service_sid,
        to=recipient
    )
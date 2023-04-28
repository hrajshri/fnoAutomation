
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACa7fb614b7bf3b0d6d230323e070bd34a'
auth_token = '409bf68f7d623edfe5d83402e71098cb'
client = Client(account_sid, auth_token)

def sendMsg():          
    message = client.messages.create(
                              body='Hello fno! Timer',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+918600240462'
                          )

    print(message.sid)

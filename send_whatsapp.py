from twilio.rest import Client
import config

# Your Twilio account SID and auth token
# account_sid = 'AC49cab586f5ac4640f7cb608d67ad5bd7' 
# auth_token = 'cecc529da5927be94333faa2e33561fa'

# Create a Twilio client
client = Client(config.account_sid, config.auth_token)

# Replace with your Twilio WhatsApp number and your own number
from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number = 'whatsapp:+919638425338'

# Message content
message = "Hi Bharat Thanks for logging in start your day bro!"

try:
    # Send the message
    message = client.messages.create(
        body=message,
        from_=from_whatsapp_number,
        to=to_whatsapp_number
    )
    print(f"Message sent successfully. SID: {message.sid}")

except Exception as e:
    print(f"Failed to send message. Error: {str(e)}")

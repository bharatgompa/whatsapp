import pywhatkit as kit
from datetime import datetime

# Function to send WhatsApp message
def send_whatsapp_message():
    # Replace with the phone number you want to send the message to
    phone_number = "+919618845845"  # Replace with your recipient's phone number in international format

    # Message content
    message = "Hi vivek from pywhatkit" 

    try:
        # Sending message
        # kit.sendwhatmsg(phone_number, message, 10, 0)  # 10 AM (IST), 0 minutes
        # kit.sendwhatmsg(phone_number, message)
        kit.sendwhatmsg_instantly(phone_number, message)

        print(f"Message sent successfully to {phone_number}")

    except Exception as e:

        print(f"Failed to send message to {phone_number}. Error: {str(e)}")

# Call the function to send the message
send_whatsapp_message()

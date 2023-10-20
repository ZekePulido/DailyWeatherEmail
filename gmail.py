import os
import smtplib
import ssl
from email.message import EmailMessage
from weather import email

# Define email sender and receiver
email_sender = 'sender email'
email_password = 'password'  # Replace with your actual email password
email_receiver = 'reciever email'

text = email()

# Set the subject and body of the email
subject = 'Weather'

# Use triple-quoted string to format the body
body = f"""\
{text}
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# Add SSL (layer of security)
context = ssl.create_default_context()

# Log in and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.send_message(em)

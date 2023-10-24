import os
import smtplib
import ssl
from email.message import EmailMessage
from weather import email
import datetime

current_date = datetime.date.today()
formatted_date = current_date.strftime("%m/%d/%Y")


# Define email sender and receiver
email_sender = 'sending email' # Replace with actual sending email
email_password = 'password for sending email'  # Replace with your actual email password
email_receiver = 'receiving email' # Replace with receiving email

text = email()

# Set the subject and body of the email
subject = f'Weather {formatted_date}'

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

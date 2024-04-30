import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# SMTP server configuration
server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
server.starttls()

# Read password from a file
with open('pwd.txt', 'r') as file:
    pwd = file.read().strip()

try:
    # Login to the SMTP server
    server.login('rexxstark20@myyahoo.com', pwd)
except smtplib.SMTPAuthenticationError:
    print('Error: Failed to authenticate with the SMTP server')
    server.quit()
    exit()

# Create the email message
msg = MIMEMultipart()
msg['From'] = 'rexxstark20@myyahoo.com'
msg['To'] = 'virgostores48@gmail.com'
msg['Subject'] = 'Python msg'

# Read the message body from a file
with open('msg.txt', 'r') as body:
    message = body.read()

# Attach the message body to the email
msg.attach(MIMEText(message, 'plain'))

# Attach an image file
img_filename = 'elijah_drone.jpg'
try:
    with open(img_filename, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename={img_filename}')
    msg.attach(part)
except FileNotFoundError:
    print(f'Error: Attachment file "{img_filename}" not found')

# Send the email
try:
    server.sendmail('rexxstark20@myahoo.com', 'virgostores48@gmail.com', msg.as_string())
    print('Email sent successfully')
except smtplib.SMTPException as e:
    print(f'Error: Failed to send email. {str(e)}')

# Close the SMTP connection
server.quit()
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_host = 'smtp.sendgrid.net'
smtp_port = 587
email = 'apikey'
password = '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'
recipient = 'robertirrgang@outlook.com'

# Create the MIME message
message = MIMEMultipart()
message["From"] = "robertirrgang@outlook.com"  # Replace with the sender's email address
message["To"] = "robertirrgang@outlook.com"  # Replace with the recipient's email address
message["Subject"] = "TEST SUBJECT"

# Add the email body
body = "Hello, this is the body of the email."
message.attach(MIMEText(body, "plain"))

try:
    with smtplib.SMTP(smtp_host, smtp_port) as smtp_server:
        smtp_server.starttls()
        smtp_server.login(email, password)
        smtp_server.sendmail(email, recipient, message)
        print("Email sent successfully!")
except Exception as e:
    print("An error occurred while sending the email:", str(e))
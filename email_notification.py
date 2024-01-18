import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "pazinojumubots@gmail.com"
receiver_email = "ioanna.loseva@gmail.com"
subject = "Notification"

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

smtp_server = "smtp.gmail.com"
smpt_port = 587
smpt_username = "pazinojumubots@gmail.com"
smpt_password = "scdr bvpo hxrf feyv"

def send_email(msg_to_user: str):
    msg.attach(MIMEText(msg_to_user, 'plain'))
    try:
        with smtplib.SMTP(smtp_server, smpt_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
        pass
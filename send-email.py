import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_port = 587
smtp_server = "smtp.gmail.com"
email_from = "itsdurva194@gmail.com"
email_to = "sonardurva194@gmail.com"
pswd = "jayz pgfw vaun pbkq"
subject = "Python Testing Email"

def send_emails(email_to):
    body = f"""
    line1
    line2
    line3
    etc
    """
    msg = MIMEMultipart()
    msg['From'] = email_from
    msg['To'] = email_to
    msg['subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()

    print("Connecting to server...")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls()
    TIE_server.login(email_from,pswd)
    print("Connected to server...")

    print()
    print(f"Sending Email to -{email_to}")
    TIE_server.sendmail(email_from, email_to, text)
    print(f"Email successfully sent to - {email_to}")

    TIE_server.quit()

send_emails(email_to)
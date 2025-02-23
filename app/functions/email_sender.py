import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ..extensions import serializer
from ..celery_worker import celery
from ..config import FROM_EMAIL, PASSWORD

@celery.task
def send_email(subject, body, to_email):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(FROM_EMAIL, PASSWORD)

        server.sendmail(FROM_EMAIL, to_email, msg.as_string())
        server.quit()
        print('Письмо отправлено')
    except Exception as e:
        print('Ошибка при отправке письма', e)

def confirm_token(token, expiration=3600):
    try:
        email = serializer.loads(
            token,
            salt='email-confirm',
            max_age=expiration
        )
    except:
        return False
    return email
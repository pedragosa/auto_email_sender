import smtplib, ssl,os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port = 587
smtp_server = 'smtp.office365.com'
sender_email = 'sender@sender.com'
receiver_email = ['receiver@receiver.com']
subject = "Today's log files"
arrayLines = []

with open('file.log','r',encoding='utf-8') as textFile:
    for line in textFile:
        arrayLines.append(line)
    fullMessage = (','.join(arrayLines)).rstrip(',').replace(',',"")
    message = '{}\n\n{}'.format(subject, fullMessage)
    context = ssl.create_default_context()

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ", ".join(receiver_email)
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    smtp_server = smtplib.SMTP(smtp_server, port)
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.login(sender_email,os.environ.get("email_sender_password"))
    text = msg.as_string()
    smtp_server.sendmail(sender_email, receiver_email, text)
    smtp_server.quit()
    
    print('Email sent successfully')
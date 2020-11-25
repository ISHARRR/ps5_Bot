from email.message import EmailMessage
import smtplib

myEmail = '**********@gmail.com'
key = '**********'

def email(context, privacy='public'):
    msg = EmailMessage()
    msg['Subject'] = context
    msg['From'] = myEmail
    if privacy == 'public':
        msg['To'] = ", ".join(recipients())
    elif privacy == 'private':
        msg['To'] = ", ".join(recipients_test())
    msg.set_content(context)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(myEmail, key)

        smtp.send_message(msg)

def recipients():
    recipients = [myEmail,
                  ]
    return recipients


def recipients_test():
    recipients = [myEmail,
                  ]
    return recipients

import ssl
import smtplib as smt
import os


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465
    context = ssl.create_default_context()

    sender = "tal.matityaho1@gmail.com"
    password = os.getenv("gmail_password")
    print(password)
    receiver = "tal.matityaho1@gmail.com"

    with smt.SMTP_SSL(host, port, context=context) as server:
        server.login(user=sender, password=password)
        server.sendmail(from_addr=sender, to_addrs=receiver, msg=message)

if __name__ == "__main__":
    send_email("ping")


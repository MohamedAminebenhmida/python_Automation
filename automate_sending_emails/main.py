# automate sending emails via python
import smtplib


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    with open('password.txt', 'r') as x:
        password = x.read
    server.login('sender_email@gmail.com', password)
    subject = "good morning from amine!"
    with open('body.txt', 'r') as n:
        body = n.read()

    msg = f"subject: {subject} \n\n\n {body}"
    server.sendmail(
        'sender_email@gmail.com',
        'receiver_email@gmail.com',
        msg
    )
    print('message is sent succefully!')


if __name__ == "__main__":
    send_mail()

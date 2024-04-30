import smtplib

smtp_server = '192.168.1.3'
smtp_port = 25

def test(target, port):
    try:
        server = smtplib.SMTP(target, port)
        server.ehlo()
        server.quit()
        return True

    except Exception as e:
        return False


print(test(smtp_server, smtp_port))

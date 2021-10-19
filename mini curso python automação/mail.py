import smtplib

class Mail:
    smtp_port = ""
    smtp_server = ""
    from_addr = ""
    username = ""
    password = ""
    headers = ""


    def __init__(self, from_addr, username, password, smtp_server, smtp_port):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password
        self.from_addr = from_addr

    def add_header(self, header, value):
        self.headers += f"{header}: {value}\r\n"

    def set_default_headers(self):
        self.headers = ""
        self.add_header("From", self.from_addr)
        self.add_header("Content-Type", "text/html")

    def send_mail(self, to, to_name="", subject="", body=""):
        headers = self.headers

        if to_name != "":
            self.add_header("To", f"{to_name}<{to}>")
        else:
            self.add_header("To", f"{to}")
        
        if subject != "":
            self.add_header("Subject", subject)

        msg = f"{self.headers}\r\n{body}"

        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.ehlo()
        server.starttls()
        server.login(self.username, self.password)
        server.sendmail(self.from_addr, to, msg.encode('utf-8'))
        server.quit()

        self.headers = headers
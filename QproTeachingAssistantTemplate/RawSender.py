import smtplib
from email.mime.text import MIMEText
from email.header import Header
from QuickProject import QproDefaultConsole, QproInfoString


class Sender:
    def __init__(self, email, password, smtp, org_name):
        self.smtp = smtplib.SMTP()
        self.smtp.connect(smtp, 25)
        self.smtp.login(email, password)
        self.sender = email
        self.org_name = org_name

    def send(self, to: list, subject: str, content: str):
        QproDefaultConsole.rule("正在发送")
        QproDefaultConsole.print(QproInfoString, f"收件列表: {to}")
        if isinstance(to, str):
            to = [to]
        message = MIMEText(content, "html", "utf-8")
        message["Subject"] = Header(subject, "utf-8")
        message["From"] = Header(self.org_name, "utf-8")
        message["To"] = Header(", ".join([i.split("@")[0] for i in to]), "utf-8")
        self.smtp.sendmail(self.sender, to, message.as_string())
        QproDefaultConsole.print(QproInfoString, "发送完毕")

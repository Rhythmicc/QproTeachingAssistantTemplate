import yagmail as yag
from QuickProject import QproDefaultConsole, QproInfoString


class Sender:
    def __init__(self, email, password, smtp):
        self.smtp = yag.SMTP(user=email, password=password, host=smtp)

    def send(self, to: list, subject: str, content: str):
        QproDefaultConsole.rule("正在发送")
        QproDefaultConsole.print(QproInfoString, f"收件列表: {to}")
        self.smtp.send(to, subject, content, prettify_html=False)
        QproDefaultConsole.print(QproInfoString, "发送完毕")

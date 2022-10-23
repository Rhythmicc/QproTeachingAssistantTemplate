from QuickProject.Commander import Commander
from . import *

app = Commander()


@app.command()
def send():
    """
    发送成绩邮件.
    Send grade email.
    """
    from .RawSender import Sender
    import time

    sender = Sender(
        config.select("email"),
        config.select("password"),
        config.select("smtp_server"),
        config.select("unit"),
    )

    students = requirePackage(
        "FuckExcel",
        "getFuckExcel",
        "git+https://github.com/Rhythmicc/FuckExcel.git",
    )(config.select("students"))

    students_num = students.sheet_size()[1]

    with open(config.select("content"), "r") as f:
        content_template = f.read()
    grade_detail = ""
    for _id, item in enumerate(students[1, 5:-1]):
        grade_detail += f"{_id + 1}. {item}: " + "{} " + "分<br/>"
    grade_detail += "总评成绩: {} 分"

    for line_id in range(2, students_num):
        if not all(students[line_id, 1:5]):
            continue
        email = students[line_id, 4]
        grade = [i if i else "无" for i in students[line_id, 5:]]
        detail = grade_detail.format(*grade)
        content = (
            content_template.replace("__student_name__", students[line_id, 3])
            .replace("__grade_detail__", detail)
            .replace("__unit__", config.select("unit"))
            .replace("__course_name__", config.select("course_name"))
            .replace("__exam_name__", config.select("exam_name"))
        )
        sender.send([email], config.select("subject"), content)

        QproDefaultConsole.print(QproInfoString, f'发送邮件给 "{email}" 成功!')
        time.sleep(float(config.select("sleep_time")))


def main():
    """
    注册为全局命令时, 默认采用main函数作为命令入口, 请勿将此函数用作它途.
    When registering as a global command, default to main function as the command entry, do not use it as another way.
    """
    app()


if __name__ == "__main__":
    main()

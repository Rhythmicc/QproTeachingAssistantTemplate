import os
import json
from QuickProject import user_lang, QproDefaultConsole, QproInfoString, _ask

enable_config = True
config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../config.json"))


questions = {
    "email": {
        "type": "input",
        "message": "Email for publishing grade" if user_lang != "zh" else "发布成绩的邮箱",
    },
    "password": {
        "type": "password",
        "message": "Password for email" if user_lang != "zh" else "邮箱密码",
    },
    "smtp_server": {
        "type": "input",
        "message": "SMTP server for email" if user_lang != "zh" else "邮箱的SMTP服务器",
    },
    "subject": {
        "type": "input",
        "message": "Subject for email" if user_lang != "zh" else "邮件主题",
    },
    "content": {
        "type": "input",
        "message": "Content Template for email" if user_lang != "zh" else "邮件内容模板",
        "default": "template/1.html",
    },
    "students": {
        "type": "input",
        "message": "Students' email table" if user_lang != "zh" else "学生邮箱表",
        "default": "dist/total.xlsx",
    },
    "course_name": {
        "type": "input",
        "message": "Course name" if user_lang != "zh" else "课程名称",
    },
    "exam_name": {
        "type": "input",
        "message": "Exam name" if user_lang != "zh" else "考试名称",
    },
    "unit": {
        "type": "input",
        "message": "Unit name" if user_lang != "zh" else "单位名称",
    },
    "sleep_time": {
        "type": "input",
        "message": "Sleep time between sending emails"
        if user_lang != "zh"
        else "发送邮件间隔时间",
        "default": "1",
    },
}


def init_config():
    with open(config_path, "w") as f:
        json.dump(
            {i: _ask(questions[i]) for i in questions}, f, indent=4, ensure_ascii=False
        )
    QproDefaultConsole.print(
        QproInfoString,
        f'Config file has been created at: "{config_path}"'
        if user_lang != "zh"
        else f'配置文件已创建于: "{config_path}"',
    )


class QproTeachingAssistantTemplateConfig:
    def __init__(self):
        if not os.path.exists(config_path):
            init_config()
        with open(config_path, "r") as f:
            self.config = json.load(f)

    def select(self, key):
        if key not in self.config and key in questions:
            self.update(key, _ask(questions[key]))
        return self.config[key]

    def update(self, key, value):
        self.config[key] = value
        with open(config_path, "w") as f:
            json.dump(self.config, f, indent=4, ensure_ascii=False)

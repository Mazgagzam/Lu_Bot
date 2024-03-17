from apscheduler.schedulers.background import BackgroundScheduler
import subprocess


class User:
    def __init__(self):
        self.name: str = ""
        self.color: str = ""
        self.update_name()

    def update_name(self):
        subprocess.run(["./env/Scripts/python", "userbot.py"])
        with open("name.txt", "r", encoding="utf-8") as file:
            text = file.read().split("\n")
            self.name = text[0]
            self.color = text[1]

    def __str__(self):
        return self.name


user = User()

scheduler = BackgroundScheduler()
scheduler.add_job(user.update_name, 'interval', minutes=30)
scheduler.start()
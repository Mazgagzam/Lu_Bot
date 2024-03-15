from apscheduler.schedulers.background import BackgroundScheduler
import subprocess


class Name:
    def __init__(self):
        self.name: str = ""
        self.update_name()

    def update_name(self):
        subprocess.run(["./env/Scripts/python", "userbot.py"])
        with open("name.txt", "r", encoding="utf-8") as file:
            self.name = file.read()

    def __str__(self, format_spec):
        return self.name


name = Name()

scheduler = BackgroundScheduler()
scheduler.add_job(name.update_name, 'interval', minutes=30)
scheduler.start()
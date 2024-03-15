import json


class Statistics:
    data_path = "data.json"

    def __init__(self, count: int = 0, users: list[int] = []):
        self.count = count
        self.users = users
        self.load_data()

    def load_data(self):
        with open(self.data_path, "r") as file:
            data = json.load(file)
            self.count = data["count"]

    def save_data(self):
        with open(self.data_path, "w") as file:
            json.dump(dict(self), file)

    def append(self, id: int):
        if id not in self.users:
            self.users.append(id)
            self.save_data()

    def get_data(self):
        return (f"📊 Аналитика данных:\n"
                f"🎨 Создано стикеров: {self.count}\n"
                f"👥 Пользователей: {len(self.users)}")

    def __add__(self, other):
        self.count += other
        self.save_data()

    def __dict__(self):
        return {
            "count": self.count,
            "users": self.users
        }




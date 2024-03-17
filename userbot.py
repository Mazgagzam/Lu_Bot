from pyrogram import Client

from colors import get_color

lu_id = "alua_krr"
api_id = 18579170
api_hash = "58289c5c3c6c6018abed570802b326f3"
app = Client("acc", api_id=api_id, api_hash=api_hash, password="2525")


async def get_name():
    user = (await app.get_users([lu_id]))[0]
    color = get_color(str(user.reply_color.color))

    with open("name.txt", "w+", encoding="utf-8") as file:
        file.write(str(user.first_name) + "\n" + color)


async def main():
    await app.start()
    await get_name()
    await app.stop()


app.run(main())

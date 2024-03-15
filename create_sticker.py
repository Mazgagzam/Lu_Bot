import requests
from asgiref.sync import sync_to_async
import base64

requests.post = sync_to_async(requests.post())


async def create_sticker(text: str, name, count):
    path = f"./photo/{count}.png"
    json = {
        "type": "quote",
        "format": "png",
        "backgroundColor": "#1b1429",
        "width": 4096,
        "height": 4096,
        "scale": 2,
        "messages": [
            {
                "entities": [],
                "chatId": 2050167589,
                "avatar": True,
                "from": {
                    "id": 2050167589,
                    "first_name": name,
                    "last_name": "",
                    "username": "alua_krr",
                    "language_code": "ru",
                    "title": name,
                    "emojiBrand": {
                        "_": "EmojiStatus",
                        "custom_emoji_id": 5458809708439677487
                    },
                    "photo": {
                        "small_file_id": "AQADAgADEdExG8GICEsAEAIAAyUTM3oABOHVNo6TChPyAAQeBA",
                        "small_photo_unique_id": "AgADEdExG8GICEs",
                        "big_file_id": "AQADAgADEdExG8GICEsAEAMAAyUTM3oABOHVNo6TChPyAAQeBA",
                        "big_photo_unique_id": "AgADEdExG8GICEs"
                    },
                    "type": "private",
                    "name": name
                },
                "text": text,
                "replyMessage": {}
            }
        ]
    }
    count += 1
    response = (await requests.post('https://bot.lyo.su/quote/generate', json=json)).json()
    buffer = base64.b64decode(response['result']['image'].encode('utf-8'))

    open(path, 'wb+').write(buffer)

    return path

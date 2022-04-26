import asyncio
import requests

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hlink

from scraper import ParserTesmania

from config import token, channel_id

tesmania = ParserTesmania()
tesmania.login()

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


async def get_fresh_articles():
    while True:
        try:
            fresh = tesmania.get_spacex()
            fresh.update(tesmania.get_tesla())

            if len(fresh) >= 1:
                for key, value in fresh.items():
                    article = f"{hlink(value['article_title'], value['article_url'])}"
                    print("send message")
                    await bot.send_message(chat_id=channel_id, text=article)

            await asyncio.sleep(15)
        except requests.exceptions.HTTPError:
            tesmania.login()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(get_fresh_articles())
    executor.start_polling(dp)

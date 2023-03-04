# (©️) Copyright 2022-2023
# meta developer: @YumaMods
# description: Auto You Tube For You!


from .. import loader, utils
from telethon.tl.types import Message  # type: ignore


@loader.tds
class GoogleForYouMod(loader.Module):
    strings = {
        "name": "YouTubeForYou",
        "youtube": "<emoji document_id=5300882244842300470>👩‍💻</emoji><code> Succesfuly!</code>\n",
    }
    strings_ru = {
        "youtube": "<emoji document_id=5300882244842300470>👩‍💻</emoji><code> Успешно!</code>\n"
    }

    async def googlecmd(self, message: Message):
        args = utils.get_args_raw(message)
        y = args.replace(" ", " ")
        youtube = f"https://m.youtube.com/results?sp=mAEA&search_query={y}"
        await utils.answer(message, self.strings("youtube") + youtube)

# (©️) Copyright 2022-2023
# meta developer: @YumaMods

from .. import loader, utils
from telethon.tl.types import Message  # type: ignore


@loader.tds
class GoogleForYouMod(loader.Module):
    strings = {
        "name": "GoogleForYou",
        "google": "<emoji document_id=5300882244842300470>👩‍💻</emoji><code> Succesfuly Googled!</code>\n",
    }
    strings_ru = {
        "google": "<emoji document_id=5300882244842300470>👩‍💻</emoji><code> Успешно загугленно!</code>\n"
    }

    async def googlecmd(self, message: Message):
        args = utils.get_args_raw(message)
        g = args.replace(" ", "%20")
        google = f"https://google.com/search?q={g}"
        await utils.answer(message, self.strings("google") + google)

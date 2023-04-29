import sys
from pyrogram import Client
from Freaky.utilities import config
from Freaky.console import LOGGER


class Bot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"❄️ sᴛᴀʀᴛɪɴɢ ʏᴏᴜʀ ʙᴏᴛ ✨️...")
        super().__init__(
            "ChampuPlayer",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        self.username = get_me.username
        self.id = get_me.id
        try:
            await self.send_message(
                config.LOG_GROUP_ID,
                f"━━━━━━━━━━━━━━━━━━━\n❄️ʙᴏᴛ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ✨️\n━━━━━━━━━━━━━━━━━━━\n❤️ ɴᴀᴍᴇ › {self.one.name}\n🌸 ʟɪɴᴋ › @{self.one.username}\n📝 ɪᴅ › {self.one.id}\n━━━━━━━━━━━━━━━━━━━\n[ᴄʜᴧᴍᴘᴜ](https://t.me/ll_Champu_ll).\n━━━━━━━━━━━━━━━━━━━",
              disable_web_page_preview=True
            )
        except:
            LOGGER(__name__).error(
                "❄️ ᴘʟᴇᴀsᴇ ғɪʀsᴛ ᴀᴅᴅ ᴍᴜsɪᴄ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ʟᴏɢ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ᴀɴ ᴀᴅᴍɪɴ ✨️..."
            )
            sys.exit()
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != "administrator":
            LOGGER(__name__).error(
                "🥀 𝐏𝐥𝐞𝐚𝐬𝐞, 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐀𝐝𝐝 𝐁𝐨𝐭 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐋𝐨𝐠 𝐆𝐫𝐨𝐮𝐩 𝐀𝐧𝐝 𝐌𝐚𝐤𝐞 𝐀𝐧 𝐀𝐝𝐦𝐢𝐧 🌷..."
            )
            sys.exit()
        LOGGER(__name__).info(f"━━━━━━━━━━━━━━━━━━━\n❄️ʙᴏᴛ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ✨️\n━━━━━━━━━━━━━━━━━━━\n❤️ ɴᴀᴍᴇ › {self.one.name}\n🌸 ʟɪɴᴋ › @{self.one.username}\n📝 ɪᴅ › {self.one.id}\n━━━━━━━━━━━━━━━━━━━\n[ᴄʜᴧᴍᴘᴜ](https://t.me/ll_Champu_ll).\n━━━━━━━━━━━━━━━━━━━")

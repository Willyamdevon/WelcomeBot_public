import disnake
from disnake.ext import commands

from config import Config


class WelcomeBot(commands.InteractionBot):
    def __init__(self) -> None:
        super().__init__(
            intents=disnake.Intents.all(),
        )


bot = WelcomeBot()
bot.load_extensions("modules")

bot.run(Config.TOKEN)

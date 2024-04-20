import disnake
from disnake.ext import commands
import os
from dotenv import load_dotenv


load_dotenv()

class WelcomeBot(commands.InteractionBot):
    def __init__(self) -> None:
        super().__init__(
            intents=disnake.Intents.all(),
        )


bot = WelcomeBot()
bot.load_extensions("modules")

bot.run(os.getenv('TOKEN'))

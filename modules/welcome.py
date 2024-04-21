import aiohttp
import disnake
from disnake.ext import commands
from PIL import Image, ImageDraw, ImageOps, ImageFont
import os
from dotenv import load_dotenv


load_dotenv()

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: disnake.Member) -> None:
        if member.guild.id == int(os.getenv('GUILD_ID')):
            channel = self.bot.get_channel(int(os.getenv('GUILD_ID')))

            url = member.display_avatar.url
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        with open("./src/imgs/avatar.png", "wb") as file:
                            file.write(await response.read())

            avatar = Image.open("./src/imgs/avatar.png")
            avatar = avatar.resize((185, 185))

            mask = Image.new("L", avatar.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, avatar.width, avatar.height), fill=255)

            rounded_image = ImageOps.fit(avatar, mask.size)
            rounded_image.putalpha(mask)
            rounded_image.save("./src/imgs/avatar.png")

            profile = Image.open("./src/imgs/background.png")
            profile = profile.resize((680, 240))
            profile.paste(avatar, (35, 35), rounded_image)


            text = "Добро пожаловать!"

            font = ImageFont.truetype("./src/fonts/font.ttf", size=50)
            font2 = ImageFont.truetype("./src/fonts/font.ttf", size=20)

            draw = ImageDraw.Draw(profile)
            
            name = member.name if len(member.name) < 9 else f'{member.name[:9]}...'

            draw.text((235, 110), text, font=font2, fill=(255, 255, 255))
            draw.text((235, 125), name, font=font, fill=(255, 255, 255))

            profile.save('./src/imgs/TempProfile.png')

            file = disnake.File("./src/imgs/TempProfile.png")

            profile.close()
            avatar.close()
            
            await channel.send(f"Добро пожаловать на сервер, {member.mention}", file=file)
            print('Сообщение добавлено')
        else: print("Несоответствие севера и места принятия")

def setup(bot: commands.Bot) -> None:
    bot.add_cog(Welcome(bot=bot))

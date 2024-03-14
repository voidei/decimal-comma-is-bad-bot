import os
import re

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN: str = str(os.getenv("DISCORD_TOKEN"))

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    guild_count = 0

    for guild in client.guilds:
        print(f"- {guild.id} (name: {guild.name})")

        guild_count = guild_count + 1

    print(f"bot is in {str(guild_count)} guilds")


@client.event
async def on_message(message):
    # comma = re.compile(r"/\d+,\d+/gm")
    # match = comma.search(message.content)
    match = re.search(r"\d+,\d+", message.content)
    # print(f"{match}")
    # print(f"{message.content}")
    if match is not None:
        await message.channel.send("stop using decimal comma!!")


client.run(TOKEN)

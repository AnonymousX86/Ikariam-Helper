# coding=utf-8

from logging import basicConfig, INFO

from discord.ext.commands import Bot
from discord import Game, Status

from bot.src.settings import *


basicConfig(level=INFO)
bot = Bot(
    max_messages=None,
    command_prefix=bot_prefix,
    owner_id=owner_id,
    description='Pomocnik sojuszu Dolina Królów',
    case_insensitive=False,
    help_command=None
)


@bot.event
async def on_ready():
    # Bot-level values
    bot.version = bot_version
    bot.error_color = 0xe60000

    # Login info
    print('Logged on as: {0} ({0.id})'.format(bot.user))

    # Changing presence
    await bot.change_presence(
        status=Status.online,
        activity=Game(name='Ikariam'),
        afk=False
    )

    # Loading cogs
    bot.load_extension('bot.cogs.podstawowe')
    bot.load_extension('bot.cogs.ikariam')

    return

bot.run(secret_token, bot=True)

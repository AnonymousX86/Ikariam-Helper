"""
encoding=utf-8
"""
from logging import basicConfig, INFO
from discord.ext.commands import Bot
from discord import Game, Status
from datetime import datetime

# Invite: https://discordapp.com/api/oauth2/authorize?client_id=672448271792472095&permissions=19520&scope=bot

basicConfig(level=INFO)
bot = Bot(
    max_messages=None,
    command_prefix='.',
    owner_id=309270832683679745,
    description='Pomocnik sojuszu Dolina Królów',
    case_insensitive=False,
    help_command=None
)


@bot.event
async def on_ready():
    # Bot-level values
    bot.version = '0.3'
    # Domyślny kolor błędu
    bot.error_color = 0xe60000

    # Login info
    print('Logged on as: {0} ({0.id})'.format(bot.user))

    # Changing presence
    await bot.change_presence(status=Status.online, activity=Game(name='Ikariam'), afk=False)

    # Loading cogs
    cogs = ['cogs.podstawowe', 'cogs.ikariam']
    for cog in cogs:
        bot.load_extension(cog)

    return

bot.run('NjcyNDQ4MjcxNzkyNDcyMDk1.XjLoSA.PxT0f-qUs1IAnt5LOJ2SjuFBeVg', bot=True)

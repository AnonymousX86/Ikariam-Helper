"""
Invite: https://discordapp.com/api/oauth2/authorize?client_id=672448271792472095&permissions=19520&scope=bot
"""
from logging import basicConfig, INFO
from discord.ext.commands import Bot
from discord import Game, Status

basicConfig(level=INFO)
bot = Bot(
    max_messages=None,
    command_prefix='.',
    owner_id=309270832683679745,
    description='Pomocnik sojuszu Dolina Królów',
    case_insensitive=False
)


@bot.event
async def on_ready():
    # Bot-level values
    bot.version = '0.2'

    # Login info
    print('Logged on as: {0.user} (v{0.version})'.format(bot))

    # Changing presence
    game = Game("Ikariam (Thanathos)")
    await bot.change_presence(status=Status.online, activity=game, afk=False)

    # Changing default help command
    bot.remove_command('help')

    # Loading cogs
    cogs = ['cogs.podstawowe', 'cogs.budynki']
    for cog in cogs:
        bot.load_extension(cog)

    return

bot.run('NjcyNDQ4MjcxNzkyNDcyMDk1.XjLoSA.PxT0f-qUs1IAnt5LOJ2SjuFBeVg', bot=True)

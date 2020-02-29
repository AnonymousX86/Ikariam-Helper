# coding=utf-8

import os
import sqlite3

from ast import literal_eval

from datetime import datetime as d

from discord import __version__ as version, Guild, Embed
from discord.ext import commands as cmd
from discord.utils import get


changelog_data = {
    '0.1': 'Podstawowa wersja bota.\n'
           'Dodane zostały wszystkie komendy z kategorii *"podstawowe"*.',
    '0.2': 'Dodano komendę *"budynki"* zawierającą wszystkie informacje o budynkach.\n'
           'Dodano komendę *"changelog"*.',
    '0.3': 'Dodano komendę *"monument"* zawierającą informacje na temat czasów trwania i odnowienia się '
           'cudów.\n '
           'Dodano komendę *"rada"*.\n'
           'Usunięto błąd związany z komendą *"pomoc"*.\n'
           'Alias *"p"* odwołuje się teraz do *"pomoc"*, a nie do *"ping"*.\n'
           'Zaktualizowano komendę *"pomoc"*, większy odstęp między polami oraz wyświetlane jest więcej typów'
           ' opisów komendy.\n'
           'Poprawki kosmetyczne.',
    '0.4': 'Dodano wszystkie budynki.\n'
           'Dodano wszystkie paczki jednostek.\n'
           'Poprawiono wygląd komend.\n'
           'Zaktualizowano opisy komend.',
    '0.5': 'Dodano wszystkie monumenty.\n',
    '0.6': 'Dodano moduł śledzenia statusu online użytkowników.\n'
}
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


class Podstawowe(cmd.Cog):

    def __init__(self, bot):
        self.bot = bot

    @cmd.Cog.listener()
    async def on_member_update(self, before, after):
        if str(after.status) == 'offline':
            conn = sqlite3.connect(os.path.join(__location__, '../src/users.sqlite'))
            user_id = str(before.id)
            user_datetime = str(d.now().strftime('%Y-%m-%d %H:%M:%S'))
            c = conn.cursor()
            try:
                c.execute('INSERT INTO last_online VALUES (?, ?);', (user_id, user_datetime))
            except sqlite3.IntegrityError:
                c.execute("UPDATE last_online SET datetime = ? WHERE uid = ?;", (user_datetime, user_id))
            conn.commit()
            conn.close()
        return

    @cmd.command(
        name='online',
        description='Pokazuje ostatni status online poszczególnych osób'
    )
    async def online_cmd(self, ctx):
        async with ctx.typing():
            conn = sqlite3.connect(os.path.join(__location__, '../src/users.sqlite'))
            c = conn.cursor()
            users = []
            for user in ctx.guild.members:
                if user.bot:
                    continue
                temp = str(user.id)
                t = (temp,)
                db_user = None
                db_status = 'brak danych'
                for row in c.execute("SELECT * FROM last_online WHERE uid LIKE ?;", t):
                    db_user = get(ctx.guild.members, id=int(row[0]))
                    db_status = row[1]

                if str(user.status) != 'offline':
                    status = 'teraz'
                elif user == db_user:
                    status = db_status
                else:
                    status = 'brak danych'

                nickname = user.display_name
                users.append([nickname, status])

            user_data = '```\n' \
                        'Użytkownik           - ostatnio online\n' \
                        '-------------------------------------------\n'
            for user in users:
                user_data += f'{fixed_width(user[0])} - {fixed_width(user[1])}\n'
            user_data += '```'
        online_embed = Embed(
            title=':green_circle: Ostatnio online',
            description=user_data,
            color=0x009900
        )
        await ctx.send(embed=online_embed)
        return

    @cmd.command(
        name='pomoc',
        description='Wyświetla pomoc na temat komend bota',
        aliases=['p', 'help', 'komendy'],
        help='Wyświetla ten komunikat lub pomoc na temat konkretniej komendy lub kategorii\n'
             '`<...>` - wymagany argument\n'
             '`[...]` - opcjonalny argument\n'
             '`[...|...]` - opcjonalny jeden z kilku argumentów\n'
             '`["..."]` - opcjonalny, konkretny argument',
        bief='Główna komenda pomocy',
        usage='[komenda|kategoria]',
        enabled=True
    )
    async def help_cmd(self, ctx, arg='all'):
        # TODO - sprawdzanie czy komenda jest ukryta
        # TODO - sprawdzanie czy komenda jest włączona

        help_embed = Embed(
            title=':question: Menu pomocy',
            color=0x3498DB
        ).set_thumbnail(
            url=self.bot.user.avatar_url
        ).set_footer(
            text='Prywatny bot sojuszu Ikariam, Dolina Królów',
            icon_url=ctx.message.author.avatar_url
        )

        # Wszystkie kategorie
        cogs = [c for c in self.bot.cogs.keys()]

        # Nie podano kategorii
        if arg == 'all':
            for cog in cogs:

                # Get all commands for each cog
                cog_command = self.bot.get_cog(cog).get_commands()
                command_list = ''
                for command in cog_command:
                    if command.brief:
                        command_list += f'**{command.name}** - *{command.brief}*\n'
                    else:
                        command_list += f'**{command.name}** - *{command.description}*\n'

                # Add field for each cog
                help_embed.add_field(
                    name=cog,
                    value=command_list,
                    inline=False
                )
            help_embed.add_field(
                name='\u200b',
                value=f'Aby poznać szczegóły każdej z kategorii lub komend, użyj:\n'
                      f'`{ctx.prefix}pomoc [kategoria|komenda]`',
                inline=False
            )

        # Podano kategorię
        else:

            # Wszystkie kategorie "lowerspace"
            lower_cogs = [c.lower() for c in cogs]

            # Wszystkie komendy
            all_commands = []
            for temp_cog in cogs:
                for temp_cmd in self.bot.get_cog(temp_cog).get_commands():
                    all_commands.append(temp_cmd)

            # Same nazwy komend
            all_commands_names = [c.name for c in all_commands]

            # Argument jest kategorią
            if arg.lower() in lower_cogs:

                # Lista wszystkich komend w kategorii
                command_list = self.bot.get_cog(cogs[lower_cogs.index(arg.lower())]).get_commands()
                help_text = ''

                for command in command_list:

                    help_text += f'```{command.name}```\n'

                    if command.description:
                        help_text += f'{command.description}\n\n'

                    if command.help:
                        temp_cmd_help = f'**Użycie:** {command.help}\n\n'
                    else:
                        temp_cmd_help = ''

                    if command.help:
                        help_text += f'{temp_cmd_help}'

                    if len(command.aliases) > 0:
                        help_text += f'**Aliasy :** {", ".join(command.aliases)}\n\n'
                    else:
                        help_text += 'Brak aliasów\n\n'

                    help_text += f'**Format :** `{ctx.prefix}' \
                                 f'{command.name}{" " + command.usage + "`" if command.usage is not None else "`"}\n\n'

                help_embed.description = help_text

            # Argument jest komendą
            elif arg.lower() in all_commands_names:
                command = None
                for c in all_commands:
                    if arg.lower() == c.name:
                        command = c

                cmd_help_text = ''

                cmd_help_text += f'```{command.name}```\n'

                if command.description:
                    cmd_help_text += f'{command.description}\n\n'

                if command.help:
                    temp_cmd_help = f'**Użycie:** {command.help}\n\n'
                else:
                    temp_cmd_help = ''

                if command.help:
                    cmd_help_text += f'{temp_cmd_help}'

                if len(command.aliases) > 0:
                    cmd_help_text += f'**Aliasy :** {", ".join(command.aliases)}\n'
                else:
                    cmd_help_text += 'Brak aliasów\n'

                cmd_help_text += f'**Format :** `{ctx.prefix}' \
                                 f'{command.name} {command.usage if command.usage is not None else ""}`\n\n'
                help_embed.description = cmd_help_text

            else:
                # TODO - dodać Embed do 'pomoc' o braku danej komendy
                await ctx.send('Błędna kategoria lub komenda\n'
                               'Sprawdź komendę `pomoc`')
                return

        await ctx.send(embed=help_embed)
        return

    @cmd.command(
        name='hej',
        description='Przywitaj się z botem',
        aliases=['cześć'],
        hidden=True
    )
    async def hello_cmd(self, ctx):
        hello_embed = Embed(
            title=f'Cześć {ctx.author.name}! :hugging:',
            color=0x33cc33
        )
        await ctx.send(embed=hello_embed)
        return

    @cmd.command(
        name='ping',
        description='Narzędzie ping',
        help='Sprawdza opóźnienie bota'
    )
    async def ping_cmd(self, ctx):
        start = d.timestamp(d.now())
        await ctx.send(embed=Embed(
            title=':ping_pong: Pong!',
            color=0xff6600,
            description=f'Opóźnienie wyniosło {float((d.timestamp(d.now()) - start) * 1000)}ms'
        ))
        return

    @cmd.command(
        name='powiedz',
        description='Bot powtórzy po tobie',
        help='Powtarza wprowadzony tekst',
        aliases=['say', 'powtórz', 'papuguj'],
        usage='<tekst>'
    )
    async def say_cmd(self, ctx):
        msg = ctx.message.content

        prefix_used = ctx.prefix
        alias_used = ctx.invoked_with
        text = msg[len(prefix_used) + len(alias_used):]

        if text == '':
            await ctx.send(embed=Embed(
                title=':no_entry: Musisz podać tekst'
            ))
        else:
            await ctx.send(embed=Embed(
                color=0x9999ff,
                description=text
            ))

        return

    @cmd.command(
        name='info',
        description='Informacje na temat bota'
    )
    async def info_command(self, ctx):
        await ctx.send(embed=Embed(
            title=':card_box: Informacje',
            color=0x66ffcc,
        ).add_field(
            name='**Nazwa**',
            value=self.bot.user.name,
            inline=False
        ).add_field(
            name='**Wersja**',
            value=self.bot.version,
            inline=False
        ).add_field(
            name='**Oprogramowanie**',
            value=f'Discord.py v{version}',
            inline=False
        ).add_field(
            name='**Autor bota**',
            value=Guild.get_member(ctx.guild, 309270832683679745),
            inline=False
        ))
        return

    @cmd.command(
        name='changelog',
        description='Ostatnie zmiany bota',
        help='Aby zobaczyć konkretną wersję wpisz jej numer, przykładowo: `0.1`',
        aliases=['cl'],
        usage='[wersja]'
    )
    async def changelog_command(self, ctx, arg_version='all'):
        changelog_embed = Embed(
            title=':gear: Changelog',
            color=0x9900ff
        )

        def add_field(x):
            changelog_embed.add_field(
                name=f'v{x}',
                value=changelog_data[x],
                inline=False
            )

        if arg_version == 'all':
            for ver in changelog_data.keys():
                add_field(ver)
        elif arg_version in changelog_data.keys():
            add_field(arg_version)
        else:
            changelog_embed.add_field(
                name='\u200b',
                value=':no_entry: Błędna wersja!'
            )

        await ctx.send(embed=changelog_embed)
        return

    @cmd.command(
        name='kalkulator',
        description='Prosty kalkulator',
        help='Wpisz zwykłe działanie, bot obsługuje podstawowe działania wraz z nawiasami.\n'
             'Poza podstawowymi 4 działaniami bot obsługuje:\n'
             '`%` - reszta z dzielenia\n'
             '`**` - potęgowanie (nie mylić z `^`)\n'
             '`//` - dzielenie bezprzecinkowe\n'
             '`==` lub `is` - sprawdzenie czy dwie liczby są równe\n'
             '`!=` lub `is not` - sprawdzenie czy dwie liczby __nie są__ równe\n'
             '**Uwaga!** Używaj notacji amerykańskiej, tzn. zamiast przecinka używaj kropki',
        aliases=['kalk', 'licz'],
        usage='<działanie>'
    )
    async def calculator_cmd(self, ctx, *, note=''):
        embed_color = 0x9966ff

        if note == '':
            calc_embed = Embed(
                title=':abacus: Kalkulator',
                description=':no_entry: Nie podano działania'
            )

        else:
            async with ctx.typing():

                calc_error = ''
                error_num = 0
                result = ''
                try:
                    if (n := type(eval(note))) is bool:
                        if n:
                            result = 'Prawda'
                        else:
                            result = 'Fałsz'
                    else:
                        result = round(float(literal_eval(note)), 3)
                except SyntaxError:
                    calc_error = 'Błąd w działaniu'
                    error_num = 1
                except NameError:
                    calc_error = 'Nieobsługiwana wartość w wyrażeniu'
                    error_num = 2
                except TypeError:
                    calc_error = 'Nieobsługiwana wartość w wyrażeniu'
                    error_num = 3
                except ZeroDivisionError:
                    calc_error = 'Nie można dzielić przez 0'
                    error_num = 4
                except FileNotFoundError:
                    calc_error = 'Nieobsługiwana wartość w wyrażeniu'
                    error_num = 5

                if calc_error != '':
                    embed_description = f'Znaleziono błąd:\n` {note} = ? `\n*{calc_error}*'
                else:
                    embed_description = f'Wynik działania:\n` {note} = {result} `'

                if (n := error_num) > 0:
                    embed_footer = f'Błąd numer {n}'
                else:
                    embed_footer = ''

                calc_embed = Embed(
                    title=':abacus: Kalkulator',
                    description=embed_description,
                    color=embed_color
                ).set_footer(
                    text=embed_footer
                )

        await ctx.send(embed=calc_embed)
        return


def setup(bot):
    bot.add_cog(Podstawowe(bot))

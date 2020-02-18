"""
encoding=utf-8
"""
from discord import Embed
from discord.ext import commands as cmd
from discord.utils import get

from src.buildings import infos as building_infos, \
    try_alias as try_building_alias
from src.miracles import infos as miracle_infos, \
    try_alias as try_miracle_alias
from src.armies import minimum as min_army, \
    recommended as rec_army


# Dodawanie separatora
def separate(value, separator=' '):
    result = ''
    for c in range(1, len(n := str(value)) + 1):
        result += n[-c]
        if c % 3 == 0:
            result += separator
    return result[::-1]


# Zmiana pierwszych liter wyrazów na wielkie
def upper_name(name):
    if ' ' not in name:
        return f'{name[0].upper()}{name[1:]}'
    else:
        result = ''
        i = 0
        while True:
            if i >= len(name):
                return result
            elif i == 0:
                result += name[0].upper()
                i += 1
            elif name[i] == ' ':
                result += name[i:i + 2].upper()
                i += 2
            else:
                result += name[i]
                i += 1


class Ikariam(cmd.Cog):

    def __init__(self, bot):
        self.bot = bot

    @cmd.command(
        name='budynek',
        description='Pokazuje informacje na temat danego budynku',
        help='Podaj nazwę budynku aby poznać jego szczegóły.'
             'Dodaj jeszcze poziom budynku, żeby sprawdzić koszty',
        brief='Informacje o budynkach',
        aliases=['b', 'budynki'],
        usage='<budynek> [poziom]'
    )
    async def building_cmd(self, ctx, building='', level=0):

        # Budynek jest przechowywany jako małe litery, aby uniknąć błędów
        building = building.lower()

        # Sprawdzanie aliasów
        building = try_building_alias(building)

        # Domyślny tytuł
        default_title = ':card_index: Architektorium'

        # Nie podano nazwy budynku
        if building == '':
            b_list = ''
            for b in building_infos:
                b_list += f'- {b}\n'
            building_embed = Embed(
                title=default_title,
                color=0xb31919
            ).add_field(
                name='Lista budynków',
                value=f'```md\n{b_list}```'
                      'Jeśli nazwa jest dwuczłonowa to zapisz ją w cudzysłowie.\n'
                      'Na przykład: `"wieża alchemika"`'
            )

        # Nie ma takiego budynku
        elif building not in building_infos:
            building_embed = Embed(
                title=default_title,
                description=f':no_entry: Budynek **{upper_name(building)}** nie istnieje!',
                color=self.bot.error_color
            )

        # Dany budynek nie ma takiego poziomu
        elif level > building_infos[building]['max_level']:
            building_embed = Embed(
                title=default_title,
                description=f':no_entry: Budynek **{upper_name(building)}**'
                            f' ma maksymalny poziom __{building_infos[building]["max_level"]}__!',
                color=self.bot.error_color
            )

        # Błędny poziom (poniżej 0)
        elif level < 0:
            building_embed = Embed(
                title=default_title,
                description=':no_entry: Błędny poziom budynku!',
                color=self.bot.error_color
            )

        # Brak błędów
        else:
            building_embed = Embed(
                title=default_title,
                color=0xb31919
            ).add_field(
                name='Budynek',
                value=f'{upper_name(building)}'
            )

            # Informacje ogólne
            if level == 0:
                building_embed.add_field(
                    name='Opis',
                    value=building_infos[building]['description'],
                    inline=False
                ).add_field(
                    name='Wymagania',
                    value=building_infos[building]['require'],
                    inline=False
                ).add_field(
                    name='Maksymalny poziom',
                    value=building_infos[building]['max_level'],
                    inline=False
                )

            # Informacje na konkretny poziom budynku
            else:
                resources = ''
                for r in building_infos[building]['needed_materials']:
                    if (n := building_infos[building]['materials'][level - 1][r]) >= 0:
                        if r == 'wood':
                            resources += f'<:drewno:671763268049829918>'
                        elif r == 'marble':
                            resources += f'<:marmur:671763268007755786>'
                        elif r == 'crystal':
                            resources += f'<:krysztal:671763268024664074>'
                        elif r == 'sulfur':
                            resources += f'<:siarka:671763267592650762>'
                        else:
                            resources += f'<:wino:671763268053893139>'

                        temp = " | " if r != building_infos[building]["needed_materials"][-1] and \
                            len(building_infos[building]["needed_materials"]) > 1 else ""
                        resources += f' {separate(n)}{temp}'
                        del temp

                building_embed.add_field(
                    name='Poziom',
                    value=level,
                    inline=True
                ).add_field(
                    name='Wymagane surowce',
                    value=resources,
                    inline=False
                )

            # Miniatura budynku
            building_embed.set_thumbnail(
                url=building_infos[building]['icon']
            )

        await ctx.send(embed=building_embed)
        return

    @cmd.command(
        name='monument',
        description='Pokazuje czas odnowienia się cudów',
        brief='Informacje o monumentach',
        help='Podaj nazwę cudu, aby poznać jego szczegóły lub dodaj argument "t", aby zobaczyć skrócony czas.'
             ' (Dla osób z Teokracją)',
        aliases=['m', 'monumenty', 'cud', 'cuda'],
        usage='[nazwa monumentu]'
    )
    async def miracle_cmd(self, ctx, miracle='all'):

        # Domyślne wartości
        default_title = ':classical_building: Monumenty'
        default_color = 0x00cccc

        # Sprawdzanie aliasu
        miracle = try_miracle_alias(miracle)

        # Cud nie został sprecyzowany
        if miracle == 'all':
            miracle_embed = Embed(
                title=default_title,
                color=default_color
            )
            text = '```md\n'
            for miracle in miracle_infos:
                text += f'- {miracle}\n'
            text += '```'
            miracle_embed.add_field(
                name='\u200b',
                value=text,
                inline=False
            )

        # Cud nie istnieje
        elif miracle not in miracle_infos:
            miracle_embed = Embed(
                title=default_title,
                description=f':no_entry: Monument **{upper_name(miracle)}** nie istnieje!',
                color=self.bot.error_color
            )

        # Podano nazwę cudu
        else:
            miracle_description = ''

            for index, description in enumerate(miracle_infos[miracle]['effects']):
                miracle_description += f'**Poziom {index + 1}** - {description}\n\n'
            miracle_embed = Embed(
                title=default_title,
                color=default_color
            ).add_field(
                name='Nazwa',
                value=upper_name(miracle),
                inline=True
            ).add_field(
                name='Czas trwania',
                value=miracle_infos[miracle]['duration'],
                inline=True
            ).add_field(
                name='Cooldown',
                value=miracle_infos[miracle]['cooldown'],
                inline=True
            ).add_field(
                name='Efekty',
                value=miracle_description,
                inline=False
            ).set_thumbnail(
                url=miracle_infos[miracle]['icon']
            )

        await ctx.send(embed=miracle_embed)
        return

    # TODO - komenda: wymagania sojuszu

    @cmd.command(
        name='rada',
        description='Pokazuje całą Radę Sojuszu',
        help='Komenda działa tylko na Discordzie sojuszu',
        aliases=['sojusz', 'soj']
    )
    async def council_cmd(self, ctx):

        # Przywódca
        leader_role = get(ctx.guild.roles, name='Przywódca')
        leader_user = '\u200b'

        # Generał
        general_role = get(ctx.guild.roles, name='Generał')
        general_user = '\u200b'

        # Dyplomata
        diplomat_role = get(ctx.guild.roles, name='Dyplomata')
        diplomat_user = '\u200b'

        # Minster Spraw Wewnętrznych
        msw_role = get(ctx.guild.roles, name='Minister Spraw Wewnętrznych')
        msw_user = '\u200b'

        # Rada Sojuszu
        council_role = get(ctx.guild.roles, name='Rada Sojuszu')
        council_users = '\u200b'

        for member in ctx.guild.members:

            """
            Nazwy użytkowników są dodawane, a nie podmieniane, aby uzyskać dodatkowo funkcję debugowania
            """

            if leader_role in member.roles:
                leader_user += f'{member.display_name}'
                if member.nick is None:
                    leader_user += ' *(brak nicku)*'
                leader_user += '\n'

            if general_role in member.roles:
                general_user += f'{member.display_name}'
                if member.nick is None:
                    general_user += ' *(brak nicku)*'
                general_user += '\n'

            if diplomat_role in member.roles:
                diplomat_user += f'{member.display_name}'
                if member.nick is None:
                    diplomat_user += ' *(brak nicku)*'
                diplomat_user += '\n'

            if msw_role in member.roles:
                msw_user += f'{member.display_name}'
                if member.nick is None:
                    msw_user += ' *(brak nicku)*'
                msw_user += '\n'

            if council_role in member.roles and \
                    leader_role not in member.roles and \
                    general_role not in member.roles and \
                    diplomat_role not in member.roles and \
                    msw_role not in member.roles:

                council_users += f'{member.display_name}'
                if member.nick is None:
                    council_users += ' *(brak nicku)*'
                council_users += '\n'

        council_embed = Embed(
            title=':man_mage: Rada Sojuszu',
            color=0xe67300
        ).add_field(
            name='Przywódca',
            value=leader_user,
            inline=False
        ).add_field(
            name='Generał',
            value=general_user,
            inline=False
        ).add_field(
            name='Dyplomata',
            value=diplomat_user,
            inline=False
        ).add_field(
            name='Minister Spraw Wewnętrznych',
            value=msw_user,
            inline=False
        ).add_field(
            name='Rada Sojuszu',
            value=council_users,
            inline=False
        )

        await ctx.send(embed=council_embed)
        return

    @cmd.command(
        name='wojsko',
        description='Pokazuje zalecane i minimalne paczki wojska dla graczy',
        brief='Paczki wojsk',
        aliases=['w'],
        usage='[minimum|zalecane] [ląd|flota]'
    )
    async def army_cmd(self, ctx, min_or_max='minimum', land_or_fleet='both'):
        # Aliasy
        aliases = {
            'minimum': ('minimum', 'min', 'm'),
            'zalecane': ('zalecane', 'zal', 'z'),
            'ląd': ('ląd', 'lad', 'l'),
            'flota': ('flota', 'f'),
            'both': ('both', 'obie', '2')
        }

        # Sprawdzanie aliasów
        if land_or_fleet in aliases['ląd']:
            land_or_fleet = 'ląd'
        elif land_or_fleet in aliases['flota']:
            land_or_fleet = 'flota'
        elif land_or_fleet in aliases['both']:
            land_or_fleet = 'both'

        army = ''

        # Wybrano zestaw jednostek "minimum"
        if min_or_max in aliases['minimum']:

            army += '*- Zestaw minimalny*\n'

            # Jeśli wybrano jednostki lądowe lub nie sprecyzowano
            if land_or_fleet == 'ląd' or land_or_fleet == 'both':
                army += '**JEDNOSTKI LĄDOWE**\n'
                for unit in min_army['land']:
                    if (n := min_army["land"][unit]["amount"]) > 0:
                        army += f'\u00A0\u00A0{upper_name(unit)} - {n}\n'

            # Jeśli wybrano jednostki morskie lub nie sprecyzowano
            if land_or_fleet == 'flota' or land_or_fleet == 'both':
                army += '**JEDNOSTKI MORSKIE**\n'
                for unit in min_army['fleet']:
                    if (n := min_army["fleet"][unit]["amount"]) > 0:
                        army += f'\u00A0\u00A0{upper_name(unit)} - {n}\n'

            # Błędny wybór
            else:
                army = f':no_entry: Typ jednostek **{land_or_fleet}** nie istnieje!'

        # Wybrano zestaw jednostek "zalecane"
        elif min_or_max in aliases['zalecane']:

            army += '*- Zestaw zalecany*\n'

            # Jeśli wybrano jednostki lądowe lub nie sprecyzowano
            if land_or_fleet == 'ląd' or land_or_fleet == 'both':
                army += '**JEDNOSTKI LĄDOWE**\n'
                for unit in rec_army['land']:
                    if (n := rec_army["land"][unit]["amount"]) > 0:
                        army += f'\u00A0\u00A0{upper_name(unit)} - {n}\n'

            # Jeśli wybrano jednostki morskie lub nie sprecyzowano
            if land_or_fleet == 'flota' or land_or_fleet == 'both':
                army += '**JEDNOSTKI MORSKIE**\n'
                for unit in rec_army['fleet']:
                    if (n := rec_army["fleet"][unit]["amount"]) > 0:
                        army += f'\u00A0\u00A0{upper_name(unit)} - {n}\n'

            # Błędny wybór
            else:
                army = f':no_entry: Typ jednostek **{land_or_fleet}** nie istnieje!'

        # Błąd wybory zestawu jednostek
        else:
            army = f':no_entry: Zestaw jednostek **{min_or_max}** nie istnieje'

        # TODO - podawanie kosztów każdego z zestawów

        army_embed = Embed(
            title=':crossed_swords: Wojska',
            color=0xffcc00,
            description=army
        ).add_field(
            name='\u200b',
            value=f'Sprawdź składnię komendy za pomocą:\n'
                  f'`{ctx.prefix}pomoc wojsko`',
            inline=False
        )
        await ctx.send(embed=army_embed)
        return


def setup(bot):
    bot.add_cog(Ikariam(bot))

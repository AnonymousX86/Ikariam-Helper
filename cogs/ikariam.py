"""
encoding=utf-8
"""
from discord.ext import commands as cmd
from discord import Embed
from src.buildings import infos as building_infos,\
    change_icon as change_building_icon,\
    try_alias as try_building_alias
from src.miracles import infos as miracle_infos,\
    change_icon as change_miracle_icon,\
    try_alias as try_miracle_alias


# Dodawanie separatora
def separate(value, separator=' '):
    data = str(value)
    result = ''
    for c in range(1, len(data) + 1):
        result += data[-c]
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


error_color = 0xe60000


class Ikariam(cmd.Cog):

    def __init__(self, bot):
        self.bot = bot

    @cmd.command(
        name='budynek',
        description='Pokazuje informacje na temat danego budynku',
        help='Podaj nazwę budynku aby poznać jego szczegóły.'
             'Dodaj jeszcze poziom budynku, żeby sprawdzić koszty',
        brief='Informacje o budowli',
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
                color=error_color
            )

        # Dany budynek nie ma takiego poziomu
        elif level > building_infos[building]['max_level']:
            building_embed = Embed(
                title=default_title,
                description=f':no_entry: Budynek **{upper_name(building)}**'
                            f' ma maksymalny poziom __{building_infos[building]["max_level"]}__!',
                color=error_color
            )

        # Poziom to co najmniej 1
        elif level < 0:
            building_embed = Embed(
                title=default_title,
                description=':no_entry: Błędny poziom budynku!',
                color=error_color
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
                        resources += f' {separate(n)}{" | " if r != building_infos[building]["needed_materials"][-1] and len(building_infos[building]["needed_materials"]) > 1 else ""} '

                building_embed.add_field(
                    name='Poziom',
                    value=level,
                    inline=False
                ).add_field(
                    name='Wymagane surowce',
                    value=resources,
                    inline=False
                )

            # Miniatura budynku
            miniature = change_building_icon(building)
            if miniature != '':
                building_embed.set_thumbnail(
                    url=miniature
                )

        await ctx.send(embed=building_embed)
        return

    @cmd.command(
        name='monument',
        description='Pokazuje czas odnowienia się cudów',
        help='Podaj nazwę cudu, aby poznać jego szczegóły lub dodaj argument "t", aby zobaczyć skrócony czas.'
             '(Dla osób z Teokracją)',
        aliases=['m', 'monumenty', 'cud', 'cuda'],
        usage='[nazwa monumentu] ["t"]',
        enabled=False
    )
    async def miracle_cmd(self, ctx, miracle='all', theocracy='n'):

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
            # TODO - wyświetlane są wszystkie monumenty (czas bez Teokracji)

        # Podano tylko argument "t"
        elif miracle == 't':
            miracle_embed = Embed(
                title=default_title,
                color=default_color
            )
            # TODO - wyświetlane są wszystkie monumenty (czas z Teokracją)

        # Cud nie istnieje
        elif miracle not in miracle_infos:
            miracle_embed = Embed(
                title=default_title,
                description=f':no_entry: Monument **{upper_name(miracle)}** nie istnieje!',
                color=error_color
            )

        # Podano argument "t"
        elif theocracy == 't':
            miracle_embed = Embed(
                title=default_title,
                color=default_color
            )
            # TODO - wysyłany jest konkretny monument (czas z Teokracją)

        # Podano nazwę cudu, ale bez Teokracji
        else:
            miracle_embed = Embed(
                title=default_title,
                color=default_color
            )
            # TODO - wysyłany jest konkretny monument (czas bez teokracji)

        await ctx.send(embed=miracle_embed)
        return

    # TODO - komenda: wymagania sojuszu


def setup(bot):
    bot.add_cog(Ikariam(bot))

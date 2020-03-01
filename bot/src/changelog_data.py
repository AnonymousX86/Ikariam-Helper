# Dodano
green_plus = '<:green_plus:683603513728696333>'

# Usunięto
red_minus = '<:red_minus:683603496695758859>'

# Zaktualizowano
blue_star = '<:blue_star:683603461526650890>'

# Zmieniono
orange_star = '<:orange_star:683603485953884185>'

# Domyślny prefix
prefix = '\u00a0- '
spaced_prefix = '\u00a0\u00a0\u00a0\u00a0\u2022 '

changelog_data = {
    '0.1': f':partying_face: Podstawowa wersja bota.\n'
           f'{green_plus} **DODANO:**\n'
           f'{prefix}wszystkie komendy z kategorii `podstawowe`.\n',

    '0.2': f'{green_plus} **DODANO:**\n'
           f'{prefix}komendę `budynki` zawierającą wszystkie informacje o budynkach.\n'
           f'{prefix}komendę `changelog`.\n',

    '0.3': f'{green_plus} **DODANO:**\n'
           f'{prefix}komendę `monument` zawierającą informacje na temat czasów trwania i odnowienia się cudów.\n '
           f'{prefix}komendę `rada`.\n\n'
           
           f'{red_minus} **USUNIĘTO:**\n'
           f'{prefix}błąd związany z komendą `pomoc`.\n\n'
           
           f'{blue_star} **ZAKTUALIZOWANO:**\n'
           f'{prefix}komendę `pomoc`, większy odstęp między polami oraz wyświetlane jest więcej typów'
           ' opisów komendy.\n\n'
           
           f'{orange_star} **ZMIENIONO**:\n'
           f'{prefix}wygląd niektórych komend bota\n'
           f'{prefix}alias `p`, odwołuje się teraz do `pomoc`, a nie do `ping`\n\n',
           
    '0.4': f'{green_plus} **DODANO:**\n'
           f'{prefix}wszystkie budynki\n'
           f'{prefix}wszystkie paczki jednostek\n\n'
           
           f'{blue_star} **ZAKTUALIZOWANO:**\n'
           f'{prefix}opisy komend\n\n'

           f'{orange_star} **ZMIENIONO:**\n'
           f'{prefix}wygląd komend\n\n',

    '0.5': f'{green_plus} **DODANO:**\n'
           f'{prefix}wszystkie monumenty\n\n',

    '0.6': f'{green_plus} **DODANO:**\n'
           f'{prefix}moduł śledzenia statusu online użytkowników\n\n',

    '0.7': f'{green_plus} **DODANO:**\n'
           f'{prefix}komendę dla administratora (administratorów) bota\n\n'
           
           f'{blue_star} **ZAKTUALIZOWANO:**\n'
           f'{prefix}komendę `pomoc`.\n'
           f'{prefix}format `changelog`:\n'
           f'{spaced_prefix}nowe i zaktualizowane komendy są wyświetlanie jako `inline code block`,'
           ' zamiast *"kursywy w cudzysłowie"*\n'
           f'{spaced_prefix}domyślnie wyświetlana jest ostatnia wersja zamiast wszystkich wersji\n'
           f'{spaced_prefix}zmiany są lepiej skategoryzowane\n'
           f'{spaced_prefix}każda podkategoria ma teraz swoje emoji\n\n',
}

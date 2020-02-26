"""
encoding=utf-8
"""
infos = {
    'kuźnia hefajstosa': {
        'duration': '1 dzień',
        'cooldown': '7 dni',
        'effects': [
            'Opancerzenie wszystkich bojowych jednostek zostało zwiększone o 0, a zadawane obrażenia o 10%.',
            'Opancerzenie wszystkich bojowych jednostek zostało zwiększone o 1, a zadawane obrażenia o 10%.',
            'Opancerzenie wszystkich bojowych jednostek zostało zwiększone o 1, a zadawane obrażenia o 15%.',
            'Opancerzenie wszystkich bojowych jednostek zostało zwiększone o 2, a zadawane obrażenia o 15%.',
            'Opancerzenie wszystkich bojowych jednostek zostało zwiększone o 2, a zadawane obrażenia o 20%.',
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/wonder/w1.png'
    },
    'święty gaj hadesa': {
        'duration': '16 godzin',
        'cooldown': '4 dni',
        'effects': [
            '20% kosztów surowca wszystkich jednostek, które zginęły w potyczkach we własnych miastach zostanie'
            ' zwrócone w postaci Marmuru.',
            '30% kosztów surowca wszystkich jednostek, które zginęły w potyczkach we własnych miastach zostanie'
            ' zwrócone w postaci Marmuru.',
            '40% kosztów surowca wszystkich jednostek, które zginęły w potyczkach we własnych miastach zostanie'
            ' zwrócone w postaci Marmuru.',
            '50% kosztów surowca wszystkich jednostek, które zginęły w potyczkach we własnych miastach zostanie'
            ' zwrócone w postaci Marmuru.',
            '80% kosztów surowca wszystkich jednostek, które zginęły w potyczkach we własnych miastach zostanie'
            ' zwrócone w postaci Marmuru.'
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/wonder/w2.png'
    },
    'ogrody demeter': {
        'duration': '36 godzin',
        'cooldown': '9 dni',
        'effects': [
            'Przyrost ludności w Twoich miastach zwiększył się o 2/h.',
            'Przyrost ludności w Twoich miastach zwiększył się o 3/h.',
            'Przyrost ludności w Twoich miastach zwiększył się o 6/h.',
            'Przyrost ludności w Twoich miastach zwiększył się o 8/h.',
            'Przyrost ludności w Twoich miastach zwiększył się o 12/h.'
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/wonder/w3.png'
    },
    'świątynia ateny': {
        'duration': '1 dzień',
        'cooldown': '7 dni',
        'effects': [
            '+40% bezpiecznych surowców we wszystkich magazynach.',
            '+80% bezpiecznych surowców we wszystkich magazynach.',
            '+160% bezpiecznych surowców we wszystkich magazynach.',
            '+240% bezpiecznych surowców we wszystkich magazynach.',
            '+400% bezpiecznych surowców we wszystkich magazynach.',
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/wonder/w4.png'
    },
    'świątynia hermesa': {
        'duration': '4 godziny',
        'cooldown': '1 dzień',
        'effects': [
            'Szybkość załadowania towarów wzrośnie o 40%.',
            'Szybkość załadowania towarów wzrośnie o 80%.',
            'Szybkość załadowania towarów wzrośnie o 120%.',
            'Szybkość załadowania towarów wzrośnie o 160%.',
            'Szybkość załadowania towarów wzrośnie o 200%.',
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/wonder/w5.png'
    },
    'forteca aresa': {
        'duration': '12 godzin',
        'cooldown': '3 dni',
        'effects': [
            '+100 morale na jedną rundę bitwy dla wszystkich armii w Twoich miastach - również dla wrogich jednostek!',
            '+200 morale na jedną rundę bitwy dla wszystkich armii w Twoich miastach - również dla wrogich jednostek!',
            '+400 morale na jedną rundę bitwy dla wszystkich armii w Twoich miastach - również dla wrogich jednostek!',
            '+600 morale na jedną rundę bitwy dla wszystkich armii w Twoich miastach - również dla wrogich jednostek!',
            '+2000 morale na jedną rundę bitwy dla wszystkich armii w Twoich miastach - również dla wrogich jednostek!',
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/wonder/w6.png'
    },
    'świątynia posejdona': {
        'duration': '4 godziny',
        'cooldown': '1 dzień',
        'effects': [
            '10% zwiększenie szybkości statków wojennych i transportowców.',
            '30% zwiększenie szybkości statków wojennych i transportowców.',
            '50% zwiększenie szybkości statków wojennych i transportowców.',
            '70% zwiększenie szybkości statków wojennych i transportowców.',
            '100% zwiększenie szybkości statków wojennych i transportowców.',
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/wonder/w7.png'
    },
    'kolos': {
        'duration': '-',
        'cooldown': '3 dni',
        'effects': [
            '10% wszystkich walczących wrogich oddziałów lądowych i statków zostało zmuszonych do ucieczki z twoich'
            ' miast. Czas rozproszenia 4h zwiększył się o 30m.',
            '20% wszystkich walczących wrogich oddziałów lądowych i statków zostało zmuszonych do ucieczki z twoich'
            ' miast. Czas rozproszenia 4h zwiększył się o 1h.',
            '30% wszystkich walczących wrogich oddziałów lądowych i statków zostało zmuszonych do ucieczki z twoich'
            ' miast. Czas rozproszenia 4h zwiększył się o 1h 30m.',
            '50% wszystkich walczących wrogich oddziałów lądowych i statków zostało zmuszonych do ucieczki z twoich'
            ' miast. Czas rozproszenia 4h zwiększył się o 2h.',
            '100% wszystkich walczących wrogich oddziałów lądowych i statków zostało zmuszonych do ucieczki z twoich'
            ' miast. Czas rozproszenia 4h zwiększył się o 3h.',
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/wonder/w8.png'
    },
}


def try_alias(name):
    if name in ('kuźnia', 'kuznia', 'kuznia hefajstosa', 'hefajstosa', 'hefajstos'):
        return 'kuźnia hefajstosa'
    elif name in ('swiety gaj hadesa', 'święty gaj', 'gaj', 'hades'):
        return 'święty gaj hadesa'
    elif name in ('ogrody', 'ogrod', 'ogród', 'demeter'):
        return 'ogrody demeter'
    elif name == 'atena':
        return 'świątynia ateny'
    elif name == 'hermes':
        return 'świątynia hermesa'
    elif name in ('forteca', 'ares'):
        return 'forteca aresa'
    elif name == 'posejdon':
        return 'świątynia posejdona'
    # Monument "kolos" nie ma aliasu
    else:
        return name

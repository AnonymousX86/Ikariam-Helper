"""
encoding=utf-8
"""
infos = {
    'kuźnia hefajstosa': {
        'duration': {
            'normal': '1D',
            'short': '0.5D'
        },
        'cooldown': {
            'normal': '7D',
            'short': '3.5D'
        },
        'effects': [
            'Opancerzenie wszystkich bojowych jednostek zostało zwiększone o 0, a zadawane obrażenia o 10%.',
            'Opancerzenie wszystkich bojowych jednostek zostało zwiększone o 1, a zadawane obrażenia o 10%.',
            'Opancerzenie wszystkich bojowych jednostek zostało zwiększone o 1, a zadawane obrażenia o 15%.',
            'Opancerzenie wszystkich bojowych jednostek zostało zwiększone o 2, a zadawane obrażenia o 15%.',
            'Opancerzenie wszystkich bojowych jednostek zostało zwiększone o 2, a zadawane obrażenia o 20%.',
        ]
    },
    'święty gaj hadesa': {},
    'ogrody demeter': {},
    'świątynia ateny': {},
    'świątynia hermesa': {},
    'forteca aresa': {},
    'świątynia posejdona': {},
    'kolos': {},
}


def change_icon(name):
    if name == 'kuźnia hefajstosa':
        return 'https://vignette.wikia.nocookie.net/ikariam/images/4/4c/Hephaistos\'_Forge.gif/revision/latest?cb' \
               '=20090904181708'
    else:
        return ''


def try_alias(name):
    if name in ('kuźnia', 'kuznia', 'hefajstosa', 'hefajstos'):
        return 'kuźnia hefajstosa'
    else:
        return name

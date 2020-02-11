"""
encoding=utf-8
"""
infos = {
    'kuźnia hefajstosa': {
        'duration': '1D',
        'cooldown': '7D',
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


# TODO - funkcja zmiany ikony monumentu
def change_icon(name):
    pass


# TODO - funkcja sprawdzania aliasu monumentu
def try_alias(name):
    if name in ('kuźnia', 'kuznia', 'hefajstosa', 'hefajstos'):
        return 'kuźnia hefajstosa'
    else:
        return name

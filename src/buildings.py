"""
encoding=utf-8
"""

# Informacje o budynkach
infos = {
    'ratusz': {
        'description': 'W sercu miasta możesz znaleźć Ratusz, którego poziom oznacza poziom Twojego miasteczka.'
                       ' Bystrzy urzędnicy miejscy, którzy tutaj pracują, uwielbiają udzielać Ci informacji'
                       ' o lokalnej populacji. Każda rozbudowa Ratusza jest równoznaczna z powiększeniem'
                       ' maksymalnej liczby obywateli w mieście.',
        'require': 'Nic',
        'max_level': 40,
        'needed_materials': ['wood', 'marble'],
        'materials': [
            {"wood": 0, "marble": 0},  # level 1
            {"wood": 158, "marble": 0},  # level 2
            {"wood": 335, "marble": 0},  # level 3
            {"wood": 623, "marble": 0},  # level 4
            {"wood": 923, "marble": 285},  # level 5
            {"wood": 1390, "marble": 551},  # level 6
            {"wood": 2015, "marble": 936},  # level 7
            {"wood": 2706, "marble": 1411},  # level 8
            {"wood": 3661, "marble": 2091},  # level 9
            {"wood": 4776, "marble": 2945},  # level 10
            {"wood": 6173, "marble": 4072},  # level 11
            {"wood": 8074, "marble": 5664},  # level 12
            {"wood": 10281, "marble": 7637},  # level 13
            {"wood": 13023, "marble": 10214},  # level 14
            {"wood": 16424, "marble": 13575},  # level 15
            {"wood": 20986, "marble": 18254},  # level 16
            {"wood": 25423, "marble": 23250},  # level 17
            {"wood": 32285, "marble": 31022},  # level 18
            {"wood": 40232, "marble": 40599},  # level 19
            {"wood": 49286, "marble": 52216},  # level 20
            {"wood": 61207, "marble": 68069},  # level 21
            {"wood": 74804, "marble": 87316},  # level 22
            {"wood": 93956, "marble": 115101},  # level 23
            {"wood": 113035, "marble": 145326},  # level 24
            {"wood": 141594, "marble": 191053},  # level 25
            {"wood": 170213, "marble": 241039},  # level 26
            {"wood": 210011, "marble": 312128},  # level 27
            {"wood": 258875, "marble": 403825},  # level 28
            {"wood": 314902, "marble": 515593},  # level 29
            {"wood": 387657, "marble": 666229},  # level 30
            {"wood": 471194, "marble": 850031},  # level 31
            {"wood": 572581, "marble": 1084293},  # level 32
            {"wood": 695617, "marble": 1382827},  # level 33
            {"wood": 854729, "marble": 1783721},  # level 34
            {"wood": 1037816, "marble": 2273687},  # level 35
            {"wood": 1274043, "marble": 2930330},  # level 36
            {"wood": 1529212, "marble": 3692591},  # level 37
            {"wood": 1876201, "marble": 4756439},  # level 38
            {"wood": 2276286, "marble": 6058643},  # level 39
            {"wood": 2761291, "marble": 7716366}  # level 40 max
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/img/city/townhall_l.png'
        # TODO - ilość mieszkańców na poziom Ratusza
    },
    'akademia': {
        'description': 'Akademia jest wzniosłym miejscem pełnym wiedzy,'
                       ' łączącym starą tradycję z nowoczesną technologią.'
                       ' Najmądrzejsze głowy z Twojego miasta oczekują'
                       ' wejścia do tego miejsca! Zauważ, że każdy naukowiec'
                       ' potrzebuje własnego laboratorium za które musisz'
                       ' ponieść koszty. Większa akademia pozwala na zatrudnienie'
                       ' większej ilości naukowców w tym samym czasie.',
        'require': 'Nic',
        'max_level': 32,
        'needed_materials': ['wood', 'crystal'],
        'materials': [
            {"wood": 60, "crystal": 0},  # level 1
            {"wood": 68, "crystal": 0},  # level 2
            {"wood": 115, "crystal": 0},  # level 3
            {"wood": 263, "crystal": 0},  # level 4
            {"wood": 382, "crystal": 225},  # level 5
            {"wood": 626, "crystal": 428},  # level 6
            {"wood": 982, "crystal": 744},  # level 7
            {"wood": 1330, "crystal": 1089},  # level 8
            {"wood": 2004, "crystal": 1748},  # level 9
            {"wood": 2665, "crystal": 2454},  # level 10
            {"wood": 3916, "crystal": 3786},  # level 11
            {"wood": 5156, "crystal": 5216},  # level 12
            {"wood": 7446, "crystal": 7862},  # level 13
            {"wood": 9753, "crystal": 10729},  # level 14
            {"wood": 12751, "crystal": 14599},  # level 15
            {"wood": 18163, "crystal": 21627},  # level 16
            {"wood": 23691, "crystal": 29322},  # level 17
            {"wood": 33451, "crystal": 43020},  # level 18
            {"wood": 43572, "crystal": 58213},  # level 19
            {"wood": 56729, "crystal": 78724},  # level 20
            {"wood": 73833, "crystal": 106414},  # level 21
            {"wood": 103459, "crystal": 154857},  # level 22
            {"wood": 144203, "crystal": 224146},  # level 23
            {"wood": 175058, "crystal": 282572},  # level 24
            {"wood": 243930, "crystal": 408877},  # level 25
            {"wood": 317208, "crystal": 552141},  # level 26
            {"wood": 439968, "crystal": 795252},  # level 27
            {"wood": 536310, "crystal": 1006648},  # level 28
            {"wood": 743789, "crystal": 1449741},  # level 29
            {"wood": 1027470, "crystal": 2079651},  # level 30
            {"wood": 1257246, "crystal": 2642548},  # level 31
            {"wood": 1736683, "crystal": 3790483}  # level 32
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/img/city/academy_l.png'
        # TODO - ilość naukowców na poziom Akademii
    },
    'magazyn': {
        'description': 'Część Twojego zaopatrzenia jest chroniona w magazynie. Magazyn pozwala zabezpieczyć'
                       ' surowce przed splądrowaniem, deszczem, ptakami i innymi zwierzętami. Zarządca magazynu'
                       ' jest zawsze dobrze poinformowany o ilości wolnej przestrzeni w budynku. Rozbudowa Twojego'
                       ' Magazynu pozwala chronić większą ilość surowców.',
        'require': 'Ochrona (Gospodarka)',
        'max_level': 40,
        'needed_materials': ['wood', 'marble'],
        'materials': [
            {"wood": 160, "marble": 0},  # level 1
            {"wood": 288, "marble": 0},  # level 2
            {"wood": 442, "marble": 0},  # level 3
            {"wood": 626, "marble": 96},  # level 4
            {"wood": 847, "marble": 211},  # level 5
            {"wood": 1113, "marble": 349},  # level 6
            {"wood": 1431, "marble": 515},  # level 7
            {"wood": 1813, "marble": 714},  # level 8
            {"wood": 2272, "marble": 953},  # level 9
            {"wood": 2822, "marble": 1240},  # level 10
            {"wood": 3483, "marble": 1584},  # level 11
            {"wood": 4275, "marble": 1997},  # level 12
            {"wood": 5226, "marble": 2492},  # level 13
            {"wood": 6368, "marble": 3086},  # level 14
            {"wood": 7737, "marble": 3800},  # level 15
            {"wood": 9380, "marble": 4656},  # level 16
            {"wood": 11353, "marble": 5683},  # level 17
            {"wood": 13719, "marble": 6915},  # level 18
            {"wood": 16559, "marble": 8394},  # level 19
            {"wood": 19967, "marble": 10169},  # level 20
            {"wood": 24056, "marble": 12299},  # level 21
            {"wood": 28963, "marble": 14855},  # level 22
            {"wood": 34852, "marble": 17922},  # level 23
            {"wood": 41918, "marble": 21602},  # level 24
            {"wood": 50398, "marble": 26019},  # level 25
            {"wood": 60574, "marble": 31319},  # level 26
            {"wood": 72784, "marble": 37678},  # level 27
            {"wood": 87437, "marble": 45310},  # level 28
            {"wood": 105021, "marble": 54468},  # level 29
            {"wood": 126121, "marble": 65458},  # level 30
            {"wood": 151441, "marble": 78645},  # level 31
            {"wood": 181825, "marble": 94471},  # level 32
            {"wood": 218286, "marble": 113461},  # level 33
            {"wood": 262039, "marble": 136249},  # level 34
            {"wood": 314543, "marble": 163595},  # level 35
            {"wood": 377548, "marble": 196409},  # level 36
            {"wood": 453153, "marble": 235787},  # level 37
            {"wood": 543880, "marble": 283041},  # level 38
            {"wood": 652752, "marble": 339745},  # level 39
            {"wood": 783398, "marble": 407790}  # level 40
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/img/city/warehouse_l.png'
        # TODO - pojemność magazynu na poziom i bezpieczna pojemność
    },
    'tawerna': {
        'description': 'Po pracowitym dniu nie ma nic przyjemniejszego niż chłodny dzban wina. Oto dlaczego Twoi'
                       ' obywatele uwielbiają spotkania w tawernie. Kiedy na koniec dnia ostatnia stara pieśń'
                       ' zostanie zaśpiewana, ludzie wesoło i radośnie wyruszają do swoich domów. Każda rozbudowa'
                       ' Twojej Tawerny oznacza możliwość zaserwowania gościom większej ilości wina.',
        'require': 'Prasa do winogron (Gospodarka)',
        'max_level': 47,
        'needed_materials': ['wood', 'marble'],
        'materials': [
            {"wood": 101, "marble": 0},  # level 1
            {"wood": 222, "marble": 0},  # level 2
            {"wood": 367, "marble": 0},  # level 3
            {"wood": 541, "marble": 94},  # level 4
            {"wood": 750, "marble": 122},  # level 5
            {"wood": 1001, "marble": 158},  # level 6
            {"wood": 1302, "marble": 206},  # level 7
            {"wood": 1663, "marble": 267},  # level 8
            {"wood": 2097, "marble": 348},  # level 9
            {"wood": 2617, "marble": 452},  # level 10
            {"wood": 3241, "marble": 587},  # level 11
            {"wood": 3990, "marble": 764},  # level 12
            {"wood": 4888, "marble": 993},  # level 13
            {"wood": 5967, "marble": 1290},  # level 14
            {"wood": 7261, "marble": 1677},  # level 15
            {"wood": 8814, "marble": 2181},  # level 16
            {"wood": 10678, "marble": 2835},  # level 17
            {"wood": 12914, "marble": 3685},  # level 18
            {"wood": 15598, "marble": 4791},  # level 19
            {"wood": 18818, "marble": 6228},  # level 20
            {"wood": 22683, "marble": 8097},  # level 21
            {"wood": 27320, "marble": 10526},  # level 22
            {"wood": 32885, "marble": 13684},  # level 23
            {"wood": 39562, "marble": 17789},  # level 24
            {"wood": 47576, "marble": 23125},  # level 25
            {"wood": 57192, "marble": 30063},  # level 26
            {"wood": 68731, "marble": 39082},  # level 27
            {"wood": 82578, "marble": 50806},  # level 28
            {"wood": 99194, "marble": 66048},  # level 29
            {"wood": 119134, "marble": 85862},  # level 30
            {"wood": 143061, "marble": 111621},  # level 31
            {"wood": 171774, "marble": 145107},  # level 32
            {"wood": 206230, "marble": 188640},  # level 33
            {"wood": 247577, "marble": 245232},  # level 34
            {"wood": 297193, "marble": 318801},  # level 35
            {"wood": 356732, "marble": 414441},  # level 36
            {"wood": 428179, "marble": 538774},  # level 37
            {"wood": 513916, "marble": 700406},  # level 38
            {"wood": 616800, "marble": 910528},  # level 39
            {"wood": 740261, "marble": 1183686},  # level 40
            {"wood": 888413, "marble": 1538791},  # level 41
            {"wood": 1066197, "marble": 2000428},  # level 42
            {"wood": 1279538, "marble": 2600558},  # level 43
            {"wood": 1535545, "marble": 3380726},  # level 44
            {"wood": 1842756, "marble": 4394943},  # level 45
            {"wood": 2211407, "marble": 5713425},  # level 46
            {"wood": 2653789, "marble": 7427454}  # level 47 max
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/img/city/taverne_l.png'
        # TODO - wyszynk i zadowolenie na wyszynk
    },
    'pałac': {
        'description': 'Pałac jest doskonałym miejscem do poprowadzenia Twojego imperium ku przyszłości! Pozwala'
                       ' również na rewelacyjną orientację na morzu. Każda rozbudowa pałacu w Twojej stolicy pozwala'
                       ' na założenie kolejnej kolonii.',
        'require': 'Ekspansja (Żegluga)',
        'max_level': 11,
        'needed_materials': ['wood', 'marble', 'sulfur', 'wine', 'crystal'],
        'materials': [
            {"wood": 712, "marble": 0, "sulfur": 0, "wine": 0, "crystal": 0},  # level 1
            {"wood": 5824, "marble": 1434, "sulfur": 0, "wine": 0, "crystal": 0},  # level 2
            {"wood": 16048, "marble": 4546, "sulfur": 3089, "wine": 0, "crystal": 0},  # level 3
            {"wood": 36496, "marble": 10770, "sulfur": 10301, "wine": 10898, "crystal": 0},  # level 4
            {"wood": 77392, "marble": 23218, "sulfur": 24725, "wine": 22110, "crystal": 21188},  # level 5
            {"wood": 159184, "marble": 48114, "sulfur": 53573, "wine": 44534, "crystal": 42400},  # level 6
            {"wood": 322768, "marble": 97906, "sulfur": 111269, "wine": 89382, "crystal": 84824},  # level 7
            {"wood": 649936, "marble": 197490, "sulfur": 226661, "wine": 179078, "crystal": 169672},  # level 8
            {"wood": 1304272, "marble": 396658, "sulfur": 457445, "wine": 358470, "crystal": 339368},  # level 9
            {"wood": 2612944, "marble": 794994, "sulfur": 919013, "wine": 717254, "crystal": 678760},  # level 10
            {"wood": 4743518, "marble": 1591666, "sulfur": 1842149, "wine": 1434822, "crystal": 1357544}  # level 11 max
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/img/city/palace_l.png'
    },
    'rezydencja gubernatora': {
        'description': 'Gubernator w Twojej kolonii gwarantuje, że wszystkie codzienne zadania administracyjne'
                       ' są odpowiednio wykonywane. Jego obecność obniża poziom korupcji w kolonii. Jeśli'
                       ' kiedykolwiek będziesz chciał przenieść swoją stolicę, to Rezydencja Gubernatora'
                       ' musi być rozbudowana do poziomu Pałacu.',
        'require': 'Ekspansja (Żegluga)',
        'max_level': 11,
        'needed_materials': ['wood', 'marble', 'sulfur', 'wine', 'crystal'],
        'materials': [
            {"wood": 712, "marble": 0, "sulfur": 0, "wine": 0, "crystal": 0},  # level 1
            {"wood": 5824, "marble": 1434, "sulfur": 0, "wine": 0, "crystal": 0},  # level 2
            {"wood": 16048, "marble": 4546, "sulfur": 3089, "wine": 0, "crystal": 0},  # level 3
            {"wood": 36496, "marble": 10770, "sulfur": 10301, "wine": 10898, "crystal": 0},  # level 4
            {"wood": 77392, "marble": 23218, "sulfur": 24725, "wine": 22110, "crystal": 21188},  # level 5
            {"wood": 159184, "marble": 48114, "sulfur": 53573, "wine": 44534, "crystal": 42400},  # level 6
            {"wood": 322768, "marble": 97906, "sulfur": 111269, "wine": 89382, "crystal": 84824},  # level 7
            {"wood": 649936, "marble": 197490, "sulfur": 226661, "wine": 179078, "crystal": 169672},  # level 8
            {"wood": 1304272, "marble": 396658, "sulfur": 457445, "wine": 358470, "crystal": 339368},  # level 9
            {"wood": 2612944, "marble": 794994, "sulfur": 919013, "wine": 717254, "crystal": 678760},  # level 10
            {"wood": 4743518, "marble": 1591666, "sulfur": 1842149, "wine": 1434822, "crystal": 1357544}  # level 11 max
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/img/city/palaceColony_l.png'
    },
    'muzeum': {
        'description': 'W Muzeum Twoi obywatele mogą zobaczyć jak bardzo inne nacje kopiują naszą wspaniałą kulturę.'
                       ' Aby pokazać więcej musisz rozbudować swoje Muzeum. Każda rozbudowa Muzeum pozwala wystawić'
                       ' kolejne dobra kulturowe.',
        'require': 'Wymiana kulturowa (Nauka)',
        'max_level': 21,
        'needed_materials': ['wood', 'marble'],
        'materials': [
            {"wood": 560, "marble": 280},  # level 1
            {"wood": 1435, "marble": 1190},  # level 2
            {"wood": 2748, "marble": 2573},  # level 3
            {"wood": 4716, "marble": 4676},  # level 4
            {"wood": 7669, "marble": 7871},  # level 5
            {"wood": 12099, "marble": 12729},  # level 6
            {"wood": 18744, "marble": 20112},  # level 7
            {"wood": 28710, "marble": 31335},  # level 8
            {"wood": 43661, "marble": 48394},  # level 9
            {"wood": 66086, "marble": 74323},  # level 10
            {"wood": 99724, "marble": 113736},  # level 11
            {"wood": 150181, "marble": 173643},  # level 12
            {"wood": 225866, "marble": 264701},  # level 13
            {"wood": 339394, "marble": 403110},  # level 14
            {"wood": 509686, "marble": 613492},  # level 15
            {"wood": 765124, "marble": 933272},  # level 16
            {"wood": 1148281, "marble": 1419338},  # level 17
            {"wood": 1723017, "marble": 2158158},  # level 18
            {"wood": 2585121, "marble": 3281165},  # level 19
            {"wood": 3878276, "marble": 4988136},  # level 20
            {"wood": 5818009, "marble": 7582731}  # level 21
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/img/city/museum_l.png'
    },
    'port handlowy': {
        'description': 'Twój port jest furtką do świata. Tutaj możesz wynająć statki handlowe i przygotować je do'
                       ' długich podróży. Tutaj możesz także przyjąć drogocenne towary z odległych miejsc.'
                       ' W większych portach handlowych są Twoje statki szybciej ładowane. Jak tylko zakończysz'
                       ' badania "suchy dok" możesz wybudować kolejny port, który zwiększy Twoją szybkość załadowczą.',
        'require': 'Nic',
        'max_level': 47,
        'needed_materials': ['wood', 'marble'],
        'materials': [
            {"wood": 0, "marble": 0},  # level 1
            {"wood": 150, "marble": 0},  # level 2
            {"wood": 274, "marble": 0},  # level 3
            {"wood": 429, "marble": 0},  # level 4
            {"wood": 637, "marble": 0},  # level 5
            {"wood": 894, "marble": 176},  # level 6
            {"wood": 1207, "marble": 326},  # level 7
            {"wood": 1645, "marble": 540},  # level 8
            {"wood": 2106, "marble": 791},  # level 9
            {"wood": 2735, "marble": 1138},  # level 10
            {"wood": 3537, "marble": 1598},  # level 11
            {"wood": 4492, "marble": 2176},  # level 12
            {"wood": 5689, "marble": 2928},  # level 13
            {"wood": 7103, "marble": 3859},  # level 14
            {"wood": 8849, "marble": 5051},  # level 15
            {"wood": 11094, "marble": 6628},  # level 16
            {"wood": 13731, "marble": 8566},  # level 17
            {"wood": 17062, "marble": 11089},  # level 18
            {"wood": 21097, "marble": 14265},  # level 19
            {"wood": 25965, "marble": 18241},  # level 20
            {"wood": 31810, "marble": 23197},  # level 21
            {"wood": 39190, "marble": 29642},  # level 22
            {"wood": 47998, "marble": 37636},  # level 23
            {"wood": 58713, "marble": 47703},  # level 24
            {"wood": 71955, "marble": 60556},  # level 25
            {"wood": 87627, "marble": 76367},  # level 26
            {"wood": 107102, "marble": 96639},  # level 27
            {"wood": 130776, "marble": 122156},  # level 28
            {"wood": 159019, "marble": 153754},  # level 29
            {"wood": 193938, "marble": 194089},  # level 30
            {"wood": 235849, "marble": 244300},  # level 31
            {"wood": 286515, "marble": 307174},  # level 32
            {"wood": 348718, "marble": 386956},  # level 33
            {"wood": 423990, "marble": 486969},  # level 34
            {"wood": 513947, "marble": 610992},  # level 35
            {"wood": 625160, "marble": 769302},  # level 36
            {"wood": 758178, "marble": 965792},  # level 37
            {"wood": 919693, "marble": 1212790},  # level 38
            {"wood": 1116013, "marble": 1523570},  # level 39
            {"wood": 1353517, "marble": 1913073},  # level 40
            {"wood": 1642275, "marble": 2403314},  # level 41
            {"wood": 1990224, "marble": 3015689},  # level 42
            {"wood": 2411062, "marble": 3782993},  # level 43
            {"wood": 2923229, "marble": 4749576},  # level 44
            {"wood": 3541580, "marble": 5959027},  # level 45
            {"wood": 4291524, "marble": 7478201},  # level 46
            {"wood": 5199343, "marble": 9383420}  # level 47 max
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/img/city/port_l.png'
        # TODO - szybkość załadunku
    },
    'stocznia': {
        'description': 'Co to za wyspa bez floty? W Stoczni budowane są potężne okręty wojenne i przygotowywane do'
                       ' dalekich wypraw przez oceany. Piraci na siedmiu morzach trzęsą się na ich widok! Większa'
                       ' Stocznia pozwala szybciej budować okręty.',
        'require': 'Suchy Dok (Wojsko)',
        'max_level': 38,
        'needed_materials': ['wood', 'marble'],
        'materials': [
            {"wood": 105, "marble": 0},  # level 1
            {"wood": 202, "marble": 0},  # level 2
            {"wood": 324, "marble": 0},  # level 3
            {"wood": 477, "marble": 0},  # level 4
            {"wood": 671, "marble": 0},  # level 5
            {"wood": 914, "marble": 778},  # level 6
            {"wood": 1222, "marble": 1052},  # level 7
            {"wood": 1609, "marble": 1397},  # level 8
            {"wood": 2096, "marble": 1832},  # level 9
            {"wood": 2711, "marble": 2381},  # level 10
            {"wood": 3485, "marble": 3071},  # level 11
            {"wood": 4460, "marble": 3942},  # level 12
            {"wood": 5689, "marble": 5038},  # level 13
            {"wood": 7238, "marble": 6420},  # level 14
            {"wood": 9190, "marble": 8161},  # level 15
            {"wood": 11648, "marble": 10354},  # level 16
            {"wood": 14746, "marble": 13118},  # level 17
            {"wood": 18649, "marble": 16601},  # level 18
            {"wood": 23568, "marble": 20989},  # level 19
            {"wood": 29765, "marble": 26517},  # level 20
            {"wood": 37573, "marble": 33484},  # level 21
            {"wood": 47412, "marble": 42261},  # level 22
            {"wood": 59808, "marble": 53321},  # level 23
            {"wood": 75428, "marble": 67256},  # level 24
            {"wood": 95108, "marble": 84814},  # level 25
            {"wood": 119906, "marble": 106938},  # level 26
            {"wood": 151151, "marble": 134814},  # level 27
            {"wood": 190520, "marble": 169937},  # level 28
            {"wood": 240124, "marble": 214192},  # level 29
            {"wood": 302626, "marble": 269954},  # level 30
            {"wood": 381378, "marble": 340214},  # level 31
            {"wood": 480605, "marble": 428741}  # level 32
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/img/city/shipyard_l.png'
        # TODO - dostępne jednostki na dany poziom Stoczni
    },
    'koszary': {
        'description': 'W koszarach niesforna młodzież jest szkolona, aby stała się gorliwymi wojownikami. Twoi'
                       ' żołnierze wiedzą jak posługiwać się mieczami, włóczniami i katapultami. Posiadają także'
                       ' zdolność dowodzenia najpotężniejszymi maszynami wojennymi na polu walki. Żołnierze są'
                       ' szkoleni szybciej, kiedy rozbudujesz swoje koszary.',
        'require': 'Nic',
        'max_level': 49,
        'needed_materials': ['wood', 'marble'],
        'materials': [
            {"wood": 49, "marble": 0},  # level 1
            {"wood": 114, "marble": 0},  # level 2
            {"wood": 195, "marble": 0},  # level 3
            {"wood": 296, "marble": 0},  # level 4
            {"wood": 420, "marble": 0},  # level 5
            {"wood": 574, "marble": 0},  # level 6
            {"wood": 766, "marble": 0},  # level 7
            {"wood": 1003, "marble": 0},  # level 8
            {"wood": 1297, "marble": 178},  # level 9
            {"wood": 1662, "marble": 431},  # level 10
            {"wood": 2115, "marble": 745},  # level 11
            {"wood": 2676, "marble": 1134},  # level 12
            {"wood": 3371, "marble": 1616},  # level 13
            {"wood": 4234, "marble": 2214},  # level 14
            {"wood": 5304, "marble": 2956},  # level 15
            {"wood": 6630, "marble": 3875},  # level 16
            {"wood": 8275, "marble": 5015},  # level 17
            {"wood": 10314, "marble": 6429},  # level 18
            {"wood": 12843, "marble": 8183},  # level 19
            {"wood": 15979, "marble": 10357},  # level 20
            {"wood": 19868, "marble": 13052},  # level 21
            {"wood": 24690, "marble": 16395},  # level 22
            {"wood": 30669, "marble": 20540},  # level 23
            {"wood": 38083, "marble": 25680},  # level 24
            {"wood": 47277, "marble": 32054},  # level 25
            {"wood": 58676, "marble": 39957},  # level 26
            {"wood": 72812, "marble": 49757},  # level 27
            {"wood": 90341, "marble": 61909},  # level 28
            {"wood": 112076, "marble": 76977},  # level 29
            {"wood": 139028, "marble": 95661},  # level 30
            {"wood": 172448, "marble": 118830},  # level 31
            {"wood": 213889, "marble": 147560},  # level 32
            {"wood": 265276, "marble": 183185},  # level 33
            {"wood": 328996, "marble": 227359},  # level 34
            {"wood": 408008, "marble": 282136},  # level 35
            {"wood": 505984, "marble": 350059},  # level 36
            {"wood": 627473, "marble": 434283},  # level 37
            {"wood": 778120, "marble": 538721},  # level 38
            {"wood": 964923, "marble": 668224},  # level 39
            {"wood": 1196558, "marble": 828808},  # level 40
            {"wood": 1483785, "marble": 1027932},  # level 41
            {"wood": 1839947, "marble": 1274847},  # level 42
            {"wood": 2281588, "marble": 1581020},  # level 43
            {"wood": 2829223, "marble": 1960675},  # level 44
            {"wood": 3508290, "marble": 2431447},  # level 45
            {"wood": 4350333, "marble": 3015205},  # level 46
            {"wood": 5394466, "marble": 3739064},  # level 47
            {"wood": 6689191, "marble": 4636650},  # level 48
            {"wood": 8294651, "marble": 5749656}  # level 49 max
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/img/city/barracks_r.png'
        # TODO - dostępne jednostki na dany poziom koszar
    },
    'mur miejski': {
        'description': 'Mur Miejski ochrania Twoich obywateli przed wrogami i palącym słońcem. Miej się na baczności!'
                       ' Wrogowie będą próbowali wydrążyć dziury w Twoim murze albo będą się wspinać na niego. Każdy'
                       ' poziom Twojego Muru Miejskiego podwyższa wytrzymałość Twojego muru..',
        'require': 'Nic',
        'max_level': 48,
        'needed_materials': ['wood', 'marble'],
        'materials': [
            {"wood": 114, "marble": 0},  # level 1
            {"wood": 361, "marble": 203},  # level 2
            {"wood": 657, "marble": 516},  # level 3
            {"wood": 1012, "marble": 892},  # level 4
            {"wood": 1439, "marble": 1344},  # level 5
            {"wood": 1951, "marble": 1885},  # level 6
            {"wood": 2565, "marble": 2535},  # level 7
            {"wood": 3302, "marble": 3315},  # level 8
            {"wood": 4186, "marble": 4251},  # level 9
            {"wood": 5247, "marble": 5374},  # level 10
            {"wood": 6521, "marble": 6721},  # level 11
            {"wood": 8049, "marble": 8338},  # level 12
            {"wood": 9882, "marble": 10279},  # level 13
            {"wood": 12083, "marble": 12608},  # level 14
            {"wood": 14724, "marble": 15402},  # level 15
            {"wood": 17892, "marble": 18755},  # level 16
            {"wood": 21695, "marble": 22779},  # level 17
            {"wood": 26258, "marble": 27607},  # level 18
            {"wood": 31733, "marble": 33402},  # level 19
            {"wood": 38304, "marble": 40355},  # level 20
            {"wood": 46189, "marble": 48699},  # level 21
            {"wood": 55650, "marble": 58711},  # level 22
            {"wood": 67004, "marble": 70726},  # level 23
            {"wood": 80629, "marble": 85144},  # level 24
            {"wood": 96979, "marble": 102446},  # level 25
            {"wood": 116599, "marble": 123208},  # level 26
            {"wood": 140143, "marble": 148122},  # level 27
            {"wood": 168395, "marble": 178019},  # level 28
            {"wood": 202298, "marble": 213896},  # level 29
            {"wood": 242982, "marble": 256948},  # level 30
            {"wood": 291802, "marble": 308610},  # level 31
            {"wood": 350387, "marble": 370605},  # level 32
            {"wood": 420688, "marble": 444998},  # level 33
            {"wood": 505049, "marble": 534270},  # level 34
            {"wood": 606284, "marble": 641397},  # level 35
            {"wood": 727765, "marble": 769949},  # level 36
            {"wood": 873541, "marble": 924213},  # level 37
            {"wood": 1048473, "marble": 1109328},  # level 38
            {"wood": 1258393, "marble": 1331467},  # level 39
            {"wood": 1510294, "marble": 1598031},  # level 40
            {"wood": 1812577, "marble": 1917913},  # level 41
            {"wood": 2175317, "marble": 2301767},  # level 42
            {"wood": 2610603, "marble": 2762392},  # level 43
            {"wood": 3132948, "marble": 3315144},  # level 44
            {"wood": 3759764, "marble": 3978446},  # level 45
            {"wood": 4511941, "marble": 4774409},  # level 46
            {"wood": 5414554, "marble": 5729565},  # level 47
            {"wood": 6497687, "marble": 6875750}  # level 48
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/buildings/y100/wall.png'
        # TODO - szczegóły obronności
    },
    'ambasada': {
        'description': 'Ambasada jest ruchliwym miejscem: Dyplomaci z całego świata negocjują tutaj kontrakty,'
                       ' podpisują traktaty i zakładają sojusze. Jeśli chcesz powiększyć sojusz, musisz rozbudować'
                       ' ambasadę. Każdy następny poziom ambasady zwiększa Twoje punkty dyplomacji.',
        'require': 'Obce kultury (Żegluga)',
        'max_level': 32,
        'needed_materials': ['wood', 'marble'],
        'materials': [
            {"wood": 242, "marble": 155},  # level 1
            {"wood": 415, "marble": 342},  # level 2
            {"wood": 623, "marble": 571},  # level 3
            {"wood": 873, "marble": 850},  # level 4
            {"wood": 1173, "marble": 1190},  # level 5
            {"wood": 1532, "marble": 1606},  # level 6
            {"wood": 1964, "marble": 2112},  # level 7
            {"wood": 2482, "marble": 2730},  # level 8
            {"wood": 3103, "marble": 3484},  # level 9
            {"wood": 3849, "marble": 4404},  # level 10
            {"wood": 4743, "marble": 5527},  # level 11
            {"wood": 5817, "marble": 6896},  # level 12
            {"wood": 7105, "marble": 8566},  # level 13
            {"wood": 8651, "marble": 10604},  # level 14
            {"wood": 10507, "marble": 13090},  # level 15
            {"wood": 12733, "marble": 16123},  # level 16
            {"wood": 15404, "marble": 19824},  # level 17
            {"wood": 18610, "marble": 24339},  # level 18
            {"wood": 22457, "marble": 29846},  # level 19
            {"wood": 27074, "marble": 36566},  # level 20
            {"wood": 32614, "marble": 44764},  # level 21
            {"wood": 39261, "marble": 54765},  # level 22
            {"wood": 47239, "marble": 66967},  # level 23
            {"wood": 56811, "marble": 81853},  # level 24
            {"wood": 68299, "marble": 100014},  # level 25
            {"wood": 82084, "marble": 122170},  # level 26
            {"wood": 98625, "marble": 149201},  # level 27
            {"wood": 118475, "marble": 182178},  # level 28
            {"wood": 142295, "marble": 222411},  # level 29
            {"wood": 170879, "marble": 271495},  # level 30
            {"wood": 205180, "marble": 331377},  # level 31
            {"wood": 246341, "marble": 404433}  # level 32
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/img/city/embassy_l.png'
    },
    'bazar': {
        'description': 'Kupcy i handlowcy przeprowadzają swoje interesy na Bazarze. Tutaj zawsze można ubić dobry'
                       ' interes lub umówić się na polowanie. Kupcy z daleka zmierzają raczej do dużych i dobrze'
                       ' znanych Bazarów! Pojemność Twojego Bazaru wzrasta wraz z każdym poziomem, natomiast'
                       ' zasięg z co drugim poziomem.',
        'require': 'Dobrobyt (Gospodarka)',
        'max_level': 39,
        'needed_materials': ['wood', 'marble'],
        'materials': [
            {"wood": 48, "marble": 0},  # level 1
            {"wood": 173, "marble": 0},  # level 2
            {"wood": 346, "marble": 0},  # level 3
            {"wood": 581, "marble": 0},  # level 4
            {"wood": 896, "marble": 540},  # level 5
            {"wood": 1314, "marble": 792},  # level 6
            {"wood": 1863, "marble": 1123},  # level 7
            {"wood": 2580, "marble": 1555},  # level 8
            {"wood": 3509, "marble": 2115},  # level 9
            {"wood": 4706, "marble": 2837},  # level 10
            {"wood": 6241, "marble": 3762},  # level 11
            {"wood": 8203, "marble": 4945},  # level 12
            {"wood": 10699, "marble": 6450},  # level 13
            {"wood": 13866, "marble": 8359},  # level 14
            {"wood": 17872, "marble": 10774},  # level 15
            {"wood": 22926, "marble": 13820},  # level 16
            {"wood": 29286, "marble": 17654},  # level 17
            {"wood": 37272, "marble": 22469},  # level 18
            {"wood": 47283, "marble": 28503},  # level 19
            {"wood": 59806, "marble": 36051},  # level 20
            {"wood": 75447, "marble": 45482},  # level 21
            {"wood": 94954, "marble": 57240},  # level 22
            {"wood": 119245, "marble": 71883},  # level 23
            {"wood": 149453, "marble": 90092},  # level 24
            {"wood": 186977, "marble": 112712},  # level 25
            {"wood": 233530, "marble": 121067},  # level 26
            {"wood": 291225, "marble": 175556},  # level 27
            {"wood": 362658, "marble": 218617},  # level 28
            {"wood": 451015, "marble": 271878},  # level 29
            {"wood": 560208, "marble": 337705},  # level 30
            {"wood": 695038, "marble": 418983},  # level 31
            {"wood": 861391, "marble": 519260}  # level 32
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/img/city/branchoffice_l.png'
        # TODO - zasięg bazaru
    },
    'warsztat': {
        'description': 'Najlepiej wyszkoleni ludzie z Twojego miasta pracują w warsztacie. To właśnie oni '
                       ' ulepszają broń i okręty w najnowsze wynalazki. Możliwe, że to właśnie dzięki nim'
                       ' będziemy lepsi i silniejsi! Każdy następny poziom budynku pozwala wykonać więcej'
                       ' ulepszeń dla żołnierzy i okrętów.',
        'require': 'Wynalazek (Nauka)',
        'max_level': 32,
        'needed_materials': ['wood', 'marble'],
        'materials': [
            {"wood": 220, "marble": 95},  # level 1
            {"wood": 383, "marble": 167},  # level 2
            {"wood": 569, "marble": 251},  # level 3
            {"wood": 781, "marble": 349},  # level 4
            {"wood": 1023, "marble": 461},  # level 5
            {"wood": 1299, "marble": 592},  # level 6
            {"wood": 1613, "marble": 744},  # level 7
            {"wood": 1971, "marble": 920},  # level 8
            {"wood": 2380, "marble": 1125},  # level 9
            {"wood": 2846, "marble": 1362},  # level 10
            {"wood": 3377, "marble": 1637},  # level 11
            {"wood": 3982, "marble": 1956},  # level 12
            {"wood": 4671, "marble": 2326},  # level 13
            {"wood": 5457, "marble": 2755},  # level 14
            {"wood": 6355, "marble": 3253},  # level 15
            {"wood": 7377, "marble": 3831},  # level 16
            {"wood": 8542, "marble": 4500},  # level 17
            {"wood": 9870, "marble": 5279},  # level 18
            {"wood": 11385, "marble": 6180},  # level 19
            {"wood": 13111, "marble": 7226},  # level 20
            {"wood": 15078, "marble": 8439},  # level 21
            {"wood": 17321, "marble": 9847},  # level 22
            {"wood": 19481, "marble": 11478},  # level 23
            {"wood": 22796, "marble": 13373},  # level 24
            {"wood": 26119, "marble": 15570},  # level 25
            {"wood": 29909, "marble": 18118},  # level 26
            {"wood": 34228, "marble": 21074},  # level 27
            {"wood": 39153, "marble": 24503},  # level 28
            {"wood": 44766, "marble": 28481},  # level 29
            {"wood": 51166, "marble": 33095},  # level 30
            {"wood": 58462, "marble": 38447},  # level 31
            {"wood": 66778, "marble": 44656}  # level 32
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/img/city/workshop_l.png'
    },
    'kryjówka': {
        'description': 'Roztropny przywódca zawsze powinien bacznie obserwować zarówno sprzymierzeńców jak'
                       ' i wrogów. Kryjówka pozwala wynająć szpiega, który potrafi dostarczyć Ci informacje'
                       ' z samego centrum innego miasta. Większa Kryjówka oznacza więcej przestrzeni, czyli'
                       ' możliwość wynajęcia większej ilości szpiegów.',
        'max_level': 32,
        'require': 'Szpiegostwo (Nauka)',
        'needed_materials': ['wood', 'marble'],
        'materials': [
            {"wood": 113, "marble": 0},  # level 1
            {"wood": 248, "marble": 0},  # level 2
            {"wood": 402, "marble": 0},  # level 3
            {"wood": 578, "marble": 129},  # level 4
            {"wood": 779, "marble": 197},  # level 5
            {"wood": 1007, "marble": 275},  # level 6
            {"wood": 1267, "marble": 366},  # level 7
            {"wood": 1564, "marble": 471},  # level 8
            {"wood": 1903, "marble": 593},  # level 9
            {"wood": 2288, "marble": 735},  # level 10
            {"wood": 2728, "marble": 900},  # level 11
            {"wood": 3230, "marble": 1090},  # level 12
            {"wood": 3801, "marble": 1312},  # level 13
            {"wood": 4453, "marble": 1569},  # level 14
            {"wood": 5195, "marble": 1866},  # level 15
            {"wood": 6042, "marble": 2212},  # level 16
            {"wood": 7008, "marble": 2613},  # level 17
            {"wood": 8108, "marble": 3078},  # level 18
            {"wood": 9363, "marble": 3617},  # level 19
            {"wood": 10793, "marble": 4243},  # level 20
            {"wood": 12423, "marble": 4968},  # level 21
            {"wood": 14282, "marble": 5810},  # level 22
            {"wood": 16401, "marble": 6787},  # level 23
            {"wood": 18816, "marble": 7919},  # level 24
            {"wood": 21570, "marble": 9233},  # level 25
            {"wood": 24709, "marble": 10758},  # level 26
            {"wood": 28288, "marble": 12526},  # level 27
            {"wood": 32368, "marble": 14577},  # level 28
            {"wood": 37019, "marble": 16956},  # level 29
            {"wood": 42321, "marble": 19716},  # level 30
            {"wood": 48365, "marble": 22917},  # level 31
            {"wood": 55255, "marble": 26631}  # level 32
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/img/city/safehouse_l.png'
    },
    'leśniczówka': {
        'description': 'Silny drwal potrafi ściąć nawet największe drzewo. Ale również wie, że las musi być'
                       ' uprawiany i nowe drzewa muszą być sadzone i dzięki temu używamy tylko najlepszego'
                       ' drewna do naszych budynków. Produkcja materiałów budowlanych zwiększa się o 2% na'
                       ' każdy poziom budynku.',
        'max_level': 32,
        'require': 'Ulepszone wydobywanie zasobów (Gospodarka)',
        'needed_materials': ['wood', 'marble'],
        'materials': [
            {"wood": 250, "marble": 0},  # level 1
            {"wood": 430, "marble": 104},  # level 2
            {"wood": 664, "marble": 237},  # level 3
            {"wood": 968, "marble": 410},  # level 4
            {"wood": 1364, "marble": 635},  # level 5
            {"wood": 1878, "marble": 928},  # level 6
            {"wood": 2546, "marble": 1309},  # level 7
            {"wood": 3415, "marble": 1803},  # level 8
            {"wood": 4544, "marble": 2446},  # level 9
            {"wood": 6013, "marble": 3282},  # level 10
            {"wood": 7922, "marble": 4368},  # level 11
            {"wood": 10403, "marble": 5781},  # level 12
            {"wood": 13629, "marble": 7617},  # level 13
            {"wood": 17823, "marble": 10004},  # level 14
            {"wood": 23274, "marble": 13108},  # level 15
            {"wood": 30362, "marble": 17142},  # level 16
            {"wood": 39574, "marble": 22386},  # level 17
            {"wood": 51552, "marble": 29204},  # level 18
            {"wood": 67123, "marble": 38068},  # level 19
            {"wood": 87363, "marble": 49589},  # level 20
            {"wood": 113680, "marble": 64569},  # level 21
            {"wood": 147889, "marble": 84041},  # level 22
            {"wood": 192360, "marble": 109356},  # level 23
            {"wood": 250173, "marble": 142266},  # level 24
            {"wood": 325330, "marble": 185046},  # level 25
            {"wood": 423034, "marble": 240663},  # level 26
            {"wood": 550049, "marble": 312965},  # level 27
            {"wood": 715169, "marble": 406956},  # level 28
            {"wood": 929826, "marble": 529144},  # level 29
            {"wood": 1208878, "marble": 687989},  # level 30
            {"wood": 1571647, "marble": 894489},  # level 31
            {"wood": 2043246, "marble": 1162937}  # level 32
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/img/city/forester_l.png'
        # TODO - bonus leśniczówki
    },
    'huta szkła': {
        'description': 'Prawdziwi mistrzowie w swojej sztuce potrafią stworzyć błyszczące fragmenty w Hucie Szkła.'
                       ' Piszczel, szkła i wszystkie inne części naszej aparatury potrafią zrozumieć tylko nasi'
                       ' naukowcy. I są tak zręczni, że rzeczy tworzą się w chwilę. Każdy poziom budynku zwiększa'
                       ' produkcję kryształu o 2%',
        'max_level': 32,
        'require': 'Ulepszone wydobywanie zasobów (Gospodarka)',
        'needed_materials': ['wood', 'marble'],
        'materials': [
            {"wood": 274, "marble": 0},  # level 1
            {"wood": 467, "marble": 116},  # level 2
            {"wood": 718, "marble": 255},  # level 3
            {"wood": 1045, "marble": 436},  # level 4
            {"wood": 1469, "marble": 671},  # level 5
            {"wood": 2021, "marble": 977},  # level 6
            {"wood": 2738, "marble": 1375},  # level 7
            {"wood": 3671, "marble": 1892},  # level 8
            {"wood": 4883, "marble": 2564},  # level 9
            {"wood": 6459, "marble": 3437},  # level 10
            {"wood": 8508, "marble": 4572},  # level 11
            {"wood": 11172, "marble": 6049},  # level 12
            {"wood": 14634, "marble": 7968},  # level 13
            {"wood": 19135, "marble": 10462},  # level 14
            {"wood": 24987, "marble": 13705},  # level 15
            {"wood": 32594, "marble": 17921},  # level 16
            {"wood": 42483, "marble": 23402},  # level 17
            {"wood": 55339, "marble": 30527},  # level 18
            {"wood": 72050, "marble": 39790},  # level 19
            {"wood": 93778, "marble": 51830},  # level 20
            {"wood": 122021, "marble": 67485},  # level 21
            {"wood": 158740, "marble": 87835},  # level 22
            {"wood": 206471, "marble": 114289},  # level 23
            {"wood": 268524, "marble": 148680},  # level 24
            {"wood": 349194, "marble": 193389},  # level 25
            {"wood": 454063, "marble": 251512},  # level 26
            {"wood": 590393, "marble": 327069},  # level 27
            {"wood": 767620, "marble": 425294},  # level 28
            {"wood": 998018, "marble": 552986},  # level 29
            {"wood": 1297536, "marble": 718988},  # level 30
            {"wood": 1686906, "marble": 934789},  # level 31
            {"wood": 2193089, "marble": 1215330}  # level 32
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/img/city/glassblowing_l.png'
        # TODO - bonus Huty Szkła
    },
    'wieża alchemika': {
        'description': 'Kiedy wiatr wieje z zachodu, zapach napełnia ulice wokół wieży i wielu mieszkańców nie'
                       ' opuszcza swoich domów bez klipsa na nosie. Nasz alchemik pracuje bez przerwy, aby znaleźć'
                       ' idealną miksturę i dzięki temu będziemy mogli wydobywać więcej siarki z naszej kopalni.'
                       ' Każdy poziom budynku zwiększa produkcję siarki o 2%',
        'max_level': 32,
        'require': 'Ulepszone wydobywanie zasobów (Gospodarka)',
        'needed_materials': ['wood', 'marble'],
        'materials': [
            {"wood": 274, "marble": 0},  # level 1
            {"wood": 467, "marble": 116},  # level 2
            {"wood": 718, "marble": 255},  # level 3
            {"wood": 1045, "marble": 436},  # level 4
            {"wood": 1469, "marble": 671},  # level 5
            {"wood": 2021, "marble": 977},  # level 6
            {"wood": 2738, "marble": 1375},  # level 7
            {"wood": 3671, "marble": 1892},  # level 8
            {"wood": 4883, "marble": 2564},  # level 9
            {"wood": 6459, "marble": 3437},  # level 10
            {"wood": 8508, "marble": 4572},  # level 11
            {"wood": 11172, "marble": 6049},  # level 12
            {"wood": 14634, "marble": 7968},  # level 13
            {"wood": 19135, "marble": 10462},  # level 14
            {"wood": 24987, "marble": 13705},  # level 15
            {"wood": 32594, "marble": 17921},  # level 16
            {"wood": 42483, "marble": 23402},  # level 17
            {"wood": 55339, "marble": 30527},  # level 18
            {"wood": 72050, "marble": 39790},  # level 19
            {"wood": 93778, "marble": 51830},  # level 20
            {"wood": 122021, "marble": 67485},  # level 21
            {"wood": 158740, "marble": 87835},  # level 22
            {"wood": 206471, "marble": 114289},  # level 23
            {"wood": 268524, "marble": 148680},  # level 24
            {"wood": 349194, "marble": 193389},  # level 25
            {"wood": 454063, "marble": 251512},  # level 26
            {"wood": 590393, "marble": 327069},  # level 27
            {"wood": 767620, "marble": 425294},  # level 28
            {"wood": 998018, "marble": 552986},  # level 29
            {"wood": 1297536, "marble": 718988},  # level 30
            {"wood": 1686906, "marble": 934789},  # level 31
            {"wood": 2193089, "marble": 1215330}  # level 32
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/img/city/alchemist_l.png'
        # TODO - bonus Wieży Alchemika
    },
    'winnica': {
        'description': 'Winiarz wybiera tylko najlepiej nasłonecznione wzgórza z otaczających obszarów, aby'
                       ' zasadzić na nich najsłodsze zielone winogrona. Dlatego winnica produkuje znacznie lepsze'
                       ' wino z naszych owoców. Każdy poziom tego budynku zwiększa Twoją produkcję wina o 2%',
        'max_level': 32,
        'require': 'Ulepszone wydobywanie zasobów (Gospodarka)',
        'needed_materials': ['wood', 'marble'],
        'materials': [
            {"wood": 274, "marble": 0},  # level 1
            {"wood": 467, "marble": 116},  # level 2
            {"wood": 718, "marble": 255},  # level 3
            {"wood": 1045, "marble": 436},  # level 4
            {"wood": 1469, "marble": 671},  # level 5
            {"wood": 2021, "marble": 977},  # level 6
            {"wood": 2738, "marble": 1375},  # level 7
            {"wood": 3671, "marble": 1892},  # level 8
            {"wood": 4883, "marble": 2564},  # level 9
            {"wood": 6459, "marble": 3437},  # level 10
            {"wood": 8508, "marble": 4572},  # level 11
            {"wood": 11172, "marble": 6049},  # level 12
            {"wood": 14634, "marble": 7968},  # level 13
            {"wood": 19135, "marble": 10462},  # level 14
            {"wood": 24987, "marble": 13705},  # level 15
            {"wood": 32594, "marble": 17921},  # level 16
            {"wood": 42483, "marble": 23402},  # level 17
            {"wood": 55339, "marble": 30527},  # level 18
            {"wood": 72050, "marble": 39790},  # level 19
            {"wood": 93778, "marble": 51830},  # level 20
            {"wood": 122021, "marble": 67485},  # level 21
            {"wood": 158740, "marble": 87835},  # level 22
            {"wood": 206471, "marble": 114289},  # level 23
            {"wood": 268524, "marble": 148680},  # level 24
            {"wood": 349194, "marble": 193389},  # level 25
            {"wood": 454063, "marble": 251512},  # level 26
            {"wood": 590393, "marble": 327069},  # level 27
            {"wood": 767620, "marble": 425294},  # level 28
            {"wood": 998018, "marble": 552986},  # level 29
            {"wood": 1297536, "marble": 718988},  # level 30
            {"wood": 1686906, "marble": 934789},  # level 31
            {"wood": 2193089, "marble": 1215330}  # level 32
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/img/city/winegrower_l.png'
        # TODO - bonus Winnicy
    },
    'kamieniarz': {
        'description': 'Wyszkolony kamieniarz swoimi silnymi rękami zawsze bierze właściwe bloki marmuru z'
                       ' kamieniołomu. Rozbija je na mniejsze i nasi budowniczowie mają potrzebne materiały. Każdy'
                       ' poziom tego budynku zwiększa produkcję marmuru o 2%',
        'max_level': 32,
        'require': 'Ulepszone wydobywanie zasobów (Gospodarka)',
        'needed_materials': ['wood', 'marble'],
        'materials': [
            {"wood": 274, "marble": 0},  # level 1
            {"wood": 467, "marble": 116},  # level 2
            {"wood": 718, "marble": 255},  # level 3
            {"wood": 1045, "marble": 436},  # level 4
            {"wood": 1469, "marble": 671},  # level 5
            {"wood": 2021, "marble": 977},  # level 6
            {"wood": 2738, "marble": 1375},  # level 7
            {"wood": 3671, "marble": 1892},  # level 8
            {"wood": 4883, "marble": 2564},  # level 9
            {"wood": 6459, "marble": 3437},  # level 10
            {"wood": 8508, "marble": 4572},  # level 11
            {"wood": 11172, "marble": 6049},  # level 12
            {"wood": 14634, "marble": 7968},  # level 13
            {"wood": 19135, "marble": 10462},  # level 14
            {"wood": 24987, "marble": 13705},  # level 15
            {"wood": 32594, "marble": 17921},  # level 16
            {"wood": 42483, "marble": 23402},  # level 17
            {"wood": 55339, "marble": 30527},  # level 18
            {"wood": 72050, "marble": 39790},  # level 19
            {"wood": 93778, "marble": 51830},  # level 20
            {"wood": 122021, "marble": 67485},  # level 21
            {"wood": 158740, "marble": 87835},  # level 22
            {"wood": 206471, "marble": 114289},  # level 23
            {"wood": 268524, "marble": 148680},  # level 24
            {"wood": 349194, "marble": 193389},  # level 25
            {"wood": 454063, "marble": 251512},  # level 26
            {"wood": 590393, "marble": 327069},  # level 27
            {"wood": 767620, "marble": 425294},  # level 28
            {"wood": 998018, "marble": 552986},  # level 29
            {"wood": 1297536, "marble": 718988},  # level 30
            {"wood": 1686906, "marble": 934789},  # level 31
            {"wood": 2193089, "marble": 1215330}  # level 32
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/img/city/stonemason_l.png'
        # TODO - bonus Kamieniarza
    },
    'warsztat cieśli': {
        'description': 'Tylko najlepsze drzewa są używane w warsztacie cieśli. Dlatego nasz rzemieślnik może budować'
                       ' mocniejsze ramy i nasze domy nie muszą być naprawiane cały czas. Każdy poziom warsztatu'
                       ' cieśli obniża zapotrzebowanie na materiały budowlane o 1% wartości podstawowej.',
        'max_level': 32,
        'require': 'Stolarka (Żegluga)',
        'needed_materials': ['wood', 'marble'],
        'materials': [
            {"wood": 63, "marble": 0},  # level 1
            {"wood": 122, "marble": 0},  # level 2
            {"wood": 191, "marble": 0},  # level 3
            {"wood": 274, "marble": 0},  # level 4
            {"wood": 372, "marble": 0},  # level 5
            {"wood": 486, "marble": 0},  # level 6
            {"wood": 620, "marble": 0},  # level 7
            {"wood": 777, "marble": 359},  # level 8
            {"wood": 962, "marble": 444},  # level 9
            {"wood": 1178, "marble": 546},  # level 10
            {"wood": 1432, "marble": 669},  # level 11
            {"wood": 1730, "marble": 816},  # level 12
            {"wood": 2078, "marble": 993},  # level 13
            {"wood": 2486, "marble": 1205},  # level 14
            {"wood": 2964, "marble": 1459},  # level 15
            {"wood": 3524, "marble": 1765},  # level 16
            {"wood": 4178, "marble": 2131},  # level 17
            {"wood": 4945, "marble": 2571},  # level 18
            {"wood": 5841, "marble": 3097},  # level 19
            {"wood": 6890, "marble": 3731},  # level 20
            {"wood": 8117, "marble": 4490},  # level 21
            {"wood": 9550, "marble": 5402},  # level 22
            {"wood": 11229, "marble": 6496},  # level 23
            {"wood": 13190, "marble": 7809},  # level 24
            {"wood": 15484, "marble": 9383},  # level 25
            {"wood": 18166, "marble": 11274},  # level 26
            {"wood": 21299, "marble": 13543},  # level 27
            {"wood": 24963, "marble": 16265},  # level 28
            {"wood": 29245, "marble": 19531},  # level 29
            {"wood": 34247, "marble": 23450},  # level 30
            {"wood": 40096, "marble": 28154},  # level 31
            {"wood": 46930, "marble": 33798}  # level 32
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/img/city/carpentering_l.png'
    },
    'optyk': {
        'description': 'Soczewka i lupa nie tylko pomaga naszym naukowcom widzieć lepiej i znajdować ważne papiery'
                       ' na swoich biurkach, są również potrzebne do wynalezienia wszystkich nowych technologii,'
                       ' co uczyni nas dumnymi. Optyk przechowuje wszystko czego potrzebujemy ostrożnie w'
                       ' magazynowanych pudełkach, a więc mniej rzeczy się tłucze i zapotrzebowanie na kryształ'
                       ' jest mniejsze w mieście na każdy poziom budynku o 1% wartości podstawowej.',
        'max_level': 32,
        'require': 'Optyka (Nauka)',
        'needed_materials': ['wood', 'marble'],
        'materials': [
            {"wood": 119, "marble": 0},  # level 1
            {"wood": 188, "marble": 35},  # level 2
            {"wood": 269, "marble": 96},  # level 3
            {"wood": 362, "marble": 167},  # level 4
            {"wood": 471, "marble": 249},  # level 5
            {"wood": 597, "marble": 345},  # level 6
            {"wood": 742, "marble": 455},  # level 7
            {"wood": 912, "marble": 584},  # level 8
            {"wood": 1108, "marble": 733},  # level 9
            {"wood": 1335, "marble": 905},  # level 10
            {"wood": 1600, "marble": 1106},  # level 11
            {"wood": 1906, "marble": 1338},  # level 12
            {"wood": 2261, "marble": 1608},  # level 13
            {"wood": 2673, "marble": 1921},  # level 14
            {"wood": 3152, "marble": 2283},  # level 15
            {"wood": 3706, "marble": 2704},  # level 16
            {"wood": 4348, "marble": 3191},  # level 17
            {"wood": 5096, "marble": 3759},  # level 18
            {"wood": 5962, "marble": 4416},  # level 19
            {"wood": 6966, "marble": 5178},  # level 20
            {"wood": 8131, "marble": 6062},  # level 21
            {"wood": 9482, "marble": 7087},  # level 22
            {"wood": 11050, "marble": 8276},  # level 23
            {"wood": 12868, "marble": 9656},  # level 24
            {"wood": 14978, "marble": 11257},  # level 25
            {"wood": 17424, "marble": 13113},  # level 26
            {"wood": 20262, "marble": 15267},  # level 27
            {"wood": 23553, "marble": 17762},  # level 28
            {"wood": 27373, "marble": 20662},  # level 29
            {"wood": 31804, "marble": 24024},  # level 30
            {"wood": 36943, "marble": 27922},  # level 31
            {"wood": 42904, "marble": 32447}  # level 32
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/img/city/optician_l.png'
    },
    'zakład pirotechnika': {
        'description': 'Ciągłe próby z fajerwerkami nie tylko rozświetlały niebo, ale też czasami otaczające'
                       ' budynki. Naszym naukowcom uda się zmniejszyć zużycia siarki, tylko wtedy, gdy będą ciągle'
                       ' testować nowe mikstury. Każdy poziom budynku zmniejsza zapotrzebowanie na siarkę w'
                       ' mieście o 1% podstawowej wartości.',
        'max_level': 32,
        'require': 'Pirotechnika (Wojsko)',
        'needed_materials': ['wood', 'marble'],
        'materials': [
            {"wood": 273, "marble": 135},  # level 1
            {"wood": 353, "marble": 212},  # level 2
            {"wood": 445, "marble": 302},  # level 3
            {"wood": 551, "marble": 405},  # level 4
            {"wood": 673, "marble": 526},  # level 5
            {"wood": 813, "marble": 665},  # level 6
            {"wood": 974, "marble": 827},  # level 7
            {"wood": 1159, "marble": 1015},  # level 8
            {"wood": 1373, "marble": 1233},  # level 9
            {"wood": 1618, "marble": 1486},  # level 10
            {"wood": 1899, "marble": 1779},  # level 11
            {"wood": 2223, "marble": 2120},  # level 12
            {"wood": 2596, "marble": 2514},  # level 13
            {"wood": 3025, "marble": 2972},  # level 14
            {"wood": 3517, "marble": 3503},  # level 15
            {"wood": 4084, "marble": 4119},  # level 16
            {"wood": 4736, "marble": 4834},  # level 17
            {"wood": 5485, "marble": 5662},  # level 18
            {"wood": 6346, "marble": 6623},  # level 19
            {"wood": 7338, "marble": 7738},  # level 20
            {"wood": 8478, "marble": 9032},  # level 21
            {"wood": 9790, "marble": 10534},  # level 22
            {"wood": 11297, "marble": 12275},  # level 23
            {"wood": 13030, "marble": 13355},  # level 24
            {"wood": 14990, "marble": 16636},  # level 25
            {"wood": 17317, "marble": 19354},  # level 26
            {"wood": 19954, "marble": 22507},  # level 27
            {"wood": 22986, "marble": 26163},  # level 28
            {"wood": 26472, "marble": 30404},  # level 29
            {"wood": 30484, "marble": 35325},  # level 30
            {"wood": 35096, "marble": 41033},  # level 31
            {"wood": 40399, "marble": 47652}  # level 32
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/img/city/fireworker_l.png'
    },
    'tłocznia win': {
        'description': 'Tylko najczystsze wina dojrzewają głęboko i w chłodnych piwnicach miasta. Właściciel piwnicy'
                       ' dba o to, żeby nic nie przeszkadzało i wszystkie wina trafiły prosto na stoły naszych'
                       ' mieszkańców. Każdy poziom tłoczni win zmniejsza zapotrzebowanie na wino w mieście o 1%'
                       ' wartości podstawowej.',
        'max_level': 32,
        'require': 'Tłocznia win (Gospodarka)',
        'needed_materials': ['wood', 'marble'],
        'materials': [
            {"wood": 339, "marble": 123},  # level 1
            {"wood": 423, "marble": 198},  # level 2
            {"wood": 520, "marble": 285},  # level 3
            {"wood": 631, "marble": 387},  # level 4
            {"wood": 758, "marble": 504},  # level 5
            {"wood": 905, "marble": 640},  # level 6
            {"wood": 1074, "marble": 798},  # level 7
            {"wood": 1269, "marble": 981},  # level 8
            {"wood": 1492, "marble": 1194},  # level 9
            {"wood": 1749, "marble": 1440},  # level 10
            {"wood": 2045, "marble": 1726},  # level 11
            {"wood": 2384, "marble": 2058},  # level 12
            {"wood": 2775, "marble": 2443},  # level 13
            {"wood": 3225, "marble": 2889},  # level 14
            {"wood": 3741, "marble": 3407},  # level 15
            {"wood": 4336, "marble": 4008},  # level 16
            {"wood": 5019, "marble": 4705},  # level 17
            {"wood": 5813, "marble": 5513},  # level 18
            {"wood": 6875, "marble": 6450},  # level 19
            {"wood": 7941, "marble": 7537},  # level 20
            {"wood": 8944, "marble": 8800},  # level 21
            {"wood": 10319, "marble": 10263},  # level 22
            {"wood": 11900, "marble": 11961},  # level 23
            {"wood": 13718, "marble": 13930},  # level 24
            {"wood": 15809, "marble": 16214},  # level 25
            {"wood": 18215, "marble": 18864},  # level 26
            {"wood": 20978, "marble": 21938},  # level 27
            {"wood": 24159, "marble": 25503},  # level 28
            {"wood": 27816, "marble": 29639},  # level 29
            {"wood": 32021, "marble": 34437},  # level 30
            {"wood": 36857, "marble": 40002},  # level 31
            {"wood": 42419, "marble": 46457}  # level 32
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/img/city/vineyard_l.png'
    },
    'biuro architekta': {
        'description': 'Kąt, cyrkiel i linijka. Biuro Architekta dostarcza wszystko co jest potrzebne do'
                       ' projektowania mocniejszych murów i stabilnych dachów. Dobrze zaplanowany budynek'
                       ' potrzebuje mniej marmuru niż budynek z krzywymi ścianami . Każdy poziom budynku'
                       ' zmniejsza zapotrzebowanie na marmur w mieście o 1% wartości podstawowej.',
        'max_level': 32,
        'require': 'Architektura (Gospodarka)',
        'needed_materials': ['wood', 'marble'],
        'materials': [
            {"wood": 185, "marble": 106},  # level 1
            {"wood": 291, "marble": 160},  # level 2
            {"wood": 413, "marble": 222},  # level 3
            {"wood": 555, "marble": 295},  # level 4
            {"wood": 720, "marble": 379},  # level 5
            {"wood": 911, "marble": 475},  # level 6
            {"wood": 1133, "marble": 587},  # level 7
            {"wood": 1390, "marble": 716},  # level 8
            {"wood": 1689, "marble": 865},  # level 9
            {"wood": 2035, "marble": 1036},  # level 10
            {"wood": 2437, "marble": 1233},  # level 11
            {"wood": 2902, "marble": 1460},  # level 12
            {"wood": 3443, "marble": 1722},  # level 13
            {"wood": 4070, "marble": 2023},  # level 14
            {"wood": 4797, "marble": 2369},  # level 15
            {"wood": 5640, "marble": 2767},  # level 16
            {"wood": 6618, "marble": 3226},  # level 17
            {"wood": 7754, "marble": 3752},  # level 18
            {"wood": 9070, "marble": 4358},  # level 19
            {"wood": 10598, "marble": 5056},  # level 20
            {"wood": 12369, "marble": 5857},  # level 21
            {"wood": 14424, "marble": 6778},  # level 22
            {"wood": 16807, "marble": 7836},  # level 23
            {"wood": 19573, "marble": 9052},  # level 24
            {"wood": 22780, "marble": 10448},  # level 25
            {"wood": 26501, "marble": 12054},  # level 26
            {"wood": 30817, "marble": 13899},  # level 27
            {"wood": 35826, "marble": 16289},  # level 28
            {"wood": 41631, "marble": 18450},  # level 29
            {"wood": 48371, "marble": 21246},  # level 30
            {"wood": 56185, "marble": 24455},  # level 31
            {"wood": 65251, "marble": 28141}  # level 32
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/img/city/architect_l.png'
    },
    'świątynia': {
        'description': 'Świątynia jest miejscem wiary, przekonań i refleksji. Mieszkają tu kapłani, oddający cześć'
                       ' swojemu Bogu i głoszący jego słowo na całej wyspie. Możesz się tu modlić o cuda, dopóki,'
                       ' dopóty będziesz mu okazywał odpowiedni respekt.',
        'max_level': 38,
        'require': 'Politeizm (Nauka)',
        'needed_materials': ['wood', 'crystal'],
        'materials': [
            {"wood": 216, "crystal": 173},  # level 1
            {"wood": 228, "crystal": 190},  # level 2
            {"wood": 333, "crystal": 290},  # level 3
            {"wood": 465, "crystal": 423},  # level 4
            {"wood": 598, "crystal": 567},  # level 5
            {"wood": 760, "crystal": 752},  # level 6
            {"wood": 958, "crystal": 989},  # level 7
            {"wood": 1197, "crystal": 1290},  # level 8
            {"wood": 1432, "crystal": 1610},  # level 9
            {"wood": 1773, "crystal": 2080},  # level 10
            {"wood": 2112, "crystal": 2586},  # level 11
            {"wood": 2512, "crystal": 3210},  # level 12
            {"wood": 3082, "crystal": 4109},  # level 13
            {"wood": 3655, "crystal": 5084},  # level 14
            {"wood": 4458, "crystal": 6471},  # level 15
            {"wood": 5126, "crystal": 7765},  # level 16
            {"wood": 6232, "crystal": 9851},  # level 17
            {"wood": 7167, "crystal": 11821},  # level 18
            {"wood": 8688, "crystal": 14952},  # level 19
            {"wood": 10247, "crystal": 18402},  # level 20
            {"wood": 11784, "crystal": 22082},  # level 21
            {"wood": 14229, "crystal": 27824},  # level 22
            {"wood": 16753, "crystal": 34184},  # level 23
            {"wood": 19266, "crystal": 41020},  # level 24
            {"wood": 23156, "crystal": 51514},  # level 25
            {"wood": 26664, "crystal": 61817},  # level 26
            {"wood": 32027, "crystal": 77477},  # level 27
            {"wood": 36831, "crystal": 92972},  # level 28
            {"wood": 43257, "crystal": 113941},  # level 29
            {"wood": 50782, "crystal": 139577},  # level 30
            {"wood": 59591, "crystal": 170911},  # level 31
            {"wood": 68529, "crystal": 205093}  # level 32
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/img/city/temple_l.png'
    },
    'składowisko': {
        'description': 'Składowisko umożliwia ci przechowywanie dużych ilości towarów. Każdy poziom rozbudowy'
                       ' składowiska może pomieścić 32 000 jednostek każdego rodzaju towaru. Składowisko nie jest'
                       ' chronione przed plądrowaniem.',
        'max_level': 40,
        'require': 'Składowisko (Gospodarka)',
        'needed_materials': ['wood', 'marble', 'crystal', 'sulfur'],
        'materials': [
            {"wood": 640, "marble": 497, "crystal": 701, "sulfur": 384},  # level 1
            {"wood": 1152, "marble": 932, "crystal": 1146, "sulfur": 845},  # level 2
            {"wood": 1766, "marble": 1445, "crystal": 1668, "sulfur": 1398},  # level 3
            {"wood": 2504, "marble": 2050, "crystal": 2278, "sulfur": 2061},  # level 4
            {"wood": 3388, "marble": 2762, "crystal": 2991, "sulfur": 2857},  # level 5
            {"wood": 4450, "marble": 3609, "crystal": 3526, "sulfur": 3813},  # level 6
            {"wood": 5724, "marble": 4604, "crystal": 4803, "sulfur": 4960},  # level 7
            {"wood": 7253, "marble": 5778, "crystal": 5946, "sulfur": 6336},  # level 8
            {"wood": 9088, "marble": 7164, "crystal": 7283, "sulfur": 7987},  # level 9
            {"wood": 11289, "marble": 8799, "crystal": 8847, "sulfur": 9968},  # level 10
            {"wood": 13931, "marble": 10728, "crystal": 10678, "sulfur": 12346},  # level 11
            {"wood": 17101, "marble": 13005, "crystal": 12819, "sulfur": 15199},  # level 12
            {"wood": 20905, "marble": 15691, "crystal": 15325, "sulfur": 18623},  # level 13
            {"wood": 25470, "marble": 18862, "crystal": 18257, "sulfur": 22731},  # level 14
            {"wood": 30948, "marble": 22602, "crystal": 21687, "sulfur": 27661},  # level 15
            {"wood": 37522, "marble": 27016, "crystal": 25700, "sulfur": 33578},  # level 16
            {"wood": 45410, "marble": 32225, "crystal": 30395, "sulfur": 40677},  # level 17
            {"wood": 54876, "marble": 38371, "crystal": 35889, "sulfur": 49197},  # level 18
            {"wood": 66236, "marble": 45623, "crystal": 42316, "sulfur": 59420},  # level 19
            {"wood": 79867, "marble": 54181, "crystal": 49837, "sulfur": 71688},  # level 20
            {"wood": 96223, "marble": 64278, "crystal": 58635, "sulfur": 86409},  # level 21
            {"wood": 115852, "marble": 76194, "crystal": 68929, "sulfur": 104076},  # level 22
            {"wood": 139407, "marble": 90256, "crystal": 80973, "sulfur": 125274},  # level 23
            {"wood": 167672, "marble": 106847, "crystal": 95065, "sulfur": 150714},  # level 24
            {"wood": 201592, "marble": 126424, "crystal": 111553, "sulfur": 181241},  # level 25
            {"wood": 242293, "marble": 149528, "crystal": 130843, "sulfur": 217872},  # level 26
            {"wood": 291136, "marble": 176787, "crystal": 153414, "sulfur": 261830},  # level 27
            {"wood": 349749, "marble": 208956, "crystal": 179821, "sulfur": 314581},  # level 28
            {"wood": 420081, "marble": 246913, "crystal": 201716, "sulfur": 377881},  # level 29
            {"wood": 504483, "marble": 291702, "crystal": 246864, "sulfur": 453842},  # level 30
            {"wood": 605763, "marble": 344555, "crystal": 289157, "sulfur": 544994},  # level 31
            {"wood": 727300, "marble": 406921, "crystal": 338642, "sulfur": 654378},  # level 32
            {"wood": 873143, "marble": 480512, "crystal": 396536, "sulfur": 785637},  # level 33
            {"wood": 1048157, "marble": 567350, "crystal": 464274, "sulfur": 943149},  # level 34
            {"wood": 1258171, "marble": 669817, "crystal": 543528, "sulfur": 1132163},  # level 35
            {"wood": 1510191, "marble": 790730, "crystal": 636253, "sulfur": 1358979},  # level 36
            {"wood": 1812613, "marble": 933408, "crystal": 744742, "sulfur": 1631159},  # level 37
            {"wood": 2175519, "marble": 1101767, "crystal": 871676, "sulfur": 1957774},  # level 38
            {"wood": 2611007, "marble": 1300431, "crystal": 1020187, "sulfur": 2349714},  # level 39
            {"wood": 3133592, "marble": 1534855, "crystal": 1193945, "sulfur": 2820041}  # level 40
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/img/city/dump_l.png'
    },
    'twierdza piracka': {
        'description': 'Nad twoją twierdzą piracką powiewa złowieszczo flaga z trupią czaszką. Hojna nagroda czeka na'
                       ' pirata, który zdobędzie najwięcej łupu. Aby nie zrabowano twoich punktów abordażu do dnia'
                       ' ich podliczenia, wzmocnij swoją załogę',
        'max_level': 30,
        'require': 'Piractwo (Żegluga)',
        'needed_materials': ['wood', 'marble'],
        'materials': [
            {"wood": 450, "marble": 250},  # level 1
            {"wood": 906, "marble": 505},  # level 2
            {"wood": 1389, "marble": 783},  # level 3
            {"wood": 1935, "marble": 1112},  # level 4
            {"wood": 2593, "marble": 1534},  # level 5
            {"wood": 3427, "marble": 2103},  # level 6
            {"wood": 4516, "marble": 2883},  # level 7
            {"wood": 5950, "marble": 3949},  # level 8
            {"wood": 7834, "marble": 5388},  # level 9
            {"wood": 10284, "marble": 7296},  # level 10
            {"wood": 13430, "marble": 9782},  # level 11
            {"wood": 17415, "marble": 12964},  # level 12
            {"wood": 22394, "marble": 16970},  # level 13
            {"wood": 28534, "marble": 21938},  # level 14
            {"wood": 36015, "marble": 28019},  # level 15
            {"wood": 45029, "marble": 35370},  # level 16
            {"wood": 55779, "marble": 44162},  # level 17
            {"wood": 68482, "marble": 54573},  # level 18
            {"wood": 83366, "marble": 66793},  # level 19
            {"wood": 100671, "marble": 81020},  # level 20
            {"wood": 120648, "marble": 97463},  # level 21
            {"wood": 143562, "marble": 116341},  # level 22
            {"wood": 169686, "marble": 137883},  # level 23
            {"wood": 199309, "marble": 162325},  # level 24
            {"wood": 232729, "marble": 189915},  # level 25
            {"wood": 270255, "marble": 220912},  # level 26
            {"wood": 312210, "marble": 255580},  # level 27
            {"wood": 358926, "marble": 294197},  # level 28
            {"wood": 410748, "marble": 337048},  # level 29
            {"wood": 468032, "marble": 384429}  # level 30
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/buildings/y100/pirateFortress.png'
        # TODO - dostępne abordaże
        # TODO - nagroda za ranking
    },
    'czarny rynek': {
        'description': 'Czarny Rynek umożliwi ci sprzedaż jednostek wojskowych za złoto i inne surowce. Rozbuduj'
                       ' budynek, aby móc sprzedać inne typy jednostek i obniżyć opodatkowanie handlu. Twoja'
                       ' oferta wyświetli się w Bazarach innych władców.',
        'max_level': 25,
        'require': 'Handel żołnierzami (Gospodarka)',
        'needed_materials': ['wood', 'marble'],
        'materials': [
            {"wood": 440, "marble": 260},  # level 1
            {"wood": 887, "marble": 525},  # level 2
            {"wood": 1360, "marble": 807},  # level 3
            {"wood": 1890, "marble": 1126},  # level 4
            {"wood": 2516, "marble": 1509},  # level 5
            {"wood": 3288, "marble": 1988},  # level 6
            {"wood": 4263, "marble": 2601},  # level 7
            {"wood": 5505, "marble": 3390},  # level 8
            {"wood": 7086, "marble": 4403},  # level 9
            {"wood": 9086, "marble": 5693},  # level 10
            {"wood": 11590, "marble": 7315},  # level 11
            {"wood": 14691, "marble": 9331},  # level 12
            {"wood": 18489, "marble": 11807},  # level 13
            {"wood": 23088, "marble": 14812},  # level 14
            {"wood": 28600, "marble": 18420},  # level 15
            {"wood": 35143, "marble": 22708},  # level 16
            {"wood": 42839, "marble": 27757},  # level 17
            {"wood": 51820, "marble": 33654},  # level 18
            {"wood": 62218, "marble": 40486},  # level 19
            {"wood": 74175, "marble": 48348},  # level 20
            {"wood": 87838, "marble": 57334},  # level 21
            {"wood": 103356, "marble": 67546},  # level 22
            {"wood": 120888, "marble": 79087},  # level 23
            {"wood": 140596, "marble": 92064},  # level 24
            {"wood": 162647, "marble": 106587}  # level 25
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/img/city/blackmarket_l.png'
        # TODO - dostępne jednostki w sprzedaży oraz upust
    },
    'archiwum map': {
        'description': 'W archiwum map są przechowywane drogocenne mapy mórz. Dzięki nim mogą nasi żeglarze'
                       ' szybciej dotrzeć do celu. Im wyższy masz poziom budynku oraz dalszy cel podróży, tym'
                       ' więcej czasu możesz zaoszczędzić w obie strony.',
        'max_level': 40,
        'require': 'Archiwizacja (Nauka)',
        'needed_materials': ['wood', 'marble', 'crystal'],
        'materials': [
            {"wood": 578, "marble": 346, "crystal": 161},  # level 1
            {"wood": 1298, "marble": 1066, "crystal": 611},  # level 2
            {"wood": 2133, "marble": 1916, "crystal": 1142},  # level 3
            {"wood": 3102, "marble": 2918, "crystal": 1769},  # level 4
            {"wood": 4226, "marble": 4101, "crystal": 2508},  # level 5
            {"wood": 5530, "marble": 5497, "crystal": 3380},  # level 6
            {"wood": 7042, "marble": 7144, "crystal": 4410},  # level 7
            {"wood": 8796, "marble": 9088, "crystal": 5625},  # level 8
            {"wood": 10831, "marble": 11381, "crystal": 7058},  # level 9
            {"wood": 13191, "marble": 14088, "crystal": 8750},  # level 10
            {"wood": 15929, "marble": 17281, "crystal": 10746},  # level 11
            {"wood": 19106, "marble": 21050, "crystal": 13101},  # level 12
            {"wood": 22790, "marble": 25496, "crystal": 15880},  # level 13
            {"wood": 27064, "marble": 30743, "crystal": 19159},  # level 14
            {"wood": 32022, "marble": 36935, "crystal": 23029},  # level 15
            {"wood": 37773, "marble": 44241, "crystal": 27595},  # level 16
            {"wood": 44444, "marble": 52862, "crystal": 32984},  # level 17
            {"wood": 52183, "marble": 63035, "crystal": 39342},  # level 18
            {"wood": 61159, "marble": 75039, "crystal": 46844},  # level 19
            {"wood": 71572, "marble": 89204, "crystal": 55697},  # level 20
            {"wood": 83651, "marble": 105918, "crystal": 66144},  # level 21
            {"wood": 97663, "marble": 125641, "crystal": 78470},  # level 22
            {"wood": 113917, "marble": 148914, "crystal": 93016},  # level 23
            {"wood": 132771, "marble": 176377, "crystal": 110180},  # level 24
            {"wood": 154642, "marble": 208782, "crystal": 130434},  # level 25
            {"wood": 180012, "marble": 247021, "crystal": 154333},  # level 26
            {"wood": 209442, "marble": 292142, "crystal": 182533},  # level 27
            {"wood": 243580, "marble": 345385, "crystal": 215810},  # level 28
            {"wood": 283180, "marble": 408212, "crystal": 255077},  # level 29
            {"wood": 329116, "marble": 482348, "crystal": 301412},  # level 30
            {"wood": 382402, "marble": 569829, "crystal": 356088},  # level 31
            {"wood": 444214, "marble": 673055, "crystal": 420604},  # level 32
            {"wood": 515916, "marble": 794863, "crystal": 496734},  # level 33
            {"wood": 599090, "marble": 938596, "crystal": 586567},  # level 34
            {"wood": 695572, "marble": 1108201, "crystal": 692571},  # level 35
            {"wood": 807491, "marble": 1308335, "crystal": 817654},  # level 36
            {"wood": 937317, "marble": 1544493, "crystal": 965253},  # level 37
            {"wood": 1087916, "marble": 1823160, "crystal": 1139420},  # level 38
            {"wood": 1262610, "marble": 2151986, "crystal": 1344936},  # level 39
            {"wood": 1465255, "marble": 2540001, "crystal": 1587446}  # level 40
        ],
        'icon': 'https://s42-pl.ikariam.gameforge.com/skin/img/city/marinechartarchive_l.png'
        # TODO - bonus Archiwum Map
    }
}  # TODO - kategorie budynków


# Sprawdzanie aliasów nazwy budynku
def try_alias(name):
    if name in ('rezydencja', 'gubernator'):
        return 'rezydencja gubernatora'
    elif name in ('port', 'handlowy'):
        return 'port handlowy'
    elif name in ('mur', 'miejski'):
        return 'mur miejski'
    else:
        return name

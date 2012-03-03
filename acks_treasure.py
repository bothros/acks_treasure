import sys
import random

SPECIAL = True

tts = {
    'A': [
        {
            'chance': 30,
            'type': 'silver',
            'number': '1d4',
        },
        {
            'chance': 30,
            'number': '1d4',
            'type': 'ornamental',
        },
        {
            'chance': 30,
            'number': '1d4',
            'type': 'trinket',
        },
        [
            {
                'type': 'any',
                'number': 1,
                'chance': 1,
            },
        ],
    ],
    'B':[
        {
            'chance': 80,
            'number': '1d6',
            'type': 'silver',
        },
        {
            'chance': 70,
            'number': '1d4',
            'type': 'ornamental',
        },
        {
            'chance': 30,
            'number': '1d4',
            'type': 'trinket',
        },
        [
            {
                'type': 'any',
                'number': 2,
                'chance': 5,
            },
        ],
    ],
    'C':[
        {
            'chance': 15,
            'number': '1d4',
            'type': 'electrum',
        },
        {
            'chance': 40,
            'number': '1d6',
            'type': 'gem',
        },
        {
            'chance': 30,
            'number': '1d4',
            'type': 'trinket',
        },
        [
            {
                'chance': 5,
                'type': 'any',
                'number': '1',
            },
        ],
    ],
    'D':[
        {
            'chance': 80,
            'number': '1d6',
            'type': 'silver',
        },
        {
            'chance': 20,
            'number': '1d4',
            'type': 'electrum',
        },
        {
            'chance': 80,
            'number': '1d6',
            'type': 'ornamental',
        },
        {
            'chance': 70,
            'number': '1d4',
            'type': 'trinket',
        },
        [
            {
                'chance': 15,
                'type': 'any',
                'number': 2,
            },
        ],
    ],
    'E':[
    ],
    'F':[
    ],
    'G':[
    ],
    'H':[
    ],
    'I':[
    ],
    'J':[
    ],
    'K':[
    ],
    'L':[
    ],
    'M':[
    ],
    'N':[
    ],
    'O':[
    ],
    'P':[
    ],
    'Q':[
    ],
    'R':[
        {
            'chance': 50,
            'number': '1d6',
            'type': 'electrum',
        },
        {
            'chance': 60,
            'number': '1d6',
            'type': 'gold',
        },
        {
            'chance': 80,
            'number': '1d8',
            'type': 'platinum',
        },
        {
            'chance': 70,
            'number': '1d4',
            'type': 'brilliant',
        },
        {
            'chance': 60,
            'number': '1d4',
            'type': 'regalium',
        },
        [
            {
                'number': '2d4',
                'type': 'potion',
            },
            {
                'number': '2d4',
                'type': 'scroll',
            },
            {
                'chance': 75,
                'list': [
                    {
                        'number': '1d3',
                        'type': 'sword',
                    },
                    {
                        'number': '1d3',
                        'type': 'armor',
                    },
                    {
                        'number': '1d3',
                        'type': 'miscellaneous weapon',
                    },
                    {
                        'number': '1d3',
                        'type': 'wand/staff/rod',
                    },
                    {
                        'number': '1d3',
                        'type': 'miscellaneous item',
                    },
                    {
                        'number': '1d3',
                        'type': 'ring',
                    },
                ],
            },
        ],
    ],
}

grolls = {
    'ornamental piece': '2d20',
    'gem piece': '1d100',
    'brilliant piece': '1d100+80',
}

gtable = {
    'roll': '2d20',
    'ranges': {
        tuple(range(1, 11)): {
            'type': ['azurite', 'hematite', 'malachite', 'obsidian', 'quartz',],
            'value': '10gp',
        },
        tuple(range(11, 26)): {
            'type': ['agate', 'lapis lazuli', 'tiger eye', 'turquoise'],
            'value': '25gp',
        },
        tuple(range(26, 41)): {
            'type': ['bloodstone', 'crystal', 'tiger eye', 'turquoise'],
            'value': '50gp',
        },
        tuple(range(41, 56)): {
            'type': ['carnelian', 'chalcedony', 'sardonyx', 'zircon'],
            'value': '75gp',
        },
        tuple(range(56, 71)): {
            'type': ['amber', 'amethyst', 'coral', 'jade', 'jet', 'tourmaline'],
            'value': '100gp',
        },
        tuple(range(71, 81)): {
            'type': ['garnet', 'pearl', 'spinel'],
            'value': '250gp',
        },
        tuple(range(81, 91)): {
            'type': ['aquamarine', 'alexandrite', 'topaz'],
            'value': '500gp',
        },
        tuple(range(91, 96)): {
            'type': ['opal', 'star ruby', 'star sapphire', 'sunset', 'amethyst', 'imperial topaz'],
            'value': '750gp',
        },
        tuple(range(96, 101)): {
            'type': ['black sapphire', 'diamond', 'emerald', 'jacinth', 'ruby',],
            'value': '1000gp',
        },
        tuple(range(101, 111)): {
            'type': ['amber with preserved extinct creatures', 'whorled nephrite jade',],
            'value': '1500gp',
        },
        tuple(range(111, 126)): {
            'type': ['black pearl', 'baroque pearl', 'crystal geode'],
            'value': '2000gp',
        },
        tuple(range(126, 146)): {
            'type': ['facet cut imperial topaz', 'flawless diamond'],
            'value': '4000gp',
        },
        tuple(range(146, 166)): {
            'type': ['facet cut star sapphire', 'facet cut star ruby'],
            'value': '6000gp',
        },
        tuple(range(166, 176)): {
            'type': ['flawless facet cut diamond', 'flawless facet cut emerald', 'flawless facet cut jacinth', 'flawless facet cut ruby'],
            'value': '8000gp',
        },
        tuple(range(176, 180)): {
            'type': ['flawless facet cut black sapphire', 'flawless facet cut blue diamond'],
            'value': '10000gp',
        },
    },
}

jrolls = {
    'trinket piece': '2d20',
    'jewelry piece': '1d100',
    'regalia piece': '1d100+80',
}

stables = {
    'silver': {
        'roll': '1d20',
        1: {
            'number': '1d100',
            'type': 'animal horns',
            'value': '20gp',
            'weight': '1 stone per 5 horns',
        },
        2: {
            'number': '2d4',
            'type': 'jar of lamp oil',
            'value': '20gp',
            'weight': '6 stone',
        },
        3: {
            'number': '2d20',
            'type': 'bottle of fine wine',
            'value': '5gp',
            'weight': '1 stone per 5 bottles',
        },
        4: {
            'number': '3d6',
            'type': 'roll of garishly dyed cloth',
            'value': '10gp',
            'weight': '4 stone',
        },
        5: {
            'number': '1d3',
            'type': ['jar of dye', 'jar of pigment',],
            'value': '50gp',
            'weight': '5 stone',
        },
        6: {
            'number': '1d3',
            'type': 'crate of terra-cotta pottery',
            'value': '50gp',
            'weight': '5 stone',
        },
        7: {
            'number': '1d3',
            'type': 'bag of loose tea',
            'value': '75gp',
            'weight': '5 stone each',
        },
        8: {
            'number': '2d6',
            'type': 'bundle of fur pelts',
            'value': '1gp',
            'weight': '3 stone',
        },
        'ranges': {
             tuple(range(9, 21)): {
                 'number': 1000,
                 'type': 'silver piece',
             }
        },
    },
    'electrum': {
        'roll': '1d10',
        1: {
            'number': '1d4',
            'type': 'liquor barrel',
            'value': '200gp/each',
            'weight': '16 stone/each',
        },
        2: {
            'number': '1d3',
            'type': 'armor and weapon crate',
            'value': '225gp',
            'weight': '10 stone',
        },
        3: {
            'number': '1d4',
            'type': 'glassware crate',
            'value': '200gp',
            'weight': '5 stone',
        },
        4: {
            'number': '1d3',
            'type': 'monster part crate',
            'value': '300gp',
            'weight': '5 stone',
        },
        'ranges': {
            tuple(range(5, 11)): {
                'number': '1000',
                'type': 'electrum piece',
            }
        }
    },
    'gold': {
        'roll': '1d20',
        1: {
            'number': '1d3',
            'type': ['bundle of ermine pelts', 'bundle of mink pelts', 'bundle of sable pelts',],
            'value': '500gp',
            'weight': '5 stone',
        },
        2: {
            'number': '1d3',
            'type': 'jar of spices',
            'weight': '1 stone',
        },
        3: {
            'number': '1d10*50',
            'type': 'monster feather',
            'value': '1d6gp',
            'weight': '1 stone / 25 feathers',
        },
        4: {
            'number': '1d100',
            'type': 'monster horns',
            'value': '1d10HD x 1d4+1gp/HD',
            'weight': '1 stone / 20 HD',
        },
        5: {
            'number': '1d6',
            'type': 'monster carcasses',
            'value': '1d10HD x 1d10x10gp/HD',
            'weight': '1 stone / HD',
        },
        6: {
            'number': '1d4',
            'type': 'crate of fine porcelain',
            'value': '500gp',
            'weight': '2 stone',
        },
        7: {
            'number': '2d20',
            'type': 'piece of ivory',
            'value': '1d100gp',
            'weight': '1 stone per 100gp',
        },
        8: {
            'number': '1d3',
            'type': 'roll of silk',
            'value': '400gp',
            'weight': '4 stone',
        },
        'ranges': {
            tuple(range(9, 21)): {
                'number': 1000,
                'type': 'gold pieces',
            },
        },
    },
    'platinum': {
        'roll': '1d10',
        1: {
            'number': '5d10',
            'type': 'rare book',
            'value': '150gp',
            'weight': '1 stone per 2 books',
        },
        2: {
            'number': '1d3',
            'type': 'ornamental jar of rare spices',
            'value': '2500gp',
            'weight': '4 stone',
        },
        3: {
            'number': '5d20',
            'type': 'typical fur cape',
            'value': '100gp',
            'weight': '1 stone',
        },
        4: {
            'number': '4d8',
            'type': 'ingots of precious metals',
            'value': '300gp',
            'weight': '2 stone',
        },
        'ranges': {
            tuple(range(5, 11)): {
                'number': 1000,
                'type': 'platinum piece',
            },
        },
    },
    'ornamental': {
         'roll': '1d8',
         1: {
             'number': '1d12',
             'type': 'silver arrow',
             'value': '5gp',
         },
         2: {
             'number': '1d6',
             'type': ['pouch of belladonna', 'pouch of wolfsbane'],
             'value': '10gp',
         },
         3: {
             'number': '1d4',
             'type': 'pouch of saffron',
             'value': '15gp',
         },
         'ranges': {
             tuple(range(4, 9)): {
                'number': 1,
                'type': 'ornamental piece',
             }
         }
    },
    'gem': {
        'roll': '1d8',
        1: {
            'number': '1d3',
            'type': 'set of engraved teeth',
            'value': '2d6x10gp',
            'weight': '1 stone per 100 sets',
        },
        2: {
            'number': '1d10',
            'type': 'stick of rare incense',
            'value': '5d6gp',
            'weight': '1 stone per 100 sticks',
        },
        3: {
            'number': '1d3',
            'type': 'vial of rare perfume',
            'value': '1d6x25gp',
            'weight': '1 stone per 100 vials',
        },
        'ranges': {
            tuple(range(4, 9)): {
                'number': 1,
                'type': 'gem piece',
            },
        },
    },
    'brilliant': {
        'roll': '1d8',
        1: {
            'number': '2d20',
            'type': 'jade carving of heroes, monsters, and gods',
            'value': '200gp',
        },
        2: {
            'number': '1d8',
            'type': ['opal cameo portrait', 'intaglio erotic tableau'],
            'value': '800gp',
        },
        3: {
            'number': '1d6',
            'type': 'amethyst cylinder seal depicting religious scene',
            'value': '1200gp',
        },
        'ranges': {
            tuple(range(4, 9)): {
                'number': 1,
                'type': 'brilliant piece',
            },
        }
    }
}

def roll_table(table, rollstring=None):
    if isinstance(table, list):
        return random.choice(table)
    else:
        if rollstring is None:
            rollstring = table.get('roll', '1d20')
        print ' rt -- rollstring ' + str(rollstring)
        roll = roll_number(rollstring)
        print ' rt -- roll - ' + str(roll)
        if roll in table:
            return table[roll]
        elif 'ranges' in table:
            for r in table['ranges']:
                if roll in r:
                    return table['ranges'][r]
            return None
        else:
            return None

def flatten(l):
    i = 0
    while i < len(l):
        if isinstance(l[i], list):
            l[i:i+1] = l[i]
        i+= 1
    return l

def item_list(lst):
    out = []
    for item in lst:
        result = roll_item(item)
        if result == None:
            pass
        elif isinstance(result, list):
            out.extend(result)
        else:
            out.append(result)
    return out

def roll_item(item):
    # items have a chance to occur, a number that do occur, a type, or a list of further
    # items. if there is a list, there can be nothing else.
    if item is None:
        return None
    elif isinstance(item, list):
        return item_list(item)
    elif roll_percent(item.get('chance', 100)):
        if 'list' in item:
            return item_list(item['list'])
        elif 'type' in item and isinstance(item['type'], list):
            spec_item = item.copy()
            spec_item['type'] = random.choice(item['type'])
            return roll_item(spec_item)
        elif SPECIAL and 'type' in item and item['type'] in stables:
            return [
                roll_item(roll_table(stables[item['type']]))
            for i in range(roll_number(item.get('number', 1)))]
        elif 'type' in item and item['type'] in jrolls:
            return [
                roll_item(roll_table(jtable, rollstring=jrolls[item['type']]))
            for i in range(roll_number(item.get('number', 1)))]
        elif 'type' in item and item['type'] in grolls:
            return [
                roll_item(roll_table(gtable, rollstring=grolls[item['type']]))
            for i in range(roll_number(item.get('number', 1)))]
        else:
            return {
                'number': roll_number(item.get('number', 1)),
                'type': item.get('type', 'UNKNOWN'),
            }
    else:
        return None

def roll_number(numstring):
    # way overkill. d has highest precedence, then regular order of operations.
    # No parens allowed, for now.
    ns = str(numstring)
    #print ns
    if '+' in ns:
        lside, rside = ns.split('+', 1)
        return roll_number(lside) + roll_number(rside)
    elif '-' in ns:
        lside, rside = ns.split('-', 1)
        return roll_number(lside) - roll_number(rside)
    elif '*' in ns:
        lside, rside = ns.split('*', 1)
        return roll_number(lside) * roll_number(rside)
    elif 'x' in ns:
        lside, rside = ns.split('x', 1)
        return roll_number(lside) * roll_number(rside)
    elif '/' in ns:
        lside, rside = ns.split('/', 1)
        return roll_number(lside) / roll_number(rside)
    elif 'd' in ns:
        dice, size = ns.split('d', 1)
        total = 0
        for die in range(int(dice)):
            total += random.randint(1, int(size))
        #print '(' + str(total) + ')'
        return total
    else:
        return int(ns)

def roll_percent(chance):
    roll = random.randint(1, 100)
    if roll <= chance:
        return True
    else:
        return False

def roll_treasure(tt):
    return consolidate(flatten(roll_item(tts[tt])))

def consolidate(treasure):
    type_to_number = {}
    print treasure
    for item in treasure:
        if item.get('type', 'UNKNOWN') in type_to_number:
            type_to_number[item.get('type', 'UNKNOWN')] += item.get('number', 1)
        else:
            type_to_number[item.get('type', 'UNKNOWN')] = item.get('number', 1)
    done = set()
    out = []
    for item in treasure:
        if item.get('type', 'UNKNOWN') not in done:
            done.add(item.get('type', 'UNKNOWN'))
            sumitem = item.copy()
            sumitem['number'] = type_to_number[item.get('type', 'UNKNOWN')]
            out.append(sumitem)
    return out


def pretty_treasure(treasure, middle=False):
    if treasure is None:
        return 'nothing'
    elif isinstance(treasure, list):
        outstring = ''
        for item in treasure:
            outstring += pretty_treasure(item, True)
            outstring += ', '
        outstring = outstring [:-2] 
    else:
        n = treasure.get('number', 1)
        outstring = str(n) + ' ' + pluralize(n, treasure.get('type', 'UNKNOWN'))
    if not middle:
        outstring += '.'
    return outstring

def pluralize(number, word):
    if number != 1:
        if word == 'regalium':
            return 'regalia'
        else:
            return word + 's'
    else:
        return word

if __name__ == "__main__":
    if len(sys.argv) > 1:
        tt = sys.argv[1]
    else:
        tt = raw_input("Enter a treasure type: ")
    tt = tt.upper()
    print pretty_treasure(roll_treasure(tt))

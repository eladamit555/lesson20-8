import random
items_options = {'sword', 'shield', 'staff', 'mace', 'ring', 'boots'}
item_icons_set = {'⚔️', '🛡️', '🪄', '🔨', '💍', '🥾'}
attributes = {
    'name': None,
    'strength': 15, 'dexterity': 12, 'constitution': 14, 'intelligence': 10, 'wisdom': 13, 'charisma': 8,
    'inventory': []
}
while True:
    name = input('Enter your name: ')
    attributes.update({'name': name})
    attributes['strength'] = random.randint(3, 18)
    attributes['dexterity'] = random.randint(3, 18)
    attributes['constitution'] = random.randint(3, 18)
    attributes['intelligence'] = random.randint(3, 18)
    attributes['wisdom'] = random.randint(3, 18)
    attributes['charisma'] = random.randint(3, 18)
    attributes['inventory'] = random.sample(list(item_icons_set), 2)
    print(attributes)
    answer = input('want to change? (yes/no)')
    if answer != 'yes':
        break


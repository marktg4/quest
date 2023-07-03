# Will contain all quest cards, including crafting, thieving, bounties, and this and that quest cards

import random

# Build the bounty quest cards
# Initially just going to have 2 for each enemy, one easier and the other with extra quantity but extra renown
bounty_cards = [
    {
        'name': 'Kill Goblins',
        'description': 'Bring 3 goblin trophies',
        'enemy': 'goblin',
        'quantity': 3,
        'renown': 2,
    },
    {
        'name': 'Slay Goblins',
        'description': 'Bring 6 goblin trophies',
        'enemy': 'goblin',
        'quantity': 6,
        'renown': 4,
    },
    {
        'name': 'Kill Bandits',
        'description': 'Bring 2 bandit trophies',
        'enemy': 'bandit',
        'quantity': 2,
        'renown': 3,
    },
    {
        'name': 'Slay Bandits',
        'description': 'Bring 4 bandit trophies',
        'enemy': 'bandit',
        'quantity': 4,
        'renown': 6,
    },
    {
        'name': 'Kill Werewolves',
        'description': 'Bring 2 werewolf trophies',
        'enemy': 'werewolf',
        'quantity': 2,
        'renown': 6,
    },
    {
        'name': 'Slay Werewolves',
        'description': 'Bring 4 werewolf trophies',
        'enemy': 'werewolf',
        'quantity': 4,
        'renown': 12,
    },
    {
        'name': 'Kill Trolls',
        'description': 'Bring 1 troll trophy',
        'enemy': 'troll',
        'quantity': 1,
        'renown': 5,
    },
    {
        'name': 'Slay Trolls',
        'description': 'Bring 3 troll trophies',
        'enemy': 'troll',
        'quantity': 3,
        'renown': 15,
    },
    {
        'name': 'Kill Vampires',
        'description': 'Bring 1 vampire trophy',
        'enemy': 'vampire',
        'quantity': 1,
        'renown': 8,
    },
    {
        'name': 'Slay Vampires',
        'description': 'Bring 2 vampire trophies',
        'enemy': 'vampire',
        'quantity': 2,
        'renown': 16,
    },
    {
        'name': 'Kill Dragons',
        'description': 'Bring 1 dragon trophy',
        'enemy': 'dragon',
        'quantity': 1,
        'renown': 12,
    },
    {
        'name': 'Slay Dragons',
        'description': 'Bring 2 dragon trophies',
        'enemy': 'dragon',
        'quantity': 2,
        'renown': 24,
    },
]

# Build the crafting quest cards
# Want roughly the same as bounties, so shooting for 12. And want a good combination of resources and difficulty levels
crafting_cards = [
    {
        'name': 'Bread Baking',
        'description': 'Craft bread',
        'difficulty_class': 1,
        'required_items': ['crop', 'crop'],
        'renown': 2,
    },
    {
        'name': 'Fence Building',
        'description': 'Craft fences',
        'difficulty_class': 1,
        'required_items': ['lumber', 'lumber', 'lumber'],
        'renown': 3,
    },
    {
        'name': 'Sword Making',
        'description': 'Craft swords',
        'difficulty_class': 2,
        'required_items': ['ore', 'ingot'],
        'renown': 4,
    },
    {
        'name': 'Enchanting',
        'description': 'Craft enchantments',
        'difficulty_class': 2,
        'required_items': ['essence', 'essence', 'rune'],
        'renown': 5,
    },
    {
        'name': 'Provisions',
        'description': 'Craft food provisions',
        'difficulty_class': 3,
        'required_items': ['lumber', 'lumber', 'food'],
        'renown': 6,
    },
    {
        'name': 'Imbued Armaments',
        'description': 'Craft magically imbued weapons',
        'difficulty_class': 3,
        'required_items': ['ore', 'ingot', 'essence'],
        'renown': 7,
    },
    {
        'name': 'Potion Brewing',
        'description': 'Craft magic potions',
        'difficulty_class': 4,
        'required_items': ['food', 'crop', 'rune'],
        'renown': 8,
    },
    {
        'name': 'Feast Making',
        'description': 'Craft a feast of food',
        'difficulty_class': 5,
        'required_items': ['food', 'food', 'crop'],
        'renown': 8,
    },
    {
        'name': 'Spellweaving',
        'description': 'Craft magic spells',
        'difficulty_class': 5,
        'required_items': ['rune', 'rune', 'essence'],
        'renown': 8,
    },
    {
        'name': 'Ship Making',
        'description': 'Craft ships',
        'difficulty_class': 6,
        'required_items': ['plank', 'plank', 'ingot'],
        'renown': 9,
    },
    {
        'name': 'Master Woodsmith',
        'description': 'Craft a masterpiece of wood',
        'difficulty_class': 10,
        'required_items': ['plank', 'plank', 'plank'],
        'renown': 15,
    },
    {
        'name': 'Master Smith',
        'description': 'Craft a masterpiece of metal',
        'difficulty_class': 10,
        'required_items': ['ingot', 'ingot', 'ingot'],
        'renown': 15,
    },
    {
        'name': 'Master Chef',
        'description': 'Craft a masterpiece of food',
        'difficulty_class': 10,
        'required_items': ['food', 'food', 'food'],
        'renown': 15,
    },
    {
        'name': 'Master Arcanist',
        'description': 'Craft a masterpiece of magic',
        'difficulty_class': 10,
        'required_items': ['rune', 'rune', 'rune'],
        'renown': 15,
    },
]

# Build the thieving quest cards
# Thinking of 14, 2 for each of the 4 special sales, 2 for the general sales, and 4 for any sale. Maybe too much?
thieving_cards = [
    {
        'name': 'Ore Lifter',
        'description': 'Steal ore from the ore sale',
        'difficulty_class': 2,
        'required_sale': 'ore',
        'renown': 5,
    },
    {
        'name': 'Lumber Lifter',
        'description': 'Steal lumber from the lumber sale',
        'difficulty_class': 2,
        'required_sale': 'lumber',
        'renown': 5,
    },
    {
        'name': 'Crop Lifter',
        'description': 'Steal crops from the crop sale',
        'difficulty_class': 2,
        'required_sale': 'crop',
        'renown': 5,
    },
    {
        'name': 'Essence Lifter',
        'description': 'Steal essence from the essence sale',
        'difficulty_class': 2,
        'required_sale': 'essence',
        'renown': 5,
    },
    {
        'name': 'Ingot Smuggler',
        'description': 'Steal ingots from the ingot sale',
        'difficulty_class': 4,
        'required_sale': 'ingot',
        'renown': 10,
    },
    {
        'name': 'Plank Smuggler',
        'description': 'Steal planks from the plank sale',
        'difficulty_class': 4,
        'required_sale': 'plank',
        'renown': 10,
    },
    {
        'name': 'Food Smuggler',
        'description': 'Steal food from the food sale',
        'difficulty_class': 4,
        'required_sale': 'food',
        'renown': 10,
    },
    {
        'name': 'Rune Smuggler',
        'description': 'Steal runes from the rune sale',
        'difficulty_class': 4,
        'required_sale': 'rune',
        'renown': 10,
    },
    {
        'name': 'Numbers Job',
        'description': 'Change numbers from some ledgers',
        'difficulty_class': 3,
        'required_sale': 'general',
        'renown': 7,
    },
    {
        'name': 'Heist',
        'description': 'Steal money from a VIP',
        'difficulty_class': 6,
        'required_sale': 'general',
        'renown': 14,
    },
    {
        'name': 'False Advertising',
        'description': 'Help a merchant upsell his product',
        'difficulty_class': 1,
        'renown': 3,
    },
    {
        'name': 'Snake Oil',
        'description': 'Sell a "wonder" product',
        'difficulty_class': 2,
        'renown': 4,
    },
    {
        'name': 'Pyramid Scheme',
        'description': 'Start a "promising" franchise',
        'difficulty_class': 3,
        'renown': 6,
    },
    {
        'name': 'Master Pickpocket',
        'description': 'Pull in a great haul',
        'difficulty_class': 5,
        'renown': 12,
    },
]

# Build the this and that quest cards
# Not sure how many of these I want, probly not 10+
tat_cards = [
    {
        'name': 'Save My Cat!',
        'description': "Rescue an old woman's cat from a tree",
        'difficulty_class': 1,
        'location': 'lumber',
        # 'skill_check_type': '',
        'item_bonus': [],
        'skill_bonus':[],
        'renown': 1,
    },
    {
        'name': 'Guard Duty',
        'description': "Stand guard",
        'difficulty_class': 3,
        'location': 'crafting',
        'skill_check_type': 'combat',
        'item_bonus': [],
        'skill_bonus':[{'thieving':2}],
        'renown': 4,
    },
    {
        'name': 'Fertilization',
        'description': "Get the crops ready for next season",
        'difficulty_class': 2,
        'location': 'crops',
        'skill_check_type': 'gathering',
        'item_bonus': [{'crops':1}],
        'skill_bonus':[{'magic':2}],
        'renown': 3,
    },
    {
        'name': 'Prospecting',
        'description': "Find where the rich ore veins are",
        'difficulty_class': 2,
        'location': 'ore',
        'skill_check_type': 'thieving',
        'item_bonus': [{'essence':1}],
        'skill_bonus':[{'gathering':2}],
        'renown': 3,
    },
    {
        'name': 'Fairy Collecting',
        'description': "Find some fairies",
        'difficulty_class': 4,
        'location': 'essence',
        'skill_check_type': 'gathering',
        'item_bonus': [{'food':1}],
        'skill_bonus':[{'magic':3}],
        'renown': 5,
    },
    {
        'name': 'Fixing The Tavern',
        'description': "Patch up the tavern",
        'difficulty_class': 4,
        'location': 'tavern',
        'skill_check_type': 'crafting',
        'item_bonus': [{'lumber':1}, {'ingot':1}],
        'skill_bonus':[],
        'renown': 5,
    },
    {
        'name': 'Auction Winner',
        'description': "Buy the item everyone wants at the auction",
        'difficulty_class': 10,
        'location': 'market_buy',
        # 'skill_check_type': '',
        'item_bonus': [{'food':1},{'ingot':1},{'rune':1},{'plank':1},],
        'skill_bonus':[{'thieving':3}],
        'renown': 15,
    },
]


quest_deck = []
# Add all cards into one deck
for a in range(len(bounty_cards)):
    quest_deck.append(bounty_cards[a])
for a in range(len(crafting_cards)):
    quest_deck.append(crafting_cards[a])
for a in range(len(thieving_cards)):
    quest_deck.append(thieving_cards[a])
for a in range(len(tat_cards)):
    quest_deck.append(tat_cards[a])
# Imports
from Quest_Cards import quest_deck, bounty_cards, crafting_cards, thieving_cards, tat_cards
from Dice import skill_dice, magic_dice
import PySimpleGUI as sg
import random


# Build some card functions

# Shuffle given deck
def shuffle_deck(deck):
    if len(deck) > 1:
        random.shuffle(deck)
        print(F"Deck shuffled!")
        # update_log(F"\nDeck shuffled!")
        return deck
    else:
        print('Deck contains only one item or is empty')
        # update_log('\nDeck contains only one item or is empty')
        return deck

# Draw a card from the quest deck
def draw_card (deck):
    #Verify explore deck has content
    if len(deck) > 0:
        current = deck.pop()
        print(F"Drew card {current.get('name', 'No card name provided')}")
        # update_log(F"\nDrew card {current.get('name', 'No card name provided')}")
        return deck, current
    else:
        print('Deck is empty')
        # update_log('\nDeck is empty')
        return deck, current

# Add discard pile back to the deck (and most likely prepare to shuffle)
def return_discarded_cards (deck, discards):
    for a in range(len(discards)):
        print(F"Returning {discards[a].get('name', 'No card name provided')} to deck..")
        deck.append(discards[a])
    discards = []
    print('Discard pile is now empty, all cards returned to deck')
    return deck, discards

# Add a set of cards to the discard pile
def discard_cards(cards, discards):
    for a in range(len(cards)):
        print(F"Adding {cards[a].get('name', 'No card name provided')} to discard pile..")
        discards.append(cards[a])
    cards = []
    print('All given cards discarded')
    return cards, discards

# Draw quest cards that will be available
def draw_quests(deck):
    available = []
    for a in range(5):
        current_card = draw_card(deck)[1]
        print(F"Adding {current_card.get('name', 'No card name provided')} to available quests..")
        available.append(current_card)
    print(F"Available quests are:")
    for b in range(len(available)):
        print(F"\t{available[b].get('name', 'No card name provided')}")
    return deck, available

# Move selected quest from available quests into the player's quests
def acquire_quest(player_quest_list, index):
    a = available_quests.pop(index)
    print(F"Adding selected quest: {a.get('name', 'No card name provided')} to player hand..")
    player_quest_list.append(a)
    print(F"Player hand is now: ")
    for b in range(len(player_quest_list)):
        print(F"\t{player_quest_list[b].get('name', 'No card name provided')}")
    print(F"Available quests are now: ")
    for c in range(len(available_quests)):
        print(F"\t{available_quests[c].get('name', 'No card name provided')}")
    return player_quest_list, available_quests


# Build some dice functions

# Roll a die
def roll_die(die):
    roll = random.randint(0, len(die)-1)
    # print(F"Die index value: {roll}")
    return roll

# Roll skill dice
def roll_skill_dice(quantity):
    result = []
    roll = 0
    print('Roll results: ')
    for a in range(quantity):
        roll = roll_die(skill_dice)
        result.append(skill_dice[roll])
        print(F"\tRolled a {result[a]}")
    return result

# Roll magic dice
def roll_magic_dice(quantity):
    result = []
    roll = 0
    print('Roll results: ')
    for a in range(quantity):
        roll = roll_die(magic_dice)
        result.append(magic_dice[roll])
        print(F"\tRolled a {result[a]}")
    return result


# Initiate decks
discard_pile = []
available_quests = []

# Initiate player quests
player1_quests = []
player2_quests = []
player3_quests = []
player4_quests = []
selected_quest = 0



# Print the size of each of the decks
print(F"Size of the bounty deck: {len(bounty_cards)}")
print(F"Size of the crafting deck: {len(crafting_cards)}")
print(F"Size of the thieving deck: {len(thieving_cards)}")
print(F"Size of the t&t deck: {len(tat_cards)}")
print(F"Size of the full deck: {len(quest_deck)}")


# Sort of an ideal flow here

# draw_card(quest_deck)
shuffle_deck(quest_deck)
available_quests = draw_quests(quest_deck)[1]
# print(F"Size of the available cards: {len(available_quests)}")
# print(F"Size of the full deck: {len(quest_deck)}")
# print(F"Size of the discard pile: {len(discard_pile)}")
##### Still need a function to select a quest, possibly handled in the main loop logic?#####
# print(F"Selected quest is: {available_quests[selected_quest]}")
player1_quests = acquire_quest(player1_quests, selected_quest)[0]
# print(F"Player 1 hand is now: {player1_quests}")
# print(F"Size of the available cards: {len(available_quests)}")
player1_quests = discard_cards(player1_quests, discard_pile)[0]
# print(F"Player 1 hand is now: {player1_quests}")
# print(F"Size of the available cards: {len(available_quests)}")
available_quests = discard_cards(available_quests, discard_pile)[0]
# print(F"Size of the available cards: {len(available_quests)}")
# print(F"Size of the full deck: {len(quest_deck)}")
# print(F"Size of the discard pile: {len(discard_pile)}")
discard_pile = return_discarded_cards(quest_deck,discard_pile)[1]
# print(F"Size of the available cards: {len(available_quests)}")
# print(F"Size of the full deck: {len(quest_deck)}")
# print(F"Size of the discard pile: {len(discard_pile)}")


# print(quest_deck)

roll_skill_dice(5)
roll_magic_dice(2)
import math
import sys
import os
import re
from collections import namedtuple
from functools import cmp_to_key
Hand = namedtuple('Hand',['cards', 'bid']) #, strength, rank

card_strength = {
    'J': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'Q': 11,
    'K': 12,
    'A': 13
}

def get_strength(x: Hand):
    # Compare type
    count = {}
    strength = 0
    for card in set(x.cards):
        count[card] = x.cards.count(card)

    # See if J is present
    if 'J' in count.keys() and len(count) != 1:
        jokers = count.pop('J')
        max_key = max(count, key=count.get)
        count[max_key] += jokers

    if len(count) == 1:
        strength = 6
    elif len(count) == 2:
        if list(count.values())[0] in [1,4]:
            # Four of a kind
            strength = 5
        else:
            # Full house
            strength = 4
    elif len(count) == 3:
        for value in count.values():
            if value == 3:
                # Three of a kind
                strength = 3
                break
            elif value == 2:
                # Two pair
                strength = 2
                break
    elif len(count) == 4:
        # one pair
        strength = 1
    else:
        # High card
        strength = 0
    return strength


def card_comparison(x :Hand, y:Hand):
    # compare type
    sx = get_strength(x)
    sy = get_strength(y)
    # if equal - compare first card in each hand, and continue until one wins
    if (sx == sy):
        for p in zip(x.cards, y.cards):
            if p[0] != p[1]:
                return 1 if card_strength[p[0]] > card_strength[p[1]] else -1
        return 0
    else:
        return 1 if sx > sy else -1
        
    return 0
def main():
    fname = sys.argv[1]
    with open(fname,'r') as f:
        lines = f.read().splitlines()
        hands = []
        for line in lines:
            cards, bid = line.split(' ')
            hands.append(Hand(cards=cards, bid=int(bid)))
        cmp_items = cmp_to_key(card_comparison)
        hands = sorted(hands, key=cmp_items)
        # print(hands)
        winnings = 0
        # bid is first, rank is in terms of overall hands
        for rank, hand in enumerate(hands):
            winnings+= hand.bid * (rank + 1)
        print(winnings)
        # not correct: 250377063

        
if __name__ == "__main__":
    main()
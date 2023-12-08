from enum import Enum
from functools import reduce # python3 compatibility
from operator import *

class HandType(Enum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1
    UNDEFINED = 0

class Hand():
    def __init__(self):
        self.cards = ""
        self.handtype = HandType.UNDEFINED
        self.bid = -1
        self.rank = 0

    def __str__(self):
        return f'Cards: {self.cards} - Rank: {self.rank} - HandType: {self.handtype}:{self.handtype.value} - bid: {self.bid}'

def has_x_different_amount_cards(hand, amount_diverse_cards):
    # "23333" geeft 2 terug, "43257" geeft 5 terug (5 distinct waarden in de set)
    return len(set(hand.cards)) == amount_diverse_cards

def is_five_of_a_kind(hand):
    return has_x_different_amount_cards(hand, 1)
        
def is_high_card(hand):
    return has_x_different_amount_cards(hand, 5)

def is_one_pair(hand):
    return has_x_different_amount_cards(hand, 4)

def is_four_of_a_kind(hand):
    if not has_x_different_amount_cards(hand, 2):
        return False

    for c in set(hand.cards): # 1x4 en 1x1
        if hand.cards.count(c) == 4:
            return True

    return False

def is_full_house(hand):
    if not has_x_different_amount_cards(hand, 2): # moet 2 distinct bevatten
        return False

    has_three_same, has_other_two_same = False, False

    for c in set(hand.cards): # 1x3 en 1x2
        if hand.cards.count(c) == 3:
            has_three_same = True
        elif hand.cards.count(c) == 2:
            has_other_two_same = True

    return (has_three_same and has_other_two_same)

def is_three_of_a_kind(hand):
    if not has_x_different_amount_cards(hand, 3): # moet 3 distinct bevatten
        return False

    has_three_same = False

    for c in set(hand.cards):
        if hand.cards.count(c) == 3: # bij 3 distinct EN 3 dezelfde
            has_three_same = True
            
    return has_three_same

def is_two_pair(hand):
    if not has_x_different_amount_cards(hand, 3): # moet 3 distinct bevatten
        return False

    has_one_pair, has_second_pair = False, False

    for c in set(hand.cards):
        if hand.cards.count(c) == 2: # bij 3 distinct EN 2x2 dezelfde
            if not has_one_pair:
                has_one_pair = True
            else:
                has_second_pair = True
            
    return (has_one_pair and has_second_pair)

def get_hand_type(hand):
    if is_five_of_a_kind(hand):
        return HandType.FIVE_OF_A_KIND
    elif is_four_of_a_kind(hand):
        return HandType.FOUR_OF_A_KIND
    elif is_full_house(hand):
        return HandType.FULL_HOUSE
    elif is_three_of_a_kind(hand):
        return HandType.THREE_OF_A_KIND
    elif is_two_pair(hand):
        return HandType.TWO_PAIR
    elif is_one_pair(hand):
        return HandType.ONE_PAIR
    elif is_high_card(hand):
        return HandType.HIGH_CARD
    else:
        return HandType.UNDEFINED

def special_card_to_value(special_card):
    special_cards = ['T', 'J', 'Q', 'K', 'A'] # 10, 11, 12 ...
    return special_cards.index(special_card) + 10 if special_card in special_cards else -1

def get_card_val(card):
    # card is a char
    if not card.isdigit():
        return special_card_to_value(card)
    else:
        return int(card)

def is_a_higher_than_b(a, b):
    for idx, c in enumerate(a.cards): # loop chars (cards)
        card_to_determine_rank = "0"
        card_to_cmp_with = b.cards[idx]

        #print(f"c1 {type(card_to_determine_rank)} c2 {type(card_to_cmp_with)}")
        #print(f"c1 {card_to_determine_rank} c2 {card_to_cmp_with}")

        card_to_determine_rank = get_card_val(c)
        card_to_cmp_with = get_card_val(card_to_cmp_with)

        if card_to_determine_rank > card_to_cmp_with:
            return '>'
        elif card_to_determine_rank < card_to_cmp_with:
            return '<'
        else:
            continue

def get_rank(hand_to_check, hands):
    rank = 1 # lowest rank
    for hand in hands:
        #print(f"Checking against ... {hand}")
        if hand_to_check.handtype.value > hand.handtype.value:
            #print(f"{hand_to_check} \nHAS HIGHER RANK THAN \n{hand}\n")
            rank += 1
        elif hand_to_check.handtype.value < hand.handtype.value:
            continue
            #print(f"{hand_to_check} \nHAS LOWER RANK THAN \n{hand}\n")
        else: # als handtype gelijk is (2x full house bijv)
            if is_a_higher_than_b(hand_to_check, hand) == '>':
                #print(f"{hand_to_check} \nFIRST CARD MORE POWERFUL \n{hand}\n")
                rank += 1

    #print(f"Calculated rank {rank}\n")
    hand_to_check.rank = rank

def day_seven_part_one(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

        hands = []
        for line in lines:
            hand, bid = [str(value) for value in line.split()]
            current_hand = Hand()
            current_hand.cards = hand
            current_hand.handtype = get_hand_type(current_hand)
            current_hand.bid = int(bid)

            print(f"{current_hand}")

            hands.append(current_hand)

        print("")

        for hand in hands:
            get_rank(hand, hands)
        
        print("")

        rank_times_bids = []
        for hand in hands:
            print(f"{hand}")
            rank_times_bids.append(hand.rank * hand.bid)

        print("")

        print(rank_times_bids)
        return sum(rank_times_bids)


filename = "D:/git/magic/aoc2023/aoc2023/src/seven/input.txt"

ans1 = day_seven_part_one(filename)

print(f"Part one {ans1}")

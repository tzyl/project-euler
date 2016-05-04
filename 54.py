class Hand(object):
    STRAIGHT = [set(['A', '2', '3', '4', '5']),
                set(['2', '3', '4', '5', '6']),
                set(['3', '4', '5', '6', '7']),
                set(['4', '5', '6', '7', '8']),
                set(['5', '6', '7', '8', '9']),
                set(['6', '7', '8', '9', 'T']),
                set(['7', '8', '9', 'T', 'J']),
                set(['8', '9', 'T', 'J', 'Q']),
                set(['9', 'T', 'J', 'Q', 'K']),
                set(['T', 'J', 'Q', 'K', 'A'])]

    CARD_SCORES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    def __init__(self, card_list):
        self.card_tuples = [(card[0], card[1]) for card in card_list]
        self.card_tuples.sort(key=lambda card_tuple: self.CARD_SCORES[card_tuple[0]])

        self.card_values = [card_tuple[0] for card_tuple in self.card_tuples]
        self.card_values_set = set(self.card_values)
        self.card_suits = [card_tuple[1] for card_tuple in self.card_tuples]
        self.card_suits_set = set(self.card_suits)
        self.multiple_cards = self.count_multiple_cards()

        self.rank = self.rank_hand()

    # Compares to another Hand object. Returns True if this hand wins or ties
    # and false if it loses.
    def beats_other_hand(self, other_hand):
        if self.rank != other_hand.rank:
            return self.rank > other_hand.rank
        else:
            if self.rank == 10:
                # Royal flush equal.
                return True

            elif self.rank == 9 or self.rank == 5:
                # Straight flush determined by highest card.
                return self.CARD_SCORES[self.card_values[-1]] >= self.CARD_SCORES[other_hand.card_values[-1]]

            elif self.rank == 8:
                # Four of a kind determined by quad or kicker if same quad.
                this_quad = [value for value in self.card_values if self.multiple_cards[value] == 4][-1]
                other_quad = [value for value in other_hand.card_values if other_hand.multiple_cards[value] == 4][-1]
                if this_quad != other_quad:
                    return self.CARD_SCORES[this_quad] > self.CARD_SCORES[other_quad]
                else:
                    return (self.CARD_SCORES[[value for value in self.card_values if self.multiple_cards[value] == 1][-1]] >=
                            self.CARD_SCORES[[value for value in other_hand.card_values if other_hand.multiple_cards[value] == 1][-1]])

            elif self.rank == 7:
                # Full house determined by triple or pair if same triple.
                this_triple = [value for value in self.card_values if self.multiple_cards[value] == 3][-1]
                other_triple = [value for value in other_hand.card_values if other_hand.multiple_cards[value] == 3][-1]
                if this_triple != other_triple:
                    return self.CARD_SCORES[this_triple] > self.CARD_SCORES[other_triple]
                else:
                    return (self.CARD_SCORES[[value for value in self.card_values if self.multiple_cards[value] == 2][-1]] >=
                            self.CARD_SCORES[[value for value in other_hand.card_values if other_hand.multiple_cards[value] == 2][-1]])

            elif self.rank == 6 or self.rank == 1:
                # Flush or high card determined by comparing highest cards of each hand until one wins.
                for i in range(1, 6):
                    if self.card_values[-i] != other_hand.card_values[-i]:
                        return self.CARD_SCORES[self.card_values[-i]] >= self.CARD_SCORES[other_hand.card_values[-i]]
                # If we get here then the hands are equal so we return True for a tie.
                return True

            elif self.rank == 4:
                # Triple determined by triple or by next highest if same triple.
                this_triple = [value for value in self.card_values if self.multiple_cards[value] == 3][-1]
                other_triple = [value for value in other_hand.card_values if other_hand.multiple_cards[value] == 3][-1]
                if this_triple != other_triple:
                    return self.CARD_SCORES[this_triple] > self.CARD_SCORES[other_triple]
                else:
                    this_singles = [value for value in self.card_values if self.multiple_cards[value] == 1]
                    other_singles = [value for value in other_hand.card_values if other_hand.multiple_cards[value] == 1]
                    if this_singles[-1] != other_singles[-1]:
                        return self.CARD_SCORES[this_singles[-1]] > self.CARD_SCORES[other_singles[-1]]
                    else:
                        return self.CARD_SCORES[this_singles[-2]] >= self.CARD_SCORES[other_singles[-2]]

            elif self.rank == 3:
                # Two pair determined by comparing pairs then kicker.
                this_pairs = [value for value in self.card_values if self.multiple_cards[value] == 2]
                other_pairs = [value for value in other_hand.card_values if other_hand.multiple_cards[value] == 2]
                if this_pairs[-1] != other_pairs[-1]:
                    return self.CARD_SCORES[this_pairs[-1]] > self.CARD_SCORES[other_pairs[-1]]
                elif this_pairs[-3] != other_pairs[-3]:
                    return self.CARD_SCORES[this_pairs[-3]] > self.CARD_SCORES[other_pairs[-3]]
                else:
                    return (self.CARD_SCORES[[value for value in self.card_values if self.multiple_cards[value] == 1][-1]] >=
                            self.CARD_SCORES[[value for value in other_hand.card_values if other_hand.multiple_cards[value] == 1][-1]])

            elif self.rank == 2:
                # One pair determined by comparing pair then kicker.
                this_pair = [value for value in self.card_values if self.multiple_cards[value] == 2][-1]
                other_pair = [value for value in other_hand.card_values if other_hand.multiple_cards[value] == 2][-1]
                this_kickers = [value for value in self.card_values if self.multiple_cards[value] == 1]
                other_kickers = [value for value in other_hand.card_values if other_hand.multiple_cards[value] == 1]

                if this_pair != other_pair:
                    return self.CARD_SCORES[this_pair] > self.CARD_SCORES[other_pair]
                elif this_kickers[-1] != other_kickers[-1]:
                    return self.CARD_SCORES[this_kickers[-1]] > self.CARD_SCORES[other_kickers[-1]]
                elif this_kickers[-2] != other_kickers[-2]:
                    return self.CARD_SCORES[this_kickers[-2]] > self.CARD_SCORES[other_kickers[-2]]
                else:
                    return self.CARD_SCORES[this_kickers[-3]] >= self.CARD_SCORES[other_kickers[-3]]

    # Gives a rank from best 10 to worst 1 based on the type of hand e.g flush.
    def rank_hand(self):
        # Check if straight, straight flush or royal flush.
        for straight in self.STRAIGHT:
            if straight.issubset(self.card_values_set):
                # This is a straight, check if flush or royal flush.
                if len(self.card_suits_set) == 1:
                    if self.card_values[-1] == 'A':
                        return 10
                    else:
                        return 9
                else:
                    return 5

        # Check if flush.
        if len(self.card_suits_set) == 1:
            return 6

        # If all cards distinct and not straight or flush, then weakest.
        if len(self.card_values_set) == 5:
            return 1

        # Check if four of a kind, full house, three of a kind, two pair, pair.
        pairs = 0
        triples = 0
        quadruples = 0
        for value in self.multiple_cards:
            if self.multiple_cards[value] == 2:
                pairs += 1
            elif self.multiple_cards[value] == 3:
                triples += 1
            elif self.multiple_cards[value] == 4:
                quadruples += 1

        if quadruples:
            return 8
        elif triples and pairs:
            return 7
        elif triples:
            return 4
        elif pairs == 2:
            return 3
        elif pairs == 1:
            return 2

    def count_multiple_cards(self):
        multiple_cards = {}
        for value in self.card_values:
            multiple_cards[value] = multiple_cards.setdefault(value, 0) + 1
        return multiple_cards


with open('p054_poker.txt', 'r') as f:
    number_of_wins = 0
    for line in f:
        card_list = line.split(' ', )
        hand_1 = Hand(card_list[0:5])
        hand_2 = Hand(card_list[5:10])
        if hand_1.beats_other_hand(hand_2):
            number_of_wins += 1

print number_of_wins

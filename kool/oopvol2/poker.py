"""Simple Poker implementation."""


class Card:
    """A card in a poker game."""

    def __init__(self, value, suit):
        """Initialze Card."""
        self.value = value
        self.suit = suit

    def __repr__(self):
        """
        Return a string representation of the card.

        "{value} of {suit}"
        "2 of hearts" or "Q of spades"

        """
        return f"{self.value} of {self.suit}"


class Hand:
    """The hand in a poker game."""

    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    values_to_int = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14
    }

    def __init__(self):
        """Initialize Hand."""
        self.cards = []

    def can_add_card(self, card: Card) -> bool:
        """
        Check for card validity.

        Can only add card if:
        - A card with the same suit and value is already not being held.
        - The player is holding less than five cards
        - The card has both a valid value and a valid suite.
        """
        if len(self.cards) < 5:
            if card.suit in Hand.suits and card.value in Hand.values:
                for item in self.cards:
                    if item.suit == card.suit and item.value == card.value:
                        return False
                return True
            else:
                return False
        else:
            return False

    def add_card(self, card: Card):
        """
        Add a card to hand.

        Before adding a card, you would have to check if it can be added.
        """
        if self.can_add_card(card):
            self.cards.append(card)

    def can_remove_card(self, card: Card):
        """
        Check if a card can be removed from hand.

        The only consideration should be that the card is already being held.
        """
        for item in self.cards:
            if item.suit == card.suit and item.value == card.value:
                return True
        return False

    def remove_card(self, card: Card):
        """
        Remove a card from hand.

        Before removing the card, you would have to check if it can be removed.
        """
        if self.can_remove_card(card):
            self.cards.remove(card)

    def get_cards(self):
        """Return a list of cards as objects."""
        return self.cards

    def is_straight(self):
        """
        Determine if the hand is a straight.

        A straight hand will have all cards in the order of value.
        Sorting will help you here as the order will vary.

        Examples:
        4 5 6 7 8
        K J 10 Q A

        For the sake of simplicity - A 2 3 4 5 will not be tested.
        You can always consider A to be the highest ranked card.
        """
        cardlist = self.get_cards()
        card_value_list = []
        for card in cardlist:
            card_value_list.append(Hand.values_to_int[card.value])
        card_value_list_sorted = sorted(card_value_list)
        for i in range(0, len(card_value_list_sorted)-1):
            if card_value_list_sorted[i] + 1 != card_value_list_sorted[i+1]:
                return False
        return True


    def is_flush(self):
        """
        Determine if the hand is a flush.

        In a flush hand all cards are the same suit. Their number value is not important here.
        """
        cardlist = self.get_cards()
        flush_suit = cardlist[0].suit
        for item in cardlist:
            if item.suit != flush_suit:
                return False
        return True

    def is_straight_flush(self):
        """
        Determine if the hand is a straight flush.

        Such a hand is both straight and flush at the same time.

        """
        if self.is_straight() and self.is_flush():
            return True
        else:
            return False

    def is_full_house(self):
        """
        Determine if the hand is a full house.

        A house will have three cards of one value, and two cards of a second value.
        For example:
        2 2 2 6 6
        K J K J K
        """
        cardlist = self.get_cards()
        cardvalues = []
        for card in cardlist:
            cardvalues.append(card.value)
        three_cards_of_one = False
        two_cards_of_one = False
        three_cards_value = ""
        for i in range(0,len(cardvalues)):
           if cardvalues.count(cardvalues[i]) == 3:
            three_cards_of_one = True
            three_cards_value = cardvalues[i]
        for i in range(0, len(cardvalues)):
            if cardvalues[i] != three_cards_value and cardvalues.count(cardvalues[i]) == 2:
                three_cards_of_one = True
        if three_cards_of_one and two_cards_of_one:
            return True
        else:
            return False

    def is_four_of_a_kind(self):
        """
        Determine if there are four cards of the same value in hand.

        For example:
        2 2 K 2 2
        9 4 4 4 4

        """
        cardlist = self.get_cards()
        cardvalues = []
        for card in cardlist:
            cardvalues.append(card.value)
        for card in cardvalues:
            if cardvalues.count(card) == 4:
                return True
        return False

    def is_three_of_a_kind(self):
        """
        Determine if there are three cards of the same value in hand.

        For Example:
        Q 4 Q Q 7
        5 5 1 5 2

        """
        cardlist = self.get_cards()
        cardvalues = []
        for card in cardlist:
            cardvalues.append(card.value)
        for card in cardvalues:
            if cardvalues.count(card) == 3:
                return True
        return False

    def is_pair(self):
        """
        Determine if there are two kinds of the same value in hand.

        For example:
        5 A 2 K A
        8 7 6 6 5

        """
        cardlist = self.get_cards()
        cardvalues = []
        for card in cardlist:
            cardvalues.append(card.value)
        for card in cardvalues:
            if cardvalues.count(card) == 2:
                return True
        return False

    def get_hand_type(self):
        """
        Return a string representation of the hand.

        Return None (or nothing), if there are less than five cards in hand.

        "straight flush" - Both a straight and a flush
        "flush" - The cards are all of the same suit
        "straight" - The cards can be ordered
        "full house" - Three cards are of the same value while the other two also share a value.
        "four of a kind" - Four cards are of the same value
        "three of a kind" - Three cards are of the same value
        "pair" - Two cards are of the same value
        "high card" - None of the above

        """
        cardlist = self.get_cards()
        hand_type = ""
        if len(cardlist) == 5:
            if self.is_straight_flush():
                hand_type = "straight flush"
            elif self.is_flush():
                hand_type = "flush"
            elif self.is_straight():
                hand_type = "straight"
            elif self.is_full_house():
                hand_type = "full house"
            elif self.is_four_of_a_kind():
                hand_type = "four of a kind"
            elif self.is_three_of_a_kind():
                hand_type = "three of a kind"
            elif self.is_pair():
                hand_type = "pair"
            else:
                hand_type = "high card"
        else:
            return None
        return hand_type

    def __repr__(self):
        """
        Return a string representation of the hand.

        I got a {type} with cards: {card list}
        I got a straight with cards: 2 of diamonds, 4 of spades, 5 of clubs, 3 of diamonds, 6 of hearts

        If a hand type cannot be yet determined, return a list of cards as so:

        I'm holding {cards}
        I'm holding 2 of diamonds, 4 of spades.

        Order of the cards is not important.
        """
        cardlist = self.get_cards()
        clean_cardlist = str(cardlist).replace("[","").replace("]","")
        card_type = self.get_hand_type()
        if card_type:
            return f"I got a {card_type} with cards {clean_cardlist}"
        else:
            return f"I'm holding {clean_cardlist}"

if __name__ == "__main__":

    hand = Hand()
    cards = [Card("2", "diamonds"), Card("4", "spades"), Card("5", "clubs"), Card("3", "diamonds"), Card("6", "hearts")]
    [hand.add_card(card) for card in cards]
    print(hand.get_hand_type())
    assert hand.get_hand_type() == "straight"

    hand = Hand()
    cards = [Card("10", "diamonds"), Card("2", "diamonds"), Card("A", "diamonds"), Card("6", "diamonds"),
             Card("9", "diamonds")]
    [hand.add_card(card) for card in cards]
    print(hand.get_hand_type())
    assert hand.get_hand_type() == "flush"

    hand = Hand()
    cards = [Card("A", "hearts"), Card("A", "clubs"), Card("A", "spades"), Card("A", "diamonds"),
             Card("9", "diamonds")]
    [hand.add_card(card) for card in cards]
    print(hand.get_hand_type())
    assert hand.get_hand_type() == "four of a kind"
    print(hand.__repr__())
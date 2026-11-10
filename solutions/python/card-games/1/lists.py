"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    Parameters:
        number (int): The current round number.

    Returns:
        list: The current round number and the two that follow.
    """

    next_round = number + 1
    round_after_next = number + 2

    return [number, next_round, round_after_next]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1 (list): The first rounds played.
        rounds_2 (list): The second group of rounds played.

    Returns:
        list:  All rounds played.
    """

    all_rounds = rounds_1 + rounds_2
    return all_rounds


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds (list): The rounds played.
        number (int): The round number.

    Returns:
        bool: Was the round played?
    """

    if number in rounds:
        return True

    return False

def card_average(hand):
    """Calculate and returns the average card value from the list.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average value of the cards in the hand.
    """

    if not hand:
        return 0

    total_value = sum(hand)
    number_of_cards = len(hand)

    return total_value / number_of_cards


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Does one of the approximate averages equal the `true average`?
    """

    average = card_average(hand)

    first_and_last_average = (hand[0] + hand[-1]) / 2
    middle_card = hand[len(hand) // 2]

    if first_and_last_average == average or middle_card == average:
        return True

    return False


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Are the even and odd averages equal?
    """

    even_indexed_cards = hand[::2]
    odd_indexed_cards = hand[1::2]

    even_average = card_average(even_indexed_cards)
    odd_average = card_average(odd_indexed_cards)

    return even_average == odd_average


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with Jacks (if present) value doubled.
    """

    if not hand or hand[-1] != 11:
        return hand

    # 拷贝一份新手牌，修改新列表的最后一张
    new_hand = hand.copy()
    new_hand[-1] *= 2
    return new_hand


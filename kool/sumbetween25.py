"""Sum elements between 2 and 5."""


def sum_between_25(numbers: list) -> int:
    """
    Return the sum of the numbers in the array which are between 2 and 5.

    Summing starts from 2 (not included) and ends at 5 (not included).
    The section can contain 2 (but cannot 5 as this would end it).
    There can be several sections to be summed.

    sum_between_25([1, 3, 6, 7]) => 0
    sum_between_25([1, 2, 3, 4, 5, 6]) => 7
    sum_between_25([1, 2, 3, 4, 6, 6]) => 19
    sum_between_25([1, 3, 3, 4, 5, 6]) => 0
    sum_between_25([1, 2, 3, 4, 5, 6, 1, 2, 9, 5, 6]) => 16
    sum_between_25([1, 2, 3, 2, 5, 5, 3, 5]) => 5

    :param numbers:
    :return:
    """

    sum_numbers = 0
    # where to start summing
    start_index = 0
    start_sum = False
    # loop through the numberslist
    for i in range(0, len(numbers)):
        # if we come to the first 2 in the list
        if numbers[i] == 2 and not start_sum:
            start_sum = True
            start_index = i + 1
        # we should start summing after the first 2 and stop before the first 5
        if start_sum and i >= start_index and numbers[i] != 5:
            sum_numbers += numbers[i]
        # if we come across 5 during summing
        if start_sum and numbers[i] == 5:
            start_sum = False
            start_index = 0

    return sum_numbers

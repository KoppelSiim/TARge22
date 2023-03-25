def close_far(a: int, b: int, c: int) -> bool:

    """
    Return if one value is "close" and other is "far".

    Given three ints, a b c, return true if one of b or c is "close" (differing from a by at most 1),
    while the other is "far", differing from both other values by 2 or more.

    close_far(1, 2, 10) => True
    close_far(1, 2, 3) => False
    close_far(4, 1, 3) => True
    """

    # a is close to b, and c is far from a and b
    if abs(a - b) <= 1 < abs(a - c) and abs(c - a) >= 2 and abs(c - b) >= 2:
        return True
    # a is close to c and b is far from a and c
    if abs(a - c) <= 1 < abs(a - b) and abs(b - a) >= 2 and abs(b - c) >= 2:
        return True

    return False

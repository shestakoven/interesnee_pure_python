def can_be_palindrome(string):
    """The function checks if a palindrome can be formed from a string.

    Args:
        string (str): Just string. What else?)

    Returns:
        bool: True if string can be palindrome.

    """

    string = str(string)
    dict_of_duplicates = dict()
    not_pair_count = 0
    for sym in string:
        if sym in dict_of_duplicates:
            dict_of_duplicates[sym] += 1
        else:
            dict_of_duplicates[sym] = 1

    for value in dict_of_duplicates.values():
        if value % 2 == 0:
            continue
        else:
            not_pair_count += 1
            if not_pair_count > 1:
                return False
    return True

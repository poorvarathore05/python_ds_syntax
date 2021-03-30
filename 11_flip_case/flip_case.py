def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_ltr = to_swap.lower()
    s = ''
    for char in phrase:
        if char.lower() == new_ltr:
            char = char.swapcase()
        s += char

    return s

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    # return sum("".join(i for i in s if str.isdigit(i)))
    result = []
    for i in s:
        if str.isdigit(i):
            result.append(int(i))
    if result == []:
        raise ValueError ("String is empty")
    return sum(result)
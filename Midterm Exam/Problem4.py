def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    import math
    x = (math.sqrt(8*k + 1) - 1) / 2
    if x - int(x) > 0: # if x is not an integer
        return False
    else:
        return True
def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None """
    best = 0
    dictList = {}
    for i in L:
        dictList[i] = dictList.get(i, 0) + 1
    for x in dictList.keys():
        if dictList[x] % 2 != 0:
            if x > best:
                best = x
    if best == 0:
        return None
    return best
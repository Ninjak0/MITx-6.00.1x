def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
            If they are permutations of each other, returns a
            tuple of 3 items in this order:
            the element occurring most, how many times it occurs, and its type
    '''
    if L1 == [] and L2 == []:
        return (None, None, None)
    if len(L1) != len(L2):
        return False
    list1 = L1.copy()
    list2 = L2.copy()
    for s in list1:
        if s not in list2:
            return False
        else:
            list1.remove(s)
            list2.remove(s)
    dictList1 = {}
    dictList2 = {}
    for i in L1:
        dictList1[i] = dictList1.get(i, 0) + 1
    for n in L2:
        dictList2[n] = dictList2.get(n, 0) + 1
    bestNbr = 0
    bestPos = 0
    bestType = 0
    for s in dictList1:
        if dictList1[s] > bestNbr:
            bestPos = s
            bestNbr = dictList1[s]
            bestType = type(s)
    return (bestPos, bestNbr, bestType)
def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    reverseDict = {}
    inList = []
    for i in d:
        if d[i] in reverseDict:
            inList.append(i)
            reverseDict[d[i]] = inList
            inList.sort()
#        print(reverseDict)
        else:
            inList = [i]
            reverseDict[d[i]] = inList
    return reverseDict
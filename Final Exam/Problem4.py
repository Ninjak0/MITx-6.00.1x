def max_val(t):
    best = 0

    for i in t:

        if isinstance(i, int):
            if i > best:
                best = i
        else:

            val = max_val(i)
            if val > best:
                best = val

    return best

max1 = max_val(([[2, 1, 5], [4, 2], 6], ([2, 1], (7, 7, 5), 6)))
print(max1)
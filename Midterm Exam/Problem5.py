def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    vowelsLow = "aeiou"
    vowelsHigh = "AEIOU"
    outPut = ""
    for letter in s:
        if letter in vowelsLow or letter in vowelsHigh:
            outPut += ""
        else:
            outPut += letter
    print(outPut)
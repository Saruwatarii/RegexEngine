'''
Updated the program from checking a single character and extended it to handle pair of rexeg and a string of
equal length. Also supporting the wildcard symbol (.)
Conditions:
    - If the regex has been consumed, the function of the program should return True, meaning that all the regex-string
      pairs are equal.
    - If the regex has not been consumed, the function should return False, meaning that the regex is longer than the
      input itself.
    - If the character of the regex does not match the  first character in the string, it should return False.
      Because its guarantees that the two patterns are in fact different.

'''
def reg_checker(regex, string, i=0):
    '''(str, str, int) --> bool
        Check if regex input is matching the string input. The regex input is supported with a wildcard "."
        The wildcard can be any character.
        i is an incrementer for the both the regex and the string in order to check if they are matching.
        If they are matching then increment the i(the index of the 2 strings) and contine to check the next character.

        reg_checker(apple, apple, i=0):
        < True
        reg_checker(, a, i=0):
        < True
        reg_checker(.ppl., apple, i=0):
        < True
        reg_checker(peach, apple, i=0):
        < False
    '''

    #Wildcard
    support = '.'
    if len(regex) == 0:
        return True
    if len(string) == 0:
        return False
    if i == len(string) - 1:
        if regex[i] == string[i] or regex[i] == support:
            return True
        elif len(regex) != len(string):
            return False
        else:
            return False
    if regex[i] == string[i] or regex[i] == support:
        return reg_checker(regex, string, i=i + 1)
    else:
        return False

# Input one string where the delimeter is a |. on the left side is the regex expression,
# while on the right side is the string
regex, string = input().split("|")

print(reg_checker(regex, string))


#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
    if word.isspace() == True:
        return False
    comparison = word.lower()
    list = comparison.split()
    xwhite = ''.join(list)
    # print(xwhite)
    upper_bound = len(xwhite) - 1
    xwhite_reverse = []
    
    for index in range(upper_bound,-1, -1):
        xwhite_reverse.append(xwhite[index])
    # print(xwhite_reverse)
    xwhite_reverse_str = ''.join(xwhite_reverse)
    # print(xwhite_reverse_str)
    if xwhite_reverse_str == xwhite:
        return True
    else:
        return False

    

if __name__ == '__main__': 
    #REMOVE PASS AND YOUR CODE GOES HERE
    word = input()
    print(palindrome(word))

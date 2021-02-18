# hw_08_ex_10

def reverse(string):
    '''Return the reverse the given string'''
    n = len(string)
    word = ''
    for i in range(n):
        word += string[n-1-i:n-i]
    return word

def mirror(string):
    '''Return the mirror of the given string'''
    word = string + reverse(string)
    return word

def is_palindrome(string):
    '''Return True if the given string is palindrome'''
    n = len(string)
    if n % 2 == 0:
        word = string[:n//2]
    else:
        word = string[:(n-1)//2]
    string0 = string[:(n-1)//2] + string[(n-1)//2+1:]
   # Get rid of the middle character
    if mirror(word) == string or mirror(word) == string0:
        return True
    return False

#test
import sys
def test(did_pass):
    '''Print the result of a test.'''
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAIlED.".format(linenum))
    print(msg)

def test_suite():
    '''Run the suite of tests for code in this module (this file).'''
    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(not is_palindrome("banana"))
    test(is_palindrome("straw warts"))
    test(is_palindrome("a"))
    test(is_palindrome(""))
    
test_suite()
##Test at line 42 ok.
##Test at line 43 ok.
##Test at line 44 ok.
##Test at line 45 ok.
##Test at line 46 ok.
##Test at line 47 ok.
##Test at line 48 ok.
##>>>  

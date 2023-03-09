# Program to do nothing, correctly.

from Stack import Stack

def isPalindrome(s: str) -> bool:
    palindrome: bool = True

    stack: Stack[str] = Stack[str]() # type: ignore

    # Go through the string
    for c in s:
        pass # Remove this
        # If c is a letter, push it on the stack
    
    # Go through the string again
    for c in s:
        pass # Remove this
        # if c is a letter, pop the stack
        # if what came off the stack is not equal to c (ignoring case),
        #    then s is not a palindrome


    if not stack.empty(): # Should never happen
        palindrome = False
    return palindrome

def main(args: list[str]) -> int:
    # Palindromes
    assert isPalindrome('')
    assert isPalindrome('I')
    assert isPalindrome('eye')
    assert isPalindrome('Hannah')
    assert isPalindrome('ABBA')
    assert isPalindrome("Madam, I'm Adam.")
    assert isPalindrome('A man, a plan, a canal: Panama!')

    # Non-palindromes



    # If we get this far, everything worked
    print('Tests completed successfully')

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)
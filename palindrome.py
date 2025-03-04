"""
    This implementation works only for words, it doesn't support palindrome phrases
"""
def is_palindrome(word):
    word_backward = ''
    i = 0
    while len(word) > i:
        word_backward = word_backward + word[(len(word)-i)-1]
        i+=1
    if word == word_backward:
        return True
    return False

if __name__ == '__main__':
    print(is_palindrome('ana'))
    print(is_palindrome('madam'))
    print(is_palindrome('hello'))
    print(is_palindrome('a'))
    print(is_palindrome(''))

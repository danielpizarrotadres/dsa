"""
    This implementation works only for words, it doesn't support palindrome phrases
"""
def is_palindrome_word(word):
    word_backward = ''
    i = 0
    while len(word) > i:
        word_backward = word_backward + word[(len(word)-i)-1]
        i+=1
    if word == word_backward:
        return True
    return False

if __name__ == '__main__':
    print(is_palindrome_word('ana'))
    print(is_palindrome_word('madam'))
    print(is_palindrome_word('hello'))
    print(is_palindrome_word('a'))
    print(is_palindrome_word(''))

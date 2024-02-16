def palindrome(*args):
    word = args[0]
    if word[::-1] == word:
        return f"{word} is a palindrome"
    else:
        return f"{word} is not a palindrome"
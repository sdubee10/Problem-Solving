def solution(word):
    upper = word.upper()
    lower = word.lower()
    count = 0
    if word == upper or word == lower:
        return True

    else:
        for i in range(len(word)):
            if word[i].isupper():
                count += 1
            if count > 1:
                return False
    if word[0].isupper() and count == 1:
        return True
    else:
        return False

"""
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()
"""
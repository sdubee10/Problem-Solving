def solution(s, n):
    answer = ''
    for letter in s:
        if letter.islower() or letter.isupper():
            if letter.islower():
                answer += chr(ord('a') + (ord(letter) - ord('a') + n) % 26)
            elif letter.isupper():
                answer += chr(ord('A') + (ord(letter) - ord('A') + n) % 26)
        else:
            answer += letter
    return answer

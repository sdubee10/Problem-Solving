from collections import Counter

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    list1 = []
    list2 = []
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            list1.append(str1[i:i + 2])

    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            list2.append(str2[i:i + 2])

    Counter1 = Counter(list1)
    Counter2 = Counter(list2)

    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())

    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)
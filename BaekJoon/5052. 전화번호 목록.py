#------------ 쉬운 풀이
"""
import sys

def findPrefix(phone):
    n = len(phone)
    for i in range(n - 1):
        if phone[i] == phone[i+1][0:len(phone[i])]:
            return "NO"
    return "YES"

input = sys.stdin.readline

n = int(input())
answer = []
for i in range(n):
    num = int(input())
    phone = []
    for i in range(num):
        phone.append(input().strip())
    phone.sort()
    print(findPrefix(phone))
"""
#Trie
import sys
import math

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.child = [None for _ in range(10)]
        self.check = False


class Trie:
    def __init__(self):
        self.root = Node('')

    def insert(self, phone):
        tmp = self.root
        for i in phone:
            if tmp.child[i] != None:  # 비어있지 않으면
                tmp = tmp.child[i]
            else:
                new = Node(i)
                tmp.child[i] = new
                tmp = new
        tmp.check = True

    def consistency(self, phone):
        tmp = self.root
        for i in range(len(phone)):
            # print(tmp.check)
            if tmp.check:  # 다른문자열을 포함하고 있다면
                return False
            tmp = tmp.child[phone[i]]
        return True


for _ in range(int(input())):
    n = int(input())
    phone_list = []
    trie = Trie()
    for _ in range(n):
        phone = list(map(int, sys.stdin.readline().rstrip()))
        trie.insert(phone)
        phone_list.append(phone)
    result = True
    for p in phone_list:
        result *= trie.consistency(p)

    if result:
        print('YES')
    else:
        print('NO')

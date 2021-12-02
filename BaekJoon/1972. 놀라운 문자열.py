# while True:
#     string = input()
#
#     if string == "*":
#         break
#
#     for i in range(len(string) - 1):
#         results = []
#         flag = False
#         for j in range(len(string) - i - 1):
#             tmp = string[j]+string[j+i+1]
#             if tmp not in results:
#                 results.append(tmp)
#             else:
#                 flag = True
#                 print(string + " is NOT surprising.")
#                 break
#         if flag:
#             break
#     else:
#         print(string + " is surprising")

input_list = []
while True:
    z = input()
    input_list.append(z)
    if z == "*":
        input_list.pop()
        break

for string in input_list:
    flag = False
    for i in range(len(string) - 1):
        results = set()
        for j in range(len(string) - i - 1):
            tmp = string[j] + string[j + i + 1]
            if tmp not in results:
                results.add(tmp)
            elif tmp in results:
                flag = True
                print(string + " is NOT surprising.")
                break
        if flag:
            break
    else:
        print(string + " is surprising.")

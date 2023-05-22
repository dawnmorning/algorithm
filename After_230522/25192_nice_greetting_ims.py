# import sys
# input = sys.stdin.readline
# n = int(input())
# chat_dialogue = []

# for _ in range(n):
#     chat = input()
#     chat_dialogue.append(chat)
# # print(chat_dialogue)
# ref_list = ["ENTER"]
# count = 0
# for i in range(1,n):
#     if "ENTER" in ref_list and chat_dialogue[i] not in ref_list:
#         count += 1
#         ref_list.append(chat_dialogue[i])
#     elif chat_dialogue[i] == "ENTER" and "ENTER" in ref_list:
#         ref_list.clear()
#         ref_list.append("ENTER")
# print(count)
from collections import defaultdict

n = int(input())
chat_dialogue = []

for _ in range(n):
    chat = input().rstrip()  
    chat_dialogue.append(chat)

ref_list = ["ENTER"]
count = 0
seen = defaultdict(int)

for chat in chat_dialogue[1:]:
    if chat == "ENTER":
        ref_list = ["ENTER"] 
        seen.clear()
    elif chat not in seen and "ENTER" in ref_list:
        count += 1
        seen[chat] = 1
        ref_list.append(chat)

print(count)

n = int(input())
candidate_vote = []
count = 0
dasom = int(input())
for _ in range(n-1):
    c = int(input())
    candidate_vote.append(c)
candidate_vote.sort(reverse=True)
if n == 1:
    print(0)
else:
    while candidate_vote[0] >= dasom:
        dasom += 1
        candidate_vote[0] -= 1
        count += 1
        candidate_vote.sort(reverse=True)
    print(count)
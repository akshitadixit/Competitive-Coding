n = int(input())
score = {}

while n > 0:
    n -= 1
    s = input()
    if s not in score:
        score[s] = 0
    score[s] += 1

print(max(score, key=score.get))

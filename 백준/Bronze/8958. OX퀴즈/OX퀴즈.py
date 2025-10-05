"""
"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점
"""

n = int(input())

for _ in range(n):
    answer = list(input())

    score = 0
    sum_score = 0

    for ox in answer:
        if ox == 'O':
            score += 1
            sum_score += score
        elif ox == "X":
            score = 0
    
    print(sum_score)
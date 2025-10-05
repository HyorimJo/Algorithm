"""
우와 자정일 때를 생각도 못함
0:30 -> 23:45여야 하는데 -1:45가 나와버림
"""

hour, min = map(int, input().split())

if min >= 45:
    print(hour, min-45)

else:
    if hour == 0: # 자정
        hour = 23
    else:
        hour -= 1
    print(hour, min + 15)
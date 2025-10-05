"""
6 12 10 -> 402호
10%6 = 4
10//6 = 1

6 12 6일때
floor = 0, room = 2
그치만 601호가 맞는 거임.
"""

times = int(input())
for _ in range(times):
    h, w, n = map(int, input().split())

    floor = n % h
    room = n // h + 1

    if floor == 0: # 나누어떨어진다면
        floor = h
        room -= 1
        
    print(floor*100 + room)
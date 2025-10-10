'''
시간초과. 제한시간 0.25초
while True:
    days += 1
    snail += up         # 낮에 올라감
    if snail >= tree:     # 정상 도착!!
        print(days)
        break
    snail -= down         # 밤에 미끄러짐
'''

import math
up, down, tree = map(int, input().split())

# 올라가야할 거리 = tree - down
# 하루에 갈 수 있는 거리 = up - down
# 2 1 5 -> 4.0
# 5 1 6 -> 1.25
days = (tree - down) / (up - down)

print(math.ceil(days)) #ceil로 올림처리
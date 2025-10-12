'''
1 7 19 37
 6 12 18 -> 6의 배수씩 커진다

n >= beehive로 생각했었음
n = 7일 때 while문 그만 돌고 level=2여야 하는데
7 >= 7이라 while문 한 번 더 돌고 beehive=19, level=3
'''

n = int(input())
beehive = 1
level = 1

while n > beehive:
    beehive += level * 6
    level += 1

print(level)
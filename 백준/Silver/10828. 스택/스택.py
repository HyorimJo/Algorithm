import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    todo, *val = input().split()

    if todo == "push":
        stack.append(int(val[0])) # 정수를 스택에 넣어
    elif todo == "pop":
        if stack:
            print(stack.pop()) # 최상단 정수를 빼고 출력
        else: print(-1)
    elif todo == "size":
        print(len(stack)) # 스택에 있는 정수 개수 출력
    elif todo == "empty":
        if stack:
            print(0) # 비어있으면1, 아님 0
        else : print(1)
    elif todo == "top":
        if stack:
            print(stack[-1]) # 최상단 정수 출력
        else: print(-1)
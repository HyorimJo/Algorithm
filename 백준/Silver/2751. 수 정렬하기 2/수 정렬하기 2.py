import sys

n = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(n)] # input 했더니 시간초과 남

numbers = sorted(set(numbers))
print(*numbers, sep='\n')
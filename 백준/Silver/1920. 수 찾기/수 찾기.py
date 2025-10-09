'''
n 리스트에 값이 있으면 1
n_numbers를 list로 돌았더니 시간 초과가 났다 -> set으로 하면 탐색시간 줄일 수 있음
'''
n = int(input())
n_numbers = set(map(int, input().split())) #시간초과 해결

m = int(input())
m_numbers = list(map(int, input().split()))

for num in m_numbers:
    if num in n_numbers:
        print('1')
    else: print('0')
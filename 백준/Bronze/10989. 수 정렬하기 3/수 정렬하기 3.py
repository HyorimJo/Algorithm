'''
메모리초과 해결하기 -> counting sort 알고리즘
해당 수를 인덱스로 하는 위치의 값을 1씩 증가
 -> 해당 수가 등장한 횟수만큼 출력 (오름차순)
'''
import sys
n = int(sys.stdin.readline())

cnt = [0] * 10001

for _ in range(n):
    num = int(sys.stdin.readline())
    cnt[num] += 1

for i in range(1, 10001):
    if cnt[i] != 0:
        for _ in range(cnt[i]):
            print(i)
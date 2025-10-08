'''
소수란? 1과 자기 자신만을 약수로 가진 수
그럼 for문으로 진짜 다 나눠봐?
'''
n = int(input())
numbers = list(map(int, input().split()))
count = 0

for num in numbers:
    for i in range(2, num+1):
        if num % i == 0: # 나누어 떨어진다면
            if num == i: # 처음으로 나누어떨어지는 수가 자기 자신이면? -> 소수
                count += 1
            else: # 아니면 반복문 탈출
                break

print(count)
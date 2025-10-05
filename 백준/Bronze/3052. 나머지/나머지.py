li = []

for i in range(10):
    num = int(input())
    li.append(num % 42)

print(len(set(li))) # 중복 제거한 리스트의 길이 (set 사용)
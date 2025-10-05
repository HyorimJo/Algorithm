li = list(map(int, input().split()))
num = 0

for i in li:
    num += i*i
    
print(num % 10)
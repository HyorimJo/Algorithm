a = int(input())
b = int(input())
c = int(input())
numbers = list(map(int, str(a*b*c))) # map 써서 리스트 담기

for i in range(10):
    print(numbers.count(i))
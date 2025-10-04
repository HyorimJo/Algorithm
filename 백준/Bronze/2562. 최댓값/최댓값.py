li = []

for _ in range(9):
    li.append(int(input()))
    
print(max(li))
print(li.index(max(li))+1) #인덱스라서 +1 해야한대
student = []
no_hw = []

for _ in range(28):
    student.append(int(input()))
    
for i in range(1,31):
    if i not in student:
        no_hw.append(i)
        
print(min(no_hw))
print(max(no_hw))
'''
티셔츠: 사이즈별 학생 수를 shirts로 나눈 몫
    -> 0명이면 0, 몫이 0이면 1, 나눠떨어지면 그냥 몫, else 몫+1
펜: 전체 학생 수를 pen으로 나눈 몫 & 나머지
'''

stu = int(input()) # 학생수
size_list = list(map(int, input().split())) # 사이즈별 학생 
shirts, pen = map(int, input().split()) # 티셔츠, 펜 한 묶음당 개수

shirts_cnt = 0
for i in size_list:
    if i == 0:
        pass
    elif i // shirts == 0:
        shirts_cnt += + 1
    else:
        if i % shirts == 0:
            shirts_cnt += i // shirts
        else:
            shirts_cnt += (i // shirts) + 1

print(shirts_cnt)
print(stu // pen, stu % pen)
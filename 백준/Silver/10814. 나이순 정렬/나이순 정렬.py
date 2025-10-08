'''
두개 동시에 order 걸 때는 lambda를 쓰자
아 근데 조건 두개가 아니다!!
나이순 - 이름순 정렬인줄 알았는데 나이순만이다
나이순-이름순이면 people = sorted(people, key = lambda x : (x[0],x[1]))
그리고 나이순 sorting 하려면 int를 붙여야 한다
'''

n = int(input())
people = []

for _ in range(n):
    age, name = input().split()
    people.append((age,name))

people = sorted(people, key = lambda x : (int(x[0])))

for age, name in people:
    print(age, name)
"""
3 4 5 가 아니라 4 5 3이면?
그럼 리스트로 받아서 max값을 빼고 나머지 두개의 제곱합 구해
"""

while True:
    tri = list(map(int, input().split()))
    if sum(tri) == 0:
        break

    max_tri = max(tri)
    tri.remove(max_tri)

    if max_tri**2 == tri[0]*tri[0] + tri[1]*tri[1]:
        print('right')
    else:
        print('wrong')
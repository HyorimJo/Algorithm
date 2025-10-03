'''
a층 b호 = a층 (b-a)호 + (a-1)층 b호
일단 0층 리스트를 만들어?
0호는 없고 1호부터 있음을 잊지 말것.. ho인지 ho+1인지!
'''

n = int(input())

for i in range(n):
    floor =int(input())
    ho = int(input())
    dp = [[0] * (ho+1) for _ in range(floor+1)]

    # 0층 넣기
    for i in range(1,ho+1):
        dp[0][i] = i

    for a in range(1, floor+1):
        for b in range(1,ho+1):
            dp[a][b] = dp[a][b-1] + dp[a-1][b]

    print(dp[floor][ho])
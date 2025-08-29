"""
dp말고 조합으로 풀면 안되나...
1) 서쪽 1번이 동쪽 1번을 고르는 경우 - dp[2][4]
2) 서쪽 1번이 동쪽 1번을 고르지 않는 경우 - dp[3][4]
dp[3][5] = dp[2][4] + dp[3][4]
dp[n][m] = dp[n-1][m-1] + dp[n][m-1]

따로 빼서 생각해야할 경우가 n=m인 경우, n=1인 경우.
이건 for문 따로 돌리나?
-> n=1인 경우는 1 고정하고 m만 돌리면 되니까 따로 for문 돌려
-> n=m인 경우는 어차피 dp 돌릴 때 n,m 다 도니까 그때 if 걸어서 돌려
아 근데 n,m 돌 때 n은 2부터. 앞에서 1 다 돌았으니까~
"""

"""
조합풀이!
import math
num = int(input())
for _ in range(num):
    N, M = map(int, input().split())
    print(math.comb(M, N))
"""

dp = [[0]*31 for _ in range(31)]

for m in range(1, 31):
    dp[1][m] = m


for n in range(2, 31):
    for m in range(1, 31):
        if n == m:
            dp[n][m] = 1
        dp[n][m] = dp[n-1][m-1] + dp[n][m-1]

num = int(input())

for _ in range(num):
    n, m = map(int, input().split())
    print(dp[n][m])
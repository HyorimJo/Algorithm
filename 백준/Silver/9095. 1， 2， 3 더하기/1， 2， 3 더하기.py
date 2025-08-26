n = int(input())

# 빈 dp 배열 만들기
dp = [0] * 11 # max값이 11이랬으니까!

dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4 # dp[i-3]까지 가니까 초기값은 3까지

for i in range(4,11): # 초기값 3까지 했으니까 4부터
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(n):
    number = int(input())
    print(dp[number])
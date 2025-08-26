dp = [0] * (10**6+1)
# dp 테이블에서 보통 0번은 버리고 인덱스로 그 값을 그대로 매칭함
# 만약에 +1을 안하면 인덱스가 10의 6승 -1 까지 돼버림

dp[0] = 0
dp[1] = 0

for i in range(2, 10**6+1):
    dp[i] = dp[i-1] + 1
    # dp[7] = dp[6] + 1임
    # 여기서 1은 1을 뺀 연산을 count 한 것

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

    # dp[10] = dp[9] + 1 = 4가 최소지만
    # i % 2 == 0 조건을 만족하기 때문에 dp[5] + 1 = 5 값으로 덮어씌워져
        # -> min값을 통해 최소값 구하기 min(4,5)

number = int(input())
print(dp[number])
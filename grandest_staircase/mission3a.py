# The total number of ways in which arrays of >2 distinct elements can be built, whose sum is N.
# Only input is N

def solution(n):

	# from distinct partitions formula Q(n,k) = Q(n-k,k) + Q(n-k,k-1); Q(1,1)=1; Q(n,0)=0
	# https://oeis.org/A008289
	# answer = Q(n,1) + Q(n,2) + Q(n,3) ... Q(n,k) - 1 [because Q(n,1)=1 and we need at least 2 stairs in our sol]
	Q = [[0]*(n+1) for _ in range(n+1)]
	for i in range(n+1):
		Q[i][1]=1
		Q[i][0]=0

	for i in range(n+1):
		for k in range(2,i):
			Q[i][k] = Q[i-k][k] + Q[i-k][k-1]

	return sum([Q[n][i] for i in range(n+1)]) - 1



# following is parthsarathi's solution
def dfs(n, MIN, dp):
    if n <= MIN * 2:
        return 0

    if dp[n][MIN] != -1:
        return dp[n][MIN]

    ans = 1
    for i in range(MIN + 1, ((n - MIN - 1) // 2) + 1):
        ans += dfs(n - MIN, i, dp)
    dp[n][MIN] = ans

    return dp[n][MIN]


def solution_parth(n):
    ans = 0
    dp = [[-1] * (n + 1) for _ in range(n + 1)]
    for i in range(1, ((n - 1) // 2) + 1):
        ans += dfs(n, i, dp)

    return ans
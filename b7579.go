package main

import (
	"fmt"
)

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	var N, M, sum int
	fmt.Scan(&N, &M)

	memory := make([]int, N+1)
	cost := make([]int, N+1)

	for i := 1; i <= N; i++ {
		fmt.Scan(&memory[i])
	}

	for i := 1; i <= N; i++ {
		fmt.Scan(&cost[i])
		sum += cost[i]
	}

	dp := make([][]int, N+1)
	for i := range dp {
		dp[i] = make([]int, sum+1)
	}

	for i := 1; i <= N; i++ {
		for c := 0; c <= sum; c++ {
			if cost[i] > c {
				dp[i][c] = dp[i-1][c]
			} else {
				dp[i][c] = max(dp[i-1][c], dp[i-1][c-cost[i]]+memory[i])
			}
		}
	}

	for i := 0; i <= sum; i++ {
		if dp[N][i] >= M {
			fmt.Println(i)
			break
		}
	}
}

__author__ = 'ray'
# problem url: https://community.topcoder.com/stat?c=problem_statement&pm=1259


class ZigZag:
	@staticmethod
	def longestZigZag(sequence):
		n = len(sequence)
		dp = [[1]*2]*n
		for i in range(1,n):
			if sequence[i] > sequence[i-1]:
				dp[i][0] = dp[i-1][0]
				dp[i][1] = dp[i-1][0] + 1
			elif sequence[i] < sequence[i-1]:
				dp[i][0] = dp[i-1][1] + 1
				dp[i][1] = dp[i-1][1]
			else:
				dp[i][0] = dp[i-1][0]
				dp[i][1] = dp[i-1][1]
		return max(dp[n-1][0], dp[n-1][1])


if __name__ == '__main__':
	_in = (1, 2, 3, 4, 5, 6, 7, 8, 9)
	print ZigZag.longestZigZag(_in)
	_in = (70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32)
	print ZigZag.longestZigZag(_in)
	_in = (374, 40, 854, 203, 203, 156, 362, 279, 812, 955,
				 600, 947, 978, 46, 100, 953, 670, 862, 568, 188,
				 67, 669, 810, 704, 52, 861, 49, 640, 370, 908,
				 477, 245, 413, 109, 659, 401, 483, 308, 609, 120,
				 249, 22, 176, 279, 23, 22, 617, 462, 459, 244)
	print ZigZag.longestZigZag(_in)

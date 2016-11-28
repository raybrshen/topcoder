__author__ = 'ray'
# problem url: https://community.topcoder.com/stat?c=problem_statement&pm=1259

# A sequence of numbers is called a zig-zag sequence if the differences between successive numbers strictly alternate between positive and negative.
# The first difference (if one exists) may be either positive or negative.
# A sequence with fewer than two elements is trivially a zig-zag sequence.
# Given a sequence of integers, return the length of the longest subsequence of sequence that is a zig-zag sequence.
# A subsequence is obtained by deleting some number of elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.

# Both greedy and DP method can achieve O(n) time complexity.
# In a greedy method, always track the first number in a monotonically increasing/decreasing subsequence.
# Increment the length of result subsequence by one when such number is encountered, return it as result.

# In a DP method, for each number in the sequence, use an array "dp" to store the number of up and down up until this point.
# dp[0] means treating current number as a going-down from its previous number.
# dp[1] means treating current number as a going-up from its previous number.
# When a number is greater than its precedent, let dp[1] be the previous dp[0] plus 1.
# When a number is smaller than its precedent, let dp[0] be the previous dp[1] plus 1.
# For all other case dp[0] and dp[1] remain the same as its precedent.
# Then max(dp[0],dp[1]) of the last number is the result.

# greedy method
class ZigZag:
  @staticmethod
  def longestZigZag(sequence):
    n = len(sequence)
    if n<2: return n
    st=1
    while st<n and sequence[st]==sequence[st-1]: st+=1
    if st==n: return 1
    ret,increase = 2,sequence[st]>sequence[st-1]
    for i in range(st+1,n):
      if sequence[i]>sequence[i-1] and not increase:
          ret,increase = ret+1,True
      if sequence[i]<sequence[i-1] and increase:
          ret,increase = ret+1,False
    return ret

# DP method
# class ZigZag:
# 	@staticmethod
# 	def longestZigZag(sequence):
# 		n = len(sequence)
# 		dp = [[1]*2]*n
# 		for i in range(1,n):
# 			if sequence[i] > sequence[i-1]:
# 				dp[i][0] = dp[i-1][0]
# 				dp[i][1] = dp[i-1][0] + 1
# 			elif sequence[i] < sequence[i-1]:
# 				dp[i][0] = dp[i-1][1] + 1
# 				dp[i][1] = dp[i-1][1]
# 			else:
# 				dp[i][0] = dp[i-1][0]
# 				dp[i][1] = dp[i-1][1]
# 		return max(dp[n-1][0], dp[n-1][1])


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

__author__ = 'ray'
# problem url: https://community.topcoder.com/stat?c=problem_statement&pm=1599


import sys

class BridgeCrossing:
	def __init__(self):
		self.flag = []
		self.n = 0
		self.people = ()
		self.remain = 0

	def backtrack(self):
		min_time = sys.maxint
		for i in range(0,self.n-1):
			if self.flag[i]:
				continue
			for j in range(i+1,self.n):
				if self.flag[j]:
					continue
				tij = max(self.people[i],self.people[j])
				if self.remain == 2:
					return tij
				self.flag[i]=True
				self.flag[j]=True
				self.remain -= 1
				for k in range(0,self.n):
					if self.flag[k]:
						self.flag[k] = False
						t = self.backtrack() + tij + self.people[k]
						if t < min_time:
							min_time = t
						self.flag[k] = True
				self.remain += 1
				self.flag[i]=False
				self.flag[j]=False
		return min_time

	def minTime(self, times):
		self.people = times
		self.remain = self.n = len(times)

		if self.n == 1:
			return times[0]

		self.flag = [False]*self.n
		return self.backtrack()

if __name__ == '__main__':
	bc = BridgeCrossing()
	re = bc.minTime((1,2,5,10))
	print re

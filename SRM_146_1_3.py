__author__ = 'ray'
# problem url: https://community.topcoder.com/stat?c=problem_statement&pm=1599

# A well-known riddle goes like this: Four people are crossing an old bridge.
# The bridge cannot hold more than two people at once.
# It is dark, so they can't walk without a flashlight, and they only have one flashlight!
# Furthermore, the time needed to cross the bridge varies among the people in the group.
# When people walk together, they always walk at the speed of the slowest person.
# The flashlight can not be tossed across the bridge, so one person always has to go back with the flashlight to the others.
# What is the minimum amount of time needed to get all the people across the bridge?

import sys

class BridgeCrossing:
	def __init__(self):
		self.flag = []
		self.n = 0
		self.people = ()
		self.remain = 0
	
	# backtrack function to calculate the minimal time needed for the rest of people to cross the bridge
	# people who has crossed is flagged true, otherwise false
	# corner case:
	#   - when there is one person who hasn't crossed, return the time for him
	#   - when there are only two people who haven't crossed, return the time for the slower person
	# run dfs for all possible arrangement, cache the minimal crossing time so far
	# prunning: if the current arrangement has exceeded the minimal crossing time, stop there and try next arrangement
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
	
	# interface function
	# given a list of crossing time for each person as input
	# return the minimum crossing time for the group
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

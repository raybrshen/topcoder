__author__ = 'ray'
# problem url: https://community.topcoder.com/stat?c=problem_statement&pm=1744

import sys

class MNS:
	checklist = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8)]

	def __init__(self):
		self.flag = []
		self.numbers = ()
		self.perm = []
		self.perms = []

	# def magic_check(self, numbers):
	# 	num_sum = numbers[0]+numbers[1]+numbers[2]
	# 	for i in range(0,6):
	# 		tmp_sum = 0
	# 		for j in range(0,3):
	# 			tmp_sum += numbers[self.checklist[i][j]]
	# 		if tmp_sum != num_sum:
	# 			return False
	# 	return True
	def magic_check(self):
		mag_sum = self.perm[0]+self.perm[1]+self.perm[2]
		magic = [mag_sum-self.perm[3]-self.perm[4],
						 mag_sum-self.perm[0]-self.perm[3],
						 mag_sum-self.perm[1]-self.perm[4],
						 self.perm[3]+self.perm[4]-self.perm[2]]
		for i in range(0,9):
			if self.flag[i]:
				continue
			if self.numbers[i] in magic:
				magic.remove(self.numbers[i])
			else:
				return
		mv = 0
		for i in range(0,5):
			mv += (10*mv + self.perm[i])
		if not mv in self.perms:
			self.perms.append(mv)

	def backtrack(self, idx):
		for i in range(0,9):
			if self.flag[i]:
				continue
			self.perm[idx] = self.numbers[i]
			self.flag[i] = True
			if idx==4:
				self.magic_check()
			else:
				self.backtrack(idx+1)
			self.flag[i] = False

	def combos(self, numbers):
		self.numbers = numbers
		self.perm = [0]*5
		self.flag = [False]*9
		self.perms = []
		self.backtrack(0)
		return len(self.perms)


if __name__ == '__main__':
	mns = MNS()
	_in = (4,4,4,4,4,4,4,4,4)
	re = mns.combos(_in)
	print re
	_in = (1,2,6,6,6,4,2,6,4)
	re = mns.combos(_in)
	print re
	_in = (1,5,1,2,5,6,2,3,2)
	re = mns.combos(_in)
	print re



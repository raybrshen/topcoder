__author__ = 'ray'
# problem url: https://community.topcoder.com/stat?c=problem_statement&pm=3942

from fractions import Fraction as ft

# simplex tableau
# b.v. | x1 x2 x3 x4 a1 a2 a3 | RHS
# ----------------------------------
# a1   |                      |
# a2   |                      |
# a3   |                      |
# ----------------------------------
# -W   |                      |
# -P   |                      |

class Mixture:
	def __init__(self):
		self.n_ele = 0 # number of elements (objective)
		self.n_mix = 0 # number of mixtures (constraints)
		self.simplex = [] # simplex tableau
		self.bv = [] # basic variables
		self.debug = False # print debug info
		self.pm = False # print matrix

	def pre_processing(self, mixture, availableMixtures):
		self.n_ele = len(mixture)
		self.n_mix = len(availableMixtures)
		self.simplex = [ [ft(0)]*(self.n_mix+self.n_ele+1) for _ in range(self.n_ele+2) ]
		self.bv = [0]*self.n_ele
		# fill the first n_mix column of the simplex tableau
		for i in range(self.n_mix):
			tmp = availableMixtures[i].split(' ')
			tmp_sum = float(0)
			for j in range(self.n_ele):
				# the j-th entry of tmp is the amount of j-th element it contains
				self.simplex[j][i] = ft(float(tmp[j]))
				tmp_sum -= float(tmp[j])
			# the last entry of tmp is the price for that mixture
			self.simplex[-1][i] = ft(float(tmp[-1]))
			# formalize the the first objective function -W
			self.simplex[-2][i] = ft(tmp_sum)
		# fill the rest of the simplex tableau
		tmp_sum = float(0)
		for i in range(self.n_ele):
			# mark artificial variables
			self.simplex[i][i+self.n_mix] = ft(float(1))
			# fill the last column with RHS of linear system
			self.simplex[i][-1] = ft(float(mixture[i]))
			tmp_sum -= float(mixture[i])
			# initialize basic variable indicators with artificial variables
			self.bv[i]=self.n_mix+i
		self.simplex[-2][-1] = ft(tmp_sum)
		self.print_matrix()

	def print_matrix(self):
		if not self.pm: return
		for row in self.simplex:
			for val in row:
				print float(val),'\t',
			print ''

	# get pivot column given row of objective function and column range to check
	def get_pc(self, r, c):
		val,idx = min((val,idx) for (idx,val) in enumerate(self.simplex[r][:c]))
		if self.debug: print '- column pivot: ', float(val)
		if val<0: return idx
		else: return -1

	# get pivot row given pivot column
	def get_pr(self, c):
		row = -1
		tmp_min= ft(float(10)**300)
		for i in range(self.n_ele):
			if self.simplex[i][c]<=0: continue
			tmp = self.simplex[i][-1]/self.simplex[i][c]
			# if ft(0) < tmp < tmp_min:
			if ft(0) <= tmp < tmp_min:
				tmp_min = tmp
				row = i
		if self.debug: print '- row pivot: ', float(tmp_min)
		return row

	# scale a row given scalar
	def scale_row(self, r, s):
		for i in range(len(self.simplex[r])):
			self.simplex[r][i] = self.simplex[r][i]/s

	# apply linear transform on r2 given r1 and parameter
	def linear_row(self, r2, r1, p):
		for i in range(len(self.simplex[r2])):
			self.simplex[r2][i] = self.simplex[r1][i]*p+self.simplex[r2][i]

	# make a basic variable given pivot row and column
	def make_basic(self, r, c):
		for i in range(self.n_ele+2):
			if i==r or self.simplex[i][c]==0: continue
			self.linear_row(i,r,-self.simplex[i][c])
		# update basic variable indicator
		self.bv[r] = c


	# run simplex algorithm given the objective function row
	def run_simplex(self, obj_r):
		# for the first objective function, check both x and a
		if obj_r==-2: c = self.get_pc(obj_r,self.n_mix+self.n_ele)
		# for the second objective function, check only x
		else: c = self.get_pc(obj_r,self.n_mix)
		# exit loop when all indicators are non-negative (get_pc return -1)
		while c!=-1:
			# get pivot row, return -1 if no found which indicates no feasible solution
			r = self.get_pr(c)
			if r==-1: return False
			if self.debug: print '- pivot:', r, c
			# make the pivot a basic variable by scale it to 1 and other rows to 0
			if self.simplex[r][c]!=1:
				self.scale_row(r,self.simplex[r][c])
			self.make_basic(r,c)
			self.print_matrix()
			if obj_r==-2: c = self.get_pc(obj_r,self.n_mix+self.n_ele)
			else: c = self.get_pc(obj_r,self.n_mix)
		if self.debug:
			for idx,val in enumerate(self.bv):
				if val in range(self.n_mix): print 'x'+str(val+1)+'=%.2f'%float(self.simplex[idx][-1]),
				else: print 'a'+str(val+1-self.n_mix)+'=%.2f'%float(self.simplex[idx][-1]),
				print ''
		return True

	def check_feasibility(self):
		if not self.run_simplex(-2): return False
		# check RHS of the objective function row
		if self.debug: print 'W-RHS: ', float(self.simplex[-2][-1])
		if self.simplex[-2][-1]>=0: return True
		else: return False

	def optimize(self):
		if not self.run_simplex(-1): return float(-1)
		return -float(self.simplex[-1][-1])

	def mix(self, mixture, availableMixtures):
		self.pre_processing(mixture, availableMixtures)
		if not self.check_feasibility():
			return float(-1)
		else:
			return self.optimize()

if __name__ == '__main__':
	in_1 = (6, 9, 8, 7, 8, 8, 8, 8)
	in_2 = ("1 10 9 7 9 6 9 9 2",
					"6 8 9 5 7 5 8 6 4",
					"4 10 5 9 0 3 9 5 7",
					"9 2 0 8 3 6 9 6 2",
					"9 7 4 0 1 9 1 4 4",
					"3 3 1 2 0 4 9 7 7",
					"8 2 2 5 9 8 3 2 0",
					"3 0 1 2 0 10 3 7 6",
					"7 6 6 10 6 5 4 2 4",
					"9 0 4 8 4 1 3 4 2")
	m = Mixture()
	print '%.16f'%m.mix(in_1,in_2)
	# 3.2867029787581328
	in_1 = (6, 7, 9, 10, 10, 9, 7, 10)
	in_2 = ("5 7 0 7 1 4 9 10 9", "9 10 1 3 7 10 5 7 7", "7 3 7 2 9 10 1 8 10", "4 5 2 9 5 3 8 7 6", "0 4 6 10 8 7 2 1 0", "2 2 7 6 9 2 1 5 7", "1 1 10 10 0 5 8 8 5", "1 8 3 3 8 0 4 2 9", "3 1 5 10 2 10 1 4 1", "10 0 4 1 10 8 10 10 8")
	m = Mixture()
	print '%.15f'%m.mix(in_1,in_2)
	# # 10.489921734948188
	in_1 = (1,2,3)
	in_2 = ("1 0 0 1","0 1 0 2","0 0 1 3")
	m = Mixture()
	print m.mix(in_1,in_2)
	in_1 = (1,2,3)
	in_2 = ("1 0 0 1","0 1 0 2","0 0 1 3","2 2 2 4")
	m = Mixture()
	print m.mix(in_1,in_2)
	in_1 = (7,7,8,10)
	in_2 = ("9 0 4 8 4","8 8 9 0 1","0 10 3 10 7","10 2 2 0 1","8 9 10 2 6",
				"1 2 5 8 8","4 7 8 9 6","2 10 6 8 10","6 3 9 7 1","3 6 9 9 1")
	m = Mixture()
	print m.mix(in_1,in_2)
	in_1 = (1,1,1,1,1,1,1,1,1,1)
	in_2 = ("10 9 9 9 9 9 9 9 9 10 0",
					"0 10 9 9 9 9 9 9 9 0 0",
					"0 0 10 9 9 9 9 9 9 0 0",
					"0 0 0 10 9 9 9 9 9 0 0",
					"0 0 0 0 10 9 9 9 9 0 0",
					"0 0 0 0 0 10 9 9 9 0 0",
					"0 0 0 0 0 0 10 9 9 0 0",
					"0 0 0 0 0 0 0 10 9 0 0",
					"0 0 0 0 0 0 0 0 10 1 0",
					"0 0 0 0 0 0 0 0 0 10 1")
	m = Mixture()
	print m.mix(in_1,in_2)
	in_1 = (6, 6, 8, 6, 4, 6, 5)
	in_2 = ("6 4 1 5 4 6 2 2", "9 9 9 1 2 0 1 9", "10 4 3 0 0 2 2 10", "7 9 6 0 9 9 8 5", "6 7 8 2 7 8 4 0", "3 2 7 7 1 7 10 1", "9 4 5 9 3 10 2 8", "7 3 8 2 10 1 2 3", "10 4 3 3 8 7 2 1", "3 6 9 10 5 8 8 5")
	m = Mixture()
	print m.mix(in_1,in_2)
	in_1 = (7, 7, 4, 8, 7, 7, 6)
	in_2 = ("9 7 6 2 2 6 10 6", "4 3 1 8 8 7 0 5", "4 4 7 5 6 1 3 2", "8 1 1 2 7 9 10 5", "10 3 2 2 0 4 7 8", "0 3 3 7 10 3 4 7", "0 5 1 8 1 3 10 7", "7 3 7 2 2 1 3 8", "6 7 10 6 9 1 1 1", "3 10 2 3 3 4 6 2")
	m = Mixture()
	print m.mix(in_1,in_2)
	in_1 = (7, 5, 2, 2, 2, 6, 7)
	in_2 = ("9 2 0 9 1 8 8 6", "10 8 3 7 4 0 7 6", "7 2 2 9 2 10 2 3", "10 8 10 10 0 3 3 3", "1 10 1 6 8 4 7 0", "10 5 2 1 0 9 10 1", "4 4 8 2 0 7 0 10", "9 7 5 3 1 8 10 7", "9 5 4 0 10 3 1 3", "0 4 1 5 3 4 8 9")
	m = Mixture()
	print '%.16f' % m.mix(in_1,in_2)

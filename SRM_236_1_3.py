__author__ = 'ray'
# problem url: https://community.topcoder.com/stat?c=problem_statement&pm=3530

import sys
from collections import deque

class Parking:
	def __init__(self):
		self.park = ()
		self.r = 0 # number of row
		self.c = 0 # number of column
		self.nc = 0 # number of car
		self.nl = 0 # number of lot
		self.car = [] # position of cars
		self.lot = [] # position of parking lots
		self.graph = [] # distance from cars to lots
		self.visited = [] # flag of visited lots
		self.limit = 0 # limit of distance from car to lot
		self.max_dis = -sys.maxint-1
		self.min_dis = sys.maxint
		self.limit = 0
		self.mat_c = [] # matched car
		self.mat_l = [] # matched lot
		self.tree = [] # tree of current augmentation
		self.lot_t = [] # flag if a lot is in tree

	def pre_processing(self, park):
		self.park = park
		self.r = len(park)
		self.c = len(park[0])
		for i in range(0,self.r):
			for j in range(0,self.c):
				if park[i][j]=='C':
					self.nc += 1
					self.car.append((i,j))
				if park[i][j]=='P':
					self.nl += 1
					self.lot.append((i,j))
		self.graph = [ [-1]*self.nl for _ in range(self.nc) ]


	def dijkstra(self):
		for c in range(0,self.nc):
			dq = deque([(self.car[c][0],self.car[c][1],0)])
			visited = [ [False]*self.c for _ in range(self.r) ]
			visited[self.car[c][0]][self.car[c][1]] = True
			n_l = 0 # number of lots being detected
			while len(dq)>0:
				(x,y,d) = dq.popleft()
				for (i,j) in ((-1,0),(1,0),(0,-1),(0,1)):
					nx = x+i
					ny = y+j
					nd = d+1
					if nx<0 or nx>=self.r or ny<0 or ny>=self.c: continue
					if visited[nx][ny]: continue
					else: visited[nx][ny] = True
					if self.park[nx][ny]=='X': continue
					elif self.park[nx][ny]=='P':
						self.graph[c][self.lot.index((nx,ny))] = nd
						if nd>self.max_dis: self.max_dis=nd
						if nd<self.min_dis: self.min_dis=nd
						n_l += 1
					dq.append((nx,ny,nd))
				if n_l==self.nl: break

	# def dfs(self, c):
	# 	if c==self.nc:
	# 		return True
	# 	for l in range(0,self.nl):
	# 		dis = self.graph[c][l]
	# 		if not self.visited[l] and dis!=-1 and dis<=self.limit:
	# 			self.visited[l] = True
	# 			if self.dfs(c+1): return True
	# 			self.visited[l] = False
	# 	return False
  #
	# def match(self, limit):
	# 	self.limit = limit
	# 	self.visited = [False]*self.nl
	# 	return self.dfs(0)

	def match(self):
		self.mat_c = [-1]*self.nc # matched lot of a car
		self.mat_l = [-1]*self.nl # matched car of a lot
		num_mat = 0 # number of matches
		# greedy initial match
		for c in range(0,self.nc):
			for l in range(0,self.nl):
				if self.mat_l[l]==-1 and 0<self.graph[c][l]<=self.limit:
					self.mat_c[c] = l
					self.mat_l[l] = c
					num_mat += 1
					break
		# augmentation
		while self.nc - num_mat > 0:
			self.lot_t = [False]*self.nl
			aug_found = False
			for c in range(0,self.nc):
				self.tree = []
				if self.mat_c[c]!=-1: continue
				self.tree.append(c)
				if self.find_aug(c):
					while len(self.tree)>0:
						tmp_l = self.tree.pop()
						tmp_c = self.tree.pop()
						self.mat_l[tmp_l] = tmp_c
						self.mat_c[tmp_c] = tmp_l
					num_mat += 1
					aug_found = True
					break
			if not aug_found: break
		if num_mat==self.nc: return True
		else: return False

	def find_aug(self, c):
		# loop all lots
		for l in range(0,self.nl):
			# continue if the lot is already in tree
			if self.lot_t[l]: continue
			# continue if the lot is not accessible
			if self.graph[c][l]<0 or self.graph[c][l]>self.limit: continue
			self.lot_t[l] = True
			# if the lot is not-matched
			if self.mat_l[l]==-1:
				self.tree.append(l)
				return True
			# if the lot is matched
			else:
				mc = self.mat_l[l]
				self.tree.append(l)
				self.tree.append(mc)
				if self.find_aug(mc): return True
				else:
					self.tree.pop()
					self.tree.pop()
		# return false if no augmenting path found
		return False

	def minTime(self, park):
		self.pre_processing(park)
		if self.nc > self.nl:
			return -1
		if self.nc == 0:
			return 0
		self.dijkstra()
		self.limit = self.max_dis
		if not self.match(): return -1
		l,r = self.min_dis-1, self.max_dis
		while r-l>1:
			self.limit = (l+r)/2
			if self.match(): r=self.limit
			else: l=self.limit
		return r


if __name__ == '__main__':
	p = Parking()
	_in = ("C.....P",
				 "C.....P",
				 "C.....P")
	print p.minTime(_in)
	p = Parking()
	_in = ("C.X.....",
				 "..X..X..",
				 "..X..X..",
				 ".....X.P")
	print p.minTime(_in)
	p = Parking()
	_in = ("PPPPPPPPPPCCCCCCCCCC",
				 "PPPPPPPPPPCCCCCCCCCC",
				 "PPPPPPPPPPCCCCCCCCCC",
				 "PPPPPPPPPPCCCCCCCCCC",
				 "PPPPPPPPPPCCCCCCCCCC",
				 "PPPPPPPPPPCCCCCCCCCC",
				 "PPPPPPPPPPCCCCCCCCCC",
				 "PPPPPPPPPPCCCCCCCCCC",
				 "PPPPPPPPPPCCCCCCCCCC",
				 "PPPPPPPPPPCCCCCCCCCC")
	print p.minTime(_in)
	p = Parking()
	_in = ("..X..",
				 "C.X.P",
				 "..X..")
	print p.minTime(_in)
	p = Parking()
	_in = ("XXXXXXXXXXX",
				 "X......XPPX",
				 "XC...P.XPPX",
				 "X......X..X",
				 "X....C....X",
				 "XXXXXXXXXXX")
	print p.minTime(_in)
	p = Parking()
	_in = ("....................................C...",
				 "...........C............P.......P.......",
				 "....C..........P....C......C........P...",
				 ".........X.....................XX.......",
				 "...C........P....X.....P........X.......",
				 ".........X.......X......C...............",
				 "........X...C....X..C.........X.....C...",
				 "..P.........................X....X....P.",
				 "..................X.......X......X......",
				 "C.....X..P...P..X......C.....P..........",
				 "..P...X.......X..........X.........X....",
				 "............X............X.....X.X....P.",
				 "......X...........C......X..C...........",
				 "........X..X.....P................P.....",
				 "......P...XX............X.....P.X.......",
				 "...C..................X.......P.X....C..",
				 ".....P..C...XX......X....C......X.......",
				 "............X..X..X.............X.......",
				 "......X...X..............C....X.........",
				 "....X...X.........X.........X.......P...",
				 "...X............X....X..................",
				 "..X......XX.X.X........X..X......C......",
				 "......C.........P........X.............C",
				 "...................P........P...........")
	print p.minTime(_in)

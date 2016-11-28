__author__ = 'ray'
# problem url: https://community.topcoder.com/stat?c=problem_statement&pm=14131

# The restaurant has infinitely many chairs, arranged in a single long row, numbered using positive integers: 1,2,3...
# There is a universal constant d, whenever two bears sit on chairs, their chair numbers must differ by d or more.
# For example, if d=10, you can have two bears in chairs 47 and 57, but you cannot have bears in chairs 47 and 56.
# Given an array "atLeast" with N integers, for each i from 0 to N-1, guest i want his chair number greater than or equal to atLeast[i].
# When seating a guest, always assigns them the smallest available chair number.
# Return an array with N elements: for each guest, in the order in which they arrived, the number of the chair where they will be seated.

# A general fact being observed is that seats are all available at the begining, and turn into unavailable when new bear comes.
# We can flag unavailable seats with a list of intervals. E,g, [(1,3),(6,8)] means seat 1,2,3,6,7,8 are unavailable.
# For each new guest coming with an at_least request, binary search to get the interval it is in or right on its left.
# Update the intervals list after each chair assignment, the search time for each bear is log(n), thus n*log(n) for all bears.
# It would save some time to use rb-tree instead of regular array for storing intervals, if the number of guest is large.
# For simplicity reason I didn't implement rb-tree, but it still pass all tests.

class Interval(object):
  def __init__(self, b, e):
    self.beg = b
    self.end = e
    return

class BearChairs(object):
  def __init__(self):
    # distance received from input
    self.dis = 0
    # intervals of unavailable positions, contains a list of (beg,end)
    # e.g. (5,15) means chairs with index 5-15 are unavailable
    # initialize with infinities to take care of corner cases
    self.intervals = [Interval(float('-inf'),float('-inf')),Interval(float('inf'),float('inf'))]
    # initialize result container
    self.result = []
    return

  def findPositions(self, atLeast, d):
    n = len(atLeast)
    if n<2: return atLeast
    self.dis = d
    for at_least in atLeast:
      self.add_bear(at_least)
    return tuple(self.result)

  def add_bear(self, at_least):
    # binary search for the largest interval beg that is smaller than at_least
    lt, rt = 0, len(self.intervals) - 1
    while lt < rt:
      mid = lt+(rt-lt+1)/2
      val = self.intervals[mid].beg
      if val <= at_least:
        lt = mid
      else:
        rt = mid-1
    # at this point lt==rt
    # let lt and rt be indexes of two adjacent intervals
    rt = lt+1
    # position for this bear
    # if at_least falls in left interval, give him the position right next to the left interval
    # otherwise give him the position indicated by at_least
    pos = max(at_least,self.intervals[lt].end+1)
    self.result.append(pos)
    # update intervals container
    # four possible scenarios here:
    # - insert new interval
    # - merge with both left and right intervals
    # - merge with left interval only
    # - merge with right interval only
    pos_beg,pos_end = pos-self.dis+1,pos+self.dis-1
    lt_overlap = self.intervals[lt].end>=pos_beg-1
    rt_overlap = self.intervals[rt].beg<=pos_end+1
    if lt_overlap and rt_overlap:
      # merge with both left and right intervals
      self.intervals[lt].end = self.intervals[rt].end
      del self.intervals[rt]
    elif lt_overlap:
      # merge with left interval only
      self.intervals[lt].end = pos_end
    elif rt_overlap:
      # merge with right interval only
      self.intervals[rt].beg = pos_beg
    else:
      # insert new interval
      self.intervals.insert(rt, Interval(pos_beg,pos_end))
    return


if __name__ == '__main__':
  # _in_1 = (1,21,11,7)
  # _in_2 = 11
  # _in_1 = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
  # _in_2 = 1000000
  _in_1 = (173, 66, 107, 171, 193, 224, 240, 95, 143, 98, 192, 165, 203, 97, 209, 124, 80, 36, 60, 60, 238, 166, 163, 36, 108, 221, 68, 54, 59, 48, 101, 198, 80, 183, 128, 32, 166, 127, 93, 60, 191, 45, 191, 154, 108, 159, 29, 155, 161, 63, 181, 159, 204, 103, 161, 63, 83, 195, 83, 108, 217, 159, 65, 57, 101, 159, 63, 233, 46, 131)
  _in_2 = 6
  s = BearChairs()
  print s.findPositions(_in_1, _in_2)
  # {1, 21, 11, 31 }

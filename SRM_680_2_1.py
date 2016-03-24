__author__ = 'ray'

class BearPair(object):
  def bigDistance(self, s):
    n = len(s)
    if n<2: return -1
    mi = [-1]*26
    mx = [-1]*26
    for i in xrange(n):
      idx = ord(s[i])-ord('a')
      if mi[idx]==-1:
        mi[idx] = i
      mx[idx] = i
    _max = 0
    for i in xrange(26):
      for j in xrange(26):
        if i!=j and mi[j]!=-1 and mx[i]-mi[j]>_max:
          _max = mx[i]-mi[j]
    if _max: return _max
    else: return -1


if __name__ == '__main__':
  _in_1 = "bear"
  # _in_2 = [3,5,7,11,19,23,29,41,43,47]
  s = BearPair()
  print s.bigDistance(_in_1)

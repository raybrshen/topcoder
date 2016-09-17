__author__ = 'ray'
# problem url: https://community.topcoder.com/stat?c=problem_statement&pm=14130

# Given a string, find two integers i and j with the following properties:
#   - both i and j must be valid indices into s
#   - the characters s[i] and s[j] must be different
#   - the difference between i and j must be as large as possible

# The fact that i and j contains at least one of the end index (either the left-most or right-most) is not obvious.
# But it can be proved by reduction of absurdity.
# If i and j are both not end index (call them 0 and n-1)
#   - we can infer that s[0] equal to s[n-1], otherwise i and j would be 0 and n-1, and produce the largest possible difference
#   - now derive the problem into two cases:
#     - if s[i]==s[n-1]
#       - also infers that s[i]==s[0], since s[n-1]==s[0]
#       - contradiction, because (0 and j) will produce larger difference than (i and j)
#     - if s[i]!=s[n-1]
#       - contradiction, because (i and n-1) will produce larger difference than (i and j)
# Thus, the solution is to be greedy.
#   - going from right-most, find the character that differs from the left-most character, get the distance
#   - going from left-most, find the character that differs from the right-most character, get the distance
# Return the larger distance between them.

class BearPair(object):
  def bigDistance(self, s):
    n = len(s)
    if n<2: return -1
    maxi = -1
    for i in xrange(n-1,0,-1):
        if s[i]!=s[0]: break
    if i!=0: maxi=i
    else: return maxi
    for i in xrange(0,n-1,1):
        if s[i]!=s[n-1]: break
    if (i!=n-1): maxi=max(maxi,n-1-i)
    return maxi


if __name__ == '__main__':
  _in_1 = "bear"
  # _in_2 = [3,5,7,11,19,23,29,41,43,47]
  s = BearPair()
  print s.bigDistance(_in_1)

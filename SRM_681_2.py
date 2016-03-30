__author__ = 'ray'
# problem url: https://community.topcoder.com/stat?c=problem_statement&pm=14114

class CoinFlipsDiv2:
    def countCoins(self, state):
        n = len(state)
        if n<2: return 0
        ret = 0
        for i in xrange(n):
            if (i>0 and state[i]!=state[i-1]) or (i<n-1 and state[i]!=state[i+1]):
                ret += 1
        return ret

# from collections import defaultdict
# class ExplodingRobots:
#     def canExplode(self, x1, y1, x2, y2, instructions):
#         dic = defaultdict(int)
#         for i in instructions: dic[i] += 1
#         hori,verti = abs(x1-x2),abs(y1-y2)
#         if dic['U']+dic['D']>=verti and dic['L']+dic['R']>=hori:
#             return 'Explosion'
#         else:
#             return 'Safe'
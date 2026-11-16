# N-QUEENS PROBLEM
# fit n Queens in n x n grid
# =======================================
# heuristic: h(s) = # of attacking pairs.
# action: move ONE queen to another row.
# algorithim: local search
#
# example: 0 = empty Q = queen
#
#      0 1 2 3 
#
#  0   0 0 0 Q                       
#  1   Q Q 0 0          h = 2 becuase there are 2 AP(attacking pairs).
#  2   0 0 0 0              AP =  { {(0,1), (1,1)}, {(0,1), (2,3)} }
#  3   0 0 Q 0 
#
# ======================================== 

import random;
seed = int(input("seed: "))
random.seed(seed)
n = int(input("n: "))

def tostring(s):                         # replace empty strings with spaces
    ret = []
    def f(_):
        if _ == '' : return '.'
        else: return _
    for r in s:
        r = [f(_) for _ in r]
        ret.append(''.join(r))
    return '\n'.join(ret)

def random_state(n):
    s = [['' for _ in range(n)] for _ in range(n)]  # n x n of empty strings
    for c in range(n):                              # for each coloumn choose:
        r = random.randrange(n)                     # random row
        s[r][c] = 'Q'                               # place queen
    return s
    
def h(s):
    n = len(s)
    r = [0 for _ in range(n)]   # r[0] is the row of Q at column 0
    for c in range(n):
        for i in range(n):
            if s[i][c] == 'Q':
                r[c] = i
                break

    for i,c in enumerate(r):
        print(i, c)

   # increment h by 1 if
   # r[c0] == r[c1] or
   # c1 - c0 == r[c1] - r[c0]
   # c1 = c0 == -(r[c1] - r[c0])

if __name__ == '__main__':
    s = random_state(n)
    print(tostring(s))
    print("h = ", h(s))




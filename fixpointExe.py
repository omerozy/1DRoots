import math
from fixpoint import fixpoint

# Inputs
def g(x):
    y = math.exp(-x)    # formula for predicitng the root
    return y            # rearrange your objective function f(x) such that x = g(x) either by algebraic manipulation or by simply adding x to both sides      

xR = 0 # initial guess

errLim = 10**-5 # error limit

maxIterNum = 100 # maximum number of iterations

# Execution of method
p = fixpoint(g, xR, errLim, maxIterNum)
p.exec()
p.result()
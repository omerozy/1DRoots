import math

# Inputs
def g(x):
    y = math.exp(-x)    # formula for predicitng the root
    return y                # rearrange your objective function f(x) such that x = g(x) either by algebraic manipulation or by simply adding x to both sides      

xR = 0 # initial guess

errLim = 10**-5 # error limit

maxIterNum = 100 # maximum number fo iterations

# Execution of method
solFound = False
for iterIdx in range(maxIterNum):
    xROld = xR
    xR = g(xROld)
    if xR != 0:
        err = abs((xR - xROld)/xR)
    if err < errLim:
        solFound = True
        break

if solFound:
    print("\nSolution was found as " + str(xR) + " with error " + str(err) + " after " + str(iterIdx + 1) + " iterations.\n")
else:
    print("\nSolution could not be found after specified number of iterations.\n")
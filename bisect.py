import sys

# Inputs
xL = 3 # lower guess for root   # Note: Select lower and upper guesses such that xL < xR and f(xL)*f(xU) < 0
xU = 9 # upper guess for root

errLim = 10**-5 # solution error limit for stopping execution

maxIterNum = 100 # maximum number of iterations

def f(x):
    y = x**2 - 15*x + 50 # define objective function here
    return y

# Check if conditions are met for execution
if not xL < xU:
    sys.exit("Method condition is not satisfied: Lower guess input shoule be lower than upper guess input.")
elif not f(xL)*f(xU) < 0:
    sys.exit("Method condition is not satisfied: Product of function outputs at two guesses shoule be less than 0.")

# Execution of method
solFound = False
fL = f(xL)
for iterIdx in range(maxIterNum):
    xR = (xL + xU)/2 # estimate root as the middle of interval
    fR = f(xR)
    if abs(fR) < errLim:
        solFound = True
        break
    elif fL*fR < 0: # root lies in lower subinterval
        xU = xR
    elif fL*fR > 0: # root lies in upper subinterval
        xL = xR
        fL = fR

if solFound:
    print("\nSolution was found as " + str(xR) + " after " + str(iterIdx + 1) + " iterations.\n")
else:
    print("\nSolution could not be found after specified number of iterations.\n")
from falpos import falpos

# Inputs
xL = 3 # lower guess for root   # Note: Select lower and upper guesses such that xL < xR and f(xL)*f(xU) < 0
xU = 9 # upper guess for root

errLim = 10**-5 # solution error limit for stopping execution

maxIterNum = 100 # maximum number of iterations

def f(x):
    y = x**2 - 15*x + 50 # define objective function here
    return y

p = falpos(f, xL, xU, errLim, maxIterNum)
p.check()
p.exec()
p.result()
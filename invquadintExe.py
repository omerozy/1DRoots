from invquadint import invquadint

# Inputs
xR = 3 # initial root guess

xRb = 3.5 # other two point for polynomial interpolation
xRb2 = 3.6

errLim = 10**-5 # solution error limit for stopping execution

maxIterNum = 100 # maximum number of iterations

def f(x):
    y = x**2 - 15*x + 50 # define objective function here
    return y

# Execution of method
p = invquadint(f, xR, xRb, xRb2, errLim, maxIterNum)
p.exec()
p.result()
p.plotIter()
from newraph import newraph

# Inputs
xR = 3 # initial root guess

errLim = 10**-5 # solution error limit for stopping execution

maxIterNum = 100 # maximum number of iterations

def f(x):
    y = x**2 - 15*x + 50 # define objective function here
    return y

def df(x):
    dy = 2*x - 15 # define the dreivaitve of objective function here
    return dy

# Execution of method
p = newraph(f, df, xR, errLim, maxIterNum)
p.exec()
p.result()
p.plotIter()
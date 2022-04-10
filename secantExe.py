from secant import secant

# Inputs
xR = 3 # initial root guess

class method:
    methodCase = 1 # method for derivative calculation, 0 for using two arbitrary values or 1 for a fractional perturbation of the independent variable
    match methodCase:
        case 0:
            xRb = 3.5
        case 1:
            dx = 0.005 

errLim = 10**-5 # solution error limit for stopping execution

maxIterNum = 100 # maximum number of iterations

def f(x):
    y = x**2 - 15*x + 50 # define objective function here
    return y

# Execution of method
p = secant(f, xR, method, errLim, maxIterNum)
p.exec()
p.result()
p.plotIter()
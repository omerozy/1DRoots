import matplotlib.pyplot as plt
import numpy as np

# Inputs
xR = 3 # initial root guess
method = 1 # method for derivative calculation, 0 for using two arbitrary values or 1 for a fractional perturbation of the independent variable

match method:
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
fR = f(xR)
xRHist = [xR]
fRHist = [fR]
if method == 0:
    fRb = f(xRb)
solFound = False
for iterIdx in range(maxIterNum):
    print(iterIdx)
    match method:
        case 0:
            dfR = (fRHist[-1]-fRb)/(xRHist[-1] - xRb)
        case 1:
            dfR = (f(xRHist[-1] + dx) - fRHist[-1])/dx
    xR = xRHist[-1] - fRHist[-1]/dfR
    fR = f(xR)
    xRb = xRHist[-1]
    fRb = fRHist[-1]
    xRHist.append(xR)
    fRHist.append(fR)
    if xR != 0:
        err = abs((xRHist[-1] - xRHist[-2])/xRHist[-1])
    if err < errLim:
        solFound = True
        break

if solFound:
    print("\nSolution was found as " + str(xR) + " with error " + str(err) + " after " + str(iterIdx + 1) + " iterations.")
    print("f(" + str(xR) + ") = " + str(f(xR)))
    print("\n")
else:
    print("\nSolution could not be found after specified number of iterations.\n")

# PLot iterations
xRHist = np.array(xRHist)
fRHist = np.array(fRHist)
xSample = np.linspace(xRHist[0], xRHist[-1], 100)
fSample = f(xSample)

plt.axhline(y=0, color='k')
plt.plot(xRHist, fRHist, "ro")
plt.plot(xSample, fSample, "b")
plt.quiver(xRHist[0:-2], fRHist[0:-2], np.subtract(xRHist[1:-1], xRHist[0:-2]), np.subtract(fRHist[1:-1], fRHist[0:-2]), angles='xy', scale_units='xy', scale=1)
plt.show()
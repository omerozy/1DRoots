import matplotlib.pyplot as plt
import numpy as np

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
fR = f(xR)
xRHist = [xR]
fRHist = [fR]
solFound = False
for iterIdx in range(maxIterNum):
    xR = xRHist[-1] - fRHist[-1]/df(xRHist[-1])
    fR = f(xR)
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
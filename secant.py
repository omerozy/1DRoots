import matplotlib.pyplot as plt
import numpy as np

class secant:
    def __init__(self, f, xR, method, errLim, maxIterNum):
        self.f = f
        self.xR = xR
        self.errLim = errLim
        self.maxIterNum = maxIterNum
        self.method = method
    
    def exec(self):
        fR = self.f(self.xR)
        xRHist = [self.xR]
        fRHist = [fR]
        if self.method.methodCase == 0:
            fRb = self.f(xRb)
        solFound = False
        for iterIdx in range(self.maxIterNum):
            match self.method.methodCase:
                case 0:
                    dfR = (fRHist[-1]-fRb)/(xRHist[-1] - xRb)
                case 1:
                    dfR = (self.f(xRHist[-1] + self.method.dx) - fRHist[-1])/self.method.dx
            xR = xRHist[-1] - fRHist[-1]/dfR
            fR = self.f(xR)
            xRb = xRHist[-1]
            fRb = fRHist[-1]
            xRHist.append(xR)
            fRHist.append(fR)
            if xR != 0:
                err = abs((xRHist[-1] - xRHist[-2])/xRHist[-1])
            if err < self.errLim:
                solFound = True
                break
        self.xRHist = xRHist
        self.fRHist = fRHist
        self.solFound = solFound
        self.xR = xR
        self.err = err
        self.iterNum = iterIdx + 1
    def result(self):
        if self.solFound:
            print("\nSolution was found as " + str(self.xR) + " with error " + str(self.err) + " after " + str(self.iterNum) + " iterations.")
            print("f(" + str(self.xR) + ") = " + str(self.f(self.xR)))
            print("\n")
        else:
            print("\nSolution could not be found after specified number of iterations.\n")

    def plotIter(self): # PLot iterations
        xRHist = np.array(self.xRHist)
        fRHist = np.array(self.fRHist)
        xSample = np.linspace(xRHist[0], xRHist[-1], 100)
        fSample = self.f(xSample)

        plt.axhline(y=0, color='k')
        plt.plot(xRHist, fRHist, "ro")
        plt.plot(xSample, fSample, "b")
        plt.quiver(xRHist[0:-2], fRHist[0:-2], np.subtract(xRHist[1:-1], xRHist[0:-2]), np.subtract(fRHist[1:-1], fRHist[0:-2]), angles='xy', scale_units='xy', scale=1)
        plt.show()
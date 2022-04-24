import matplotlib.pyplot as plt
import numpy as np

class invquadint:
    def __init__(self, f, xR, xRb, xRb2, errLim, maxIterNum):
        self.f = f
        self.xR = xR
        self.xRb = xRb
        self.xRb2 = xRb2
        self.errLim = errLim
        self.maxIterNum = maxIterNum
    
    def exec(self):
        xR = self.xR
        xRb = self.xRb
        xRb2 = self.xRb2
        fR = self.f(xR)
        fRb = self.f(xRb)
        fRb2 = self.f(xRb2)
        xRHist = [xR]
        fRHist = [fR]
        solFound = False
        for iterIdx in range(self.maxIterNum):
            xR = fRb*fR*xRb2/((fRb2 - fRb)*(fRb2 - fR)) + fRb2*fR*xRb/((fRb - fRb2)*(fRb - fR)) + fRb2*fRb*xR/((fR - fRb2)*(fR - fRb))
            fR = self.f(xR)
            xRb2 = xRb
            fRb2 = fRb
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
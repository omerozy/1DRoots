import math

class fixpoint:
    def __init__(self, g, xR, errLim, maxIterNum):
        self.g = g
        self.xR = xR
        self.errLim = errLim
        self.maxIterNum = maxIterNum

    def exec(self):
        self.solFound = False
        xR = self.xR
        for iterIdx in range(self.maxIterNum):
            xROld = xR
            xR = self.g(xROld)
            if xR != 0:
                err = abs((xR - xROld)/xR)
            if err < self.errLim:
                self.solFound = True
                break
        self.err = err
        self.xR = xR
        self.iterNum = iterIdx + 1

    def result(self):
        if self.solFound:
            print("\nSolution was found as " + str(self.xR) + " with error " + str(self.err) + " after " + str(self.iterNum) + " iterations.\n")
        else:
            print("\nSolution could not be found after specified number of iterations.\n")
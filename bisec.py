import sys

class bisec:
    def __init__(self, objFunc, xL, xU, errLim, maxIterNum):
        self.xL = xL
        self.xU = xU
        self.errLim = errLim
        self.maxIterNum = maxIterNum
        self.objFunc = objFunc

    def check(self):    # Check if conditions are met for execution
        if not self.xL < self.xU:
            sys.exit("Method condition is not satisfied: Lower guess input should be lower than upper guess input.")
        elif not self.objFunc(self.xL)*self.objFunc(self.xU) < 0:
            sys.exit("Method condition is not satisfied: Product of function outputs at two guesses should be less than 0.")

    def exec(self):
        self.solFound = False
        xL = self.xL
        xU = self.xU
        fL = self.objFunc(xL)
        for iterIdx in range(self.maxIterNum):
            xR = (xL + xU)/2 # estimate root as the middle of interval
            fR = self.objFunc(xR)
            test = fL*fR
            self.err = abs(fR)
            if self.err < self.errLim:
                self.solFound = True
                break
            elif test < 0: # root lies in lower subinterval
                xU = xR
            elif test > 0: # root lies in upper subinterval
                xL = xR
                fL = fR
        self.iterNum = iterIdx + 1
        self.xR = xR

    def result(self):
        if self.solFound:
            print("\nSolution was found as " + str(self.xR) + " with error " + str(self.err) + " after " + str(self.iterNum) + " iterations.\n")
        else:
            print("\nSolution could not be found after specified number of iterations.\n")
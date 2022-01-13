from functions import log
from sys import print_exception


class HandleException:

    def __init__(self):
        log("Initializing exception handler...")
        self.exceptionCount = 0

    def handleException(self, exception, description, showDescription, showException, increaseExceptionCount):
        if showDescription:
            log(description)

        if showException:
            print_exception(exception)

        if increaseExceptionCount:
            self.addToExceptionCount()

    def addToExceptionCount(self):
        self.exceptionCount = self.exceptionCount + 1

    def resetExceptionCount(self):
        self.exceptionCount = 0

    def getExceptionCount(self):
        return self.exceptionCount

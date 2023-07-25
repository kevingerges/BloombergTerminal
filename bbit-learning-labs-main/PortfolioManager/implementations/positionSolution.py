#Uncomment line above & run cell to save solution
#TODO Define class that implements positionInterface & allows for the management of a position

# import pytest
# import implementations.positionSolution
# from implementations.securitySolution import security
# from generators.positionDataGenerator import positionUpdates



import os
import sys
module_path = os.path.abspath('..')
if module_path not in sys.path:
    sys.path.append(module_path)

from generators.positionDataGenerator import positionUpdates
positionUpdates
posUpdater = positionUpdates()

#Check if there is an available position update
if posUpdater.isNextAvailable():
    #Get the current position update value
    print(posUpdater.getNextTransaction())

#Return the list of all positions update generated
posList = posUpdater.getTransactionList()


from implementations.securitySolution import security
from interfaces.positionInterface import positionInterface
from interfaces.securityInterface import securityInterface


class position(positionInterface):
    def __init__(self, security_name, initialPosition: int) -> None:
        super().__init__(security_name, initialPosition)
        self.initialPosition = initialPosition

        if isinstance(security_name, securityInterface):
            self.security_name = security_name
        else:
            self.security_name = security(security_name)
        
    def getSecurity(self) -> securityInterface:
        return self.security_name

    def getPosition(self) -> int:
        return self.initialPosition

    def setPosition(self, inputValue: int) -> None:
        if inputValue > 0:
            self.initialPosition = inputValue
            print("input value is valid")
        else:
            raise Exception('error')
    
    def addPosition(self, inputValue: int) -> None:
        if inputValue + self.initialPosition < 0:
               raise Exception('error')
        else:
            self.initialPosition += inputValue

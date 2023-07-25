#Uncomment line above & run cell to save solution
#TODO Define class that implements accountInterface & allows for the management of an account

import os
import sys
module_path = os.path.abspath('..')
if module_path not in sys.path:
    sys.path.append(module_path)

from interfaces.accountInterface import accountInterface
from interfaces.portfolioInterface import portfolioInterface
from interfaces.positionInterface import positionInterface
from interfaces.securityInterface import securityInterface

from typing import Any, Dict, Set, Iterable

class account(accountInterface):
    def __init__(self, positions: Set[positionInterface], accountName: str) -> None:
        super().__init__(portfolioName, accounts)
        self.m_name = portfolioName
        self.m_accounts =  {accItem.getName(): accItem for accItem in accounts}

    def getAllAccounts(self) -> Iterable[accountInterface]:
        return list(self.m_accounts.values())

    def getAccounts(self, accountNamesFilter:Set[str], securitiesFilter:Set) -> Iterable[accountInterface]:
        if (len(accountNamesFilter) == 0 and len(securitiesFilter) == 0):
            return self.getAllAccounts()
        
        if len(accountNamesFilter) != 0:
            filteredAcc = set()

            for acc in accountNamesFilter:
                if acc in self.m_accounts:
                    filteredAcc.add(self.m_accounts[acc])
        else:
            filteredAcc = set(self.m_accounts.values())

        finalSet = set()
        if len(securitiesFilter) != 0:
            for acc in filteredAcc:
                if len(acc.getPositions(securitiesFilter)) != 0:
                    finalSet.add(acc)
        else:
            finalSet = filteredAcc

        return finalSet   

    def addAccounts(self, accounts: Set[accountInterface]) -> None:
        for accounts in accounts:
            self.m_accounts[accounts.getName()] = accounts

    def removeAccounts(self, accountNames: Set[str]) -> None:
        for accName in accountNames:
            self.m_accounts.pop(accName, None)



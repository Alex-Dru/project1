from Person import *
from PhoneBook import *
from Table import *
from Node import *
from BST import *
import numpy as np

def createTestTable():
    list = []
    list.append({"First Name":"Michelle", "Last Name":"Obama"})
    list.append({"First Name":"Bruce", "Last Name":"Wayne"})
    list.append({"First Name":"Jack", "Last Name":"Nickolson"})
    list.append({"First Name":"Alex", "Last Name":"Turner"})
    list.append({"First Name":"Lewis", "Last Name":"Hamilton"})
    list.append({"First Name":"Jack", "Last Name":"Brabham"})

    return Table(list)

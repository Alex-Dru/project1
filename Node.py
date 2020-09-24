from Person import *
from PhoneBook import *
from Table import *
from Node import *
from BST import *
import numpy as np

class Node:
    def __init__(self, value, id, nextRight = None, nextLeft = None, parent = None):
        self.value = value
        self.id = id
        self.nextLeft = nextLeft
        self.nextRight = nextRight
        self.parent = parent

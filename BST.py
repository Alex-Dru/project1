from Person import *
from PhoneBook import *
from Table import *
from Node import *
from BST import *
import numpy as np

class BSTException(Exception):
    pass

class BST:

    def __init__(self, head = None):
        self.head = head

    def addNode(self, node):
        if self.head == None:  # Cas où l'arbre est vide
            self.head = node
        else:
            currentNode = self.head
            placed = False
            while placed == False:
                if node.value <= currentNode.value:
                    if currentNode.nextLeft != None:
                        currentNode = currentNode.nextLeft
                    else:
                        currentNode.nextLeft = node
                        node.parent = currentNode
                        placed = True
                else:
                    if currentNode.nextRight != None:
                        currentNode = currentNode.nextRight
                    else:
                        currentNode.nextRight = node
                        node.parent = currentNode
                        placed = True

    def affInfixe(self):
        def affInfixeRec(node) -> str:
            if node == None:
                return ""
            return str(affInfixeRec(node.nextLeft)) + " " + str(node.value) + " " + str(affInfixeRec(node.nextRight))
        return affInfixeRec(self.head)

    def searchIndex(self, value):  # Retourne l'index si la valeur est trouvée, retourne -1 sinon
        found = False
        id = -1
        currentNode = self.head
        if self.head == None:
            raise BSTException("error: no entity in the table yet")
        else:
            if currentNode.value == value:  # Cas où la valeur est dans le head
                id = currentNode.id
            else:
                while found == False:
                    if currentNode.value < value and currentNode.nextRight != None:
                        currentNode = currentNode.nextRight
                    else:
                        if currentNode.value > value and currentNode.nextLeft != None:
                            currentNode = currentNode.nextLeft
                        else:
                            if currentNode.value == value:
                                found = True
                                id = currentNode.id
                            else:
                                if currentNode.nextLeft == None and currentNode.nextRight == None:
                                    found = True
                                else:
                                    found = True
        return id

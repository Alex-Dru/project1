from Person import *
from PhoneBook import *
from Table import *
from Node import *
from BST import *
from test import *
import numpy as np

# a = Person("0612457845", "alex", "dru")
# b = Person("0614785478","Jack", "Nicolson")
# c = Person("0614782478","Michelle", "Obama")
# d = Person("0644785478","John", "Doe")
# e = Person("0614785458","John", "Lennon")
# dataPB = []
# myPB = PhoneBook(dataPB)
# myPB.addPerson(a)
# myPB.addPerson(b)
# myPB.addPerson(c)
# myPB.addPerson(d)
# myPB.addPerson(e)

# list = []
# myTable = Table(list)
# myTable.addEntity()
# myTable.addEntity()
# node1 = Node(1, 1)
# node2 = Node(9, 2)
# node3 = Node(5, 3)
# tree = BST()
# tree.addNode(node1)
# tree.addNode(node2)
# tree.addNode(node3)
# myTableTrees = []
# myTableTrees = myTable.buildAllBST()
# for arbre in myTableTrees:
#     print(arbre.affInfixeRec2(arbre.head))

tableTest = createTestTable()
# myTableTrees = tableTest.buildAllBST()
# for arbre in myTableTrees:
#     print(arbre.affInfixe())

att = tableTest.whichAtt()
tree1 = tableTest.buildBST(att)
print(tree1.affInfixe())

tableTest.reBuildBST(tree1)
print(tree1.affInfixe())

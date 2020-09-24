from Person import *
from PhoneBook import *
from Table import *
from Node import *
from BST import *
import numpy as np

class Table:
    def __init__(self, data):
        self.data = data  # Liste de Dictionnaires
                          # Un attribut de la table par case du Dictionnaire

    def printTable(self):
        for dico in self.data:
            print(dico)

    def addEntity(self):
        dico = {}
        self.data.append(dico)
        if len(self.data) == 1:    # Cas de création de la table
            finished = 0
            print("Let's start with the attributes in your table")
            print("First attribute?")
            a = str(input())
            print("Value ?")
            b = input()
            dico[a] = b
            print("Other attributes? 0 for yes, 1 for no")
            finished = int(input())
            while finished == 0:
                print("Attribute ?")
                a = str(input())
                print("Value ?")
                b = input()
                dico[a] = b
                print("Other attributes? 0 for yes, 1 for no")
                finished = int(input())
        else:        # Cas où la liste dispose déjà d'au moins un dictionnaire
              for key in self.data[0].keys():
                  print(str(key) + ":  ")
                  dico[key] = input()

    def buildAllBST(self):
        allBST = []   # liste de tous les arbres
        for att in self.data[0].keys(): # Pour chaque argument, on crée un arbre
            a = BST()
            for dico in self.data:  # Pour chacun des Dictionnaires, on ajoute l'argument 'att' dans l'arbre
                node = Node(dico[att], self.data.index(dico))
                a.addNode(node)
            allBST.append(a)
        return allBST

    def whichAtt(self):  # Demande et renvoie l'index de l'attribut voulu
        print("What is the desired attribute ?\n")
        i = 0
        for att in self.data[0].keys():
            print("For the " + str(att) + ", enter " + str(att))
            i += 1
        return str(input())

    def buildBST(self, att):
        a = BST()
        for dico in self.data:
            node = Node(dico[att], self.data.index(dico))
            a.addNode(node)
        return a

    def delBST(self, tree):
        del(tree.head)

    def reBuildBST(self, tree):
        att = self.whichAtt()
        tree1 = self.buildBST(att)

    def printAllTrees(self, allTrees): # allTrees est une liste des arbres (fournie par buildAllBST)
        for arbre in myTableTrees:
            print(arbre.affInfixe())

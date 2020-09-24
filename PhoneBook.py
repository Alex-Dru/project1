from Person import *

class PhoneBookException(Exception):
    pass

class PhoneBook:
    def __init__(self, data):
        self.data = data

    def addPerson(self, personAdd):
        for person in self.data:
            if person.num == personAdd.num:
                raise PhoneBookException("error: person already created")
        self.data.append(personAdd)

    def delPerson(self, personDel):
        for person in self.data:
            if person.num == personDel.num:
                self.data.remove(person)

    def printPB(self):
        for person in self.data:
            print(person.num + "  " + person.lastName + "  " + person.firstName)

    def lookUpNumber(self, number):
        for person in self.data:
            if person.num == number:
                print("Person Found!")
                print("Phone Number:" + person.num)
                print("Last Name:  " + person.lastName)
                print("First Name:  " + person.firstName)

    def lookUpLastName(self, lastName):
        i = 0
        for person in self.data:
            if person.lastName == lastName:
                i+=1
                print("Phone Number:" + person.num)
                print("Last Name:  " + person.lastName)
                print("First Name:  " + person.firstName)
        print("number of results displayed:  " + str(i))

    def lookUpFirstName(self, firstName):
        i = 0
        for person in self.data:
            if person.firstName == firstName:
                i+=1
                print("Phone Number:" + person.num)
                print("Last Name:  " + person.lastName)
                print("First Name:  " + person.firstName + "\n")
        print("number of results displayed:  " + str(i))

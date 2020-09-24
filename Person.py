class PersonException(Exception):
    pass

class Person:
    def __init__(self, num, firstName, lastName, nextPerson=None):
        if len(num)==10:
            self.num = num
        else:
            raise PersonException("error: number not valid")
        if len(firstName)<30:
            self.firstName = firstName.lower()
        else:
            raise PersonException("error: firstname is too long")
        if len(lastName)<30:
            self.lastName = lastName.upper()
        else:
            raise PersonException("error: lastname is too long")
        self.nextPerson=None

    def printPerson(self):
        print(self.num + "  " + self.firstName + "  " + self.lastName)

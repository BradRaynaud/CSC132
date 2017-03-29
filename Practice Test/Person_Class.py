class Person(object):
    def __init__(self, pname):
        self.name = pname

    def eat(self):
        pass

    def grow(self):
        pass


class Adult(Person):
    def __init__(self, dareresponse):
        Person.__init__(self, "John")
        self.responsibilities = dareresponse


class Child(Person):
    def __init__(self):
        Person.__init__(self, "Jane")

    def procrastinate(self):
        pass


class Programmer(Adult):
    def __init__(self):
        Adult.__init__(self)

    def goToWork(self):
        pass


class Student(Adult, Child):
    def __init__(self, dagrades):
        Adult.__init__(self, "Pass Tests")
        Child.__init__(self)
        self.grades = float(dagrades)

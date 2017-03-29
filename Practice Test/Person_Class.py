class Person(object):
    def __init__(self):
        name = str

    def eat(self):
        pass

    def grow(self):
        pass


class Adult(Person):
    def __init__(self):
        Person.__init__(self)
        responsibilities = str


class Child(Person):
    def __init__(self):
        Person.__init__(self)

    def procrastinate(self):
        pass


class Programmer(Adult):
    def __init__(self):
        Adult.__init__(self)

    def goToWork(self):
        pass


class Student(Adult, Child):
    def __init__(self):
        Adult.__init__(self)
        Child.__init__(self)
        grades = float

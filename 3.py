class Bird:
    def printSize(self):
        print('small')

class Eagle(Bird):
    def printSize(self):
        print('large')

bird=Bird()
bird.printSize()        
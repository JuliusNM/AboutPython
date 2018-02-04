class Pet(object):

    num_pets = 0

    def __init__(self, name):

        self.name = name
        Pet.num_pets += 1
        #self.num_pets += 1

    def speak(self):

        print('Name %s & number of pets is %d' % (self.name, self.num_pets))

kim = Pet('Kim')
tom = Pet('Tom')
pap = Pet('Pap')
kim.speak()
tom.speak()
pap.speak()

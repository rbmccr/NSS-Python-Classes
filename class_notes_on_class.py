class Animal: # or class Animal(): ... if class is not a sub-class, don't put parenthesis. In this example, Animal is the base class
  def __init__(self, species, leg_num=0, domesticated=False): # override init method to give properties to each instance as parameters. self is always the first arg
    self.species = species
    self.leg_num = leg_num
    self.domesticated = domesticated

  def saySomething(self):
    if self.species == 'dog':
      return 'woof'
    else:
      return 'Thanos did nothing wrong'

  def __str__(self):
    return f'This animal is a {self.species} that says {self.saySomething()}'

# Inheritance ---------------------------------------------------------------

class Dog(Animal):
  def __init__(self, breed):
    self.breed = breed
    super().__init__('dog', leg_num=4, domesticated=True) # call the init method of the parent class

  def speak(self):
    return f'I\'m a dog, so I say {self.saySomething()}'

# ---------------------------------------------------------------------------

class Pet: # we will use this class to create a relationship without direct inheritance
  def __init__(self, name, critter_instance):
    self.name = name
    self.animal_type = critter_instance

  def set_owner(self, name, phone):
    self.owner_name = name
    self.owner_number = phone

  def __str__(self):
    return f'This pet\'s name is {self.name}. It has {self.animal_type.leg_num} legs, and it likes to say {self.animal_type.saySomething()}!'

# make a dog and make it someone's pet
aussie_mix = Dog('Aussie Mix')
murph = Pet('Murphis', aussie_mix) # IMPORTANT LINE RIGHT HERE
murph.set_owner('The Sheps', '555-555-1234')

# ---------------------------------------------------------------------------

if __name__ == '__main__':
  dog = Animal('dog', 4, True) #species var is the only requirement
  cat = Animal('cat', 4)

  print(dog)
  print(cat)

print('Here\'s the dog that\'s got an owner: ', murph)
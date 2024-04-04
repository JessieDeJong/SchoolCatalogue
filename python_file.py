#The parent class School
class School:

  def __init__(self, name, level, numberOfStudents=0):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def get_name(self):
    return self.name
  
  def get_level(self):
    return self.level

  def get_numberOfStudents(self):
    return self.numberOfStudents

  def set_numberOfStudents(self, new_number):
    self.numberOfStudents = new_number

  def __repr__(self):
    return f"This is a {self.level} school named {self.name} with {self.numberOfStudents} students."

#The child class PrimarySchool
class PrimarySchool(School):
  
  def __init__(self, name, numberOfStudents, pickUpPolicy):
    super().__init__(name, "Primary", numberOfStudents)
    self.pickUpPolicy = pickUpPolicy

  def get_pickUpPolicy(self):
    return self.pickUpPolicy

  def __repr__(self):
    return super().__repr__() + f"The PickUp Policy of this school is: {self.pickUpPolicy}"

#The child class MiddleSchool
class MiddleSchool(School):
  
  def __init__(self, name, numberOfStudents):
    super().__init__(name, "Middle", numberOfStudents)

#The child class HighSchool
class HighSchool(School):
  
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, "High", numberOfStudents)
    self.sportsTeams = sportsTeams

  def get_sportsTeams(self):
    return self.sportsTeams

  def __repr__(self):
    list_sportsTeams = ""
    for team in self.sportsTeams:
      if team == self.sportsTeams[-1]:
        list_sportsTeams += team + "."
      else:
        list_sportsTeams += team + ", "
    return super().__repr__() + f"This school has these sports teams: {list_sportsTeams}" 

#Here is some code that I used to test my classes out
Imaculata = School("Imaculata", "High")
Imaculata.set_numberOfStudents(150)
#print(Imaculata)

a = PrimarySchool("Peuterbos", 50, "Pickup after 3pm.")
#print(a)
#print(a.get_numberOfStudents())

b = MiddleSchool("Lorcana", 120)
b.set_numberOfStudents(130)
#print(b.get_name())
#print(b)

c = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
#print(c.get_sportsTeams())
#print(c)

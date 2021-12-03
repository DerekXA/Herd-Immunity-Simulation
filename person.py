import random
random.seed()
from virus import Virus


class Person(object):
    ''' Person objects will populate the simulation. '''

    def __init__(self, _id, is_vaccinated, infection=None):   
        self._id = _id  # int
        self.is_alive = True  # boolean
        self.is_vaccinated = is_vaccinated  # boolean
        self.infection = infection  # Virus object or None

    def did_survive_infection(self):
        chance_infection = random.random()
        print(f"chance: {chance_infection}")
        if chance_infection > self.infection.mortality_rate:
            self.is_vaccinated = True
        else:
            self.is_alive = False
        return self.is_alive
        # Only called if infection attribute is not None.
        # TODO:  Finish this method. Should return a Boolean
       

''' These are simple tests to ensure that you are instantiating your Person class correctly. '''
def test_vacc_person_instantiation():
    # create some people to test if our init method works as expected
    person = Person(1, True)
    assert person._id == 1
    assert person.is_alive is True
    assert person.is_vaccinated is True
    assert person.infection is None


def test_not_vacc_person_instantiation():
    person = Person(2, False)
    # TODO: complete your own assert statements that test
    # the values at each attribute
    # assert ...
    assert person._id == 2
    assert person.is_alive is True
    assert person.is_vaccinated is False
    assert person.infection is None
   


def test_sick_person_instantiation():
    # Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # Create a Person object and give them the virus infection
    person = Person(3, False, virus)
    # TODO: complete your own assert statements that test
    # the values at each attribute
    # assert ...
    assert person._id == 3
    assert person.is_vaccinated is False
    assert person.infection == Virus
    


def test_did_survive_infection():
    # TODO: Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # TODO: Create a Person object and give them the virus infection
    person = Person(4, False, virus)
    survived = person.did_survive_infection()
    print(f'survived? {survived}')
    if survived:
        assert person.is_alive is True
        assert person.is_vaccinated is True
    else:
        assert person.is_alive is False
    
    # Resolve whether the Person survives the infection or not
    survived = person.did_survive_infection()
    # Check if the Person survived or not
    
    if survived:
        assert person.is_alive is True
        # TODO: Write your own assert statements that test
        # the values of each attribute for a Person who survived
        # assert ...
    else:
        assert person.is_alive is False
        # TODO: Write your own assert statements that test
        # the values of each attribute for a Person who did not survive
        # assert ...
        pass
    

# my_virus = Virus("ebola", .8, .3)
# derek = Person (1, False, my_virus)
# print(derek.did_survive_infection())
# test_vacc_person_instantiation()
# test_not_vacc_person_instantiation()
if __name__ == "__main__":
    test_vacc_person_instantiation()
    test_sick_person_instantiation()
    test_did_survive_infection()
    test_did_survive_infection()
    test_did_survive_infection()
    test_did_survive_infection()

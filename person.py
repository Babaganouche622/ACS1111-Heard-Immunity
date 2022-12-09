import random
# random.seed(42)
from virus import Virus

class Person(object):
    def __init__(self, _id, is_vaccinated, infection = None, infection_date=None):
        self._id = _id  # int
        self.is_vaccinated = is_vaccinated
        self.is_alive = True
        self.infection = infection
        self.infection_date = infection_date

    def did_survive_infection(self):
        if self.infection:
            infect_num = round(random.uniform(0.0, 1.0), 2)
            if infect_num < self.infection.mortality_rate:
                self.is_alive = False
                self.infection = None
            else:
                self.is_vaccinated = True
                self.infection = None

        return self.is_alive








if __name__ == "__main__":
    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None

    unvaccinated_person = Person(2, False)
    assert unvaccinated_person._id == 2
    assert unvaccinated_person.is_alive is True
    assert unvaccinated_person.is_vaccinated is False
    assert unvaccinated_person.infection is None
    virus = Virus("Dysentery", 0.7, 0.2)
    infected_person = Person(3, False, infection=virus)
    assert infected_person._id == 3
    assert infected_person.is_alive is True
    assert infected_person.is_vaccinated is False
    assert infected_person.infection is virus

    
    people = []
    for i in range(1, 101):
        people.append(Person(i, False, infection=virus))

    for person in people:
        if person.did_survive_infection():
            assert person.is_alive
            assert person.is_vaccinated
            assert not person.infection
        else:
            assert not person.is_alive
            assert not person.is_vaccinated
            assert not person.infection


    """Testing for infected and not infected people passing did_survive_infection() correctly"""    
    virus2 = Virus("Bad news", 0.4, 0.12)
    people2 = []

    for i in range(1, 101):
        infection_num = round(random.uniform(0.0, 1.0), 2)
        if infection_num < virus2.repro_rate:
            people2.append(Person(i, False, infection=virus2))
        else:
            people2.append(Person(i, False))
        
    for person in people2:
            if person.did_survive_infection and person.infection is None:
                assert person.is_alive
                assert not person.is_vaccinated
                assert not person.infection  
            elif person.did_survive_infection() and person.infection:
                assert person.is_alive
                assert person.is_vaccinated
                assert not person.infection
            elif not person.did_survive_infection():
                assert not person.is_alive
                assert not person.is_vaccinated
                assert not person.infection
        

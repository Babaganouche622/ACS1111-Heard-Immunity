import random, sys
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus

class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        self.logger = Logger("/Users/briancahill/Desktop/ACS Courses/ACS-1111-Object-Oriented-Programming-master/Heard-Immunity/ACS1111-Heard-Immunity/data.txt")
        self.virus = virus
        self.pop_size = pop_size
        self.total_alive = pop_size
        self.total_dead = 0
        self.dead_people = list()
        self.vacc_percentage = vacc_percentage
        self.total_vaccinated = 0
        self.initial_infected = initial_infected
        self.infected_people = list()
        self.time_step_counter = 0
        self.number_interactions = 0
        self.total_infections = 0
        self.people = self._create_population()


    def _create_population(self):
        people = []
        vax_percentage = self.vacc_percentage * self.pop_size
        for i in range(1, int(self.pop_size + 1)):
            if i <= vax_percentage:
                people.append(Person(i, True))
                self.total_vaccinated += 1
            elif i <= initial_infected + vax_percentage:
                people.append(Person(i, True, infection=self.virus, infection_date=0))
                self.total_vaccinated += 1
                self.total_infections += 1
            else:
                people.append(Person(i, False))
        return people

    def _simulation_should_continue(self):
        for person in self.people:
            if person.is_alive and not person.is_vaccinated:
                return True   
        return False

    def run(self):
        should_continue = True
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus, self.virus.mortality_rate, self.virus.repro_rate, self.initial_infected)
        while should_continue:
            self.time_step_counter += 1
            self.time_step() 
            self._infect_newly_infected()
            should_continue = self._simulation_should_continue()
            self.logger.log_interactions(self.time_step_counter, self.number_interactions, len(self.dead_people), self.total_vaccinated, self.total_infections)

    def time_step(self):
        for person in self.people:
            if person.infection and person.is_alive:
                for i in range(101):
                    random_person = random.choice(self.people)
                    while not random_person.is_alive:
                        random_person = random.choice(self.people)
                    if random_person.infection:
                        pass
                    elif not random_person.is_vaccinated:  
                        self.interaction(person, random_person)
                        self.number_interactions += 1
                if person.did_survive_infection():
                    self.total_vaccinated += 1
                else:
                    self.dead_people.append(person)
                    self.people.remove(person)
                    self.total_dead += 1

    def interaction(self, infected_person, random_person):
            if random_person.infection is None:
                sickness = round(random.uniform(0.0, 1.0), 2)
                if sickness < virus.repro_rate:
                    self.infected_people.append(random_person)
                    self.people.remove(random_person)

    def _infect_newly_infected(self):
        for person in self.infected_people:
            person.infection = self.virus
            self.total_infections += 1
            self.people.append(person)
        self.infected_people = []








if __name__ == "__main__":
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12
    virus = Virus(virus_name, repro_num, mortality_rate)

    pop_size = 10000
    vacc_percentage = 0.1
    initial_infected = 10

    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)

    sim.run()

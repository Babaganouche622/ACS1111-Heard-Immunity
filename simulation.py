import random, sys
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        # TODO: Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding parts of the simulation.
        self.logger = Logger("/Users/briancahill/Desktop/ACS Courses/ACS-1111-Object-Oriented-Programming-master/Heard-Immunity/ACS1111-Heard-Immunity/data.txt")
        # TODO: Store the virus in an attribute
        self.virus = virus
        # TODO: Store pop_size in an attribute
        self.pop_size = pop_size
        # TODO: Store the vacc_percentage in a variable
        self.vacc_percentage = vacc_percentage
        # TODO: Store initial_infected in a variable
        self.initial_infected = initial_infected
        # You need to store a list of people (Person instances)
        # Some of these people will be infected some will not. 
        # Use the _create_population() method to create the list and 
        # return it storing it in an attribute here. 
        # TODO: Call self._create_population() and pass in the correct parameters.
        self.people = self._create_population()
        self.infected_people = list()
        self.time_step_counter = 0
        pass

    def _create_population(self):
        # TODO: Create a list of people (Person instances). This list 
        # should have a total number of people equal to the pop_size. 
        # Some of these people will be uninfected and some will be infected.
        # The number of infected people should be equal to the the initial_infected
        # TODO: Return the list of people
        people = []
        vax_percentage = self.vacc_percentage * self.pop_size
        # print(self.pop_size)
        for i in range(1, int(self.pop_size + 1)):
            if i <= vax_percentage:
                people.append(Person(i, True))
            elif i <= initial_infected + vax_percentage:
                people.append(Person(i, True, infection=self.virus, infection_date=0))
            else:
                people.append(Person(i, False))
        return people

    def _simulation_should_continue(self):
        # This method will return a boolean indicating if the simulation 
        # should continue. 
        # The simulation should not continue if all of the people are dead, 
        # or if all of the living people have been vaccinated. 
        # TODO: Loop over the list of people in the population. Return True
        # if the simulation should continue or False if not.
        alive_unvaccinated = 0
        for person in self.people:
            if person.is_alive: 
                if not person.is_vaccinated:
                    alive_unvaccinated += 1
        # print(alive_unvaccinated)
        if int(alive_unvaccinated) > 0:
            return True
        else: 
            return False


    def run(self):
        # This method starts the simulation. It should track the number of 
        # steps the simulation has run and check if the simulation should 
        # continue at the end of each step. 

        should_continue = True
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus, self.virus.mortality_rate, self.virus.repro_rate)

        while should_continue:
            for person in self.people:
                if person.infection_date != None:
                    if person.infection_date + 1 == self.time_step_counter:
                        person.infection = None
                        person.infection_date = None
                        person.is_vaccinated = True
            # TODO: Increment the time_step_counter
            self.time_step_counter += 1
            # TODO: for every iteration of this loop, call self.time_step()
            self.time_step() 
            # Call the _simulation_should_continue method to determine if 
            # the simulation should continue
            self._infect_newly_infected()
            self.logger.log_infection_survival(self.time_step_counter, self.pop_size, self.people)
            should_continue = self._simulation_should_continue()

        print(f"Simulation ran: {self.time_step_counter} times.")
        # print(self.people)
        alive_people = 0
        dead_people = 0
        for person in self.people:
            if person.is_alive:
                alive_people += 1
            else: 
                dead_people += 1

        print(f"This many survived: {alive_people}")
        print(f"This many died: {dead_people}")
        print(f"Virus repoductive rate: {self.virus.repro_rate}")
        print(f"Virus mortality rate: {self.virus.mortality_rate}")
        # TODO: Write meta data to the logger. This should be starting 
        # statistics for the simulation. It should include the initial
        # population size and the virus. 
        
        # TODO: When the simulation completes you should conclude this with 
        # the logger. Send the final data to the logger. 

    def time_step(self):
        # This method will simulate interactions between people, calulate 
        # new infections, and determine if vaccinations and fatalities from infections
        # The goal here is have each infected person interact with a number of other 
        # people in the population
        # TODO: Loop over your population
        # For each person if that person is infected
        # have that person interact with 100 other living people 
        # Run interactions by calling the interaction method below. That method
        # takes the infected person and a random person
        
        for person in self.people:
            alive_people = []
            # print(person._id)
            if person.infection is not None:
                for alive_person in self.people:
                    # print(alive_person._id)
                    test_sample = []
                    if alive_person.is_alive:
                        if not alive_person.is_vaccinated:
                            # print(alive_person)
                            alive_people.append(alive_person)
                            # print(alive_person._id)
                            # print(alive_person.is_vaccinated)
                            # print(alive_person.infection)
                            # print(alive_person.is_alive)
                if len(alive_people) < 100:
                    # print("we are here")
                    test_sample = random.choices(alive_people, k=len(alive_people))
                else:
                    test_sample = random.choices(alive_people, k=100)

                # print(f"Test sample: {test_sample}")
                for person2 in test_sample:
                    self.interaction(person, person2)
                self.logger.log_interactions(self.time_step_counter, test_sample, self.infected_people)
                # print(self.infected_people[0].infection)
        # print(alive_people)

    def interaction(self, infected_person, random_person):
        # TODO: Finish this method.
        # The possible cases you'll need to cover are listed below:
            # random_person is vaccinated:
            #     nothing happens to random person.
            # random_person is already infected:
            #     nothing happens to random person.
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0.0 and 1.0.  If that number is smaller
            #     than repro_rate, add that person to the newly infected array
            #     Simulation object's newly_infected array, so that their infected
            #     attribute can be changed to True at the end of the time step.
        # TODO: Call logger method during this method.
        if not random_person.is_vaccinated:
            # print(random_person.is_vaccinated)
            if random_person.infection is None:
                # print(random_person.infection)
                sickness = round(random.uniform(0.0, 1.0), 2)
                if sickness < virus.repro_rate:
                    # print(random_person.is_alive)
                    # random_person.infection = self.virus
                    self.infected_people.append(random_person)
                    random_person.infection_date = self.time_step_counter
                    # print(random_person.infection_date)


        return

    def _infect_newly_infected(self):
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        # print(self.infected_people)
        for person in self.infected_people:
            # print(person.is_alive)
            if person.is_alive:
                # print(person.is_alive)
                person.infection = self.virus
                # print(f"Person is infected? {person.infection}")
                person.did_survive_infection()
                # print(f"Di person survive? {person.is_alive}")
            # print(person._id)
            # print(person.is_alive)
            # print(person.infection)
            # print(person.is_vaccinated)
        self.infected_people = []
        # print(self.infected_people)


if __name__ == "__main__":
    # Test your simulation here
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12
    virus = Virus(virus_name, repro_num, mortality_rate)

    # Set some values used by the simulation
    pop_size = 10000
    vacc_percentage = 0.1
    initial_infected = 10

    # Make a new instance of the imulation
    # virus = Virus(virus, pop_size, vacc_percentage, initial_infected)
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)

    sim.run()

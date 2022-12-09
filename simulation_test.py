from simulation import Simulation
from virus import Virus
    
virus_name = "Sniffles"
repro_num = 0.5
mortality_rate = 0.12
virus = Virus(virus_name, repro_num, mortality_rate)

pop_size = 10000
vacc_percentage = 0.1
initial_infected = 10

sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)

"""Test the initial instantiation is what we expecct."""
assert sim.total_alive == sim.pop_size
assert len(sim.dead_people) == 0
assert sim.total_vaccinated == 1000
assert sim.total_infections == 10
assert sim.initial_infected == 10

"""This test only works if you comment out the auto run function on line 26."""
sim.run()

"""Test that the simulation changes our initial values"""
assert sim.total_alive != sim.pop_size
assert len(sim.dead_people) != 0
assert sim.total_vaccinated != 1000
assert sim.total_infections != 10
assert sim.initial_infected == 10

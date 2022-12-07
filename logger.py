class Logger(object):
    def __init__(self, file_name):
        self.file_name = file_name
        pass

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num, initial_infected):
        outfile = open(self.file_name, "w")
        to_file = f"""
The population size was: {pop_size}.
The vaccinated percentage was: {vacc_percentage}.
The virus used for testing was: {virus_name.name}.
The mortality rate was: {mortality_rate}.
The reproductive rate of this virus was: {basic_repro_num}.
Total initial infected: {initial_infected}.
"""
        outfile.write(to_file)
        outfile.close()

    def log_interactions(self, step_number, number_of_interactions, dead_people, total_vaccinated, total_infections):
        outfile = open(self.file_name, "a")
        to_file = f"""
On step {step_number}
Total interactions: {number_of_interactions} 
Total people dead: {dead_people}
Total vaccinated: {total_vaccinated}
Total infections: {total_infections}
"""
        outfile.write(to_file)
        outfile.close()


    # def log_infection_survival(self, step_number, population_count, number_of_new_fatalities):
    #     outfile = open(self.file_name, "a")
    #     number_dead = 0
    #     for person in number_of_new_fatalities:
    #         if not person.is_alive:
    #             number_dead += 1
    #     to_file = f"On step {step_number} we have a total of {number_dead} people dead of a total population of {population_count}.\n"
    #     outfile.write(to_file)
    #     outfile.close()
    #     pass

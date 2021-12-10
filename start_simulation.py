from simulation import Simulation
from virus import Virus
from validate_input import validate_input

virus_name = validate_input('What is the virus name?  ', str)
repro_rate = validate_input('What is the reproduction rate?  ')/100
mortality_rate = validate_input('What is the mortality rate?  ')/100

virus = Virus(virus_name, repro_rate, mortality_rate)

population_size = validate_input('What is the population size?  ')
ammount_vacc = validate_input('What percentage of the population is vaccinated?  ')/100
first_infected = validate_input('How many people are initially infected?  ')
average_interactions = validate_input('How many interactions should each infected person have?  ')

sim = Simulation (virus, population_size, ammount_vacc, first_infected, average_interactions)


sim.run()

class Logger(object):

    def __init__(self, file_name):
        self.file_name = file_name
        self.file = f'*SIM_master_{self.file_name}.txt'
        self.microlog = f'*sim_micro_{self.file_name}.txt'

    def write_metadata(self, virus_name, repro_rate, mortality_rate, pop_size, ammount_vacc, first_infected):

        repro_rate = repro_rate * 100
        mortality_rate = mortality_rate * 100
        ammount_vacc = ammount_vacc * 100

        
        file = open(self.file, 'a')

        file.write('----- VIRUS STATS -----\n')
        file.write(f'Virus: {virus_name}\n')
        file.write(f'Reproduction Rate: {repro_rate}%\n')
        file.write(f'Mortality Rate: {mortality_rate}%\n')
        
        file.write('\n--- POPULATION STATS ---\n')
        file.write(f' Population: {pop_size}\n')
        file.write(f' Vaccination Rate: {ammount_vacc}%\n')
        file.write(f' Initial Infections: {first_infected}\n')


        file.write('\n\n---------------------{virus_name}---------------------- \n\n')
                   
        file.close()
        
 
        

    def log_interaction(self, person, random_person, infected=False):
        
        
        file = open(self.microlog, 'a')
        file.write('\n\n')
        file.write('*** INTERACTION ***\n')
        
        if random_person.is_vaccinated:
            file.write(f'infected + vaccinated = no infection {person._id} did not infect {random_person._id} because they are vaccinated.\n')
        elif random_person.natural_immunity: 
            file.write(f'infected + infected = immune {person._id} did not infect {random_person._id} because they are naturally immune.\n')
        elif random_person.virus != None: 
            file.write(f'infected + sick = sick {person._id} did not infect {random_person._id} because they are already sick.\n')
        elif infected: 
            file.write(f'infected + person = sick {person._id} has infected {random_person._id}.\n')
        else: 
            file.write(f'infected + person = lucky {person._id} did not infect {random_person._id}. Nothing but luck. \n')

        file.close()


    def log_infection_survival(self, person, did_die_from_infection=False):
        file = open(self.microlog, 'a')
        file.write('\n')
        file.write('NFECTION OUTCOME:\n')
        if did_die_from_infection:
            file.write(f'{person._id} did not survive the infection.\n')
        else:
            file.write(f'{person._id} survived and has natural immunity now.\n')

        file.close()

    def log_time_step(self, time_step, time_step_infections, time_step_deaths, total_infections, total_deaths, total_immune, total_population, herd_immunity):
        file = open(self.microlog, 'a')
        file.write('\n')
        file.write(f'========== TIME STEP {time_step} ENDED ============= \n')
        file.close()

        file = open(self.file, 'a')
        file.write(f'\ TIME STEP {time_step} ENDED.  \n')
        file.write(f'>> Infections in this time step: {time_step_infections} \n')
        file.write(f'>> Deaths in this time step: {time_step_deaths} \n\n')
        file.write(f'CUMULATIVE STATS 📈\n')
        file.write(f'Total infections: {total_infections} \n')
        file.write(f'Total deaths: {total_deaths} \n\n')
        file.write(f' IMMUNITY PROGRESS: \n')
        file.write(f'Total Immune: {total_immune}/{total_population} \n')
        file.write(f'Current Immunity Rate: {round((total_immune/total_population*100),2)}% \n')
        file.write(f'Herd Immunity Rate: {round(herd_immunity*100, 2)}% \n\n')
        file.close()

    def log_conclusion(self, conclusion, total_dead, total_alive, total_immune):
        file = open(self.file, 'a')
        file.write(f'🔬 FINAL OUTCOME: \n\n')
        if conclusion == 'herd immunity':
            file.write(f'>> The simulation ended because herd immunity was achieved.\n')
        elif conclusion == 'no infections':
            file.write(f'>> The simulation ended because there were no more active infections.\n')
        else:
            file.write(f'>> The simulation ended because the entire population died from the disease.\n')
        file.write(f'\nTotal Deaths: {total_dead}')
        file.write(f'\nTotal Survivors: {total_alive}')
        file.write(f'\nTotal Immune: {total_immune}')
        file.close()
def test_logger_instantiation():
    logger = Logger('herd_immunity_simulation')
    assert logger.file_name == 'herd_immunity_simulation'
    assert logger.file == 'herd_immunity_simulation.txt'

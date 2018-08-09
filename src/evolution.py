import cnn
import random
import simulation

class Evolution():
    """
    initializes Evolution algorithm

    @param population_size: int (size of populations)
    @param populations_number: int (number of populations)
    """
    def __init__(self, population_size, populations_number, mutation_rate):
        self.population_size = population_size
        self.populations_number = populations_number
        self.mutation_rate = mutation_rate
        self.initial_population = cnn.create_list_cnn(population_size)


    def _mix_individuals(self, parent_A, parent_B):
        #TODO
        return None

    def _create_population(self):
        new_population = []
        for i in range(self.population_size):
            parent_A = random.randint(0,self.population_size)
            parent_B = random.randint(0,self.population_size)

            new_individual = self._mix_individuals(parent_A, parent_B)
            new_population.append(new_individual)

        return new_population


    def start_evolution(self):
        
        self.population = self.initial_population
        for i in range(self.populations_number):
            #TODO

            self.population = self._create_population()



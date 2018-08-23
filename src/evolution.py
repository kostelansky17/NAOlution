import cnn
import random
import simulation
import consts
import time
import object
import vrep
import vision
import numpy as np


class Individual():
    def __init__(self, model, rank):
        self.model = model
        self.rank = rank


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
        self.population = self._create_initial_population()
        

    def _mix_individuals(self, parent_A, parent_B):
        #TODO
        return None


    def _create_initial_population(self):
        population = []
        models = cnn.create_list_cnn(self.population_size)

        for model in models:
            individual = Individual(model, None)
            population.append(individual)

        return population

    def _create_population(self):
        new_population = []
        for i in range(self.population_size):
            parent_A = random.randint(0,self.population_size)
            parent_B = random.randint(0,self.population_size)

            
            new_individual = self._mix_individuals(parent_A, parent_B)
            new_population.append(new_individual)

        return new_population

    def _run_simulation(self, model_number):
        client_ID = simulation.start_connection(consts.vrep_ip_2, consts.vrep_port_2)
        simulation.start_simulation(client_ID)

        model = self.population[model_number]
        
        nao_handle = object.get_object_handle(client_ID, consts.nao)
        target_handle = object.get_object_handle(client_ID, consts.target)

        vision_handle = object.get_vison_sensor_handle(client_ID, consts.nao_vision_1)
        return_code, resolution, sensor_img = vrep.simxGetVisionSensorImage(client_ID, vision_handle,
                                                                            0, vrep.simx_opmode_streaming)
        
        time.sleep(1) #mandatory sleep, WON'T WORK without it      

        target_position =  object.get_position(client_ID, target_handle)


        while True:
            nao_position = object.get_position(client_ID, nao_handle)
            nao_orientation = object.get_orientation(client_ID, nao_handle)
            return_code, resolution, sensor_img = vrep.simxGetVisionSensorImage(client_ID, vision_handle,
                                                                                0, vrep.simx_opmode_buffer)

    
            model_input = vision.sensor_output_to_model_input(resolution, sensor_img)
            results = model.predict(model_input)

        simulation.stop_simulation(client_ID)
        simulation.stop_connection(client_ID)
        time.sleep(5)

    def _run_epoch(self):
        for i in range(self.population_size):
            self._run_simulation(i)

    def start_evolution(self):       
        for i in range(self.populations_number):
            self._run_epoch()

    def _distance_from_taget(self, nao_position, target_position):
        return np.sqrt((nao_position[0] - target_position[0])**2 + (nao_position[1] - target_position[1])**2)

    def _nao_failed(self, nao_orientation):
            """Checks if object referenced by compass is lying on the ground.
            "Lying on the ground" entails the compass is turned upside/downside
            or sideways. That is, rotate by `pi/2` degrees around the `x`
            axis minus a small "just-in-case" error of `.1`.
            """
            
            return abs(nao_orientation[0]) > .9 * np.pi / 2

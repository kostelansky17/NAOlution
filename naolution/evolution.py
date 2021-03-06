from naolution.utils import cnn
import random
from naolution.managers import simulation_manager as simulation
from consts import NAO, TARGET, NAO_VISION_1, VREP_IP_2, VREP_PORT_2, \
                   NAOQI_BIN_IP, NAOQI_BIN_PORT, SCENES_SET_1
from naolution.managers import object_manager
from naolution.vrep import vrep
from naolution.managers import vision_manager as vision
import numpy as np
from naolution.managers.movement_manager import Movement
import logging
import datetime
import time
from keras import models
import os


class Individual():
    """
    Initializes Individual used in Evolution algorithm

    @param model: Convolutional neural network
    @param rank: rank of the Individual
    """
    def __init__(self, model):
        self.model = model
        self.rank = 0


class Evolution():
    """
    Initializes Evolution algorithm

    @param population_size: int (size of populations)
    @param populations_number: int (number of populations)
    """
    def __init__(self, population_size, populations_number,
                 scene_timeout, scenes):
        self.population_size = population_size
        self.populations_number = populations_number
        self.scene_timeout = scene_timeout
        self.scenes = scenes
        self.population = self._create_initial_population()
        self.date_time = datetime.datetime.now().strftime("%y-%m-%d_%H:%M")
        logging.basicConfig(filename='../logs/evolution_' +
                           self.date_time
                            + '.log',level=logging.INFO)

    """
    Select Individual from population for crossing
    
    @return population: list of models
    """
    def _select_individual(self, population_select):
        selected = int(abs(np.random.normal(0, population_select)))
        
        if selected > (self.population_size - 1):
            return self._select_individual(population_select)

        return selected


    """
    Creates initual population by generating models with randomly generated weights
    
    @return population: list of models
    """
    def _create_initial_population(self):
        population = []
        models = cnn.create_list_cnn(self.population_size)

        for model in models:
            individual = Individual(model)
            population.append(individual)

        return population


    def _save_models(self):
        self.population.sort(key=lambda x: x.rank, reverse=True)
        directory_path = "../models/evolution_" + datetime.datetime.now().strftime("%y-%m-%d_%H:%M")
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
        
        for i in range(int(self.population_size/10)):
            self.population[i].model.save( directory_path + "/model_" + str( self.population[i].rank) + ".h5")


    def _save_generation(self):
        directory_path = "../models/evolution_" + self.date_time
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        for i in range(self.population_size):
            self.population[i].model.save( directory_path + "/model_" + str( self.population[i].rank) + ".h5")


    """
    Creates population by crossing individuals. Propability to use Individual is based on its Rank.
    
    @return population: list of models
    """
    def _create_population(self):
        new_population = []
        self.population.sort(key=lambda x: x.rank, reverse=True)
        population_select = int(self.population_size * 0.3)

        for _ in range(self.population_size):
            rand_A = self._select_individual(population_select)
            rand_B = self._select_individual(population_select)

            new_model = cnn.mix_two_models(self.population[rand_A].model,
                                           self.population[rand_B].model)

            new_individual = Individual(new_model)
            new_population.append(new_individual)

        return new_population


    """
    Evaluates Individual performance in Scene
    
    @param run_time: Scene total running time
    @param distance_from_target: Nao's distance from target

    @return -rank
    """
    def _evaluate_individual(self, run_time, distance_from_target):
        return - distance_from_target * 10


    """
    Counts Nao's distance from target

    @param nao_position: list of floats
    @param target_position: list of floats
    """
    def _distance_from_taget(self, nao_position, target_position):
        return np.sqrt((nao_position[0] - target_position[0])**2 +
                       (nao_position[1] - target_position[1])**2)


    """
    Stops running simuation
    
    @param nao_position: list of floats
    @param target_position: list of floats
    @param run_time: float

    @return -rank
    """
    def _stop_simulation(self, nao_position, target_position, run_time):
        distance = self._distance_from_taget(nao_position, target_position)
        if run_time > self.scene_timeout or distance < 0.25:
           return True
        return False


    """
    Runs simulation - navigates NAO trough scene until he gets to the Target or Timeout
    
    @param model_number: int, Number of model which is to be used in simulation 
    @param client_ID: int
    @param movement: instance of class Movement
    """
    def _run_simulation(self, model_number, client_ID, movement):
        simulation.start_simulation(client_ID)
        time.sleep(6)

        model = self.population[model_number].model
        
        nao_handle = object_manager.get_object_handle(client_ID, NAO)
        target_handle = object_manager.get_object_handle(client_ID, TARGET)
        vision_handle = object_manager.get_vison_sensor_handle(client_ID, NAO_VISION_1)
        resolution, sensor_img = simulation.get_vision_sensor_image_str(client_ID, vision_handle)

        time.sleep(1) #mandatory sleep, WON'T WORK without it      

        nao_position = object_manager.get_position(client_ID, nao_handle)
        target_position = object_manager.get_position(client_ID, target_handle)

        movement.move_init()     
        movement.standInit(0.5)

        start_time = time.time()
        end_time = time.time()
        while not self._stop_simulation(nao_position, target_position, end_time - start_time):
            nao_position = object_manager.get_position(client_ID, nao_handle)
            resolution, sensor_img = simulation.get_vision_sensor_image_buff(client_ID, vision_handle)

            model_input = vision.sensor_output_to_model_input(resolution, sensor_img)
            results = model.predict(model_input)

            movement.move(float(results[0][0]), float(results[0][1]), float(results[0][2]))           
            end_time = time.time()

        movement.move(0,0,0)      
        end_time = time.time()

        distance_from_target = self._distance_from_taget(nao_position, target_position)
        self.population[model_number].rank += self._evaluate_individual(end_time - start_time, 
                                                                        distance_from_target)

        movement.standZero(1)
        simulation.stop_simulation(client_ID)

    """
    Runs Model/Individual in every Simulation used in Evolution alg
    
    @param i: int
    @param client_ID: int
    @param model_number: int
    @param movement: instance of class Movement
    """
    def _run_simulations(self, model_number, client_ID, movement):
        for scene in self.scenes:
            simulation.load_scene(client_ID, scene)
            self._run_simulation(model_number, client_ID, movement)
            simulation.close_scene(client_ID)

        print(self.population[model_number].rank)
        logging.info(str(self.population[model_number].rank))


    """
    Runs epoch - every individual in generation
    """
    def _run_epoch(self, population_number):
        client_ID = simulation.start_connection(VREP_IP_2, 
                                                VREP_PORT_2)
        movement = Movement(NAOQI_BIN_IP, NAOQI_BIN_PORT)
        
        for i in range(self.population_size):
            logging.info("INDIVIDUAL NUMBER: " + str(i))
            print("INDIVIDUAL NUMBER: " + str(i))
            self._run_simulations(i, client_ID, movement)
        
        simulation.stop_connection(client_ID)


    """
    Starts Evolution
    """
    def start_evolution(self):
        for i in range(self.populations_number) - 1:
            print("POPULATION NUMBER: " + str(i))
            self._run_epoch(i)

            new_population = self._create_population()
            self.population = new_population
        
        self._run_epoch(self.populations_number - 1)
        self._save_generation()


"""
Functionality testing created while developent
"""
if __name__ == "__main__":
    SCENES = ["../scenes/NAO1.ttt"]
    ev = Evolution(50, 30, 25, SCENES)
    ev.start_evolution()

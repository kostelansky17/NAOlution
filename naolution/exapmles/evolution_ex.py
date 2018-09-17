from naolution.evolution import Evolution

if __name__ == "__main__":
    population_size = 10
    population_number = 20
    scene_timeout = 10
    scenes = ["../scenes/NAO1.ttt", "../scenes/NAO2.ttt", "../scenes/NAO3.ttt"]

    my_evolution = Evolution(population_size, population_number, scene_timeout,scenes)
    my_evolution.start_evolution()
import os
import numpy as np
import matplotlib.pyplot as plt

GENGERATIONS = 30
POPULATION_SIZE = 50
LOG_FILE_NAME = "../../logs/evolution_18-09-29_17:15.log"
LABELS = ['Average','Best individual','Worst individual']


if __name__ == "__main__":
    lines = [line.rstrip('\n') for line in open(LOG_FILE_NAME)]
    lines_pure = lines[1::2]

    data =  np.empty((POPULATION_SIZE, GENGERATIONS))

    row = 0
    column = 0

    for line in lines_pure:
        rank = line.split(':')
        data[row][column] = rank[2] 
        row += 1
        if row == POPULATION_SIZE:
            row = 0
            column +=1
        
    data *= -1
    generations_avg = np.mean(data, axis=0)
    generations_max = data.max(axis=0)
    generations_min = data.min(axis=0)
    
    plt.figure()
    plt.plot(generations_avg, label = LABELS[0])
    plt.plot(generations_min, label = LABELS[1])
    plt.plot(generations_max, label = LABELS[2])


    plt.xlabel('Generation')
    plt.ylabel('Distance from target')
    plt.grid()
    plt.legend(loc=1)
    plt.show()

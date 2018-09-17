# NAOlution 

This project researches training Convolutional neural networks by genetic algorithm to navigate robot NAO to target objects. NAOlution was created during Research Summer 2018 at Faculty of information Technology CTU in Prague.

The project composes from three main parts:
 - Joints Manager transmits NAO's movement from NAOqi to V-REP simulator and alows you to use this framework no work with NAO in simulator
 - Evolution which is genetic algorithm running real-time in V-REP created for training CNNs
 - CNN which creates used Convolutional neural networks

## Instalation
This project is written in `Python 2.7` becouse of dependecis also written in `Python 2`. Virtual environment is installed by command ``pipenv install`` in directory `NAOlution`. You need to install V-REP simulator (version 3.4 ADD LINK TO DOWNLOAD) and NAOqi (used version 2.14... ADDLINK TO DOWNLOAD).   

## Project Structure
  ---scenes: used V-REP scenes
  ---src: source codes
  ---src/logs: every run of evolution creates own logs file
  ---src/models: contains models from evolution

## How to find V-REP and NAOqi IP & ports
TODO!


## Usage and exapmles

### To Use NAOqi framework for NAO in V-REP
 First of all you need to change ip adresses and ports in src/consts.py. Especially `vrep_ip_1` and `vrep_port_2`. 
 - Open V-REP load and run the simulation
 - Next you need to run `joints_manager.py`.
 - When is joints manager ready you can connect to NAO in NAOqi and use commands from NAOqi API. Expamle is in TODOOOOO!!!!.

### Run genetic algorithm
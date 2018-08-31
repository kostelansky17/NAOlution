# NAOlution 

This project researches training Convolutional neural networks bz genetic algorithm to navigate robot NAO to target objects and was created during project Research Summer 2018 at Faculty of information Technology in Prague.
The project composes from three main parts:
 - Joints Manager transmits NAO's movement from NAOqi to V-REP simulator and alows you to use this framework no work with NAO in V-REP
 - Evolution which is genetic algorithm running real-time in v-rep

Project Structure
  ---scenes: used V-REP scenes
  ---src: source codes
  ---src/logs: every run of evolution creates own logs file
  ---src/models: contains models from evolution


Usage
-To Use NAOqi framework for NAO in V-REP
  First of all you need to change ip adresses and ports in src/consts.py. 
- Open V-REP load and run the simulation
- run naoqi


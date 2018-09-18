# NAOlution 
This project researches training Convolutional neural networks by genetic algorithm to navigate robot NAO to target objects. NAOlution was created during Research Summer 2018 at Faculty of information Technology CTU in Prague.

The project composes from three main parts:
 - Joints Manager transmits NAO's movement from NAOqi to V-REP simulator and alows you to use this framework no work with NAO in simulator
 - Evolution which is genetic algorithm running real-time in V-REP created for training CNNs
 - CNN which creates used Convolutional neural networks and cross them over during the evolution

---

## How does it work?

---

## Project Structure
```
naolution
│   README.md
│   requriments.txt    
│   Pipfile.lock
|   setup.py
│
└───docs
│       #GitHub page sources
│
└───scenes
│       #V-REP scenes
│
└───logs
│       #where logs from evolution will be stored
│
└───models
│       #where trained models will be stored
│
└───naolution
    |   #source code
    |   evolution.py
    |   consts.py
    |
    └───examples
    |       evolution_ex.py
    |       nao_movement_ex1.py
    |       nao_movement_ex2.py
    |
    └───managers
    |       joints_manager.py
    |       movement_manager.py
    |       object_manager.py
    |       simulation_manager.py
    |       sensors_manager.py
    |       vision_manager.py
    |       vision_manager.py
    |
    └───utils
    |       checker.py
    |       cnn.py
    |
    └───vrep
            vrep.py
            vrepConst.py
            remoteApi.dylib
            remoteApi.so     

```

---

## Installation
This project is written in `Python 2.7` becouse of dependecis also written in `Python 2`. 

### V-REP
V-REP 3.4 can be freely downloaded from [V-REP page](http://www.coppeliarobotics.com/previousversions.html) for Mac, Windows and Linux.

### NAOqi
In this project was used version 2.1. Additional information and software can be found in [NAOqi installation guide](http://doc.aldebaran.com/2-1/dev/python/install_guide.html).

### Python requriments
#### Pipenv
Virtual environment can be installed by command:
```bash 
pipenv install
``` 
in directory `NAOlution`.

#### Pip
Dependencies can be installed by command:
```bash 
pip install -r requriments.txt
``` 
in directory `NAOlution`.

---

## How to find V-REP and NAOqi IPs & ports

### NAOqi
Accessable NAOqi IPs and ports are usually shown when is `NAOqi-bin` started.

### V-REP
#### Linux
Accessable V-REP ports can be listed by command:
```bash
```

---

## Usage and exapmles
First of all you need to change ip adresses and ports in `naolution/consts.py`. Especially `VREP_IP_1`, `VREP_PORT_1`, `VREP_IP_2`, `VREP_PORT_2`, `NAOQI_BIN_IP`, `NAOQI_BIN_PORT`.

### To Use NAOqi framework for NAO in V-REP
 - Open V-REP load and run the simulation
  - Run NAOqi-bin. At my computer (Ubuntu) is this done by command 
```bash
/opt/Aldebaran\ Robotics/Choregraphe\ Suite\ 2.1/bin/naoqi-bin`
```
 - Run `naolution/managers/joints_manager.py`
 - Run `nao_movement_ex1.py` or `nao_movement_ex1.py`

### Training CNNs by evolution algorithm
 - Open V-REP load and run the simulation
 - Run NAOqi-bin. At my computer (Ubuntu) is this done by command 
```bash
/opt/Aldebaran\ Robotics/Choregraphe\ Suite\ 2.1/bin/naoqi-bin`
```
 - Run `naolution/managers/joints_manager.py`
 - Run `evolution_ex.py`

---

## Participate
Any help is apriciated. If you would like to participate, please use *GitHub flow* and create reasonable names *Feature branch* and *Pull request*. 
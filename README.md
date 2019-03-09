# I-Temp

I-Temp (I-Temperature) is a open source project for intelligent temperature control in your house, office or anywhere.

# Goals

- Using cheap and contactless temperature sensor to collect users' skin temperature to know the comfort level
- Implement machine learning to predict comfort level after training
- Control Heating, Ventilation and Air Conditioning (HVAC) system based on prediction

# Getting Start

Since the project is still in progress, this is not a totally perfect guideline.

1. Purchase a temperature sensor (now we use MLX90640 Far infrared thermal sensor array (32x24 RES)). 

2. Connect the temperature sensor to micro controller (now we use OpenMV which is like a Arduino but it supports python)

3. Train the system. Give comfort level feedback and collect data of your facial temperature

   for example: 0 for too cold, 1 for cold, 2 for comfortable, 3 for hot and 4 for too hot 

   Choose a right model to make prediction

4. Send control signal to IoT (Internet of Things) platform to control your HVAC system

# Reference 

> Ghahramani, A., Castro, G., Becerik-Gerber, B. and Yu, X., 2016. Infrared thermography of human face for monitoring thermoregulation performance and estimating personal thermal comfort. *Building and Environment*, *109*, pp.1-11.


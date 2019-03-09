# I-Temp

I-Temp (I-Temperature) is a open source project for intelligent temperature control in your house, office or anywhere. (Still in progress)

# Goals

- Using cheap and contactless temperature sensor to collect users' skin temperature to know the comfort level
- Implement machine learning to predict comfort level after training
- Control Heating, Ventilation and Air Conditioning (HVAC) system based on prediction

# Advantages of I-Temp

- When you come back home after doing sports, you really want the temperature to cool down immediately. However, if you forget to turn up the temperature after you already cool your body, you may get cold. I-Temp can monitor you facial temperature which reflects your comfort level and control the temperature for you.

- Easy to train and easy to predict. The sensor is contactless like a PC camera, you just sit there and you can train it just make few feedback. It will make prediction when you are working or doing other things after training.

- Babies, children and old people might be sensitivity to temperature. It is necessary to customize control pattern for different people. This is the training process in machine learning.

- There are already some smart-house devices in market like [Ecobee4](https://www.ecobee.com/ecobee4/) but they are so expensive. I-temp can understand what you need and control the temperature for you. In addition, what you need is a sensor and a micro controller, the total cost is less than $50 and the software is right here for you.


# Getting Start

Since the project is still in progress, this is not a perfect guideline.

1. Purchase a temperature sensor (now we use [MLX90640](https://www.melexis.com/en/product/MLX90640/Far-Infrared-Thermal-Sensor-Array) Far infrared thermal sensor array (32x24 RES)). 

2. Connect the temperature sensor to micro controller (now we use [OpenMV](https://openmv.io/) which is like a Arduino but it supports python)

3. Train the system. Give comfort level feedback and collect data of your facial temperature

   for example: 0 for too cold, 1 for cold, 2 for comfortable, 3 for hot and 4 for too hot 

   Choose a right model to make prediction

4. Send control signal to IoT (Internet of Things) platform like [Thingsboard](https://thingsboard.io/) to control your HVAC system


# How to Contribute

I have some basic ideas but I have no hardware to make it come true

- Using other micro controller or platform like Arduino or Raspberry Pi
- More temperature and feedback data. As you know, different people at different age will have different thermo regulation system, and their sensitivity to temperature change really matters.
- Model choosen. More accurate model or prediction method to predict or control?
- IoT platform

# Reference 

> Ghahramani, A., Castro, G., Becerik-Gerber, B. and Yu, X., 2016. Infrared thermography of human face for monitoring thermoregulation performance and estimating personal thermal comfort. *Building and Environment*, *109*, pp.1-11.


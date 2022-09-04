#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import time
import math
import pandas as pd

# Python scripts w/ objects
from ICM20948 import ICM20948
from BME280 import BME280
# from TSL2591 import TSL2591 # Lux

# Sensors being used
icm20948 = ICM20948() # Accelerometer and Gyroscope
tempsensor = BME280() # Pressure, Temperature and Humidity
tempsensor.get_calib_param()
start = time.time()
# luxsensor = TSL2591()
# luxsensor.SET_LuxInterrupt(20, 200)

# df = pd.read_csv('./outputs/sensorReadings.csv')

print('Sensor Readings')
print('Time (s), Temperature (F), Roll (deg), Pitch (deg), AccX (g), AccY (g), AccZ (g)')

try:
	while True:
		# time.sleep(1) # How long to wait between readings
		# lux = luxsensor.Lux() # getting lux value
		icm = icm20948.getdata() # getting accelerometer and gyroscope data
		tempdata = tempsensor.readData() # getting pressure, temperature, humidity data

		roll, pitch, yaw, accX, accY, accZ, gyroX, gyroY, gyroZ, magX, magY, magZ = icm
		pres, temp, hum = tempdata
		
		# functions to change output format
		now = time.time() - start
		accX = accX / 2048 # turns output into g-force units
		accY = accY / 2048
		accZ = accZ / 2048
		temp = temp * 9/5 + 32 # convert to Fahrenheit
		# hum = hum * 100 # convert to percentage
		# pres = pres * 0.0145037738 # convert hPa to psi

		# Time, Temperature, Roll, Pitch, AccX, AccY, AccZ
		# df.loc[len(df.index)] = [now,temp,roll,pitch,accX,accY,accZ] 

		print("%.2f , %.2f , %.2f , %.2f , %.2f , %.2f , %.2f" %(now,temp,roll,pitch,accX,accY,accZ), end="\r")
		
				# print("/-------------------------------------------------------------/")
				# print("Lux: %d" %lux)
				# print("Roll = %.2f , Pitch = %.2f , Yaw = %.2f" %(icm[0],icm[1],icm[2]))
				# print("Acceleration: X = %d, Y = %d, Z = %d" %(icm[3],icm[4],icm[5]))
				# print("Gyroscope:     X = %d , Y = %d , Z = %d" %(icm[6],icm[7],icm[8]))
				# print("Magnetic:      X = %d , Y = %d , Z = %d" %(icm[9],icm[10],icm[11]))
				# print("pressure : %7.2f hPa" %tempdata[0])
				# print("temp : %-6.2f ℃" %tempdata[1])
				# print("hum : %6.2f ％" %tempdata[2])
		
except KeyboardInterrupt:
	# sensor.Disable()
	# print('Writing to file /outputs/sensorReadings.csv')
	# df.to_csv('./outputs/sensorReadings.csv', index=False, float_format='%.2f')
	exit()

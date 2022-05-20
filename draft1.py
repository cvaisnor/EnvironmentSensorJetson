#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import time
import math
import pandas as pd

from TSL2591 import TSL2591
from ICM20948 import ICM20948
from BME280 import BME280

luxsensor = TSL2591()
icm20948 = ICM20948()

tempsensor = BME280()
tempsensor.get_calib_param()


luxsensor.SET_LuxInterrupt(20, 200)
time.sleep(1)

df = pd.read_csv('./outputs/sensorReadings.csv')

try:
	while True:
		time.sleep(2)
		lux = luxsensor.Lux()
		# print("Lux: %d" %lux)

		icm = icm20948.getdata()
		# print("/-------------------------------------------------------------/")
		# print("Roll = %.2f , Pitch = %.2f , Yaw = %.2f" %(icm[0],icm[1],icm[2]))
		# print("Acceleration: X = %d, Y = %d, Z = %d" %(icm[3],icm[4],icm[5]))
		# print("Gyroscope:     X = %d , Y = %d , Z = %d" %(icm[6],icm[7],icm[8]))
		# print("Magnetic:      X = %d , Y = %d , Z = %d" %(icm[9],icm[10],icm[11]))

		tempdata = tempsensor.readData()
		
		# print("pressure : %7.2f hPa" %data[0])
		# print("temp : %-6.2f ℃" %data[1])
		# print("hum : %6.2f ％" %data[2])

		df.loc[len(df.index)] = [lux,tempdata[1],icm[0],icm[1],icm[2],icm[3],icm[4],icm[5],icm[6],icm[7],icm[8]] 
		# Lux, Temperature, Roll, Pitch, Yaw, AccX, AccY, AccZ, GyroX, GyroY, GyroZ,
		
		
except KeyboardInterrupt:
	# sensor.Disable()
	df.to_csv('./outputs/sensorReadings.csv', index=False)
	exit()
"""Case Study: Aircraft Engine Sensor Matrix Analysis for Predictive Maintenance

You are working in an aerospace company.

Each aircraft engine has:

						5 temperature sensors
						5 vibration sensors
						5 pressure sensors

Data from multiple engines is collected as multidimensional NumPy arrays.

The company wants to:

					preprocess engine data
					identify abnormal engines
					normalize sensor readings
					prepare matrices for future ML anomaly detection models

Faulty sensor criteria :
				->constant/dead sensor reading [20,20,20,20,20,20]
				->excessive noise/random fluctuations [sudden spike or drop]
				->physically impossible values
				->high missing data percentage (NaN, NaN, NaN) around 30-50%
				->slowly deviats over time 
					"""

import numpy as np
engine_o=np.arange(3*5*3).reshape(3,5,3)
engine_n=engine_o.reshape(15,3)
print(f"previous dataset: \n{engine_o} \n"+"=="*20+f"\nreshaped: \n{engine_n}")

def sensor_data_classifying(arr):
	#creating a default condition
	result=np.full(arr.shape, "normal", dtype=object)
	result[arr[:,0]>120, 0] = "OH" #over heating
	result[arr[:, 1]>80, 1] = "MI" #mechanical instability 
	result[arr[:, 2]<40, 2] = "HRF" #hydrolic risk faliure
	return result

results=sensor_data_classifying(engine_n)

mean=np.mean(engine_n, axis=0)
std=np.std(engine_n, axis=0)
normalized=(engine_n-mean)/std
new_mean=np.mean(normalized, axis=0)
new_std=np.std(normalized, axis=0)

# fault sensor isolation 
dead_sensor=np.std(engine_n, axis=0) == 0 # when there is no variation between the mean and the data

noise_sensor=np.abs(np.diff(engine_n))
noise=noise_sensor>150 # sudden spike

engine_n=engine_n.astype(float)

engine_n[(engine_n<0) | (engine_n>300)] = np.nan
missing_data=np.mean(np.isnan(engine_n), axis=0)
bad_sensor=missing_data>0.35           # where the NaN is apprearing more no of times 

cleaned_sensor=engine_n[:, ~bad_sensor]

# storeing the values in a file formate(.txt)
file=open("sensor_repot_for_aircraft", "w")
file.write(f"dead sensor :{dead_sensor}\nsuddenspike in sensor reading :{noise}\nsensor haveing higher missing data: {bad_sensor}")
file.write("="*35)
file.write(f"cleaned sensor data: {cleaned_sensor}")
file.write("="*35)
file.close()

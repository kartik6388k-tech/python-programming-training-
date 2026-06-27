"""Case Study: CNC Machine Vibration Monitoring for Predictive Maintenance

You are working in a mechanical manufacturing plant.

A CNC machine produces shafts continuously.

A vibration sensor records machine vibration values every hour.

The data is stored inside a text file:

vibration_data.txt

Example file content:

45
78
120
error
65
999
34

Meaning:

normal numeric values → valid vibration readings
"error" → corrupted sensor data
999 → emergency machine shutdown signal

The company wants to build an ML-ready preprocessing system before training a predictive maintenance model."""

def mashine_health(vib):
	if vib<50:
		return "Stable" 
	
	elif 50<=vib<=100:
		return "Warning"
	
	elif 100<vib:
		return "Critical"

class Emergency(Exception):
	print("Emergency Shutdown Detected")
	pass
count_s, count_w, count_c, count_e=0,0,0,0	

file=open("vibration_data.txt", "r")

for i in file:
	line=i.strip()

	current=mashine_health(value)
	if current=="Critical":
		count_c+=1
	if current=="Warning":
		count_w+=1
	if current=="Stable":
		count_s+=1

	try :
		if line=="error":
			raise ValueError
		value=int(line)
		if value==999:
			count_e+=1
			raise Emergency
	except ValueError:
		print("Corrupted Sensor Reading")
		continue
	except Emergency:
		print("Emergency Shutdown Detected")
		break 

	print(f"codition of mashine :{current}")

file.close()
	    

#task3 
file = open("maintenance_report.txt", "w") #as we are createing new report 
file.write(f"total Stable readings: {count_s}\n")
file.write(f"total Warning readings: {count_w}\n")
file.write(f"total Critical readings: {count_c}\n")
file.write(f"emergency shutdown occurrence: {count_e}\n")
file.close()

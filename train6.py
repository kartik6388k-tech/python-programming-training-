"""Case Study: Industrial Boiler Monitoring System

You are working in a thermal power plant.

Multiple industrial boilers are operating simultaneously.

Each boiler sends:

pressure value (bar)
temperature value (°C)

Safety Rules:

Pressure < 50 AND temperature < 200
→ "Stable"
Pressure between 50–80 OR temperature between 200–350
→ "Warning"
Pressure > 80 OR temperature > 350
→ "Critical"

The company now wants modular software because hundreds of boilers will later be
 connected to an ML-based predictive maintenance system."""


def boiler_status(pressure, temprature):
	#analysising the codition 
	if pressure>80 or temprature>350:
		return "critical"
	elif 50<=pressure<=80 or 200<=temprature<=350:
		return "Warning"
	elif pressure<50 and temprature<200:
		return "Stable"

count=0
for i in range(1,4):
	globals()[f"boiler_p{i}"] = int(
		input(f"Enter value for boiler_{i} pressure in *bar*:")
		)
	
	globals()[f"boiler_t{i}"] = int(
		input(f"Enter value for boiler_{i} temprature in *degree c*:")
		)

for i in range(1,4):
	status=boiler_status(
		globals()[f"boiler_p{i}"],
		globals()[f"boiler_t{i}"])
	
	if status=="critical":
		count+=1

print ("boiler having critical condition :"+str(count))

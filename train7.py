"""Case Study: Smart Grid Power Distribution Monitoring System

You are working in an electrical power distribution control center.

Multiple substations send:

voltage readings
current readings

The system calculates:

Power = Voltage × Current

But real sensor networks are unreliable:

operators may enter text instead of numbers
current may become zero
corrupted values may occur
emergency shutdown may happen

Your task is to build a fault-tolerant monitoring system."""

count=0

class emergecy(Exception):
    pass

def power_classify(num):
    if num < 500:
        return "low load"
    if 500 <= num < 2000:
        return "normal load"
    return "high load"


for i in range(1,6):
    try:
        voltage = float(input("Enter the voltage reading :"))
        
        if voltage==999:
            raise emergecy
        
        current = float(input("Enter the current reading :"))
        
        power = voltage * current
        x = power_classify(power)
        
        if x == "high load":
            count += 1

    except ValueError:
        print("Invalid Sensor Input")
        continue
    except emergecy:
        print("Emergency Shutdown Triggered")
        
    finally:
        print(f"Substation {i}:{x}")
        
print (f"no of substation at higfh load:{count}")




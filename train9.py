"""Case Study: Hydraulic Press Monitoring System

You are working in an automotive manufacturing plant.

A hydraulic press machine is monitored continuously.

Each machine has:

machine ID
pressure value
temperature value

The company wants to move from basic scripting toward an object-oriented 
monitoring architecture because future ML systems will manage hundreds of 
machines simultaneously."""

class Machine:
    def __init__(self, machine_id, pressure, temperature):
        self.machine_id = machine_id
        self.pressure = pressure
        self.temperature = temperature

    def machine_status(self):
        if self.pressure > 180 or self.temperature > 120:
            return "Critical"
        elif 100 <= self.pressure <= 180 or 80 <= self.temperature <= 120:
            return "Warning"
        else:
            return "Stable"


def store_report(count_s, count_w, count_c):
    with open("press_report.txt", "a") as file:
        file.write("Categorization of machine based on their condition\n")
        file.write(f"machine in stable condition :{count_s}\n")
        file.write(f"machine in warning condition :{count_w}\n")
        file.write(f"machine in critical condition:{count_c}\n")


def main():
    try:
        machine_count = int(input("enter the no of machines: "))
    except ValueError:
        print("Invalid number of machines.")
        return

    count_s = count_w = count_c = 0
    for i in range(machine_count):
        machine_id = input(f"enter the machine id for machine {i+1}: ")
        try:
            pressure = float(input("enter the pressure value: "))
            temperature = float(input("enter the temperature value: "))
        except ValueError:
            print("Invalid pressure or temperature value.")
            continue

        m = Machine(machine_id, pressure, temperature)
        status = m.machine_status()
        if status == "Stable":
            count_s += 1
        elif status == "Warning":
            count_w += 1
        else:
            count_c += 1

        print(f"Machine {m.machine_id}: {status}")

    store_report(count_s, count_w, count_c)




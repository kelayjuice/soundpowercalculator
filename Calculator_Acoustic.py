import numpy as np
import math
from cmath import pi

def workdone(distance, mass):
    Force = mass * 9.81
    return Force * distance

distance = float(input("Height off the ground (in meters): "))
mass = float(input("Mass of the object (in kg): "))

work = workdone(distance, mass)
print(f"Work Done: {work} Joules")

def powerovertime(time, work):
    return work / time

time = np.array([10, 20, 30, 40, 50, 60])
power_time = powerovertime(time, work)

for t, powertime in zip(time, power_time):
    print(f"Time: {t}, Power: {powertime}")

def frequency(radius, power_time):
    rho = 1.225
    v = 343
    smax = 1e-6
    surface_area = 4 * pi *(radius) ** 2

    # Calculate frequency using the power_time and radius arrays
    freq = (1 / (2 * pi)) * np.sqrt((power_time * 2) / (surface_area * (smax ** 2) * rho * v))
    return freq

radius = float(input("Radius of Speaker (in meters): "))
corresponding_frequency = frequency(time, power_time)

for t, freq in zip(time, corresponding_frequency):
    print(f"Time: {t}, Frequency: {freq}")

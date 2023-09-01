# Relate rod diameter, force applied and stress
# see documentation (plan.pdf) for calculations
# Calculate cross-sectional area while at it...

# import maths module for usage of pi and sqrt function
import math


# find stress (MPa), given the diameter and force values (in mm and kN, respectively)
def find_stress(var_force, var_diameter):
    var_stress = (4000 * var_force) / (math.pi * (var_diameter ** 2))
    return var_stress


# find force (kN), given the stress and diameter values (in MPa and mm, respectively)
def find_force(var_diameter, var_stress):
    var_force = (math.pi * var_stress * (var_diameter ** 2)) / 4000
    return var_force


# find diameter (mm), given the stress and force values (in MPa and kN, respectively)
def find_diameter(var_stress, var_force):
    var_diameter = math.sqrt((4000 * var_force) / (math.pi * var_stress))
    return var_diameter


# find cross-sectional area (m^2), given the stress and force values (in MPa and kN, respectively)
def find_cross_sect_area(var_stress, var_force):
    var_area = var_force / (1000 * var_stress)
    return var_area


# MAIN ROUTINE

# diameter = 0  # set diameter value (mm)
# force = 0  # set force value (kN)
# stress = 0  # set stress value (MPa)

round_dp = 1
mode = input("What would you like to find?\nStress (A)\nForce (B)\nDiameter (C)\nType here: ").lower

if mode == 'a':
    force = float(input('Enter applied load in kN: '))
    diameter = float(input('Enter rod diameter in mm: '))
    stress = round(find_stress(force, diameter), round_dp)
    print("Given a rod diameter of {} mm and an applied load of {} kN, the appropriate stress is {} MPA"
          .format(diameter, stress, force))
elif mode == 'b':
    stress = float(input('Enter applied stress in MPa: '))
    diameter = float(input('Enter rod diameter in mm: '))
    force = round(find_force(diameter, stress), round_dp)
    print("Given a rod diameter of {} mm and an applied stress of {} MPa, the appropriate load is {} kN"
          .format(diameter, stress, force))
elif mode == 'c':
    force = float(input('Enter applied load in kN: '))
    stress = float(input('Enter applied stress in MPa: '))
    diameter = round(find_diameter(stress, force), round_dp)
    print("Given a rod diameter of {} mm and an applied stress of {} MPa, the appropriate load is {} kN"
          .format(diameter, stress, force))
else:
    print("Error! You didn't pick a correct mode!")

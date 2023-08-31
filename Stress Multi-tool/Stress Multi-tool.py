# Relate rod diameter, force applied and stress
# see documentation (plan.pdf) for calculations
# Calculate cross-sectional area while at it...

# import maths module for usage of pi and sqrt function
import math


# find diameter (mm), given the stress and force values (in MPa and kN, respectively)
def find_diameter(var_stress, var_force):
    var_diameter = math.sqrt((4000 * var_force) / (math.pi * var_stress))
    return var_diameter


# find stress (MPa), given the diameter and force values (in mm and kN, respectively)
def find_stress(var_force, var_diameter):
    var_stress = (4000 * var_force) / (math.pi * (var_diameter ** 2))
    return var_stress


# find force (kN), given the stress and diameter values (in MPa and mm, respectively)
def find_force(var_diameter, var_stress):
    var_force = (math.pi * var_stress * (var_diameter ** 2)) / 4000
    return var_force


# find cross-sectional area (m^2), given the stress and force values (in MPa and kN, respectively)
def find_cross_sect_area(var_stress, var_force):
    var_area = var_force / (1000 * var_stress)
    return var_area


# MAIN ROUTINE
diameter = 0  # set diameter value (mm)
force = 0  # set force value (kN)
stress = 0  # set stress value (MPa)


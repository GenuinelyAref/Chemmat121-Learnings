# Tool to help with calculating different quantities in the fracture mechanics equation
# import math library to use exact value of pi
import math


# calculate k_1
def k_1_calculation(var_y, var_stress, var_a):
    var_k_1 = var_y * var_stress * math.sqrt(math.pi * var_a)
    return var_k_1


# calculate a value, depending on crack size and crack type
def a_type_calculation(var_crack_length, var_crack_type):
    if var_crack_type == "internal":
        var_a = var_crack_length / 2
    else:
        var_a = var_crack_length
    return var_a


# calculate dimensionless geometric factor
def geometric_factor_calculation(var_stress, var_a, var_k_1):
    var_y = var_k_1 / (var_stress * math.sqrt(math.pi * var_a))
    return var_y


# calculate stress on part (not on crack/notch)
def stress_calculation(var_y, var_a, var_k_1):
    var_stress = var_k_1 / (var_y * math.sqrt(math.pi * var_a))
    return var_stress


# calculate a-value based on other parameters
def a_value_calculation(var_y, var_stress, var_k_1):
    var_a = ((var_k_1 / (var_y * var_stress)) ** 2) / math.pi
    return var_a


# converts any value to its SI unit size
def convert_si_units(var_value, var_order_magnitude):
    var_si_equivalent = var_value * (10 ** var_order_magnitude)
    return var_si_equivalent


def convert_conventional_unit(var_value, var_order_magnitude):
    var_conventional_unit = var_value * (1 / (10 ** var_order_magnitude))
    return var_conventional_unit


# MAIN ROUTINE
# constants
stress_magnitude = 6  # Mega in MPa --> 10^(6)
k_1_magnitude = 6  # Mega in MPa m^0.5 --> 10^(6)
a_magnitude = -3  # milli in mm --> 10^(-3)


# values used
rounding_dp = 2  # number of decimal places to round output to
a = 11.3  # in mm
nominal_stress = 592  # in MPa
y = 1.2  # dimensionless geometric constant

# adjust value of a depending on crack size
a = a_type_calculation(a, "internal")

# convert all units to SI
a = convert_si_units(a, a_magnitude)
nominal_stress = convert_si_units(nominal_stress, stress_magnitude)

k_1_value = k_1_calculation(y, nominal_stress, a)
k_1_value = convert_conventional_unit(k_1_value, k_1_magnitude)
print("K\u2081 value is: {} MPa m^0.5".format(round(k_1_value, rounding_dp)))

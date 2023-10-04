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
        a = var_crack_length / 2
    else:
        a = var_crack_length
    return a


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

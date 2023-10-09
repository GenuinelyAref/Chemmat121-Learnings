# calculator for different values in the creep rate equation
# note: rate of creep = change in strain / change in time
import math


def celsius_to_kelvin(var_celsius):
    kelvin = var_celsius + 273.15
    return kelvin


def calc_creep_rate(var_constant, var_activation_energy, var_r, var_temperature):
    rate = var_constant * (math.e ** ((-1 * var_activation_energy) / (var_r * var_temperature)))
    return rate


def calc_temp(var_constant, var_activation_energy, var_r, var_creep_rate):
    var_temperature = (-1 * (var_r / var_activation_energy)) / (math.log(var_constant) - math.log(var_creep_rate))
    return var_temperature


def calc_constant(var_activation_energy, var_r, var_temperature, var_creep_rate):
    rate = var_creep_rate / (math.e ** ((-1 * var_activation_energy) / (var_r * var_temperature)))
    return rate


universal_gas_constant = 8.314  # J / mol K
mode = 2  # modes: 1 --> rate, 2 --> temperature

if mode == 1:
    print(calc_creep_rate(3 * (10 ^ -6), 40000, universal_gas_constant, celsius_to_kelvin(85)))
elif mode == 2:
    print(calc_temp(3 * (10 ^ -6), 40000, universal_gas_constant, -7.034 * (10 ^ -5)))
elif mode == 3:
    print(calc_constant(40000, universal_gas_constant, celsius_to_kelvin(85), -7.034 * (10 ^ -5)))

# calculator for different values in the arrhenius equation
# note: rate = 1/time
import math


def celsius_to_kelvin(var_celsius):
    kelvin = var_celsius + 273.15
    return kelvin


def calc_rate(var_constant, var_activation_energy, var_r, var_temperature):
    rate = var_constant * (math.e ** ((-1 * var_activation_energy) / (var_r * var_temperature)))
    return rate


def calc_temp(var_constant, var_activation_energy, var_r, var_rate):
    var_temperature = (-1*(var_r/var_activation_energy))/(math.log(var_constant) - math.log(var_rate))
    return var_temperature

# Tool to help with calculating yield stress & grain size using hall-petch equation

# find yield stress (MPa), given the grain size, k and yield stress naught values
def find_yield_stress(var_yield_naught, var_k, var_grain_size):
    var_yield_stress = var_yield_naught + (var_k * (var_grain_size ** -0.5))
    return var_yield_stress


# find force (kN), given the stress and diameter values (in MPa and mm, respectively)
def find_grain_size(var_yield_stress, var_yield_naught, var_k):
    var_grain_size = (var_k / (var_yield_stress - var_yield_naught)) ** 2
    return var_grain_size


round_dp = 1
mode = input("What would you like to find?\nYield Stress (A)\nGrain Size (B)\nType here: ").lower

if mode == 'a':
    yield_naught = float(input('Enter yield naught (MPa): '))
    k = float(input('Enter k value: '))
    grain_size = float(input('Enter grain size in mm: '))
    yield_stress = round(find_yield_stress(yield_naught, k, grain_size), round_dp)
    #print("Given a rod diameter of {} mm and an applied load of {} kN, the appropriate stress is {} MPA"
          #.format(diameter, stress, force))
"""elif mode == 'b':
    stress = float(input('Enter applied stress in MPa: '))
    diameter = float(input('Enter rod diameter in mm: '))
    force = round(find_force(diameter, stress), round_dp)
    print("Given a rod diameter of {} mm and an applied stress of {} MPa, the appropriate load is {} kN"
          .format(diameter, stress, force))

"""
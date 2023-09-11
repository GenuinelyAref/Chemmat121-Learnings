# Tool to help with calculating yield stress & grain size using hall-petch equation


# find the k-value using two points on the hall petch equation graph
def find_k_value(var_points_list, var_adjustment_factor):
    [var_d_1, var_y_1, var_d_2, var_y_2] = var_points_list[0:4]
    if var_adjustment_factor == 'raw_value':
        var_d_1 = var_d_1 ** -0.5
        var_d_2 = var_d_2 ** -0.5
    var_k = (var_y_2 - var_y_1) / (var_d_2 - var_d_1)
    return var_k


# find yield stress (MPa), given the grain size, k and yield stress naught values
def find_yield_stress(var_yield_naught, var_k, var_grain_size):
    var_yield_stress = var_yield_naught + (var_k * (var_grain_size ** -0.5))
    return var_yield_stress


# find force (kN), given the stress and diameter values (in MPa and mm, respectively)
def find_grain_size(var_yield_stress, var_yield_naught, var_k):
    var_grain_size = (var_k / (var_yield_stress - var_yield_naught)) ** 2
    return var_grain_size


# MAIN ROUTINE

# answer rounding precision
round_dp = 5

# get input for type of measurement to solve for
mode = input("What would you like to find?\n"
             "Yield Stress (A)\n"
             "Grain Size (B)\n"
             "Type here: ").lower()

# get input for k-value input options
k_input = input("\nChoose an option for the k-value\n"
                "I know the k-value (A)\n"
                "Calculate it for me using two points from the graph (B)\n"
                "Calculate it for me using two grain size values (mm) (C)\n"
                "Type here: ").lower()

print()

# get k value / parameters
if k_input == 'a':
    # get value of k 'as-is'
    k = float(input('Enter k value: '))
elif k_input == 'b':
    # get 2 yield stress values and 2 d^-0.5 sizes
    k_list = [
        float(input('Enter the first d^-0.5 (x) value: ')),
        float(input('Enter the first yield stress (y) value: ')),
        float(input('Enter the second d^-0.5 (x) value: ')),
        float(input('Enter the second yield stress (y) value: '))
    ]
    # calculate the value of k
    k = find_k_value(k_list, 'half_done')
else:
    # get 2 yield stress values and 2 grain sizes
    k_list = [
        float(input('Enter the first grain size value (mm): ')),
        float(input('Enter the first yield stress (MPa) value: ')),
        float(input('Enter the second grain size value (mm): ')),
        float(input('Enter the second yield stress (MPa) value: '))
    ]
    # calculate the value of k
    k = find_k_value(k_list, 'raw_value')

# get yield stress naught value from user
yield_naught = float(input('\nEnter y\u2080 (MPa): '))

print()

# calculate yield stress
if mode == 'a':
    # get grain size input
    grain_size = float(input('Enter grain size in mm: '))
    # calculate yield stress
    yield_stress = round(find_yield_stress(yield_naught, k, grain_size), round_dp)
    # print result
    print("\nGiven a y\u2080 of {} MPa, a k value of {} and a grain size of {} mm, the yield stress is {} MPa."
          .format(yield_naught, round(k, round_dp), grain_size, yield_stress))

# calculate grain size
else:
    # get yield stress input
    yield_stress = float(input('Enter yield stress (MPa): '))
    # calculate grain size
    grain_size = round(find_grain_size(yield_stress, yield_naught, k), round_dp)
    # print result
    print("\nGiven a yield stress value of {} MPa, y\u2080 of {} MPa and a k value of {}, the grain size is {} mm."
          .format(yield_stress, yield_naught, round(k, round_dp), grain_size))

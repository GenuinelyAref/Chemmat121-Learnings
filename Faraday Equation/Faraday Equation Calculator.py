# this tool will aide in the calculation of the different quantities in faraday's equation for corrosion

# m = (I * t * M) / (F * n)

def get_electrons():
    num_electrons = int(input("Electrons: "))
    return num_electrons


def get_current():
    current_amount = float(input("Current (A): "))
    return current_amount


def get_time():
    time_unit = (input("Unit of time, choose from Y (year), W (week), D (day) or S (seconds): ").lower())[0]
    time_prefixes = ["second", "day", "week", "year"]
    if time_unit == "y":
        # unit is year
        time_multiplier = 31536000  # number of seconds in a year (based on 365 days)
    elif time_unit == "w":
        # unit is week
        time_multiplier = 604800  # number of seconds in a week
    elif time_unit == "d":
        # unit is day
        time_multiplier = 86400  # number of seconds in a day
    else:
        # unit is seconds
        time_multiplier = 1  # number of seconds in an hour
    try:
        time_prefix = time_prefixes.index(time_unit)
    except ValueError:

    amount_time = input("Number of {}s: ")


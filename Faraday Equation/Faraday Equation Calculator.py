# this tool will aide in the calculation of the different quantities in faraday's equation for corrosion

# m = (I * t * M) / (F * n)

def get_electrons():
    num_electrons = int(input("Electrons: "))
    return num_electrons


def get_current():
    current_amount = float(input("Current (A): "))
    return current_amount


def get_time():
    time_unit = (input("Unit of time, choose from Y (year), W (week), D (day) or H (hour): ").lower())[0]
    time_multiplier = 1
    if time_unit == "Y":
        # unit is year
        time_multiplier = 31536000  # number of seconds in a year (based on 365 days)
    elif time_unit == "W":
        # unit is week
        time_multiplier = 604800  # number of seconds in a week
    elif time_unit == "D":
        # unit is day
        time_multiplier = 86400  # number of seconds in a day
    else:
        # unit is hour
        time_multiplier = 3600  # number of seconds in an hour


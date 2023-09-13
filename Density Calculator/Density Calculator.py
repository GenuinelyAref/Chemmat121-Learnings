# tool to help in calculating density of object

def find_volume(var_structure_type, var_radius):
    var_radius = var_radius / (10 ** 9) # convert to metres
    if var_structure_type == 'bcc':
        a = (4 * var_radius) / (3 ** 0.5)
    else:
        a = (4 * var_radius) / (2 ** 0.5)
    var_volume = a^3 * (10 ** 6)
    return var_volume


# number of atoms in unit cell
structure_type = 'bcc'  # could also be 'fcc'
atomic_radius = 0.109 # in nanometers
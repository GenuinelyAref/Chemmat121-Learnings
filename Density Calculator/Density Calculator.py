# tool to help in calculating density of object

# find volume of unit cell based on atomic radius and structure type
def find_volume(var_structure_type, var_radius):
    var_radius = var_radius / (10 ** 9)  # convert to metres
    if var_structure_type == 'bcc':
        a = (4 * var_radius) / (3 ** 0.5)
    else:
        a = (4 * var_radius) / (2 ** 0.5)
    var_volume = (a ** 3) * (10 ** 6)  # calculate volume & convert to cm^3
    return var_volume


# match number of atoms per unit cell with structure type
def get_atom_num(var_structure_type):
    if var_structure_type == 'bcc':
        var_atom_num = 2
    else:
        var_atom_num = 4
    return var_atom_num


# calculate density
def find_density(var_n, var_atomic_mass, var_volume, var_avogadro_num):
    var_density = (var_n * var_atomic_mass) / (var_volume * var_avogadro_num)
    return var_density


# calculate the atomic radius
def find_atomic_radius(var_n, var_atomic_mass, var_avogadro_num, var_density, var_structure_type):
    var_atomic_volume = (var_n * var_atomic_mass) / (var_density * var_avogadro_num)
    var_atomic_volume = var_atomic_volume / (10 ** 6)
    if var_structure_type == 'bcc':
        # calculate atomic radius for bcc and convert to nanometers
        var_atomic_radius = ((var_atomic_volume ** (1/3)) * (3 ** 0.5) * 0.25) * (10 ** 9)
    else:
        # calculate atomic radius for fcc and convert to nanometers
        var_atomic_radius = ((var_atomic_volume ** (1 / 3)) * (2 ** 0.5) * 0.25) * (10 ** 9)
    return var_atomic_radius


def find_atomic_mass(var_n, var_volume, var_avogadro_num, var_density):
    var_atomic_mass = (var_volume * var_avogadro_num * var_density) / var_n
    return var_atomic_mass


# MAIN ROUTINE
avogadro_num = 6.022 * (10 ** 23)  # in mol^-1

structure_type = 'fcc'  # could also be 'fcc'
rounding_dp = 3  # 3dp of rounding
mode = 1  # mode 1 for finding density, mode 2 for finding atomic radius, mode 3 for finding atomic (molar) mass

# calculate number of atoms in unit cell
n = get_atom_num(structure_type)

# find density
if mode == 1:
    # set atomic radius
    atomic_radius = float(input("Enter the atomic radius in nanometres: "))  # in nanometers
    # calculate volume
    volume = find_volume(structure_type, atomic_radius)  # in cm^3
    # set atomic mass
    atomic_mass = float(input("Enter the atomic mass in g/mol: "))  # in g mol^-1
    # calculate density
    density = find_density(n, atomic_mass, volume, avogadro_num)  # in g/cm^3
    print("\nDensity: {} g/cm\u00b3".format(round(density, rounding_dp)))

# find atomic radius
elif mode == 2:
    # set atomic mass
    atomic_mass = float(input("Enter the atomic mass in g/mol: "))  # in g mol^-1
    # set density
    density = float(input("Enter the density in g/cm^3: "))  # in g/cm^3
    # calculate atomic radius
    atomic_radius = find_atomic_radius(n, atomic_mass, avogadro_num, density, structure_type)  # in nanometres
    print("\nAtomic radius = {} nm".format(round(atomic_radius, rounding_dp)))

# find atomic mass
else:
    # set density
    density = float(input("Enter the density in g/cm^3: "))  # in g/cm^3
    # set atomic radius
    atomic_radius = float(input("Enter the atomic radius in nanometres: "))  # in nanometers
    # calculate volume
    volume = find_volume(structure_type, atomic_radius)  # in cm^3
    # calculate atomic mass:
    atomic_mass = find_atomic_mass(n, volume, avogadro_num, density)  # in g mol^-1
    print("\nAtomic mass = {}g".format(round(atomic_mass, rounding_dp)))

import numpy as np
Yprimordial = 0.2437  # Eqn 83 from https://ui.adsabs.harvard.edu/abs/2020A%26A...641A...6P/abstract

# Result of running symbol_to_name()
symbol_to_element = {'H': 'Hydrogen', 'He': 'Helium', 'Li': 'Lithium', 'Be': 'Beryllium', 'B': 'Boron', 'C': 'Carbon', 'N': 'Nitrogen', 'O': 'Oxygen', 'F': 'Fluorine', 'Ne': 'Neon', 'Na': 'Sodium', 'Mg': 'Magnesium', 'Al': 'Aluminium', 'Si': 'Silicon', 'P': 'Phosphorus', 'S': 'Sulfur', 'Cl': 'Chlorine', 'Ar': 'Argon', 'K': 'Potassium', 'Ca': 'Calcium', 'Sc': 'Scandium', 'Ti': 'Titanium', 'V': 'Vanadium', 'Cr': 'Chromium', 'Mn': 'Manganese', 'Fe': 'Iron', 'Co': 'Cobalt', 'Ni': 'Nickel', 'Cu': 'Copper', 'Zn': 'Zinc', 'Ga': 'Gallium', 'Ge': 'Germanium', 'As': 'Arsenic', 'Se': 'Selenium', 'Br': 'Bromine', 'Kr': 'Krypton', 'Rb': 'Rubidium', 'Sr': 'Strontium', 'Y': 'Yttrium', 'Zr': 'Zirconium', 'Nb': 'Niobium', 'Mo': 'Molybdenum', 'Tc': 'Technetium', 'Ru': 'Ruthenium', 'Rh': 'Rhodium', 'Pd': 'Palladium', 'Ag': 'Silver', 'Cd': 'Cadmium', 'In': 'Indium', 'Sn': 'Tin', 'Sb': 'Antimony', 'Te': 'Tellurium', 'I': 'Iodine', 'Xe': 'Xenon', 'Cs': 'Caesium', 'Ba': 'Barium', 'La': 'Lanthanum', 'Ce': 'Cerium', 'Pr': 'Praseodymium', 'Nd': 'Neodymium', 'Pm': 'Promethium', 'Sm': 'Samarium', 'Eu': 'Europium', 'Gd': 'Gadolinium', 'Tb': 'Terbium', 'Dy': 'Dysprosium', 'Ho': 'Holmium', 'Er': 'Erbium', 'Tm': 'Thulium', 'Yb': 'Ytterbium', 'Lu': 'Lutetium', 'Hf': 'Hafnium', 'Ta': 'Tantalum', 'W': 'Tungsten', 'Re': 'Rhenium', 'Os': 'Osmium', 'Ir': 'Iridium', 'Pt': 'Platinum', 'Au': 'Gold', 'Hg': 'Mercury', 'Tl': 'Thallium', 'Pb': 'Lead', 'Bi': 'Bismuth', 'Po': 'Polonium', 'At': 'Astatine', 'Rn': 'Radon', 'Fr': 'Francium', 'Ra': 'Radium', 'Ac': 'Actinium', 'Th': 'Thorium', 'Pa': 'Protactinium', 'U': 'Uranium', 'Np': 'Neptunium', 'Pu': 'Plutonium', 'Am': 'Americium', 'Cm': 'Curium', 'Bk': 'Berkelium', 'Cf': 'Californium', 'Es': 'Einsteinium', 'Fm': 'Fermium', 'Md': 'Mendelevium', 'No': 'Nobelium', 'Lr': 'Lawrencium', 'Rf': 'Rutherfordium', 'Db': 'Dubnium', 'Sg': 'Seaborgium', 'Bh': 'Bohrium', 'Hs': 'Hassium', 'Mt': 'Meitnerium', 'Ds': 'Darmstadtium', 'Rg': 'Roentgenium', 'Cn': 'Copernicium', 'Nh': 'Nihonium', 'Fl': 'Flerovium', 'Mc': 'Moscovium', 'Lv': 'Livermorium', 'Ts': 'Tennessine', 'Og': 'Oganesson'}
# Result of running read_weights()
element_weights = {'Hydrogen': 1.008, 'Helium': 4.002602, 'Lithium': 6.94, 'Beryllium': 9.0121831, 'Boron': 10.81, 'Carbon': 12.011, 'Nitrogen': 14.007, 'Oxygen': 15.999, 'Fluorine': 18.998403162, 'Neon': 20.1797, 'Sodium': 22.98976928, 'Magnesium': 24.305, 'Aluminium': 26.9815384, 'Silicon': 28.085, 'Phosphorus': 30.973761998, 'Sulfur': 32.06, 'Chlorine': 35.45, 'Argon': 39.95, 'Potassium': 39.0983, 'Calcium': 40.078, 'Scandium': 44.955907, 'Titanium': 47.867, 'Vanadium': 50.9415, 'Chromium': 51.9961, 'Manganese': 54.938043, 'Iron': 55.845, 'Cobalt': 58.933194, 'Nickel': 58.6934, 'Copper': 63.546, 'Zinc': 65.38, 'Gallium': 69.723, 'Germanium': 72.63, 'Arsenic': 74.921595, 'Selenium': 78.971, 'Bromine': 79.904, 'Krypton': 83.798, 'Rubidium': 85.4678, 'Strontium': 87.62, 'Yttrium': 88.905838, 'Zirconium': 91.222, 'Niobium': 92.90637, 'Molybdenum': 95.95, 'Technetium': 97.0, 'Ruthenium': 101.07, 'Rhodium': 102.90549, 'Palladium': 106.42, 'Silver': 107.8682, 'Cadmium': 112.414, 'Indium': 114.818, 'Tin': 118.71, 'Antimony': 121.76, 'Tellurium': 127.6, 'Iodine': 126.90447, 'Xenon': 131.293, 'Caesium': 132.90545196, 'Barium': 137.327, 'Lanthanum': 138.90547, 'Cerium': 140.116, 'Praseodymium': 140.90766, 'Neodymium': 144.242, 'Promethium': 145.0, 'Samarium': 150.36, 'Europium': 151.964, 'Gadolinium': 157.249, 'Terbium': 158.925354, 'Dysprosium': 162.5, 'Holmium': 164.930329, 'Erbium': 167.259, 'Thulium': 168.934219, 'Ytterbium': 173.045, 'Lutetium': 174.96669, 'Hafnium': 178.486, 'Tantalum': 180.94788, 'Tungsten': 183.84, 'Rhenium': 186.207, 'Osmium': 190.23, 'Iridium': 192.217, 'Platinum': 195.084, 'Gold': 196.96657, 'Mercury': 200.592, 'Thallium': 204.38, 'Lead': 207.2, 'Bismuth': 208.9804, 'Polonium': 209.0, 'Astatine': 210.0, 'Radon': 222.0, 'Francium': 223.0, 'Radium': 226.0, 'Actinium': 227.0, 'Thorium': 232.0377, 'Protactinium': 231.03588, 'Uranium': 238.02891, 'Neptunium': 237.0, 'Plutonium': 244.0, 'Americium': 243.0, 'Curium': 247.0, 'Berkelium': 247.0, 'Californium': 251.0, 'Einsteinium': 252.0, 'Fermium': 257.0, 'Mendelevium': 258.0, 'Nobelium': 259.0, 'Lawrencium': 262.0, 'Rutherfordium': 267.0, 'Dubnium': 270.0, 'Seaborgium': 269.0, 'Bohrium': 270.0, 'Hassium': 270.0, 'Meitnerium': 278.0, 'Darmstadtium': 281.0, 'Roentgenium': 281.0, 'Copernicium': 285.0, 'Nihonium': 286.0, 'Flerovium': 289.0, 'Moscovium': 289.0, 'Livermorium': 293.0, 'Tennessine': 293.0, 'Oganesson': 294.0}
# Result of running read_asplund2009()
asplund2009 = {'Hydrogen': 1.0, 'Helium': 0.08511380382023759, 'Lithium': 1.1220184543019653e-11, 'Beryllium': 2.398832919019485e-11, 'Boron': 5.011872336272714e-10, 'Carbon': 0.0002691534803926914, 'Nitrogen': 6.760829753919819e-05, 'Oxygen': 0.0004897788193684457, 'Fluorine': 3.63078054770101e-08, 'Neon': 8.51138038202376e-05, 'Sodium': 1.7378008287493763e-06, 'Magnesium': 3.9810717055349695e-05, 'Aluminium': 2.818382931264455e-06, 'Silicon': 3.235936569296281e-05, 'Phosphorus': 2.570395782768865e-07, 'Sulfur': 1.3182567385564074e-05, 'Chlorine': 3.162277660168379e-07, 'Argon': 2.5118864315095823e-06, 'Potassium': 1.0715193052376071e-07, 'Calcium': 2.1877616239495517e-06, 'Scandium': 1.4125375446227555e-09, 'Titanium': 8.912509381337459e-08, 'Vanadium': 8.511380382023759e-09, 'Chromium': 4.365158322401656e-07, 'Manganese': 2.691534803926914e-07, 'Iron': 3.1622776601683795e-05, 'Cobalt': 9.772372209558111e-08, 'Nickel': 1.6595869074375596e-06, 'Copper': 1.5488166189124828e-08, 'Zinc': 3.63078054770101e-08, 'Gallium': 1.0964781961431829e-09, 'Germanium': 4.466835921509635e-09, 'Arsenic': 1.9952623149688828e-10, 'Selenium': 2.1877616239495518e-09, 'Bromine': 3.46736850452531e-10, 'Krypton': 1.7782794100389228e-09, 'Rubidium': 3.3113112148259076e-10, 'Strontium': 7.413102413009192e-10, 'Yttrium': 1.621810097358933e-10, 'Zirconium': 3.801893963205613e-10, 'Niobium': 2.8840315031266117e-11, 'Molybdenum': 7.58577575029182e-11, 'Ruthenium': 5.6234132519034906e-11, 'Rhodium': 8.128305161640995e-12, 'Palladium': 3.7153522909717275e-11, 'Silver': 8.709635899560796e-12, 'Cadmium': 5.1286138399136583e-11, 'Indium': 6.309573444801943e-12, 'Tin': 1.0964781961431829e-10, 'Antimony': 1.0232929922807536e-11, 'Tellurium': 1.5135612484362072e-10, 'Iodine': 3.548133892335761e-11, 'Xenon': 1.7378008287493763e-10, 'Caesium': 1.202264434617413e-11, 'Barium': 1.5135612484362072e-10, 'Lanthanum': 1.2589254117941662e-11, 'Cerium': 3.801893963205613e-11, 'Praseodymium': 5.248074602497734e-12, 'Neodymium': 2.6302679918953815e-11, 'Samarium': 9.120108393559116e-12, 'Europium': 3.3113112148259077e-12, 'Gadolinium': 1.1748975549395303e-11, 'Terbium': 1.9952623149688827e-12, 'Dysprosium': 1.2589254117941662e-11, 'Holmium': 3.0199517204020193e-12, 'Erbium': 8.317637711026709e-12, 'Thulium': 1.258925411794166e-12, 'Ytterbium': 6.918309709189362e-12, 'Lutetium': 1.258925411794166e-12, 'Hafnium': 7.079457843841373e-12, 'Tantalum': 7.585775750291852e-13, 'Tungsten': 7.079457843841373e-12, 'Rhenium': 1.8197008586099825e-12, 'Osmium': 2.5118864315095823e-11, 'Iridium': 2.398832919019485e-11, 'Platinum': 4.168693834703364e-11, 'Gold': 8.317637711026709e-12, 'Mercury': 1.4791083881682073e-11, 'Thallium': 7.943282347242821e-12, 'Lead': 5.6234132519034906e-11, 'Bismuth': 4.466835921509635e-12, 'Thorium': 1.0471285480508985e-12, 'Uranium': 2.8840315031266116e-13}

from .simulations import nugrid_abundances, limongi_chieffi_abundances

def read_asplund2009(filename):
    # Read in Asplund 2009 and return number abundance
    # file can be found in data/asplund2009.txt
    abundances = {}
    with open(filename) as filein:
        for line in filein.readlines():
            if line.startswith("#"): continue  # Skip comments
            proton_number, symbol, photospheric_abundance, meteoric_abundance = line.strip("\n").split(",")
            abundance = float(photospheric_abundance.split(" ± ")[0]) if photospheric_abundance != "" else float(meteoric_abundance.split(" ± ")[0])
            abundances[symbol_to_element[symbol]] = 10 ** (abundance - 12)
    return abundances

def scale_asplund2009_abundance(Z, elements=None):
    """
    Return mass fraction of `elements` for an Asplund (2009) abundance pattern,
    assuming Helium fraction scales linearly from primordial value.

    Parameters
    ----------
    Z : number
        Metallicity, as total metal mass fraction.
    elements : list of str, optional
        Elements to include, None (default) returns all elements in original paper.
        Hydrogen and Helium always included.

    Returns
    -------
    dict
        Dictionary of element name: mass fraction pairs
    """
    # Return mass fraction of elements, if provided
    Ysolar = 0.2485
    Zsolar = 0.0134
    # Use idea (https://ui.adsabs.harvard.edu/abs/2021MNRAS.502.3045K/abstract) that there is a linear relation between Y and Z
    Y = (Ysolar - Yprimordial) / (Zsolar) * (Z) + Yprimordial

    X = 1 - Y - Z

    mass_abundance = {}
    number_abundance = asplund2009
    elements = elements if elements is not None else list(number_abundance)
    for element in elements:
        mass_abundance[element] = X * number_abundance[element] * element_weights[element] / element_weights["Hydrogen"] * Z / Zsolar
    mass_abundance["Hydrogen"] = X
    mass_abundance["Helium"] = Y
    return mass_abundance

def scale_NuGrid_abundance(Z, elements=None):
    """
    Return mass fraction of `elements` for NuGrid abundance pattern,
    interpolating for their different metallicities.

    Basically just wraps the SimulationAbundances class.

    Parameters
    ----------
    Z : number
        Metallicity, as total metal mass fraction.
    elements : list of str, optional
        Elements to include, None (default) returns all elements in original paper.
        Hydrogen and Helium NOT always included.

    Returns
    -------
    dict
        Dictionary of element name: mass fraction pairs
    """
    return nugrid_abundances.interpolate(Z, elements=elements)

def scale_LimongiChieffi_abundance(Z, elements=None):
    """
    Return mass fraction of `elements` for Limongi & Chieffi (2018) abundance pattern,
    interpolating for their different metallicities.

    Basically just wraps the SimulationAbundances class.

    Parameters
    ----------
    Z : number
        Metallicity, as total metal mass fraction.
    elements : list of str, optional
        Elements to include, None (default) returns all elements in original paper.
        Hydrogen and Helium NOT always included.

    Returns
    -------
    dict
        Dictionary of element name: mass fraction pairs
    """
    return limongi_chieffi_abundances.interpolate(Z, elements=elements)

def mass_fraction_to_logAB(mass_fractions, elementA, elementB):
    """
    Convert mass fractions to log(A/B), i.e. log of ratio of number densities.

    See also: `mass_fraction_to_AX` to convert directly to A(X) = 12 + log(X/H).

    Parameters
    ----------
    mass_fractions : dict of name: mass_fraction pairs
        _description_
    elementA : string
        name of element A, the numerator.
    elementB : string
        name of element B, the denominator.
    """
    return np.log10(mass_fractions[elementA] / mass_fractions[elementB]) - np.log10(element_weights[elementA]/element_weights[elementB])

def mass_fraction_to_AX(mass_fractions, element):
    """
    Convert mass fractions to A(X) = 12 + log(X/H).

    See also: `mass_fraction_to_logAB` to convert log(A/B).

    Parameters
    ----------
    mass_fractions : dict of name: mass_fraction pairs
        _description_
    element : string
        name of element.
    """
    return 12 + mass_fraction_to_logAB(mass_fractions, element, "Hydrogen")

def symbol_to_name(filename="elements.txt"):
    elements = {}
    with open(filename) as filein:
        for line in filein.readlines():
            if line.startswith("#"): continue  # Skip comments
            # Some elements have extra notes
            if len(tokens:=line.rstrip("\n").split(";")) == 4:
                atomic_number, symbol, element, weight_string = tokens
            else:
                atomic_number, symbol, element, weight_string, notes = tokens

            elements[symbol] = element
    return elements

def read_weights(weight_filename="elements.txt"):
    weights = {}
    with open(weight_filename) as filein:
        for line in filein.readlines():
            if line.startswith("#"): continue  # Skip comments
            # Some elements have extra notes
            if len(tokens:=line.rstrip("\n").split(";")) == 4:
                atomic_number, symbol, element, weight_string = tokens
            else:
                atomic_number, symbol, element, weight_string, notes = tokens
            # weight_string has two possible forms, depending on if the element is radioactive:
            #  (i) number with uncertainty, i.e. 1.23(4)
            # (ii) Number in square brackets, corresponding to most stable isotope
            # Strip these off, and cast to a float
            weights[element] = float(weight_string.split("(")[0]) if "(" in weight_string else float(weight_string[1:-1])
    return weights
import numpy as np

class SimulationAbundances:
    """
    Class to hold Simulation info together. Contains:
        elements: list of elements as str
        metallicities: np array of metallicities where abundances are defined
        mass_fractions: np array of shape (nZ, nE) for the mass fraction of an element.
            nZ is number of metallicity valies, nE number of elements.
    """
    def __init__(self, elements, metallicities, mass_fractions):
        self.elements = elements
        self.metallicities = metallicities
        self.mass_fractions = mass_fractions

    def interpolate(self, Z, elements=None):
        """
        Interpolate mass fractions.

        Parameters
        ----------
        Z : _type_
            _description_
        """
        elements = self.elements if elements is None else elements
        if isinstance(elements, str):
            raise TypeError("`elements` should be a list, not a string.")
        i = np.searchsorted(self.metallicities, Z)
        dZ = self.metallicities[i] - self.metallicities[i - 1]
        dM = self.mass_fractions[i] - self.mass_fractions[i - 1]
        interpolated = dM/dZ * (Z - self.metallicities[i-1]) + self.mass_fractions[i-1]
        return {element: interpolated[self.elements.index(element)] for element in elements}

_nugrid_elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminium', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium']
_nugrid_metallicities = np.array([0.0001, 0.001, 0.006, 0.01, 0.02])
_nugrid_mass_fractions = np.array([
    [0.7514, 0.2485, 7.612e-14, 0.0, 2.858e-12, 1.254e-05, 1.064e-06, 7.412e-05, 5.616e-10, 5.905e-06, 4.003e-08, 1.678e-06, 6.487e-08, 1.579e-06, 7.113e-09, 1.115e-06, 9.135e-09, 1.796e-07, 4.2e-09, 1.231e-07, 5.419e-11, 6.445e-09, 4.152e-10, 1.982e-08, 1.099e-08, 1.439e-06, 3.995e-09, 8.507e-08, 9.644e-10, 2.381e-09, 7.665e-11],
    [0.7493, 0.2497, 7.612e-13, 0.0, 2.858e-11, 0.0001254, 1.064e-05, 0.0007412, 5.616e-09, 5.905e-05, 4.003e-07, 1.678e-05, 6.487e-07, 1.579e-05, 7.113e-08, 1.115e-05, 9.135e-08, 1.796e-06, 4.2e-08, 1.231e-06, 5.419e-10, 6.445e-08, 4.152e-09, 1.982e-07, 1.099e-07, 1.439e-05, 3.995e-08, 8.507e-07, 9.644e-09, 2.381e-08, 7.665e-10],
    [0.7381, 0.2559, 4.567e-12, 0.0, 1.715e-10, 0.0007527, 6.384e-05, 0.004447, 3.37e-08, 0.0003543, 2.402e-06, 0.0001007, 3.892e-06, 9.471e-05, 4.268e-07, 6.692e-05, 5.481e-07, 1.078e-05, 2.52e-07, 7.384e-06, 3.251e-09, 3.867e-07, 2.491e-08, 1.189e-06, 6.595e-07, 8.636e-05, 2.397e-07, 5.104e-06, 5.786e-08, 1.428e-07, 4.599e-09],
    [0.729, 0.261, 3.803e-11, 0.0, 1.428e-09, 0.001733, 0.0005315, 0.004825, 2.805e-07, 0.0009847, 2e-05, 0.000376, 3.241e-05, 0.0004056, 3.553e-06, 0.0002117, 4.563e-06, 4.889e-05, 2.098e-06, 3.737e-05, 2.707e-08, 2.041e-06, 2.074e-07, 9.902e-06, 5.491e-06, 0.000719, 1.996e-06, 4.249e-05, 4.818e-07, 1.189e-06, 3.829e-08],
    [0.7065, 0.2735, 7.605e-11, 0.0, 2.856e-09, 0.003466, 0.001063, 0.00965, 5.611e-07, 0.001969, 4e-05, 0.0007521, 6.481e-05, 0.0008112, 7.106e-06, 0.0004233, 9.127e-06, 9.779e-05, 4.196e-06, 7.475e-05, 5.414e-08, 4.081e-06, 4.148e-07, 1.98e-05, 1.098e-05, 0.001438, 3.991e-06, 8.499e-05, 9.635e-07, 2.379e-06, 7.658e-08]
                ])

nugrid_abundances = SimulationAbundances(_nugrid_elements, _nugrid_metallicities, _nugrid_mass_fractions)

# Limongi & Chieffi (2018) with Roberti+ (2024) data.
_LC_elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminium', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium']
_LC_metallicities = np.array([0.00003236, 0.0003236, 0.003236, 0.01345, 0.0269])
_LC_mass_fractions = np.array([
    [0.76, 0.24003, 2.0497e-09, 1.6051e-13, 4.0247e-12, 4.431e-06, 6.9682e-07, 2.0472e-05, 5.0778e-10, 1.2617e-06, 2.942e-08, 1.2673e-06, 5.6013e-08, 1.7209e-06, 5.8652e-09, 6.9718e-07, 8.2596e-09, 1.5029e-07, 3.0867e-09, 1.4462e-07, 4.6788e-11, 6.2722e-09, 3.195e-10, 1.6726e-08, 1.0896e-08, 1.3014e-06, 4.244e-09, 7.1779e-08, 7.2526e-10, 1.7497e-09, 5.6333e-11],
    [0.75971, 0.24003, 2.0497e-09, 1.6051e-12, 4.0247e-11, 4.431e-05, 6.9682e-06, 0.00020472, 5.0778e-09, 1.2617e-05, 2.942e-07, 1.2673e-05, 5.6013e-07, 1.7209e-05, 5.8652e-08, 6.9718e-06, 8.2596e-08, 1.5029e-06, 3.0867e-08, 1.4462e-06, 4.6788e-10, 6.2722e-08, 3.195e-09, 1.6726e-07, 1.0896e-07, 1.3014e-05, 4.244e-08, 7.1779e-07, 7.2526e-09, 1.7497e-08, 5.6333e-10],
    [0.74679, 0.25003, 2.0497e-09, 1.6051e-11, 4.0247e-10, 0.0004431, 6.9682e-05, 0.0020472, 5.0778e-08, 0.00012617, 2.942e-06, 0.00012673, 5.6013e-06, 0.00017209, 5.8652e-07, 6.9718e-05, 8.2596e-07, 1.5029e-05, 3.0867e-07, 1.4462e-05, 4.6788e-09, 6.2722e-07, 3.195e-08, 1.6726e-06, 1.0896e-06, 0.00013014, 4.244e-07, 7.1779e-06, 7.2526e-08, 1.7497e-07, 5.6333e-09],
    [0.72158, 0.26503, 9.0621e-09, 1.5889e-10, 3.9841e-09, 0.0023799, 0.00069691, 0.0057706, 5.0785e-07, 0.0012619, 2.9424e-05, 0.00071276, 5.602e-05, 0.0006696, 5.866e-06, 0.00031146, 8.2607e-06, 6.7141e-05, 3.0871e-06, 6.4609e-05, 4.6794e-08, 3.144e-06, 3.1954e-07, 1.6728e-05, 1.0898e-05, 0.0013016, 4.2445e-06, 7.1789e-05, 7.2535e-07, 1.7499e-06, 5.634e-08],
    [0.67313, 0.30003, 9.0621e-09, 3.1779e-10, 7.9682e-09, 0.0047598, 0.0013938, 0.011541, 1.0157e-06, 0.0025237, 5.8849e-05, 0.0014255, 0.00011204, 0.0013392, 1.1732e-05, 0.00062293, 1.6521e-05, 0.00013428, 6.1743e-06, 0.00012922, 9.3588e-08, 6.288e-06, 6.3908e-07, 3.3456e-05, 2.1796e-05, 0.0026031, 8.4891e-06, 0.00014358, 1.4507e-06, 3.4998e-06, 1.1268e-07]
                            ])

limongi_chieffi_abundances = SimulationAbundances(_LC_elements, _LC_metallicities, _LC_mass_fractions)
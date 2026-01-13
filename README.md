# abundance-scaling
A (set of) function(s) to scale given elemental abundances to a given metallicity.

Remember to add to pythonpath to use in other directories.

To try to keep things simple, albeit less flexible, I have saved the outputs of some functions directly to the source code, but those functions and the raw data files still exist.

To work out the Helium mass fraction, we assume that helium is linearly correlated to metallicity, as in e.g. [Kurichin et al. (2021)](https://ui.adsabs.harvard.edu/abs/2021MNRAS.502.3045K/abstract) and [Mastumoto et al. (2022)](https://ui.adsabs.harvard.edu/abs/2022ApJ...941..167M/abstract).

The latter reference includes a plot showing primordial helium abundance between various measurents. There is some uncertainty, so we take the [Planck 2018 (Eqn. 83)](https://ui.adsabs.harvard.edu/abs/2020A%26A...641A...6P/abstract) value of 0.2437.

## Currently implemented
* Asplund et al 2009 Photospheric abundances
* NuGrid abundances, taken from their data directly (https://download1.nugridstars.org/set1ext/Yield_tables/, but see Ritter C., et al. (2018) MNRAS, 480, 538.)
* Limongi & Chieffi (2018) abundances, taken from their data directly (http://orfeo.iaps.inaf.it/index.html, see Limongi M., et al. (2018) ApJS, 237, 13; Roberti L., et al. (2024) ApJS, 272, 15)
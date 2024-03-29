
Metabolic flux estimation
-------------------------

`influx_si` can be used for estimation of metabolic fluxes and concentrations   based on labeling data from MS and/or NMR measurements. `influx_s` is used for stationary labeling and `influx_i` for instationary one (hence the '_s' and '_i' in the names). The name `influx_si` is used as common for both tools.

The input for `influx_si` is an MTF (Multiple TSV Files) collection describing metabolic network, label transition, labeling data and options to use during estimation.

The output is a zip archive with files generated by `influx_si`. File ending with `.tvar.sim` which contains the estimated fluxes and concentrations. Other files ending with `.sim` contain simulated measurements. File ending with `.stat` has results of chi2 test assessing quality of fit.

If, in your `.opt` file, you have requested plotting information (`plot_smeas.R` or `plot_ilab.R`), it can be found in the respective `.pdf` file.

For detailed documentation about `influx_si` and accompanying tools see https://influx-si.readthedocs.io

For getting a standalone version of `influx_si <https://anaconda.org/bioconda/influx_si>`_, you can install it e.g. with `conda <https://docs.conda.io/en/latest/miniconda.html>`_ package manager: ::

 conda install -c conda-forge -c bioconda influx_si

Author: Serguei Sokol

License: GPL2

© INRAE/INSA/CNRS 2023

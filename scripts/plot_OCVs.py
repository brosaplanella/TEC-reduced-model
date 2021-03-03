#
# Plot OCVs
#

import pybamm
import numpy as np
import matplotlib.pyplot as plt
from os import path
from cycler import cycler
from palettable.scientific.sequential import Batlow_5

color_cycle = [
    (0.005193, 0.098238, 0.349842),
    (0.981354, 0.800406, 0.981267),
    (0.511253, 0.510898, 0.193296),
    (0.133298, 0.375282, 0.379395),
    (0.946612, 0.614218, 0.419767),
    (0.302379, 0.450282, 0.300122),
    (0.066899, 0.263188, 0.377594),
    (0.992900, 0.704852, 0.704114),
    (0.754268, 0.565033, 0.211761),
    (0.088353, 0.322167, 0.384731),
]

plt.rcParams.update(
    {"font.size": 8, "axes.prop_cycle": cycler('color', color_cycle)}
)


pybamm.set_logging_level("INFO")

root = path.dirname(path.dirname(__file__))

# Define parameter set Chen 2020 (see PyBaMM documentation for details)
param = pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Chen2020)

Up = param["Positive electrode OCP [V]"][1]
Un = param["Negative electrode OCP [V]"][1]

fig, axes = plt.subplots(1, 2, figsize=(5.5, 2.5))

axes[0].plot(Up[:, 0], Up[:, 1])
axes[0].set_xlabel("Stoichiometry")
axes[0].set_ylabel("Positive electrode OCV (V)")

axes[1].plot(Un[:, 0], Un[:, 1])
axes[1].set_xlabel("Stoichiometry")
axes[1].set_ylabel("Negative electrode OCV (V)")

plt.tight_layout()

fig.savefig(path.join(root, "figures", "OCVs.png"), dpi=300)

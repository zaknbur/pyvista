import warnings
from pyvista._version import __version__
from pyvista.plotting import *
from pyvista.utilities import *
from pyvista.core import *
# Per contract with Sphinx-Gallery, this method must be availabe at top level
from pyvista.utilities.sphinx_gallery import _get_sg_image_scraper

import numpy as np
import scooby
import vtk

# get the int type from vtk
ID_TYPE = np.int32
if vtk.VTK_ID_TYPE == 12:
    ID_TYPE = np.int64


# determine if using vtk > 5
if vtk.vtkVersion().GetVTKMajorVersion() <= 5:
    raise AssertionError('VTK version must be 5.0 or greater.')

# catch annoying numpy/vtk future warning:
warnings.simplefilter(action='ignore', category=FutureWarning)

# A simple flag to set when generating the documentation
OFF_SCREEN = False
try:
    if os.environ['PYVISTA_OFF_SCREEN'].lower() == 'true':
        OFF_SCREEN = True
except KeyError:
    pass

# A threshold for the max cells to compute a volume for when repr-ing
REPR_VOLUME_MAX_CELLS = 1e6

# Set where figures are saved
FIGURE_PATH = None

# Set up data directory
import appdirs
import os

USER_DATA_PATH = appdirs.user_data_dir('pyvista')
if not os.path.exists(USER_DATA_PATH):
    os.makedirs(USER_DATA_PATH)

EXAMPLES_PATH = os.path.join(USER_DATA_PATH, 'examples')
if not os.path.exists(EXAMPLES_PATH):
    os.makedirs(EXAMPLES_PATH)

# Send VTK messages to the logging module:
send_errors_to_logging()


# Set up panel for interactive notebook rendering
try:
    if os.environ['PYVISTA_USE_PANEL'].lower() == 'false':
        rcParams['use_panel'] = False
    elif os.environ['PYVISTA_USE_PANEL'].lower() == 'true':
        rcParams['use_panel'] = True
except KeyError:
    pass
# Only initialize panel if in a Jupyter environment
if scooby.in_ipykernel():
    try:
        import panel
        panel.extension('vtk')
    except ImportError:
        pass

# Set preferred plot theme
try:
    theme = os.environ['PYVISTA_PLOT_THEME'].lower()
    set_plot_theme(theme)
except KeyError:
    pass


# Set a parameter to control default print format for floats
FLOAT_FORMAT = "{:.3e}"

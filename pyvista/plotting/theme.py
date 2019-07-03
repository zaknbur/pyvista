
import vtk

from .colors import string_to_rgb


MAX_N_COLOR_BARS = 10
PV_BACKGROUND = [82/255., 87/255., 110/255.]
FONT_KEYS = {'arial': vtk.VTK_ARIAL,
             'courier': vtk.VTK_COURIER,
             'times': vtk.VTK_TIMES}


rcParams = {
    'background' : [0.3, 0.3, 0.3],
    'camera' : {
        'position' : [1, 1, 1],
        'viewup' : [0, 0, 1],
    },
    'window_size' : [1024, 768],
    'font' : {
        'family' : 'courier',
        'size' : 12,
        'title_size': None,
        'label_size' : None,
        'color' : [1, 1, 1],
        'fmt' : None,
    },
    'cmap' : 'viridis',
    'color' : 'white',
    'nan_color' : 'darkgray',
    'edge_color' : 'black',
    'outline_color' : 'white',
    'colorbar_orientation' : 'horizontal',
    'colorbar_horizontal' : {
        'width' : 0.60,
        'height' : 0.08,
        'position_x' : 0.35,
        'position_y' : 0.02,
    },
    'colorbar_vertical' : {
        'width' : 0.1,
        'height' : 0.8,
        'position_x' : 0.85,
        'position_y' : 0.1,
    },
    'show_scalar_bar' : True,
    'show_edges' : False,
    'lighting' : True,
    'interactive' : False,
    'render_points_as_spheres' : False,
    'use_panel' : True,
    'transparent_background' : False
}

DEFAULT_THEME = dict(rcParams)

def set_plot_theme(theme):
    """Set the plotting parameters to a predefined theme"""
    if theme.lower() in ['paraview', 'pv']:
        rcParams['background'] = PV_BACKGROUND
        rcParams['cmap'] = 'coolwarm'
        rcParams['font']['family'] = 'arial'
        rcParams['font']['label_size'] = 16
        rcParams['show_edges'] = False
    elif theme.lower() in ['document', 'doc', 'paper', 'report']:
        rcParams['background'] = 'white'
        rcParams['cmap'] = 'viridis'
        rcParams['font']['size'] = 18
        rcParams['font']['title_size'] = 18
        rcParams['font']['label_size'] = 18
        rcParams['font']['color'] = 'black'
        rcParams['show_edges'] = False
        rcParams['color'] = 'tan'
        rcParams['outline_color'] = 'black'
    elif theme.lower() in ['night', 'dark']:
        rcParams['background'] = 'black'
        rcParams['cmap'] = 'viridis'
        rcParams['font']['color'] = 'white'
        rcParams['show_edges'] = False
        rcParams['color'] = 'tan'
        rcParams['outline_color'] = 'white'
        rcParams['edge_color'] = 'white'
    elif theme.lower() in ['default']:
        for k,v in DEFAULT_THEME.items():
            rcParams[k] = v



def parse_color(color):
    """ Parses color into a vtk friendly rgb list """
    if color is None:
        color = rcParams['color']
    if isinstance(color, str):
        return string_to_rgb(color)
    elif len(color) == 3:
        return color
    else:
        raise Exception("""
    Invalid color input
    Must ba string, rgb list, or hex color string.  For example:
        color='white'
        color='w'
        color=[1, 1, 1]
        color='#FFFFFF'""")



def parse_font_family(font_family):
    """ checks font name """
    # check font name
    font_family = font_family.lower()
    if font_family not in ['courier', 'times', 'arial']:
        raise Exception('Font must be either "courier", "times" ' +
                        'or "arial"')

    return FONT_KEYS[font_family]

import ctypes
import numpy as np

import pyvista


def voxelize(mesh, density):
    """voxelize mesh to UnstructuredGrid"""
    x_min, x_max, y_min, y_max, z_min, z_max = mesh.bounds
    x = np.arange(x_min, x_max, density)
    y = np.arange(y_min, y_max, density)
    z = np.arange(z_min, z_max, density)
    x, y, z = np.meshgrid(x, y, z)

    # Create unstructured grid from the structured grid
    grid = pyvista.StructuredGrid(x, y, z)
    ugrid = pyvista.UnstructuredGrid(grid)

    # get part of the mesh within the mesh
    selection = ugrid.select_enclosed_points(mesh, tolerance=0.0)
    mask = selection.point_arrays['SelectedPoints'].view(np.bool)

    # extract cells from point indices
    return ugrid.extract_selection_points(mask)


def create_grid(dataset, dimensions=(101, 101, 101)):
    """Creates a uniform grid surrounding the given dataset with the specified
    dimensions. This grid is commonly used for interpolating the input dataset.
    """
    bounds = np.array(dataset.bounds)
    if dimensions is None:
        # TODO: we should implement an algorithm to automaitcally deterime an
        # "optimal" grid size by looking at the sparsity of the points in the
        # input dataset - I actaully think VTK might have this implemented
        # somewhere
        raise NotImplementedError('Please specifiy dimensions.')
    dimensions = np.array(dimensions, dtype=int)
    image = pyvista.UniformGrid()
    image.dimensions = dimensions
    dims = (dimensions - 1)
    dims[dims==0] = 1
    image.spacing = (bounds[1::2] - bounds[:-1:2]) / dims
    image.origin = bounds[::2]
    return image


def single_triangle():
    """ A single PolyData triangle """
    points = np.zeros((3, 3))
    points[1] = [1, 0, 0]
    points[2] = [0.5, 0.707, 0]
    cells = np.array([[3, 0, 1, 2]], ctypes.c_long)
    return pyvista.PolyData(points, cells)

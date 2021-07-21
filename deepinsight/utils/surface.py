# -*- coding: utf-8 -*-
##########################################################################
# NSAp - Copyright (C) CEA, 2021
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

"""
Surface utilities.
"""

from surfify.utils import (
    interpolate, neighbors, downsample, neighbors_rec, icosahedron,
    number_of_ico_vertices, get_rectangular_projection)

__all__ = ["interpolate", "neighbors", "downsample", "neighbors_rec",
           "icosahedron", "number_of_ico_vertices",
           "get_rectangular_projection"]

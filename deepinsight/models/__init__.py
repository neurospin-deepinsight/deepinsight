# -*- coding: utf-8 -*-
##########################################################################
# NSAp - Copyright (C) CEA, 2021
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

"""
Common architectures.
"""

from brainite.models import VAE
from brainite.models import MCVAE
from brainite.models import PMVAE
from surfify.models import SphericalUNet

__all__ = ["VAE", "MCVAE", "PMVAE", "SphericalUNet"]

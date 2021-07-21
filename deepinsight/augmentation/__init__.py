# -*- coding: utf-8 -*-
##########################################################################
# NSAp - Copyright (C) CEA, 2021
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

"""
Common MRI data augmentation methods.
"""

from brainrise import Transform
from brainrise import Compose, ToTensor, RandomApply
from brainrise import (
    RandomOffset, RandomBlur, RandomNoise, RandomGhosting, RandomSpike,
    RandomBiasField, RandomMotion)
from brainrise import Rescale, ZScoreNormalize, KDENormalize
from brainrise import RandomAffine, RandomFlip, RandomDeformation
from brainrise import Padd, Downsample

__all__ = ["Transform", "Compose", "ToTensor", "RandomApply", "RandomOffset",
           "RandomBlur", "RandomNoise", "RandomGhosting", "RandomSpike",
           "RandomBiasField", "RandomMotion", "Rescale", "ZScoreNormalize",
           "KDENormalize", "RandomAffine", "RandomFlip", "RandomDeformation",
           "Padd", "Downsample"]

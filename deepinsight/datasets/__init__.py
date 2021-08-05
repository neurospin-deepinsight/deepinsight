# -*- coding: utf-8 -*-
##########################################################################
# NSAp - Copyright (C) CEA, 2021
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

"""
Common datasets.
"""

from dataify import BraTSDataset
from dataify import DSpritesDataset
from dataify import EchocardiographyDataset
from dataify import SinOscillatorDataset
from dataify import HCPAnatDataset
from dataify import IMPACDataset
from dataify import SingleCellRNASeqDataset
from dataify import MovingMNISTDataset
from surfify.datasets import make_classification, ClassificationDataset
from brainrise.datasets import MRIToyDataset


__all__ = ["BraTSDataset", "DSpritesDataset", "EchocardiographyDataset",
           "SinOscillatorDataset", "HCPAnatDataset", "IMPACDataset",
           "SingleCellRNASeqDataset", "MovingMNISTDataset",
           "make_classification", "ClassificationDataset", "MRIToyDataset"]

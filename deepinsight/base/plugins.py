# -*- coding: utf-8 -*-
##########################################################################
# NSAp - Copyright (C) CEA, 2021
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

"""
Define a hook to load plugins into the module.
"""

# System import
import sys
import re
import os
import importlib
from ..info import REQUIRES


class PluginsMetaImportHook(object):
    """ A class that import a module like normal except for the plugins that
    monted on the pysap plugins module. The return value from the hack call
    is put into sys.modules.
    """
    def __init__(self):
        self.module = None
        self.requires = self.parse_requirements()

    def parse_requirements(self):
        requires = [re.split("[^a-z]", req)[0] for req in REQUIRES]
        return requires

    def find_module(self, name, path=None):
        """ This method is called by Python if this class is on sys.path.
        'name' is the fully-qualified name of the module to look for, and
        'path' is either __path__ (for submodules and subpackages) or None (for
        a top-level module/package).

        Note that this method will be called every time an import statement
        is detected (or __import__ is called), before Python's built-in
        package/module-finding code kicks in.
        """
        # Use this loader only on registered modules
        match = re.match("deepinsight\.plugins\.(.*)", name)
        if match is None:
            return None
        name = match.groups()[0]
        if (len(name.split(".")) == 1):
            path = None

        # Get parent module and associated sub module names
        self.sub_name = name.split(".")[-1]
        self.mod_name = name.rpartition(".")[0]

        # Find the sub module and build the module path
        try:
            self.spec = importlib.machinery.PathFinder().find_spec(
                self.sub_name, path)
            if self.spec is None:
                raise ImportError
            self.path = [self.spec.origin]
        except ImportError:
            return None

        # Return The loader, here the object itself
        return self

    def load_module(self, name):
        """ This method is called by Python if the class
        'find_module' does not return None. 'name' is the fully-qualified name
        of the module/package that was requested.
        """
        # Load the module
        module = self.spec.loader.load_module()

        # Update the module required information
        module.__path__ = self.path
        module.__loader__ = self
        module.__package__ = name
        module.__name__ = name
        module.__file__ = self.path[0]
        sys.modules[module.__name__] = module

        return module


sys.meta_path.insert(0, PluginsMetaImportHook())

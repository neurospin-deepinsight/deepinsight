# -*- coding: utf-8 -*-
##########################################################################
# NSAp - Copyright (C) CEA, 2021
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

# Imports
import unittest
import importlib


class TestMetaModule(unittest.TestCase):
    """ Test the meta module.
    """
    def setUp(self):
        """ Setup test.
        """
        pass

    def tearDown(self):
        """ Run after each test.
        """
        pass

    def test_wrong_import(self):
        """ Test wrong import.
        """
        self.assertRaises(
            ImportError, importlib.import_module, name="deepinsight.bad")

    def test_wrong_meta_import(self):
        """ Test wrong meta import.
        """
        self.assertRaises(
            ImportError,
            importlib.import_module, name="deepinsight.plugins.bad")

    def test_module_import(self):
        """ Test module import.
        """
        importlib.import_module("deepinsight.plugins")

    def test_meta_import(self):
        """ Test meta import.
        """
        import deepinsight.plugins.surfify as mod
        self.assertTrue(isinstance(mod.__doc__, str))


if __name__ == "__main__":

    unittest.main()

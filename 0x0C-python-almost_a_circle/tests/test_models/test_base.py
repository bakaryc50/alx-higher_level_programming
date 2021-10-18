#!/usr/bin/python3
"""Provides unittest for the 'Base' class provided by the 'models' module
"""


import unittest
import json
from os import chdir, getcwd, remove
from shutil import rmtree
from tempfile import mkdtemp

from models.base import Base


class TestBase(unittest.TestCase):
    """ Test base model methods """
    def setUp(self):
        """ Create a temporary directory and Base instance
        """
        self.base = Base()
        chdir(mkdtemp())

    def tearDown(self):
        """ Remove temporary files and directories """
        rmtree(getcwd(), ignore_errors=True)

    def test_base(self):
        """ Test the __init__ method """
        self.assertIsInstance(self.base, Base)

    def test_base_id(self):
        """ Test the __init__ method """
        self.assertIsInstance(self.base.id, int)
        self.assertGreater(self.base.id, 0)

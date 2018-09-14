# -*- coding: utf-8 -*-
# configure logging for the library with a null handler (nothing is printed by default). See
# http://docs.pthon-guide.org/en/latest/writing/logging/

"""Top-level package for SDV."""

__author__ = """MIT Data To AI Lab"""
__email__ = 'dailabmit@gmail.com'
__version__ = '0.1.0'

import logging
import os

from sdv.DataNavigator import DataLoader, CSVDataLoader, DataNavigator
from sdv.Modeler import Modeler
from sdv.Sampler import Sampler

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_SUFFIX = '.pkl'

__all__ = (
    'DataLoader',
    'CSVDataLoader',
    'DataNavigator',
    'Modeler',
    'Sampler',
)

logging.getLogger('btb').addHandler(logging.NullHandler())

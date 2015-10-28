#! /usr/bin/env python
# -*- coding: utf-8 -*-

###########################################################################
#    
#    multiNetX -- a python package for manipulating general multilayer graphs
#
#    Copyright (C) 2013-2014 by Nikos E. Kouvaris <nkouba@gmail.com>
#    Project LASAGNE -- multi-LAyer SpAtiotemporal Generalized NEtworks
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
###########################################################################    
    
"""
multiNetX - a general multilayer graph manipulation python module based on NetworkX
"""

from __future__ import division, absolute_import

# check for Python verion
import sys
if sys.version_info[:2] < (2, 6):
    raise ImportError("Python version 2.6 or later"\
                        "is required for multiNetX (%d.%d detected)." % 
                        sys.version_info[:2])
del sys

__author__ = "Nikos E. Kouvaris <nkouba@gmail.com>"
__copyright__ = "Copyright (C) 2013-2014 by Nikos E. Kouvaris <nkouba@gmail.com>\
                 Project LASAGNE -- multi-LAyer SpAtiotemporal Generalized NEtworks"
__license__ = "GNU GPL"
__version__ = "0.1."
#
#import all modules of the packages
#
from multinetx.exceptions import *
import multinetx.exceptions
#
from multinetx.classes import *
import multinetx.classes
#
from multinetx.draw import *
import  multinetx.draw
#
# from multinetx.linear_algebra import *
# import multinetx.linear_algebra
#
#
#
from multinetx.utilities import *
import multinetx.utilities



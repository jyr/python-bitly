#!/usr/bin/python

# The MIT License
#
# Copyright (c) 2009 Osvaldo Jair Gaxiola Mercado
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

'''A wrapper library for Bitly http://bit.ly'''

__author__ =  'Jair Gaxiola'
__email__ = 'jyr.gaxiola@gmail.com'
__license__ = 'MIT License'
__version__ = '0.0.1'

from bitly import Api
import sys

if len(sys.argv) != 5:
    print "Usage: \n\t python info.py \'version\' \'hash\' \'login\' \'apiKey\'"
    sys.exit(1)

version = sys.argv[1]
hashUrl = sys.argv[2]
login = sys.argv[3]
apiKey = sys.argv[4]

api = Api(version, login, apiKey)
api.info(hashUrl)
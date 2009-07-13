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

'''A wrapper library for File Social http://filesocial.com'''

__author__ =  'Jair Gaxiola'
__email__ = 'jyr.gaxiola@gmail.com'
__license__ = 'MIT License'
__version__ = '0.0.1'

from urllib import urlopen, urlencode

class Api:
    def __init__(self, version = None, login = None, apiKey = None):
        self.version = version
        self.login = login
        self.apiKey = apiKey
        
    def shorten(self, longUrl= None):
        self.longUrl = longUrl
        self.url = 'http://api.bit.ly/shorten?'
        self.values = {'version': self.version, 'longUrl': self.longUrl, 'login': self.login, 'apiKey': self.apiKey}
        
        self.params = urlencode(self.values)
        self.data = urlopen(self.url + self.params)
        print self.data.read()
        
    def expand(self, shortUrl = None):
        self.shortUrl = shortUrl
        self.url = 'http://api.bit.ly/expand?'
        self.values = {'version': self.version, 'shortUrl': self.shortUrl, 'login': self.login, 'apiKey': self.apiKey}
        
        self.params = urlencode(self.values)
        self.data = urlopen(self.url + self.params)
        print self.data.read()
        
    def info(self):
        pass
    
    def stats(self):
        pass
        
    def errors(self):
        pass
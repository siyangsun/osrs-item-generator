# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 23:26:25 2018

@author: Siyang
"""

import urllib2
from bs4 import BeautifulSoup
import re

url = 'http://oldschoolrunescape.wikia.com/wiki/Category:Items?pageuntil=Ahrim%27s+armour+set'

page = urllib2.urlopen(url, timeout=20).read()
soup = BeautifulSoup(page, 'html.parser')

### Starts with the first instance of <ul><li><a href=
### Ends before </tr></table></div>(

### Grab the full block of text between those
### Then, for each line grab what's between "/wiki/ and " title="
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###################
#    This package uses PyPeLoader to load a PE program from a HTTP server
#    (from an URL).
#    Copyright (C) 2025  PyPeUrlLoader

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
###################

'''
This package uses PyPeLoader to load a PE program from a HTTP server
(from an URL).
'''

__version__ = "0.0.1"
__author__ = "Maurice Lambert"
__author_email__ = "mauricelambert434@gmail.com"
__maintainer__ = "Maurice Lambert"
__maintainer_email__ = "mauricelambert434@gmail.com"
__description__ = '''
This package uses PyPeLoader to load a PE program from a HTTP server
(from an URL).
'''
__url__ = "https://github.com/mauricelambert/PyPeUrlLoader"

# __all__ = []

__license__ = "GPL-3.0 License"
__copyright__ = '''
PyPeUrlLoader  Copyright (C) 2025  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
'''
copyright = __copyright__
license = __license__

print(copyright)

from PyPeLoader import load

from sys import argv, executable, exit
from urllib.request import urlopen
from io import BytesIO

def main() -> int:
    """
    This is the main function to start the program from command line.
    """

    if len(argv) <= 1:
        print(
            'USAGES: "',
            executable,
            '" "',
            argv[0],
            '" <URL to download PE files...>',
            sep="",
        )
        return 1

    for url in argv[1:]:
        load(BytesIO(urlopen(url).read()))

    return 0

if __name__ == "__main__":
    exit(main())
#!/usr/bin/python
"""
Copyright 2007 Glencoe Software, Inc. All rights reserved.
Use is subject to license terms supplied in LICENSE.txt

Simple renaming module which forwards items to sys. Unfortunately,
before the creation of the python bindings, blitz started using the
omero.sys package which causes weird issues at certain levels in the
hierarchy. When those arise, pysys can be used as a replacement.
"""

import sys
argv = sys.argv
stderr = sys.stderr
exit = sys.exit

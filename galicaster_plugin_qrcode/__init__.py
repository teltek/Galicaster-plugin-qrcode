# -*- coding:utf-8 -*-

from . import qrcode
from distutils.version import LooseVersion

try:
    import galicaster
except:
    print "Error: Galicaster not found"

def init():
    if LooseVersion(galicaster.__version__) <= LooseVersion("2.0.x"):
        qrcode.init()
    else:
        raise Exception("Plugin version mismatch")

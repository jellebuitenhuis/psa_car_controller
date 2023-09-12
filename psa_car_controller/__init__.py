#import sys

#if sys.version_info[:2] >= (3, 8):
 #   from importlib import metadata
#else:
#    import importlib_metadata as metadata

__version__ = "3.0.13" #metadata.version(__package__)

#del metadata, sys

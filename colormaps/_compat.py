"""Matplotlib version compatibility helpers."""
import matplotlib
import matplotlib.cm
from packaging import version

_mlp_version = version.parse(matplotlib.__version__)
_USE_NEW_API = _mlp_version >= version.parse("3.6.0")
_HAS_COLORMAPS_ATTR = _USE_NEW_API

if _USE_NEW_API:
    from matplotlib.cm import _colormaps


def get_cmap(name):
    if _mlp_version >= version.parse("3.9.0"):
        return matplotlib.colormaps[name]
    else:
        return matplotlib.cm.get_cmap(name)


def register_cmap(name, cmap):
    if _USE_NEW_API:
        matplotlib.colormaps.register(name=name, cmap=cmap, force=True)
    else:
        matplotlib.cm.register_cmap(name=name, cmap=cmap)


def is_registered(name):
    if _USE_NEW_API:
        return name in sorted(_colormaps)
    else:
        return name in matplotlib.cm._cmap_registry

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
from glob import glob

import numpy as np

from ._version import __version__
from .colormap import Colormap
from ._compat import get_cmap, register_cmap, is_registered
from ._registry import build_registry, CMAPSFILE_DIR

USER_CMAPFILE_DIR = os.environ.get('CMAP_DIR')

_REGISTRY = build_registry()


class Cmaps(object):
    """colormaps"""

    def __init__(self):
        self._cache = {}
        self.__version__ = __version__
        self._load_user_cmaps()

    @staticmethod
    def _coltbl(cmap_file):
        pattern = re.compile(r'(\d\.?\d*)\s+(\d\.?\d*)\s+(\d\.?\d*).*')
        with open(cmap_file) as cmap:
            cmap_buff = cmap.read()
        cmap_buff = re.compile('ncolors.*\n').sub('', cmap_buff)
        if re.search(r'\s*\d\.\d*', cmap_buff):
            return np.asarray(pattern.findall(cmap_buff), 'f4')
        else:
            return np.asarray(pattern.findall(cmap_buff), 'u1') / 255.

    def _load_colormap(self, name):
        if name in self._cache:
            return self._cache[name]

        fpath = _REGISTRY.get(name)
        if fpath is None:
            raise AttributeError(f"colormaps has no colormap named '{name}'")

        reversed_ = name.endswith('_r')
        colors = self._coltbl(fpath)
        if reversed_:
            colors = colors[::-1]

        cmap = Colormap(colors, name=name)

        if not is_registered(name):
            register_cmap(name, cmap)
        else:
            cmap = get_cmap(name)

        self._cache[name] = cmap
        return cmap

    def _load_user_cmaps(self):
        if USER_CMAPFILE_DIR is None:
            return
        cmapsflist = sorted(glob(os.path.join(USER_CMAPFILE_DIR, '*.rgb')))
        for cmap_file in cmapsflist:
            cname = os.path.basename(cmap_file).split('.rgb')[0]
            if cname[0].isdigit() or cname.startswith('_'):
                cname = 'C' + cname
            cname = cname.replace('-', '_').replace('+', '_')

            cmap = Colormap(self._coltbl(cmap_file), name=cname)
            register_cmap(cname, cmap)
            self._cache[cname] = cmap

            cname_r = cname + '_r'
            cmap_r = Colormap(self._coltbl(cmap_file)[::-1], name=cname_r)
            register_cmap(cname_r, cmap_r)
            self._cache[cname_r] = cmap_r

    def register_all(self):
        """Register all colormaps with matplotlib."""
        for name in _REGISTRY:
            self._load_colormap(name)

    def register_collection(self, collection):
        """Register all colormaps from a named collection with matplotlib.

        Parameters
        ----------
        collection : str
            Collection name. One of: 'carbonplan', 'cartocolors', 'cmasher',
            'cmocean', 'colorbrewer', 'colorcet', 'cubehelix', 'ncar_ncl',
            'scientific', 'sciviz', 'tableau'.
        """
        from ._registry import COLLECTIONS
        if collection not in COLLECTIONS:
            raise ValueError(
                f"Unknown collection '{collection}'. "
                f"Available collections: {COLLECTIONS}"
            )
        for name, path in _REGISTRY.items():
            if os.path.basename(os.path.dirname(path)) == collection:
                self._load_colormap(name)

    def __getattr__(self, name):
        if name.startswith('_'):
            raise AttributeError(name)
        if name in _REGISTRY or name in self._cache:
            return self._load_colormap(name)
        raise AttributeError(f"colormaps has no colormap named '{name}'")

    def __dir__(self):
        base = list(self._cache.keys()) + list(_REGISTRY.keys())
        base.append('__version__')
        base.append('register_all')
        base.append('register_collection')
        return sorted(set(base))

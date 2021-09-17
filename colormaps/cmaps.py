#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
from glob import glob

import matplotlib.cm
import numpy as np

# from ._version import __version__
from .colormap import Colormap

CMAPSFILE_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'colormaps')
USER_CMAPFILE_DIR = os.environ.get('CMAP_DIR')


class Cmaps(object):
    """colormaps"""

    def __init__(self, ):
        self._parse_cmaps()
        # self.__version__ = __version__

    def _coltbl(self, cmap_file):
        pattern = re.compile(r'(\d\.?\d*)\s+(\d\.?\d*)\s+(\d\.?\d*).*')
        with open(cmap_file) as cmap:
            cmap_buff = cmap.read()
        cmap_buff = re.compile('ncolors.*\n').sub('', cmap_buff)
        if re.search(r'\s*\d\.\d*', cmap_buff):
            return np.asarray(pattern.findall(cmap_buff), 'f4')
        else:
            return np.asarray(pattern.findall(cmap_buff), 'u1') / 255.

    @property
    def colors(self):
        """
        Colors expressed on the range 0-1 as used by matplotlib.
        """
        mc = []

        for color in self.colors:
            mc.append(tuple([x / 255. for x in color]))

        return mc

    def _parse_cmaps(self):
        if USER_CMAPFILE_DIR is not None:
            cmapsflist = sorted(glob(os.path.join(USER_CMAPFILE_DIR, '*.rgb')))
            for cmap_file in cmapsflist:
                cname = os.path.basename(cmap_file).split('.rgb')[0]
                # start with the number will result illegal attribute
                if cname[0].isdigit() or cname.startswith('_'):
                    cname = 'C' + cname
                if '-' in cname:
                    cname = cname.replace('-', '_')
                if '+' in cname:
                    cname = cname.replace('+', '_')

                cmap = Colormap(self._coltbl(cmap_file), name=cname)
                matplotlib.cm.register_cmap(name=cname, cmap=cmap)
                setattr(self, cname, cmap)

                cname = cname + '_r'
                cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
                matplotlib.cm.register_cmap(name=cname, cmap=cmap)
                setattr(self, cname, cmap)
    @property
    def aggrnyl(self):
        cname = "aggrnyl"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "aggrnyl.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def aggrnyl_r(self):
        cname = "aggrnyl_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "aggrnyl.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def agsunset(self):
        cname = "agsunset"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "agsunset.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def agsunset_r(self):
        cname = "agsunset_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "agsunset.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def antique(self):
        cname = "antique"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "antique.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def antique_r(self):
        cname = "antique_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "antique.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def armyrose(self):
        cname = "armyrose"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "armyrose.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def armyrose_r(self):
        cname = "armyrose_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "armyrose.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blugrn(self):
        cname = "blugrn"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "blugrn.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blugrn_r(self):
        cname = "blugrn_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "blugrn.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bluyl(self):
        cname = "bluyl"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "bluyl.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bluyl_r(self):
        cname = "bluyl_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "bluyl.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bold(self):
        cname = "bold"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "bold.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bold_r(self):
        cname = "bold_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "bold.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brwnyl(self):
        cname = "brwnyl"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "brwnyl.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brwnyl_r(self):
        cname = "brwnyl_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "brwnyl.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def burg(self):
        cname = "burg"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "burg.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def burg_r(self):
        cname = "burg_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "burg.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def burgyl(self):
        cname = "burgyl"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "burgyl.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def burgyl_r(self):
        cname = "burgyl_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "burgyl.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def darkmint(self):
        cname = "darkmint"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "darkmint.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def darkmint_r(self):
        cname = "darkmint_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "darkmint.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def earth(self):
        cname = "earth"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "earth.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def earth_r(self):
        cname = "earth_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "earth.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def emrld(self):
        cname = "emrld"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "emrld.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def emrld_r(self):
        cname = "emrld_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "emrld.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def fall(self):
        cname = "fall"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "fall.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def fall_r(self):
        cname = "fall_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "fall.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def geyser(self):
        cname = "geyser"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "geyser.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def geyser_r(self):
        cname = "geyser_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "geyser.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def magenta(self):
        cname = "magenta"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "magenta.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def magenta_r(self):
        cname = "magenta_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "magenta.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def mint(self):
        cname = "mint"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "mint.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def mint_r(self):
        cname = "mint_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "mint.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def oryel(self):
        cname = "oryel"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "oryel.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def oryel_r(self):
        cname = "oryel_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "oryel.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel(self):
        cname = "pastel"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "pastel.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel_r(self):
        cname = "pastel_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "pastel.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def peach(self):
        cname = "peach"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "peach.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def peach_r(self):
        cname = "peach_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "peach.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pinkyl(self):
        cname = "pinkyl"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "pinkyl.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pinkyl_r(self):
        cname = "pinkyl_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "pinkyl.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prism(self):
        cname = "prism"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "prism.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prism_r(self):
        cname = "prism_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "prism.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purp(self):
        cname = "purp"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "purp.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purp_r(self):
        cname = "purp_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "purp.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purpor(self):
        cname = "purpor"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "purpor.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purpor_r(self):
        cname = "purpor_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "purpor.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def redor(self):
        cname = "redor"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "redor.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def redor_r(self):
        cname = "redor_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "redor.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def safe(self):
        cname = "safe"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "safe.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def safe_r(self):
        cname = "safe_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "safe.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def sunset(self):
        cname = "sunset"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "sunset.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def sunset_r(self):
        cname = "sunset_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "sunset.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def sunsetdark(self):
        cname = "sunsetdark"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "sunsetdark.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def sunsetdark_r(self):
        cname = "sunsetdark_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "sunsetdark.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def teal(self):
        cname = "teal"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "teal.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def teal_r(self):
        cname = "teal_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "teal.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tealgrn(self):
        cname = "tealgrn"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "tealgrn.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tealgrn_r(self):
        cname = "tealgrn_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "tealgrn.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tealrose(self):
        cname = "tealrose"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "tealrose.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tealrose_r(self):
        cname = "tealrose_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "tealrose.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def temps(self):
        cname = "temps"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "temps.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def temps_r(self):
        cname = "temps_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "temps.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tropic(self):
        cname = "tropic"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "tropic.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tropic_r(self):
        cname = "tropic_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "tropic.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def vivid(self):
        cname = "vivid"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "vivid.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def vivid_r(self):
        cname = "vivid_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cartocolors",  "vivid.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def algae(self):
        cname = "algae"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "algae.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def algae_r(self):
        cname = "algae_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "algae.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def amp(self):
        cname = "amp"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "amp.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def amp_r(self):
        cname = "amp_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "amp.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def balance(self):
        cname = "balance"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "balance.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def balance_r(self):
        cname = "balance_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "balance.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def curl(self):
        cname = "curl"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "curl.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def curl_r(self):
        cname = "curl_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "curl.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def deep(self):
        cname = "deep"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "deep.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def deep_r(self):
        cname = "deep_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "deep.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def delta(self):
        cname = "delta"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "delta.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def delta_r(self):
        cname = "delta_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "delta.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def dense(self):
        cname = "dense"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "dense.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def dense_r(self):
        cname = "dense_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "dense.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gray(self):
        cname = "gray"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "gray.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gray_r(self):
        cname = "gray_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "gray.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def haline(self):
        cname = "haline"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "haline.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def haline_r(self):
        cname = "haline_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "haline.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ice(self):
        cname = "ice"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "ice.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ice_r(self):
        cname = "ice_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "ice.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def matter(self):
        cname = "matter"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "matter.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def matter_r(self):
        cname = "matter_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "matter.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def oxy(self):
        cname = "oxy"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "oxy.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def oxy_r(self):
        cname = "oxy_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "oxy.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def phase(self):
        cname = "phase"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "phase.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def phase_r(self):
        cname = "phase_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "phase.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def solar(self):
        cname = "solar"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "solar.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def solar_r(self):
        cname = "solar_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "solar.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def speed(self):
        cname = "speed"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "speed.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def speed_r(self):
        cname = "speed_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "speed.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tempo(self):
        cname = "tempo"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "tempo.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tempo_r(self):
        cname = "tempo_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "tempo.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def thermal(self):
        cname = "thermal"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "thermal.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def thermal_r(self):
        cname = "thermal_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "thermal.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def turbid(self):
        cname = "turbid"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "turbid.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def turbid_r(self):
        cname = "turbid_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cmocean",  "turbid.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def accent(self):
        cname = "accent"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "accent.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def accent_r(self):
        cname = "accent_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "accent.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def accent_3(self):
        cname = "accent_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "accent_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def accent_3_r(self):
        cname = "accent_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "accent_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def accent_4(self):
        cname = "accent_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "accent_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def accent_4_r(self):
        cname = "accent_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "accent_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def accent_5(self):
        cname = "accent_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "accent_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def accent_5_r(self):
        cname = "accent_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "accent_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def accent_6(self):
        cname = "accent_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "accent_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def accent_6_r(self):
        cname = "accent_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "accent_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def accent_7(self):
        cname = "accent_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "accent_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def accent_7_r(self):
        cname = "accent_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "accent_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def accent_8(self):
        cname = "accent_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "accent_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def accent_8_r(self):
        cname = "accent_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "accent_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blues(self):
        cname = "blues"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "blues.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blues_r(self):
        cname = "blues_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "blues.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blues_3(self):
        cname = "blues_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "blues_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blues_3_r(self):
        cname = "blues_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "blues_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blues_4(self):
        cname = "blues_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "blues_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blues_4_r(self):
        cname = "blues_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "blues_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blues_5(self):
        cname = "blues_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "blues_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blues_5_r(self):
        cname = "blues_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "blues_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blues_6(self):
        cname = "blues_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "blues_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blues_6_r(self):
        cname = "blues_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "blues_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blues_7(self):
        cname = "blues_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "blues_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blues_7_r(self):
        cname = "blues_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "blues_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blues_8(self):
        cname = "blues_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "blues_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blues_8_r(self):
        cname = "blues_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "blues_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blues_9(self):
        cname = "blues_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "blues_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blues_9_r(self):
        cname = "blues_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "blues_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brbg(self):
        cname = "brbg"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "brbg.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brbg_r(self):
        cname = "brbg_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "brbg.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brbg_10(self):
        cname = "brbg_10"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "brbg_10.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brbg_10_r(self):
        cname = "brbg_10_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "brbg_10.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brbg_11(self):
        cname = "brbg_11"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "brbg_11.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brbg_11_r(self):
        cname = "brbg_11_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "brbg_11.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brbg_3(self):
        cname = "brbg_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "brbg_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brbg_3_r(self):
        cname = "brbg_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "brbg_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brbg_4(self):
        cname = "brbg_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "brbg_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brbg_4_r(self):
        cname = "brbg_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "brbg_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brbg_5(self):
        cname = "brbg_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "brbg_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brbg_5_r(self):
        cname = "brbg_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "brbg_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brbg_6(self):
        cname = "brbg_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "brbg_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brbg_6_r(self):
        cname = "brbg_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "brbg_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brbg_7(self):
        cname = "brbg_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "brbg_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brbg_7_r(self):
        cname = "brbg_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "brbg_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brbg_8(self):
        cname = "brbg_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "brbg_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brbg_8_r(self):
        cname = "brbg_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "brbg_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brbg_9(self):
        cname = "brbg_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "brbg_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brbg_9_r(self):
        cname = "brbg_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "brbg_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bugn(self):
        cname = "bugn"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bugn.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bugn_r(self):
        cname = "bugn_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bugn.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bugn_3(self):
        cname = "bugn_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bugn_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bugn_3_r(self):
        cname = "bugn_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bugn_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bugn_4(self):
        cname = "bugn_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bugn_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bugn_4_r(self):
        cname = "bugn_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bugn_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bugn_5(self):
        cname = "bugn_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bugn_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bugn_5_r(self):
        cname = "bugn_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bugn_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bugn_6(self):
        cname = "bugn_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bugn_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bugn_6_r(self):
        cname = "bugn_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bugn_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bugn_7(self):
        cname = "bugn_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bugn_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bugn_7_r(self):
        cname = "bugn_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bugn_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bugn_8(self):
        cname = "bugn_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bugn_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bugn_8_r(self):
        cname = "bugn_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bugn_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bugn_9(self):
        cname = "bugn_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bugn_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bugn_9_r(self):
        cname = "bugn_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bugn_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bupu(self):
        cname = "bupu"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bupu.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bupu_r(self):
        cname = "bupu_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bupu.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bupu_3(self):
        cname = "bupu_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bupu_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bupu_3_r(self):
        cname = "bupu_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bupu_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bupu_4(self):
        cname = "bupu_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bupu_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bupu_4_r(self):
        cname = "bupu_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bupu_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bupu_5(self):
        cname = "bupu_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bupu_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bupu_5_r(self):
        cname = "bupu_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bupu_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bupu_6(self):
        cname = "bupu_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bupu_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bupu_6_r(self):
        cname = "bupu_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bupu_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bupu_7(self):
        cname = "bupu_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bupu_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bupu_7_r(self):
        cname = "bupu_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bupu_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bupu_8(self):
        cname = "bupu_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bupu_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bupu_8_r(self):
        cname = "bupu_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bupu_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bupu_9(self):
        cname = "bupu_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bupu_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bupu_9_r(self):
        cname = "bupu_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "bupu_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def dark2(self):
        cname = "dark2"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "dark2.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def dark2_r(self):
        cname = "dark2_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "dark2.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def dark2_3(self):
        cname = "dark2_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "dark2_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def dark2_3_r(self):
        cname = "dark2_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "dark2_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def dark2_4(self):
        cname = "dark2_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "dark2_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def dark2_4_r(self):
        cname = "dark2_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "dark2_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def dark2_5(self):
        cname = "dark2_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "dark2_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def dark2_5_r(self):
        cname = "dark2_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "dark2_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def dark2_6(self):
        cname = "dark2_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "dark2_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def dark2_6_r(self):
        cname = "dark2_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "dark2_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def dark2_7(self):
        cname = "dark2_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "dark2_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def dark2_7_r(self):
        cname = "dark2_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "dark2_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def dark2_8(self):
        cname = "dark2_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "dark2_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def dark2_8_r(self):
        cname = "dark2_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "dark2_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gnbu(self):
        cname = "gnbu"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "gnbu.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gnbu_r(self):
        cname = "gnbu_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "gnbu.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gnbu_3(self):
        cname = "gnbu_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "gnbu_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gnbu_3_r(self):
        cname = "gnbu_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "gnbu_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gnbu_4(self):
        cname = "gnbu_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "gnbu_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gnbu_4_r(self):
        cname = "gnbu_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "gnbu_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gnbu_5(self):
        cname = "gnbu_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "gnbu_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gnbu_5_r(self):
        cname = "gnbu_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "gnbu_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gnbu_6(self):
        cname = "gnbu_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "gnbu_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gnbu_6_r(self):
        cname = "gnbu_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "gnbu_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gnbu_7(self):
        cname = "gnbu_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "gnbu_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gnbu_7_r(self):
        cname = "gnbu_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "gnbu_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gnbu_8(self):
        cname = "gnbu_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "gnbu_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gnbu_8_r(self):
        cname = "gnbu_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "gnbu_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gnbu_9(self):
        cname = "gnbu_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "gnbu_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gnbu_9_r(self):
        cname = "gnbu_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "gnbu_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greens(self):
        cname = "greens"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greens.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greens_r(self):
        cname = "greens_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greens.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greens_3(self):
        cname = "greens_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greens_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greens_3_r(self):
        cname = "greens_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greens_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greens_4(self):
        cname = "greens_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greens_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greens_4_r(self):
        cname = "greens_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greens_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greens_5(self):
        cname = "greens_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greens_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greens_5_r(self):
        cname = "greens_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greens_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greens_6(self):
        cname = "greens_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greens_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greens_6_r(self):
        cname = "greens_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greens_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greens_7(self):
        cname = "greens_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greens_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greens_7_r(self):
        cname = "greens_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greens_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greens_8(self):
        cname = "greens_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greens_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greens_8_r(self):
        cname = "greens_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greens_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greens_9(self):
        cname = "greens_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greens_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greens_9_r(self):
        cname = "greens_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greens_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greys(self):
        cname = "greys"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greys.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greys_r(self):
        cname = "greys_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greys.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greys_3(self):
        cname = "greys_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greys_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greys_3_r(self):
        cname = "greys_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greys_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greys_4(self):
        cname = "greys_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greys_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greys_4_r(self):
        cname = "greys_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greys_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greys_5(self):
        cname = "greys_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greys_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greys_5_r(self):
        cname = "greys_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greys_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greys_6(self):
        cname = "greys_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greys_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greys_6_r(self):
        cname = "greys_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greys_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greys_7(self):
        cname = "greys_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greys_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greys_7_r(self):
        cname = "greys_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greys_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greys_8(self):
        cname = "greys_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greys_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greys_8_r(self):
        cname = "greys_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greys_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greys_9(self):
        cname = "greys_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greys_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greys_9_r(self):
        cname = "greys_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "greys_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def oranges(self):
        cname = "oranges"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "oranges.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def oranges_r(self):
        cname = "oranges_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "oranges.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def oranges_3(self):
        cname = "oranges_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "oranges_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def oranges_3_r(self):
        cname = "oranges_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "oranges_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def oranges_4(self):
        cname = "oranges_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "oranges_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def oranges_4_r(self):
        cname = "oranges_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "oranges_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def oranges_5(self):
        cname = "oranges_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "oranges_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def oranges_5_r(self):
        cname = "oranges_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "oranges_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def oranges_6(self):
        cname = "oranges_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "oranges_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def oranges_6_r(self):
        cname = "oranges_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "oranges_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def oranges_7(self):
        cname = "oranges_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "oranges_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def oranges_7_r(self):
        cname = "oranges_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "oranges_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def oranges_8(self):
        cname = "oranges_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "oranges_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def oranges_8_r(self):
        cname = "oranges_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "oranges_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def oranges_9(self):
        cname = "oranges_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "oranges_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def oranges_9_r(self):
        cname = "oranges_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "oranges_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def orrd(self):
        cname = "orrd"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "orrd.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def orrd_r(self):
        cname = "orrd_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "orrd.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def orrd_3(self):
        cname = "orrd_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "orrd_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def orrd_3_r(self):
        cname = "orrd_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "orrd_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def orrd_4(self):
        cname = "orrd_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "orrd_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def orrd_4_r(self):
        cname = "orrd_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "orrd_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def orrd_5(self):
        cname = "orrd_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "orrd_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def orrd_5_r(self):
        cname = "orrd_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "orrd_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def orrd_6(self):
        cname = "orrd_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "orrd_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def orrd_6_r(self):
        cname = "orrd_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "orrd_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def orrd_7(self):
        cname = "orrd_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "orrd_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def orrd_7_r(self):
        cname = "orrd_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "orrd_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def orrd_8(self):
        cname = "orrd_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "orrd_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def orrd_8_r(self):
        cname = "orrd_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "orrd_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def orrd_9(self):
        cname = "orrd_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "orrd_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def orrd_9_r(self):
        cname = "orrd_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "orrd_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def paired(self):
        cname = "paired"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "paired.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def paired_r(self):
        cname = "paired_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "paired.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def paired_10(self):
        cname = "paired_10"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "paired_10.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def paired_10_r(self):
        cname = "paired_10_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "paired_10.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def paired_11(self):
        cname = "paired_11"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "paired_11.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def paired_11_r(self):
        cname = "paired_11_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "paired_11.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def paired_12(self):
        cname = "paired_12"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "paired_12.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def paired_12_r(self):
        cname = "paired_12_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "paired_12.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def paired_3(self):
        cname = "paired_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "paired_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def paired_3_r(self):
        cname = "paired_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "paired_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def paired_4(self):
        cname = "paired_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "paired_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def paired_4_r(self):
        cname = "paired_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "paired_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def paired_5(self):
        cname = "paired_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "paired_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def paired_5_r(self):
        cname = "paired_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "paired_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def paired_6(self):
        cname = "paired_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "paired_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def paired_6_r(self):
        cname = "paired_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "paired_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def paired_7(self):
        cname = "paired_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "paired_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def paired_7_r(self):
        cname = "paired_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "paired_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def paired_8(self):
        cname = "paired_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "paired_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def paired_8_r(self):
        cname = "paired_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "paired_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def paired_9(self):
        cname = "paired_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "paired_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def paired_9_r(self):
        cname = "paired_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "paired_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel1(self):
        cname = "pastel1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pastel1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel1_r(self):
        cname = "pastel1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pastel1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel1_3(self):
        cname = "pastel1_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pastel1_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel1_3_r(self):
        cname = "pastel1_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pastel1_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel1_4(self):
        cname = "pastel1_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pastel1_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel1_4_r(self):
        cname = "pastel1_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pastel1_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel1_5(self):
        cname = "pastel1_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pastel1_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel1_5_r(self):
        cname = "pastel1_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pastel1_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel1_6(self):
        cname = "pastel1_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pastel1_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel1_6_r(self):
        cname = "pastel1_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pastel1_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel1_7(self):
        cname = "pastel1_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pastel1_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel1_7_r(self):
        cname = "pastel1_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pastel1_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel1_8(self):
        cname = "pastel1_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pastel1_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel1_8_r(self):
        cname = "pastel1_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pastel1_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel1_9(self):
        cname = "pastel1_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pastel1_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel1_9_r(self):
        cname = "pastel1_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pastel1_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel2(self):
        cname = "pastel2"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pastel2.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel2_r(self):
        cname = "pastel2_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pastel2.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel2_3(self):
        cname = "pastel2_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pastel2_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel2_3_r(self):
        cname = "pastel2_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pastel2_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel2_4(self):
        cname = "pastel2_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pastel2_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel2_4_r(self):
        cname = "pastel2_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pastel2_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel2_5(self):
        cname = "pastel2_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pastel2_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel2_5_r(self):
        cname = "pastel2_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pastel2_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel2_6(self):
        cname = "pastel2_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pastel2_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel2_6_r(self):
        cname = "pastel2_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pastel2_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel2_7(self):
        cname = "pastel2_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pastel2_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel2_7_r(self):
        cname = "pastel2_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pastel2_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel2_8(self):
        cname = "pastel2_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pastel2_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pastel2_8_r(self):
        cname = "pastel2_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pastel2_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def piyg(self):
        cname = "piyg"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "piyg.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def piyg_r(self):
        cname = "piyg_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "piyg.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def piyg_10(self):
        cname = "piyg_10"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "piyg_10.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def piyg_10_r(self):
        cname = "piyg_10_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "piyg_10.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def piyg_11(self):
        cname = "piyg_11"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "piyg_11.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def piyg_11_r(self):
        cname = "piyg_11_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "piyg_11.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def piyg_3(self):
        cname = "piyg_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "piyg_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def piyg_3_r(self):
        cname = "piyg_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "piyg_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def piyg_4(self):
        cname = "piyg_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "piyg_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def piyg_4_r(self):
        cname = "piyg_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "piyg_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def piyg_5(self):
        cname = "piyg_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "piyg_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def piyg_5_r(self):
        cname = "piyg_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "piyg_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def piyg_6(self):
        cname = "piyg_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "piyg_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def piyg_6_r(self):
        cname = "piyg_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "piyg_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def piyg_7(self):
        cname = "piyg_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "piyg_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def piyg_7_r(self):
        cname = "piyg_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "piyg_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def piyg_8(self):
        cname = "piyg_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "piyg_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def piyg_8_r(self):
        cname = "piyg_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "piyg_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def piyg_9(self):
        cname = "piyg_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "piyg_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def piyg_9_r(self):
        cname = "piyg_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "piyg_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prgn(self):
        cname = "prgn"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "prgn.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prgn_r(self):
        cname = "prgn_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "prgn.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prgn_10(self):
        cname = "prgn_10"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "prgn_10.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prgn_10_r(self):
        cname = "prgn_10_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "prgn_10.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prgn_11(self):
        cname = "prgn_11"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "prgn_11.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prgn_11_r(self):
        cname = "prgn_11_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "prgn_11.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prgn_3(self):
        cname = "prgn_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "prgn_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prgn_3_r(self):
        cname = "prgn_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "prgn_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prgn_4(self):
        cname = "prgn_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "prgn_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prgn_4_r(self):
        cname = "prgn_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "prgn_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prgn_5(self):
        cname = "prgn_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "prgn_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prgn_5_r(self):
        cname = "prgn_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "prgn_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prgn_6(self):
        cname = "prgn_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "prgn_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prgn_6_r(self):
        cname = "prgn_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "prgn_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prgn_7(self):
        cname = "prgn_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "prgn_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prgn_7_r(self):
        cname = "prgn_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "prgn_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prgn_8(self):
        cname = "prgn_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "prgn_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prgn_8_r(self):
        cname = "prgn_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "prgn_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prgn_9(self):
        cname = "prgn_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "prgn_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prgn_9_r(self):
        cname = "prgn_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "prgn_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubu(self):
        cname = "pubu"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubu.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubu_r(self):
        cname = "pubu_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubu.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubu_3(self):
        cname = "pubu_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubu_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubu_3_r(self):
        cname = "pubu_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubu_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubu_4(self):
        cname = "pubu_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubu_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubu_4_r(self):
        cname = "pubu_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubu_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubu_5(self):
        cname = "pubu_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubu_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubu_5_r(self):
        cname = "pubu_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubu_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubu_6(self):
        cname = "pubu_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubu_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubu_6_r(self):
        cname = "pubu_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubu_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubu_7(self):
        cname = "pubu_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubu_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubu_7_r(self):
        cname = "pubu_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubu_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubu_8(self):
        cname = "pubu_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubu_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubu_8_r(self):
        cname = "pubu_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubu_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubu_9(self):
        cname = "pubu_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubu_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubu_9_r(self):
        cname = "pubu_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubu_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubugn(self):
        cname = "pubugn"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubugn.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubugn_r(self):
        cname = "pubugn_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubugn.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubugn_3(self):
        cname = "pubugn_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubugn_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubugn_3_r(self):
        cname = "pubugn_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubugn_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubugn_4(self):
        cname = "pubugn_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubugn_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubugn_4_r(self):
        cname = "pubugn_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubugn_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubugn_5(self):
        cname = "pubugn_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubugn_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubugn_5_r(self):
        cname = "pubugn_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubugn_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubugn_6(self):
        cname = "pubugn_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubugn_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubugn_6_r(self):
        cname = "pubugn_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubugn_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubugn_7(self):
        cname = "pubugn_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubugn_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubugn_7_r(self):
        cname = "pubugn_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubugn_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubugn_8(self):
        cname = "pubugn_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubugn_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubugn_8_r(self):
        cname = "pubugn_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubugn_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubugn_9(self):
        cname = "pubugn_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubugn_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pubugn_9_r(self):
        cname = "pubugn_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "pubugn_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def puor(self):
        cname = "puor"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "puor.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def puor_r(self):
        cname = "puor_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "puor.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def puor_10(self):
        cname = "puor_10"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "puor_10.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def puor_10_r(self):
        cname = "puor_10_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "puor_10.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def puor_11(self):
        cname = "puor_11"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "puor_11.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def puor_11_r(self):
        cname = "puor_11_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "puor_11.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def puor_3(self):
        cname = "puor_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "puor_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def puor_3_r(self):
        cname = "puor_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "puor_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def puor_4(self):
        cname = "puor_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "puor_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def puor_4_r(self):
        cname = "puor_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "puor_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def puor_5(self):
        cname = "puor_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "puor_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def puor_5_r(self):
        cname = "puor_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "puor_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def puor_6(self):
        cname = "puor_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "puor_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def puor_6_r(self):
        cname = "puor_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "puor_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def puor_7(self):
        cname = "puor_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "puor_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def puor_7_r(self):
        cname = "puor_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "puor_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def puor_8(self):
        cname = "puor_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "puor_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def puor_8_r(self):
        cname = "puor_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "puor_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def puor_9(self):
        cname = "puor_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "puor_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def puor_9_r(self):
        cname = "puor_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "puor_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purd(self):
        cname = "purd"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purd.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purd_r(self):
        cname = "purd_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purd.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purd_3(self):
        cname = "purd_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purd_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purd_3_r(self):
        cname = "purd_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purd_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purd_4(self):
        cname = "purd_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purd_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purd_4_r(self):
        cname = "purd_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purd_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purd_5(self):
        cname = "purd_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purd_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purd_5_r(self):
        cname = "purd_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purd_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purd_6(self):
        cname = "purd_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purd_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purd_6_r(self):
        cname = "purd_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purd_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purd_7(self):
        cname = "purd_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purd_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purd_7_r(self):
        cname = "purd_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purd_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purd_8(self):
        cname = "purd_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purd_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purd_8_r(self):
        cname = "purd_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purd_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purd_9(self):
        cname = "purd_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purd_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purd_9_r(self):
        cname = "purd_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purd_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purples(self):
        cname = "purples"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purples.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purples_r(self):
        cname = "purples_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purples.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purples_3(self):
        cname = "purples_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purples_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purples_3_r(self):
        cname = "purples_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purples_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purples_4(self):
        cname = "purples_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purples_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purples_4_r(self):
        cname = "purples_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purples_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purples_5(self):
        cname = "purples_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purples_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purples_5_r(self):
        cname = "purples_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purples_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purples_6(self):
        cname = "purples_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purples_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purples_6_r(self):
        cname = "purples_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purples_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purples_7(self):
        cname = "purples_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purples_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purples_7_r(self):
        cname = "purples_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purples_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purples_8(self):
        cname = "purples_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purples_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purples_8_r(self):
        cname = "purples_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purples_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purples_9(self):
        cname = "purples_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purples_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purples_9_r(self):
        cname = "purples_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "purples_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdbu(self):
        cname = "rdbu"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdbu.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdbu_r(self):
        cname = "rdbu_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdbu.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdbu_10(self):
        cname = "rdbu_10"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdbu_10.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdbu_10_r(self):
        cname = "rdbu_10_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdbu_10.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdbu_11(self):
        cname = "rdbu_11"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdbu_11.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdbu_11_r(self):
        cname = "rdbu_11_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdbu_11.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdbu_3(self):
        cname = "rdbu_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdbu_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdbu_3_r(self):
        cname = "rdbu_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdbu_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdbu_4(self):
        cname = "rdbu_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdbu_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdbu_4_r(self):
        cname = "rdbu_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdbu_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdbu_5(self):
        cname = "rdbu_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdbu_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdbu_5_r(self):
        cname = "rdbu_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdbu_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdbu_6(self):
        cname = "rdbu_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdbu_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdbu_6_r(self):
        cname = "rdbu_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdbu_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdbu_7(self):
        cname = "rdbu_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdbu_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdbu_7_r(self):
        cname = "rdbu_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdbu_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdbu_8(self):
        cname = "rdbu_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdbu_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdbu_8_r(self):
        cname = "rdbu_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdbu_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdbu_9(self):
        cname = "rdbu_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdbu_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdbu_9_r(self):
        cname = "rdbu_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdbu_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdgy(self):
        cname = "rdgy"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdgy.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdgy_r(self):
        cname = "rdgy_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdgy.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdgy_10(self):
        cname = "rdgy_10"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdgy_10.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdgy_10_r(self):
        cname = "rdgy_10_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdgy_10.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdgy_11(self):
        cname = "rdgy_11"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdgy_11.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdgy_11_r(self):
        cname = "rdgy_11_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdgy_11.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdgy_3(self):
        cname = "rdgy_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdgy_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdgy_3_r(self):
        cname = "rdgy_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdgy_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdgy_4(self):
        cname = "rdgy_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdgy_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdgy_4_r(self):
        cname = "rdgy_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdgy_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdgy_5(self):
        cname = "rdgy_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdgy_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdgy_5_r(self):
        cname = "rdgy_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdgy_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdgy_6(self):
        cname = "rdgy_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdgy_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdgy_6_r(self):
        cname = "rdgy_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdgy_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdgy_7(self):
        cname = "rdgy_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdgy_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdgy_7_r(self):
        cname = "rdgy_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdgy_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdgy_8(self):
        cname = "rdgy_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdgy_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdgy_8_r(self):
        cname = "rdgy_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdgy_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdgy_9(self):
        cname = "rdgy_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdgy_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdgy_9_r(self):
        cname = "rdgy_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdgy_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdpu(self):
        cname = "rdpu"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdpu.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdpu_r(self):
        cname = "rdpu_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdpu.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdpu_3(self):
        cname = "rdpu_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdpu_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdpu_3_r(self):
        cname = "rdpu_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdpu_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdpu_4(self):
        cname = "rdpu_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdpu_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdpu_4_r(self):
        cname = "rdpu_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdpu_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdpu_5(self):
        cname = "rdpu_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdpu_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdpu_5_r(self):
        cname = "rdpu_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdpu_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdpu_6(self):
        cname = "rdpu_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdpu_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdpu_6_r(self):
        cname = "rdpu_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdpu_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdpu_7(self):
        cname = "rdpu_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdpu_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdpu_7_r(self):
        cname = "rdpu_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdpu_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdpu_8(self):
        cname = "rdpu_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdpu_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdpu_8_r(self):
        cname = "rdpu_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdpu_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdpu_9(self):
        cname = "rdpu_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdpu_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdpu_9_r(self):
        cname = "rdpu_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdpu_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylbu(self):
        cname = "rdylbu"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylbu.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylbu_r(self):
        cname = "rdylbu_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylbu.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylbu_10(self):
        cname = "rdylbu_10"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylbu_10.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylbu_10_r(self):
        cname = "rdylbu_10_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylbu_10.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylbu_11(self):
        cname = "rdylbu_11"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylbu_11.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylbu_11_r(self):
        cname = "rdylbu_11_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylbu_11.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylbu_3(self):
        cname = "rdylbu_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylbu_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylbu_3_r(self):
        cname = "rdylbu_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylbu_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylbu_4(self):
        cname = "rdylbu_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylbu_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylbu_4_r(self):
        cname = "rdylbu_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylbu_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylbu_5(self):
        cname = "rdylbu_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylbu_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylbu_5_r(self):
        cname = "rdylbu_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylbu_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylbu_6(self):
        cname = "rdylbu_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylbu_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylbu_6_r(self):
        cname = "rdylbu_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylbu_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylbu_7(self):
        cname = "rdylbu_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylbu_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylbu_7_r(self):
        cname = "rdylbu_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylbu_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylbu_8(self):
        cname = "rdylbu_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylbu_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylbu_8_r(self):
        cname = "rdylbu_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylbu_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylbu_9(self):
        cname = "rdylbu_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylbu_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylbu_9_r(self):
        cname = "rdylbu_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylbu_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylgn(self):
        cname = "rdylgn"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylgn.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylgn_r(self):
        cname = "rdylgn_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylgn.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylgn_10(self):
        cname = "rdylgn_10"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylgn_10.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylgn_10_r(self):
        cname = "rdylgn_10_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylgn_10.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylgn_11(self):
        cname = "rdylgn_11"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylgn_11.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylgn_11_r(self):
        cname = "rdylgn_11_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylgn_11.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylgn_3(self):
        cname = "rdylgn_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylgn_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylgn_3_r(self):
        cname = "rdylgn_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylgn_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylgn_4(self):
        cname = "rdylgn_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylgn_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylgn_4_r(self):
        cname = "rdylgn_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylgn_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylgn_5(self):
        cname = "rdylgn_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylgn_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylgn_5_r(self):
        cname = "rdylgn_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylgn_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylgn_6(self):
        cname = "rdylgn_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylgn_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylgn_6_r(self):
        cname = "rdylgn_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylgn_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylgn_7(self):
        cname = "rdylgn_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylgn_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylgn_7_r(self):
        cname = "rdylgn_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylgn_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylgn_8(self):
        cname = "rdylgn_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylgn_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylgn_8_r(self):
        cname = "rdylgn_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylgn_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylgn_9(self):
        cname = "rdylgn_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylgn_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rdylgn_9_r(self):
        cname = "rdylgn_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "rdylgn_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def reds(self):
        cname = "reds"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "reds.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def reds_r(self):
        cname = "reds_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "reds.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def reds_3(self):
        cname = "reds_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "reds_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def reds_3_r(self):
        cname = "reds_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "reds_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def reds_4(self):
        cname = "reds_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "reds_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def reds_4_r(self):
        cname = "reds_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "reds_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def reds_5(self):
        cname = "reds_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "reds_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def reds_5_r(self):
        cname = "reds_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "reds_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def reds_6(self):
        cname = "reds_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "reds_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def reds_6_r(self):
        cname = "reds_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "reds_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def reds_7(self):
        cname = "reds_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "reds_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def reds_7_r(self):
        cname = "reds_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "reds_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def reds_8(self):
        cname = "reds_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "reds_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def reds_8_r(self):
        cname = "reds_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "reds_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def reds_9(self):
        cname = "reds_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "reds_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def reds_9_r(self):
        cname = "reds_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "reds_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set1(self):
        cname = "set1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set1_r(self):
        cname = "set1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set1_3(self):
        cname = "set1_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set1_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set1_3_r(self):
        cname = "set1_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set1_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set1_4(self):
        cname = "set1_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set1_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set1_4_r(self):
        cname = "set1_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set1_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set1_5(self):
        cname = "set1_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set1_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set1_5_r(self):
        cname = "set1_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set1_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set1_6(self):
        cname = "set1_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set1_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set1_6_r(self):
        cname = "set1_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set1_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set1_7(self):
        cname = "set1_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set1_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set1_7_r(self):
        cname = "set1_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set1_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set1_8(self):
        cname = "set1_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set1_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set1_8_r(self):
        cname = "set1_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set1_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set1_9(self):
        cname = "set1_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set1_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set1_9_r(self):
        cname = "set1_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set1_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set2(self):
        cname = "set2"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set2.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set2_r(self):
        cname = "set2_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set2.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set2_3(self):
        cname = "set2_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set2_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set2_3_r(self):
        cname = "set2_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set2_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set2_4(self):
        cname = "set2_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set2_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set2_4_r(self):
        cname = "set2_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set2_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set2_5(self):
        cname = "set2_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set2_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set2_5_r(self):
        cname = "set2_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set2_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set2_6(self):
        cname = "set2_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set2_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set2_6_r(self):
        cname = "set2_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set2_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set2_7(self):
        cname = "set2_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set2_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set2_7_r(self):
        cname = "set2_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set2_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set2_8(self):
        cname = "set2_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set2_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set2_8_r(self):
        cname = "set2_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set2_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set3(self):
        cname = "set3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set3_r(self):
        cname = "set3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set3_10(self):
        cname = "set3_10"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set3_10.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set3_10_r(self):
        cname = "set3_10_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set3_10.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set3_11(self):
        cname = "set3_11"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set3_11.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set3_11_r(self):
        cname = "set3_11_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set3_11.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set3_12(self):
        cname = "set3_12"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set3_12.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set3_12_r(self):
        cname = "set3_12_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set3_12.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set3_3(self):
        cname = "set3_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set3_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set3_3_r(self):
        cname = "set3_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set3_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set3_4(self):
        cname = "set3_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set3_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set3_4_r(self):
        cname = "set3_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set3_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set3_5(self):
        cname = "set3_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set3_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set3_5_r(self):
        cname = "set3_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set3_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set3_6(self):
        cname = "set3_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set3_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set3_6_r(self):
        cname = "set3_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set3_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set3_7(self):
        cname = "set3_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set3_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set3_7_r(self):
        cname = "set3_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set3_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set3_8(self):
        cname = "set3_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set3_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set3_8_r(self):
        cname = "set3_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set3_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set3_9(self):
        cname = "set3_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set3_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def set3_9_r(self):
        cname = "set3_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "set3_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def spectral(self):
        cname = "spectral"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "spectral.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def spectral_r(self):
        cname = "spectral_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "spectral.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def spectral_10(self):
        cname = "spectral_10"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "spectral_10.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def spectral_10_r(self):
        cname = "spectral_10_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "spectral_10.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def spectral_11(self):
        cname = "spectral_11"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "spectral_11.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def spectral_11_r(self):
        cname = "spectral_11_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "spectral_11.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def spectral_3(self):
        cname = "spectral_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "spectral_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def spectral_3_r(self):
        cname = "spectral_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "spectral_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def spectral_4(self):
        cname = "spectral_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "spectral_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def spectral_4_r(self):
        cname = "spectral_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "spectral_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def spectral_5(self):
        cname = "spectral_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "spectral_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def spectral_5_r(self):
        cname = "spectral_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "spectral_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def spectral_6(self):
        cname = "spectral_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "spectral_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def spectral_6_r(self):
        cname = "spectral_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "spectral_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def spectral_7(self):
        cname = "spectral_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "spectral_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def spectral_7_r(self):
        cname = "spectral_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "spectral_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def spectral_8(self):
        cname = "spectral_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "spectral_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def spectral_8_r(self):
        cname = "spectral_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "spectral_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def spectral_9(self):
        cname = "spectral_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "spectral_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def spectral_9_r(self):
        cname = "spectral_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "spectral_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgn(self):
        cname = "ylgn"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgn.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgn_r(self):
        cname = "ylgn_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgn.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgn_3(self):
        cname = "ylgn_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgn_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgn_3_r(self):
        cname = "ylgn_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgn_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgn_4(self):
        cname = "ylgn_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgn_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgn_4_r(self):
        cname = "ylgn_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgn_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgn_5(self):
        cname = "ylgn_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgn_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgn_5_r(self):
        cname = "ylgn_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgn_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgn_6(self):
        cname = "ylgn_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgn_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgn_6_r(self):
        cname = "ylgn_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgn_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgn_7(self):
        cname = "ylgn_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgn_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgn_7_r(self):
        cname = "ylgn_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgn_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgn_8(self):
        cname = "ylgn_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgn_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgn_8_r(self):
        cname = "ylgn_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgn_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgn_9(self):
        cname = "ylgn_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgn_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgn_9_r(self):
        cname = "ylgn_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgn_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgnbu(self):
        cname = "ylgnbu"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgnbu.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgnbu_r(self):
        cname = "ylgnbu_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgnbu.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgnbu_3(self):
        cname = "ylgnbu_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgnbu_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgnbu_3_r(self):
        cname = "ylgnbu_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgnbu_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgnbu_4(self):
        cname = "ylgnbu_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgnbu_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgnbu_4_r(self):
        cname = "ylgnbu_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgnbu_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgnbu_5(self):
        cname = "ylgnbu_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgnbu_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgnbu_5_r(self):
        cname = "ylgnbu_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgnbu_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgnbu_6(self):
        cname = "ylgnbu_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgnbu_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgnbu_6_r(self):
        cname = "ylgnbu_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgnbu_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgnbu_7(self):
        cname = "ylgnbu_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgnbu_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgnbu_7_r(self):
        cname = "ylgnbu_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgnbu_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgnbu_8(self):
        cname = "ylgnbu_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgnbu_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgnbu_8_r(self):
        cname = "ylgnbu_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgnbu_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgnbu_9(self):
        cname = "ylgnbu_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgnbu_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylgnbu_9_r(self):
        cname = "ylgnbu_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylgnbu_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorbr(self):
        cname = "ylorbr"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorbr.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorbr_r(self):
        cname = "ylorbr_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorbr.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorbr_3(self):
        cname = "ylorbr_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorbr_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorbr_3_r(self):
        cname = "ylorbr_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorbr_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorbr_4(self):
        cname = "ylorbr_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorbr_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorbr_4_r(self):
        cname = "ylorbr_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorbr_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorbr_5(self):
        cname = "ylorbr_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorbr_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorbr_5_r(self):
        cname = "ylorbr_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorbr_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorbr_6(self):
        cname = "ylorbr_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorbr_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorbr_6_r(self):
        cname = "ylorbr_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorbr_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorbr_7(self):
        cname = "ylorbr_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorbr_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorbr_7_r(self):
        cname = "ylorbr_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorbr_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorbr_8(self):
        cname = "ylorbr_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorbr_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorbr_8_r(self):
        cname = "ylorbr_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorbr_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorbr_9(self):
        cname = "ylorbr_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorbr_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorbr_9_r(self):
        cname = "ylorbr_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorbr_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorrd(self):
        cname = "ylorrd"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorrd.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorrd_r(self):
        cname = "ylorrd_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorrd.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorrd_3(self):
        cname = "ylorrd_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorrd_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorrd_3_r(self):
        cname = "ylorrd_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorrd_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorrd_4(self):
        cname = "ylorrd_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorrd_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorrd_4_r(self):
        cname = "ylorrd_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorrd_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorrd_5(self):
        cname = "ylorrd_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorrd_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorrd_5_r(self):
        cname = "ylorrd_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorrd_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorrd_6(self):
        cname = "ylorrd_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorrd_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorrd_6_r(self):
        cname = "ylorrd_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorrd_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorrd_7(self):
        cname = "ylorrd_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorrd_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorrd_7_r(self):
        cname = "ylorrd_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorrd_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorrd_8(self):
        cname = "ylorrd_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorrd_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorrd_8_r(self):
        cname = "ylorrd_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorrd_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorrd_9(self):
        cname = "ylorrd_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorrd_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ylorrd_9_r(self):
        cname = "ylorrd_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorbrewer",  "ylorrd_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def classic_16(self):
        cname = "classic_16"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cubehelix",  "classic_16.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def classic_16_r(self):
        cname = "classic_16_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cubehelix",  "classic_16.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cubehelix1_16(self):
        cname = "cubehelix1_16"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cubehelix",  "cubehelix1_16.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cubehelix1_16_r(self):
        cname = "cubehelix1_16_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cubehelix",  "cubehelix1_16.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cubehelix2_16(self):
        cname = "cubehelix2_16"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cubehelix",  "cubehelix2_16.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cubehelix2_16_r(self):
        cname = "cubehelix2_16_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cubehelix",  "cubehelix2_16.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cubehelix3_16(self):
        cname = "cubehelix3_16"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cubehelix",  "cubehelix3_16.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cubehelix3_16_r(self):
        cname = "cubehelix3_16_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cubehelix",  "cubehelix3_16.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def jim_special_16(self):
        cname = "jim_special_16"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cubehelix",  "jim_special_16.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def jim_special_16_r(self):
        cname = "jim_special_16_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cubehelix",  "jim_special_16.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def perceptual_rainbow_16(self):
        cname = "perceptual_rainbow_16"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cubehelix",  "perceptual_rainbow_16.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def perceptual_rainbow_16_r(self):
        cname = "perceptual_rainbow_16_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cubehelix",  "perceptual_rainbow_16.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purple_16(self):
        cname = "purple_16"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cubehelix",  "purple_16.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purple_16_r(self):
        cname = "purple_16_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cubehelix",  "purple_16.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def red_16(self):
        cname = "red_16"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cubehelix",  "red_16.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def red_16_r(self):
        cname = "red_16_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "cubehelix",  "red_16.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BkBlAqGrYeOrReViWh200(self):
        cname = "BkBlAqGrYeOrReViWh200"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BkBlAqGrYeOrReViWh200.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BkBlAqGrYeOrReViWh200_r(self):
        cname = "BkBlAqGrYeOrReViWh200_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BkBlAqGrYeOrReViWh200.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlAqGrWh2YeOrReVi22(self):
        cname = "BlAqGrWh2YeOrReVi22"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlAqGrWh2YeOrReVi22.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlAqGrWh2YeOrReVi22_r(self):
        cname = "BlAqGrWh2YeOrReVi22_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlAqGrWh2YeOrReVi22.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlAqGrYeOrRe(self):
        cname = "BlAqGrYeOrRe"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlAqGrYeOrRe.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlAqGrYeOrRe_r(self):
        cname = "BlAqGrYeOrRe_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlAqGrYeOrRe.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlAqGrYeOrReVi200(self):
        cname = "BlAqGrYeOrReVi200"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlAqGrYeOrReVi200.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlAqGrYeOrReVi200_r(self):
        cname = "BlAqGrYeOrReVi200_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlAqGrYeOrReVi200.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlGrYeOrReVi200(self):
        cname = "BlGrYeOrReVi200"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlGrYeOrReVi200.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlGrYeOrReVi200_r(self):
        cname = "BlGrYeOrReVi200_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlGrYeOrReVi200.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlRe(self):
        cname = "BlRe"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlRe.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlRe_r(self):
        cname = "BlRe_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlRe.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlWhRe(self):
        cname = "BlWhRe"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlWhRe.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlWhRe_r(self):
        cname = "BlWhRe_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlWhRe.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlueDarkOrange18(self):
        cname = "BlueDarkOrange18"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlueDarkOrange18.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlueDarkOrange18_r(self):
        cname = "BlueDarkOrange18_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlueDarkOrange18.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlueDarkRed18(self):
        cname = "BlueDarkRed18"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlueDarkRed18.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlueDarkRed18_r(self):
        cname = "BlueDarkRed18_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlueDarkRed18.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlueGreen14(self):
        cname = "BlueGreen14"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlueGreen14.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlueGreen14_r(self):
        cname = "BlueGreen14_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlueGreen14.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlueRed(self):
        cname = "BlueRed"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlueRed.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlueRed_r(self):
        cname = "BlueRed_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlueRed.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlueRedGray(self):
        cname = "BlueRedGray"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlueRedGray.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlueRedGray_r(self):
        cname = "BlueRedGray_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlueRedGray.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlueWhiteOrangeRed(self):
        cname = "BlueWhiteOrangeRed"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlueWhiteOrangeRed.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlueWhiteOrangeRed_r(self):
        cname = "BlueWhiteOrangeRed_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlueWhiteOrangeRed.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlueYellowRed(self):
        cname = "BlueYellowRed"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlueYellowRed.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlueYellowRed_r(self):
        cname = "BlueYellowRed_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlueYellowRed.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BrownBlue12(self):
        cname = "BrownBlue12"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BrownBlue12.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BrownBlue12_r(self):
        cname = "BrownBlue12_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BrownBlue12.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def Cat12(self):
        cname = "Cat12"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "Cat12.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def Cat12_r(self):
        cname = "Cat12_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "Cat12.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GHRSST_anomaly(self):
        cname = "GHRSST_anomaly"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GHRSST_anomaly.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GHRSST_anomaly_r(self):
        cname = "GHRSST_anomaly_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GHRSST_anomaly.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_cool(self):
        cname = "GMT_cool"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_cool.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_cool_r(self):
        cname = "GMT_cool_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_cool.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_copper(self):
        cname = "GMT_copper"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_copper.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_copper_r(self):
        cname = "GMT_copper_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_copper.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_drywet(self):
        cname = "GMT_drywet"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_drywet.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_drywet_r(self):
        cname = "GMT_drywet_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_drywet.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_gebco(self):
        cname = "GMT_gebco"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_gebco.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_gebco_r(self):
        cname = "GMT_gebco_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_gebco.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_globe(self):
        cname = "GMT_globe"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_globe.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_globe_r(self):
        cname = "GMT_globe_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_globe.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_gray(self):
        cname = "GMT_gray"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_gray.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_gray_r(self):
        cname = "GMT_gray_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_gray.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_haxby(self):
        cname = "GMT_haxby"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_haxby.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_haxby_r(self):
        cname = "GMT_haxby_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_haxby.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_hot(self):
        cname = "GMT_hot"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_hot.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_hot_r(self):
        cname = "GMT_hot_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_hot.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_jet(self):
        cname = "GMT_jet"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_jet.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_jet_r(self):
        cname = "GMT_jet_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_jet.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_nighttime(self):
        cname = "GMT_nighttime"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_nighttime.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_nighttime_r(self):
        cname = "GMT_nighttime_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_nighttime.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_no_green(self):
        cname = "GMT_no_green"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_no_green.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_no_green_r(self):
        cname = "GMT_no_green_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_no_green.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_ocean(self):
        cname = "GMT_ocean"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_ocean.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_ocean_r(self):
        cname = "GMT_ocean_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_ocean.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_paired(self):
        cname = "GMT_paired"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_paired.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_paired_r(self):
        cname = "GMT_paired_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_paired.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_panoply(self):
        cname = "GMT_panoply"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_panoply.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_panoply_r(self):
        cname = "GMT_panoply_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_panoply.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_polar(self):
        cname = "GMT_polar"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_polar.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_polar_r(self):
        cname = "GMT_polar_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_polar.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_red2green(self):
        cname = "GMT_red2green"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_red2green.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_red2green_r(self):
        cname = "GMT_red2green_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_red2green.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_relief(self):
        cname = "GMT_relief"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_relief.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_relief_r(self):
        cname = "GMT_relief_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_relief.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_relief_oceanonly(self):
        cname = "GMT_relief_oceanonly"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_relief_oceanonly.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_relief_oceanonly_r(self):
        cname = "GMT_relief_oceanonly_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_relief_oceanonly.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_seis(self):
        cname = "GMT_seis"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_seis.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_seis_r(self):
        cname = "GMT_seis_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_seis.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_split(self):
        cname = "GMT_split"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_split.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_split_r(self):
        cname = "GMT_split_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_split.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_topo(self):
        cname = "GMT_topo"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_topo.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_topo_r(self):
        cname = "GMT_topo_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_topo.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_wysiwyg(self):
        cname = "GMT_wysiwyg"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_wysiwyg.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_wysiwyg_r(self):
        cname = "GMT_wysiwyg_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_wysiwyg.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_wysiwygcont(self):
        cname = "GMT_wysiwygcont"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_wysiwygcont.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_wysiwygcont_r(self):
        cname = "GMT_wysiwygcont_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_wysiwygcont.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GSFC_landsat_udf_density(self):
        cname = "GSFC_landsat_udf_density"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GSFC_landsat_udf_density.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GSFC_landsat_udf_density_r(self):
        cname = "GSFC_landsat_udf_density_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GSFC_landsat_udf_density.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GrayWhiteGray(self):
        cname = "GrayWhiteGray"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GrayWhiteGray.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GrayWhiteGray_r(self):
        cname = "GrayWhiteGray_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GrayWhiteGray.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GreenMagenta16(self):
        cname = "GreenMagenta16"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GreenMagenta16.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GreenMagenta16_r(self):
        cname = "GreenMagenta16_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GreenMagenta16.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GreenYellow(self):
        cname = "GreenYellow"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GreenYellow.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GreenYellow_r(self):
        cname = "GreenYellow_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GreenYellow.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_banded(self):
        cname = "NCV_banded"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_banded.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_banded_r(self):
        cname = "NCV_banded_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_banded.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_blu_red(self):
        cname = "NCV_blu_red"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_blu_red.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_blu_red_r(self):
        cname = "NCV_blu_red_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_blu_red.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_blue_red(self):
        cname = "NCV_blue_red"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_blue_red.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_blue_red_r(self):
        cname = "NCV_blue_red_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_blue_red.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_bright(self):
        cname = "NCV_bright"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_bright.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_bright_r(self):
        cname = "NCV_bright_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_bright.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_gebco(self):
        cname = "NCV_gebco"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_gebco.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_gebco_r(self):
        cname = "NCV_gebco_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_gebco.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_jaisnd(self):
        cname = "NCV_jaisnd"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_jaisnd.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_jaisnd_r(self):
        cname = "NCV_jaisnd_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_jaisnd.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_jet(self):
        cname = "NCV_jet"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_jet.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_jet_r(self):
        cname = "NCV_jet_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_jet.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_manga(self):
        cname = "NCV_manga"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_manga.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_manga_r(self):
        cname = "NCV_manga_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_manga.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_rainbow2(self):
        cname = "NCV_rainbow2"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_rainbow2.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_rainbow2_r(self):
        cname = "NCV_rainbow2_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_rainbow2.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_roullet(self):
        cname = "NCV_roullet"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_roullet.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_roullet_r(self):
        cname = "NCV_roullet_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_roullet.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NEO_div_vegetation_a(self):
        cname = "NEO_div_vegetation_a"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NEO_div_vegetation_a.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NEO_div_vegetation_a_r(self):
        cname = "NEO_div_vegetation_a_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NEO_div_vegetation_a.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NEO_div_vegetation_b(self):
        cname = "NEO_div_vegetation_b"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NEO_div_vegetation_b.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NEO_div_vegetation_b_r(self):
        cname = "NEO_div_vegetation_b_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NEO_div_vegetation_b.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NEO_div_vegetation_c(self):
        cname = "NEO_div_vegetation_c"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NEO_div_vegetation_c.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NEO_div_vegetation_c_r(self):
        cname = "NEO_div_vegetation_c_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NEO_div_vegetation_c.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NEO_modis_ndvi(self):
        cname = "NEO_modis_ndvi"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NEO_modis_ndvi.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NEO_modis_ndvi_r(self):
        cname = "NEO_modis_ndvi_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NEO_modis_ndvi.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NMCRef(self):
        cname = "NMCRef"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NMCRef.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NMCRef_r(self):
        cname = "NMCRef_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NMCRef.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NMCVel(self):
        cname = "NMCVel"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NMCVel.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NMCVel_r(self):
        cname = "NMCVel_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NMCVel.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NOC_ndvi(self):
        cname = "NOC_ndvi"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NOC_ndvi.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NOC_ndvi_r(self):
        cname = "NOC_ndvi_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NOC_ndvi.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def OceanLakeLandSnow(self):
        cname = "OceanLakeLandSnow"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "OceanLakeLandSnow.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def OceanLakeLandSnow_r(self):
        cname = "OceanLakeLandSnow_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "OceanLakeLandSnow.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_Gallet13(self):
        cname = "SVG_Gallet13"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_Gallet13.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_Gallet13_r(self):
        cname = "SVG_Gallet13_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_Gallet13.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_Lindaa06(self):
        cname = "SVG_Lindaa06"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_Lindaa06.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_Lindaa06_r(self):
        cname = "SVG_Lindaa06_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_Lindaa06.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_Lindaa07(self):
        cname = "SVG_Lindaa07"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_Lindaa07.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_Lindaa07_r(self):
        cname = "SVG_Lindaa07_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_Lindaa07.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_bhw3_22(self):
        cname = "SVG_bhw3_22"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_bhw3_22.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_bhw3_22_r(self):
        cname = "SVG_bhw3_22_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_bhw3_22.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_es_landscape_79(self):
        cname = "SVG_es_landscape_79"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_es_landscape_79.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_es_landscape_79_r(self):
        cname = "SVG_es_landscape_79_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_es_landscape_79.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_feb_sunrise(self):
        cname = "SVG_feb_sunrise"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_feb_sunrise.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_feb_sunrise_r(self):
        cname = "SVG_feb_sunrise_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_feb_sunrise.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_foggy_sunrise(self):
        cname = "SVG_foggy_sunrise"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_foggy_sunrise.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_foggy_sunrise_r(self):
        cname = "SVG_foggy_sunrise_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_foggy_sunrise.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_fs2006(self):
        cname = "SVG_fs2006"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_fs2006.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_fs2006_r(self):
        cname = "SVG_fs2006_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_fs2006.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def StepSeq25(self):
        cname = "StepSeq25"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "StepSeq25.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def StepSeq25_r(self):
        cname = "StepSeq25_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "StepSeq25.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def UKM_hadcrut(self):
        cname = "UKM_hadcrut"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "UKM_hadcrut.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def UKM_hadcrut_r(self):
        cname = "UKM_hadcrut_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "UKM_hadcrut.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ViBlGrWhYeOrRe(self):
        cname = "ViBlGrWhYeOrRe"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "ViBlGrWhYeOrRe.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ViBlGrWhYeOrRe_r(self):
        cname = "ViBlGrWhYeOrRe_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "ViBlGrWhYeOrRe.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhBlGrYeRe(self):
        cname = "WhBlGrYeRe"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhBlGrYeRe.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhBlGrYeRe_r(self):
        cname = "WhBlGrYeRe_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhBlGrYeRe.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhBlReWh(self):
        cname = "WhBlReWh"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhBlReWh.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhBlReWh_r(self):
        cname = "WhBlReWh_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhBlReWh.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhViBlGrYeOrRe(self):
        cname = "WhViBlGrYeOrRe"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhViBlGrYeOrRe.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhViBlGrYeOrRe_r(self):
        cname = "WhViBlGrYeOrRe_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhViBlGrYeOrRe.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhViBlGrYeOrReWh(self):
        cname = "WhViBlGrYeOrReWh"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhViBlGrYeOrReWh.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhViBlGrYeOrReWh_r(self):
        cname = "WhViBlGrYeOrReWh_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhViBlGrYeOrReWh.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhiteBlue(self):
        cname = "WhiteBlue"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhiteBlue.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhiteBlue_r(self):
        cname = "WhiteBlue_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhiteBlue.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhiteBlueGreenYellowRed(self):
        cname = "WhiteBlueGreenYellowRed"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhiteBlueGreenYellowRed.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhiteBlueGreenYellowRed_r(self):
        cname = "WhiteBlueGreenYellowRed_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhiteBlueGreenYellowRed.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhiteGreen(self):
        cname = "WhiteGreen"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhiteGreen.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhiteGreen_r(self):
        cname = "WhiteGreen_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhiteGreen.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhiteYellowOrangeRed(self):
        cname = "WhiteYellowOrangeRed"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhiteYellowOrangeRed.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhiteYellowOrangeRed_r(self):
        cname = "WhiteYellowOrangeRed_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhiteYellowOrangeRed.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def amwg(self):
        cname = "amwg"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "amwg.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def amwg_r(self):
        cname = "amwg_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "amwg.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def amwg256(self):
        cname = "amwg256"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "amwg256.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def amwg256_r(self):
        cname = "amwg256_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "amwg256.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def amwg_blueyellowred(self):
        cname = "amwg_blueyellowred"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "amwg_blueyellowred.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def amwg_blueyellowred_r(self):
        cname = "amwg_blueyellowred_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "amwg_blueyellowred.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cb_9step(self):
        cname = "cb_9step"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cb_9step.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cb_9step_r(self):
        cname = "cb_9step_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cb_9step.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cb_rainbow(self):
        cname = "cb_rainbow"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cb_rainbow.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cb_rainbow_r(self):
        cname = "cb_rainbow_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cb_rainbow.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cb_rainbow_inv(self):
        cname = "cb_rainbow_inv"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cb_rainbow_inv.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cb_rainbow_inv_r(self):
        cname = "cb_rainbow_inv_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cb_rainbow_inv.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def circular_0(self):
        cname = "circular_0"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "circular_0.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def circular_0_r(self):
        cname = "circular_0_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "circular_0.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def circular_1(self):
        cname = "circular_1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "circular_1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def circular_1_r(self):
        cname = "circular_1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "circular_1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def circular_2(self):
        cname = "circular_2"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "circular_2.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def circular_2_r(self):
        cname = "circular_2_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "circular_2.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cividis(self):
        cname = "cividis"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cividis.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cividis_r(self):
        cname = "cividis_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cividis.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmp_b2r(self):
        cname = "cmp_b2r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmp_b2r.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmp_b2r_r(self):
        cname = "cmp_b2r_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmp_b2r.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmp_flux(self):
        cname = "cmp_flux"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmp_flux.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmp_flux_r(self):
        cname = "cmp_flux_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmp_flux.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmp_haxby(self):
        cname = "cmp_haxby"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmp_haxby.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmp_haxby_r(self):
        cname = "cmp_haxby_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmp_haxby.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cosam(self):
        cname = "cosam"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cosam.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cosam_r(self):
        cname = "cosam_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cosam.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cosam12(self):
        cname = "cosam12"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cosam12.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cosam12_r(self):
        cname = "cosam12_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cosam12.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cyclic(self):
        cname = "cyclic"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cyclic.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cyclic_r(self):
        cname = "cyclic_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cyclic.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def default(self):
        cname = "default"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "default.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def default_r(self):
        cname = "default_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "default.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def detail(self):
        cname = "detail"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "detail.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def detail_r(self):
        cname = "detail_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "detail.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def drought_severity(self):
        cname = "drought_severity"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "drought_severity.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def drought_severity_r(self):
        cname = "drought_severity_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "drought_severity.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def example(self):
        cname = "example"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "example.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def example_r(self):
        cname = "example_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "example.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def extrema(self):
        cname = "extrema"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "extrema.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def extrema_r(self):
        cname = "extrema_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "extrema.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gauss3(self):
        cname = "gauss3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "gauss3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gauss3_r(self):
        cname = "gauss3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "gauss3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def grads_default(self):
        cname = "grads_default"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "grads_default.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def grads_default_r(self):
        cname = "grads_default_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "grads_default.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def grads_rainbow(self):
        cname = "grads_rainbow"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "grads_rainbow.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def grads_rainbow_r(self):
        cname = "grads_rainbow_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "grads_rainbow.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gscyclic(self):
        cname = "gscyclic"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "gscyclic.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gscyclic_r(self):
        cname = "gscyclic_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "gscyclic.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gsdtol(self):
        cname = "gsdtol"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "gsdtol.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gsdtol_r(self):
        cname = "gsdtol_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "gsdtol.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gsltod(self):
        cname = "gsltod"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "gsltod.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gsltod_r(self):
        cname = "gsltod_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "gsltod.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gui_default(self):
        cname = "gui_default"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "gui_default.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gui_default_r(self):
        cname = "gui_default_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "gui_default.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def helix(self):
        cname = "helix"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "helix.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def helix_r(self):
        cname = "helix_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "helix.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def helix1(self):
        cname = "helix1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "helix1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def helix1_r(self):
        cname = "helix1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "helix1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def hlu_default(self):
        cname = "hlu_default"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "hlu_default.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def hlu_default_r(self):
        cname = "hlu_default_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "hlu_default.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def hotcold_18lev(self):
        cname = "hotcold_18lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "hotcold_18lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def hotcold_18lev_r(self):
        cname = "hotcold_18lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "hotcold_18lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def hotcolr_19lev(self):
        cname = "hotcolr_19lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "hotcolr_19lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def hotcolr_19lev_r(self):
        cname = "hotcolr_19lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "hotcolr_19lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def hotres(self):
        cname = "hotres"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "hotres.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def hotres_r(self):
        cname = "hotres_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "hotres.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def lithology(self):
        cname = "lithology"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "lithology.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def lithology_r(self):
        cname = "lithology_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "lithology.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def matlab_hot(self):
        cname = "matlab_hot"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "matlab_hot.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def matlab_hot_r(self):
        cname = "matlab_hot_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "matlab_hot.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def matlab_hsv(self):
        cname = "matlab_hsv"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "matlab_hsv.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def matlab_hsv_r(self):
        cname = "matlab_hsv_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "matlab_hsv.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def matlab_jet(self):
        cname = "matlab_jet"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "matlab_jet.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def matlab_jet_r(self):
        cname = "matlab_jet_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "matlab_jet.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def matlab_lines(self):
        cname = "matlab_lines"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "matlab_lines.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def matlab_lines_r(self):
        cname = "matlab_lines_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "matlab_lines.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def mch_default(self):
        cname = "mch_default"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "mch_default.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def mch_default_r(self):
        cname = "mch_default_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "mch_default.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ncl_default(self):
        cname = "ncl_default"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "ncl_default.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ncl_default_r(self):
        cname = "ncl_default_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "ncl_default.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ncview_default(self):
        cname = "ncview_default"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "ncview_default.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ncview_default_r(self):
        cname = "ncview_default_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "ncview_default.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def nice_gfdl(self):
        cname = "nice_gfdl"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "nice_gfdl.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def nice_gfdl_r(self):
        cname = "nice_gfdl_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "nice_gfdl.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def nrl_sirkes(self):
        cname = "nrl_sirkes"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "nrl_sirkes.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def nrl_sirkes_r(self):
        cname = "nrl_sirkes_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "nrl_sirkes.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def nrl_sirkes_nowhite(self):
        cname = "nrl_sirkes_nowhite"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "nrl_sirkes_nowhite.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def nrl_sirkes_nowhite_r(self):
        cname = "nrl_sirkes_nowhite_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "nrl_sirkes_nowhite.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def perc2_9lev(self):
        cname = "perc2_9lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "perc2_9lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def perc2_9lev_r(self):
        cname = "perc2_9lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "perc2_9lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def percent_11lev(self):
        cname = "percent_11lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "percent_11lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def percent_11lev_r(self):
        cname = "percent_11lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "percent_11lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def posneg_1(self):
        cname = "posneg_1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "posneg_1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def posneg_1_r(self):
        cname = "posneg_1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "posneg_1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def posneg_2(self):
        cname = "posneg_2"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "posneg_2.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def posneg_2_r(self):
        cname = "posneg_2_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "posneg_2.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prcp_1(self):
        cname = "prcp_1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "prcp_1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prcp_1_r(self):
        cname = "prcp_1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "prcp_1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prcp_2(self):
        cname = "prcp_2"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "prcp_2.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prcp_2_r(self):
        cname = "prcp_2_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "prcp_2.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prcp_3(self):
        cname = "prcp_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "prcp_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prcp_3_r(self):
        cname = "prcp_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "prcp_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip2_15lev(self):
        cname = "precip2_15lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip2_15lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip2_15lev_r(self):
        cname = "precip2_15lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip2_15lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip2_17lev(self):
        cname = "precip2_17lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip2_17lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip2_17lev_r(self):
        cname = "precip2_17lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip2_17lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip3_16lev(self):
        cname = "precip3_16lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip3_16lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip3_16lev_r(self):
        cname = "precip3_16lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip3_16lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip4_11lev(self):
        cname = "precip4_11lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip4_11lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip4_11lev_r(self):
        cname = "precip4_11lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip4_11lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip4_diff_19lev(self):
        cname = "precip4_diff_19lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip4_diff_19lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip4_diff_19lev_r(self):
        cname = "precip4_diff_19lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip4_diff_19lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip_11lev(self):
        cname = "precip_11lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip_11lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip_11lev_r(self):
        cname = "precip_11lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip_11lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip_diff_12lev(self):
        cname = "precip_diff_12lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip_diff_12lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip_diff_12lev_r(self):
        cname = "precip_diff_12lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip_diff_12lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip_diff_1lev(self):
        cname = "precip_diff_1lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip_diff_1lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip_diff_1lev_r(self):
        cname = "precip_diff_1lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip_diff_1lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def psgcap(self):
        cname = "psgcap"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "psgcap.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def psgcap_r(self):
        cname = "psgcap_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "psgcap.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def radar(self):
        cname = "radar"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "radar.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def radar_r(self):
        cname = "radar_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "radar.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def radar_1(self):
        cname = "radar_1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "radar_1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def radar_1_r(self):
        cname = "radar_1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "radar_1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rainbow(self):
        cname = "rainbow"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "rainbow.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rainbow_r(self):
        cname = "rainbow_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "rainbow.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rainbow_gray(self):
        cname = "rainbow_gray"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "rainbow_gray.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rainbow_gray_r(self):
        cname = "rainbow_gray_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "rainbow_gray.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rainbow_white(self):
        cname = "rainbow_white"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "rainbow_white.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rainbow_white_r(self):
        cname = "rainbow_white_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "rainbow_white.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rainbow_white_gray(self):
        cname = "rainbow_white_gray"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "rainbow_white_gray.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rainbow_white_gray_r(self):
        cname = "rainbow_white_gray_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "rainbow_white_gray.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rh_19lev(self):
        cname = "rh_19lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "rh_19lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rh_19lev_r(self):
        cname = "rh_19lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "rh_19lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def saw3(self):
        cname = "saw3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "saw3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def saw3_r(self):
        cname = "saw3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "saw3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def seaice_1(self):
        cname = "seaice_1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "seaice_1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def seaice_1_r(self):
        cname = "seaice_1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "seaice_1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def seaice_2(self):
        cname = "seaice_2"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "seaice_2.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def seaice_2_r(self):
        cname = "seaice_2_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "seaice_2.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def so4_21(self):
        cname = "so4_21"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "so4_21.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def so4_21_r(self):
        cname = "so4_21_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "so4_21.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def so4_23(self):
        cname = "so4_23"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "so4_23.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def so4_23_r(self):
        cname = "so4_23_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "so4_23.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def spread_15lev(self):
        cname = "spread_15lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "spread_15lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def spread_15lev_r(self):
        cname = "spread_15lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "spread_15lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def srip_reanalysis(self):
        cname = "srip_reanalysis"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "srip_reanalysis.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def srip_reanalysis_r(self):
        cname = "srip_reanalysis_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "srip_reanalysis.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def sunshine_9lev(self):
        cname = "sunshine_9lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "sunshine_9lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def sunshine_9lev_r(self):
        cname = "sunshine_9lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "sunshine_9lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def sunshine_diff_12lev(self):
        cname = "sunshine_diff_12lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "sunshine_diff_12lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def sunshine_diff_12lev_r(self):
        cname = "sunshine_diff_12lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "sunshine_diff_12lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def t2m_29lev(self):
        cname = "t2m_29lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "t2m_29lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def t2m_29lev_r(self):
        cname = "t2m_29lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "t2m_29lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tbrAvg1(self):
        cname = "tbrAvg1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "tbrAvg1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tbrAvg1_r(self):
        cname = "tbrAvg1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "tbrAvg1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tbrStd1(self):
        cname = "tbrStd1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "tbrStd1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tbrStd1_r(self):
        cname = "tbrStd1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "tbrStd1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tbrVar1(self):
        cname = "tbrVar1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "tbrVar1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tbrVar1_r(self):
        cname = "tbrVar1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "tbrVar1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tbr_240_300(self):
        cname = "tbr_240_300"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "tbr_240_300.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tbr_240_300_r(self):
        cname = "tbr_240_300_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "tbr_240_300.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tbr_stdev_0_30(self):
        cname = "tbr_stdev_0_30"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "tbr_stdev_0_30.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tbr_stdev_0_30_r(self):
        cname = "tbr_stdev_0_30_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "tbr_stdev_0_30.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tbr_var_0_500(self):
        cname = "tbr_var_0_500"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "tbr_var_0_500.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tbr_var_0_500_r(self):
        cname = "tbr_var_0_500_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "tbr_var_0_500.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def temp1(self):
        cname = "temp1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "temp1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def temp1_r(self):
        cname = "temp1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "temp1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def temp_19lev(self):
        cname = "temp_19lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "temp_19lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def temp_19lev_r(self):
        cname = "temp_19lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "temp_19lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def temp_diff_18lev(self):
        cname = "temp_diff_18lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "temp_diff_18lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def temp_diff_18lev_r(self):
        cname = "temp_diff_18lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "temp_diff_18lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def temp_diff_1lev(self):
        cname = "temp_diff_1lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "temp_diff_1lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def temp_diff_1lev_r(self):
        cname = "temp_diff_1lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "temp_diff_1lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def testcmap(self):
        cname = "testcmap"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "testcmap.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def testcmap_r(self):
        cname = "testcmap_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "testcmap.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def thelix(self):
        cname = "thelix"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "thelix.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def thelix_r(self):
        cname = "thelix_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "thelix.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def topo_15lev(self):
        cname = "topo_15lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "topo_15lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def topo_15lev_r(self):
        cname = "topo_15lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "topo_15lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def uniform(self):
        cname = "uniform"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "uniform.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def uniform_r(self):
        cname = "uniform_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "uniform.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def vegetation_ClarkU(self):
        cname = "vegetation_ClarkU"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "vegetation_ClarkU.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def vegetation_ClarkU_r(self):
        cname = "vegetation_ClarkU_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "vegetation_ClarkU.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def vegetation_modis(self):
        cname = "vegetation_modis"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "vegetation_modis.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def vegetation_modis_r(self):
        cname = "vegetation_modis_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "vegetation_modis.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def wgne15(self):
        cname = "wgne15"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "wgne15.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def wgne15_r(self):
        cname = "wgne15_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "wgne15.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def wh_bl_gr_ye_re(self):
        cname = "wh_bl_gr_ye_re"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "wh_bl_gr_ye_re.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def wh_bl_gr_ye_re_r(self):
        cname = "wh_bl_gr_ye_re_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "wh_bl_gr_ye_re.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def wind_17lev(self):
        cname = "wind_17lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "wind_17lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def wind_17lev_r(self):
        cname = "wind_17lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "wind_17lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def wxpEnIR(self):
        cname = "wxpEnIR"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "wxpEnIR.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def wxpEnIR_r(self):
        cname = "wxpEnIR_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "wxpEnIR.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def acton(self):
        cname = "acton"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "acton.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def acton_r(self):
        cname = "acton_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "acton.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bamako(self):
        cname = "bamako"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "bamako.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bamako_r(self):
        cname = "bamako_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "bamako.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def batlow(self):
        cname = "batlow"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "batlow.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def batlow_r(self):
        cname = "batlow_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "batlow.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def berlin(self):
        cname = "berlin"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "berlin.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def berlin_r(self):
        cname = "berlin_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "berlin.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bilbao(self):
        cname = "bilbao"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "bilbao.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bilbao_r(self):
        cname = "bilbao_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "bilbao.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def broc(self):
        cname = "broc"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "broc.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def broc_r(self):
        cname = "broc_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "broc.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def buda(self):
        cname = "buda"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "buda.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def buda_r(self):
        cname = "buda_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "buda.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cork(self):
        cname = "cork"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "cork.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cork_r(self):
        cname = "cork_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "cork.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def davos(self):
        cname = "davos"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "davos.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def davos_r(self):
        cname = "davos_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "davos.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def devon(self):
        cname = "devon"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "devon.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def devon_r(self):
        cname = "devon_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "devon.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def grayc(self):
        cname = "grayc"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "grayc.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def grayc_r(self):
        cname = "grayc_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "grayc.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def hawaii(self):
        cname = "hawaii"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "hawaii.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def hawaii_r(self):
        cname = "hawaii_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "hawaii.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def imola(self):
        cname = "imola"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "imola.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def imola_r(self):
        cname = "imola_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "imola.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def lajolla(self):
        cname = "lajolla"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "lajolla.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def lajolla_r(self):
        cname = "lajolla_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "lajolla.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def lapaz(self):
        cname = "lapaz"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "lapaz.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def lapaz_r(self):
        cname = "lapaz_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "lapaz.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def lisbon(self):
        cname = "lisbon"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "lisbon.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def lisbon_r(self):
        cname = "lisbon_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "lisbon.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def nuuk(self):
        cname = "nuuk"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "nuuk.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def nuuk_r(self):
        cname = "nuuk_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "nuuk.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def oleron(self):
        cname = "oleron"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "oleron.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def oleron_r(self):
        cname = "oleron_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "oleron.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def oslo(self):
        cname = "oslo"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "oslo.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def oslo_r(self):
        cname = "oslo_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "oslo.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def roma(self):
        cname = "roma"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "roma.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def roma_r(self):
        cname = "roma_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "roma.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tofino(self):
        cname = "tofino"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "tofino.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tofino_r(self):
        cname = "tofino_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "tofino.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tokyo(self):
        cname = "tokyo"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "tokyo.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tokyo_r(self):
        cname = "tokyo_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "tokyo.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def turku(self):
        cname = "turku"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "turku.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def turku_r(self):
        cname = "turku_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "turku.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def vik(self):
        cname = "vik"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "vik.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def vik_r(self):
        cname = "vik_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "scientific",  "vik.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bluered_12(self):
        cname = "bluered_12"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "tableau",  "bluered_12.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bluered_12_r(self):
        cname = "bluered_12_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "tableau",  "bluered_12.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bluered_6(self):
        cname = "bluered_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "tableau",  "bluered_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bluered_6_r(self):
        cname = "bluered_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "tableau",  "bluered_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def colorblind_10(self):
        cname = "colorblind_10"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "tableau",  "colorblind_10.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def colorblind_10_r(self):
        cname = "colorblind_10_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "tableau",  "colorblind_10.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gray_5(self):
        cname = "gray_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "tableau",  "gray_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gray_5_r(self):
        cname = "gray_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "tableau",  "gray_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greenorange_12(self):
        cname = "greenorange_12"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "tableau",  "greenorange_12.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greenorange_12_r(self):
        cname = "greenorange_12_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "tableau",  "greenorange_12.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greenorange_6(self):
        cname = "greenorange_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "tableau",  "greenorange_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def greenorange_6_r(self):
        cname = "greenorange_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "tableau",  "greenorange_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purplegray_12(self):
        cname = "purplegray_12"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "tableau",  "purplegray_12.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purplegray_12_r(self):
        cname = "purplegray_12_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "tableau",  "purplegray_12.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purplegray_6(self):
        cname = "purplegray_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "tableau",  "purplegray_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purplegray_6_r(self):
        cname = "purplegray_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "tableau",  "purplegray_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tableau_10(self):
        cname = "tableau_10"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "tableau",  "tableau_10.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tableau_10_r(self):
        cname = "tableau_10_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "tableau",  "tableau_10.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tableau_20(self):
        cname = "tableau_20"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "tableau",  "tableau_20.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tableau_20_r(self):
        cname = "tableau_20_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "tableau",  "tableau_20.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tableaulight_10(self):
        cname = "tableaulight_10"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "tableau",  "tableaulight_10.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tableaulight_10_r(self):
        cname = "tableaulight_10_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "tableau",  "tableaulight_10.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tableaumedium_10(self):
        cname = "tableaumedium_10"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "tableau",  "tableaumedium_10.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tableaumedium_10_r(self):
        cname = "tableaumedium_10_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "tableau",  "tableaumedium_10.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def trafficlight_9(self):
        cname = "trafficlight_9"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "tableau",  "trafficlight_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def trafficlight_9_r(self):
        cname = "trafficlight_9_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "tableau",  "trafficlight_9.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def b2_31(self):
        cname = "b2_31"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "b2_31.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def b2_31_r(self):
        cname = "b2_31_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "b2_31.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bl_11(self):
        cname = "bl_11"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "bl_11.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bl_11_r(self):
        cname = "bl_11_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "bl_11.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blue_8_5g2(self):
        cname = "blue_8_5g2"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "blue_8_5g2.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blue_8_5g2_r(self):
        cname = "blue_8_5g2_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "blue_8_5g2.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blue_bl111(self):
        cname = "blue_bl111"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "blue_bl111.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blue_bl111_r(self):
        cname = "blue_bl111_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "blue_bl111.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blue_blgra2(self):
        cname = "blue_blgra2"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "blue_blgra2.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blue_blgra2_r(self):
        cname = "blue_blgra2_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "blue_blgra2.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blue_blue3(self):
        cname = "blue_blue3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "blue_blue3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blue_blue3_r(self):
        cname = "blue_blue3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "blue_blue3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blue_blueb1(self):
        cname = "blue_blueb1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "blue_blueb1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blue_blueb1_r(self):
        cname = "blue_blueb1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "blue_blueb1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blue_c16adjw(self):
        cname = "blue_c16adjw"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "blue_c16adjw.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blue_c16adjw_r(self):
        cname = "blue_c16adjw_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "blue_c16adjw.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blue_gblue(self):
        cname = "blue_gblue"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "blue_gblue.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blue_gblue_r(self):
        cname = "blue_gblue_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "blue_gblue.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blue_lbluec1(self):
        cname = "blue_lbluec1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "blue_lbluec1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blue_lbluec1_r(self):
        cname = "blue_lbluec1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "blue_lbluec1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blue_medb717b(self):
        cname = "blue_medb717b"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "blue_medb717b.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def blue_medb717b_r(self):
        cname = "blue_medb717b_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "blue_medb717b.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def br4div(self):
        cname = "br4div"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "br4div.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def br4div_r(self):
        cname = "br4div_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "br4div.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brown_br119a(self):
        cname = "brown_br119a"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "brown_br119a.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brown_br119a_r(self):
        cname = "brown_br119a_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "brown_br119a.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brown_browns(self):
        cname = "brown_browns"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "brown_browns.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brown_browns_r(self):
        cname = "brown_browns_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "brown_browns.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brown_brye1b(self):
        cname = "brown_brye1b"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "brown_brye1b.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brown_brye1b_r(self):
        cname = "brown_brye1b_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "brown_brye1b.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brown_grawarm1(self):
        cname = "brown_grawarm1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "brown_grawarm1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brown_grawarm1_r(self):
        cname = "brown_grawarm1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "brown_grawarm1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brown_orange1(self):
        cname = "brown_orange1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "brown_orange1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brown_orange1_r(self):
        cname = "brown_orange1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "brown_orange1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brown_ortanish1(self):
        cname = "brown_ortanish1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "brown_ortanish1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brown_ortanish1_r(self):
        cname = "brown_ortanish1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "brown_ortanish1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brown_peachy(self):
        cname = "brown_peachy"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "brown_peachy.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brown_peachy_r(self):
        cname = "brown_peachy_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "brown_peachy.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brown_red3b(self):
        cname = "brown_red3b"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "brown_red3b.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brown_red3b_r(self):
        cname = "brown_red3b_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "brown_red3b.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brown_sable(self):
        cname = "brown_sable"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "brown_sable.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brown_sable_r(self):
        cname = "brown_sable_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "brown_sable.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brown_vbrown1(self):
        cname = "brown_vbrown1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "brown_vbrown1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def brown_vbrown1_r(self):
        cname = "brown_vbrown1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "brown_vbrown1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def browngray(self):
        cname = "browngray"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "browngray.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def browngray_r(self):
        cname = "browngray_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "browngray.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bruce2(self):
        cname = "bruce2"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "bruce2.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def bruce2_r(self):
        cname = "bruce2_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "bruce2.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def c_7_16(self):
        cname = "c_7_16"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "c_7_16.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def c_7_16_r(self):
        cname = "c_7_16_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "c_7_16.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def c_blgr1(self):
        cname = "c_blgr1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "c_blgr1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def c_blgr1_r(self):
        cname = "c_blgr1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "c_blgr1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def c_pch1(self):
        cname = "c_pch1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "c_pch1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def c_pch1_r(self):
        cname = "c_pch1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "c_pch1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def c_violet1(self):
        cname = "c_violet1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "c_violet1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def c_violet1_r(self):
        cname = "c_violet1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "c_violet1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def c_yelpch1(self):
        cname = "c_yelpch1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "c_yelpch1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def c_yelpch1_r(self):
        cname = "c_yelpch1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "c_yelpch1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def colormap66(self):
        cname = "colormap66"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "colormap66.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def colormap66_r(self):
        cname = "colormap66_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "colormap66.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def d_blgr3(self):
        cname = "d_blgr3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "d_blgr3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def d_blgr3_r(self):
        cname = "d_blgr3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "d_blgr3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def d_seteq2(self):
        cname = "d_seteq2"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "d_seteq2.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def d_seteq2_r(self):
        cname = "d_seteq2_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "d_seteq2.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def dasy_grbr1(self):
        cname = "dasy_grbr1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "dasy_grbr1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def dasy_grbr1_r(self):
        cname = "dasy_grbr1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "dasy_grbr1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def discrete_Bg(self):
        cname = "discrete_Bg"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "discrete_Bg.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def discrete_Bg_r(self):
        cname = "discrete_Bg_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "discrete_Bg.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def discrete_Bo(self):
        cname = "discrete_Bo"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "discrete_Bo.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def discrete_Bo_r(self):
        cname = "discrete_Bo_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "discrete_Bo.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def discrete_autumn(self):
        cname = "discrete_autumn"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "discrete_autumn.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def discrete_autumn_r(self):
        cname = "discrete_autumn_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "discrete_autumn.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def discrete_dark(self):
        cname = "discrete_dark"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "discrete_dark.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def discrete_dark_r(self):
        cname = "discrete_dark_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "discrete_dark.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def discrete_light_aut(self):
        cname = "discrete_light_aut"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "discrete_light_aut.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def discrete_light_aut_r(self):
        cname = "discrete_light_aut_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "discrete_light_aut.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def discrete_muted(self):
        cname = "discrete_muted"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "discrete_muted.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def discrete_muted_r(self):
        cname = "discrete_muted_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "discrete_muted.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def discrete_vaneyck(self):
        cname = "discrete_vaneyck"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "discrete_vaneyck.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def discrete_vaneyck_r(self):
        cname = "discrete_vaneyck_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "discrete_vaneyck.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def div1_blue_orange(self):
        cname = "div1_blue_orange"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "div1_blue_orange.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def div1_blue_orange_r(self):
        cname = "div1_blue_orange_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "div1_blue_orange.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def div2_gray_gold(self):
        cname = "div2_gray_gold"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "div2_gray_gold.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def div2_gray_gold_r(self):
        cname = "div2_gray_gold_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "div2_gray_gold.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def div3_green_brown(self):
        cname = "div3_green_brown"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "div3_green_brown.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def div3_green_brown_r(self):
        cname = "div3_green_brown_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "div3_green_brown.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def div5_asym_Ob(self):
        cname = "div5_asym_Ob"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "div5_asym_Ob.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def div5_asym_Ob_r(self):
        cname = "div5_asym_Ob_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "div5_asym_Ob.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def fushia_red_pink1(self):
        cname = "fushia_red_pink1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "fushia_red_pink1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def fushia_red_pink1_r(self):
        cname = "fushia_red_pink1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "fushia_red_pink1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def green_9_17e(self):
        cname = "green_9_17e"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "green_9_17e.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def green_9_17e_r(self):
        cname = "green_9_17e_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "green_9_17e.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def green_c_gry1(self):
        cname = "green_c_gry1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "green_c_gry1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def green_c_gry1_r(self):
        cname = "green_c_gry1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "green_c_gry1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def green_gr1214b(self):
        cname = "green_gr1214b"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "green_gr1214b.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def green_gr1214b_r(self):
        cname = "green_gr1214b_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "green_gr1214b.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def green_green1(self):
        cname = "green_green1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "green_green1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def green_green1_r(self):
        cname = "green_green1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "green_green1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def green_green6(self):
        cname = "green_green6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "green_green6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def green_green6_r(self):
        cname = "green_green6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "green_green6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def green_mistyteal(self):
        cname = "green_mistyteal"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "green_mistyteal.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def green_mistyteal_r(self):
        cname = "green_mistyteal_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "green_mistyteal.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def green_mustard(self):
        cname = "green_mustard"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "green_mustard.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def green_mustard_r(self):
        cname = "green_mustard_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "green_mustard.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def green_rox(self):
        cname = "green_rox"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "green_rox.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def green_rox_r(self):
        cname = "green_rox_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "green_rox.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def hier1p(self):
        cname = "hier1p"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "hier1p.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def hier1p_r(self):
        cname = "hier1p_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "hier1p.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def hier2p(self):
        cname = "hier2p"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "hier2p.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def hier2p_r(self):
        cname = "hier2p_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "hier2p.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def hier4w(self):
        cname = "hier4w"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "hier4w.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def hier4w_r(self):
        cname = "hier4w_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "hier4w.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def hier5(self):
        cname = "hier5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "hier5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def hier5_r(self):
        cname = "hier5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "hier5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def high2ml(self):
        cname = "high2ml"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "high2ml.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def high2ml_r(self):
        cname = "high2ml_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "high2ml.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def high3(self):
        cname = "high3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "high3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def high3_r(self):
        cname = "high3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "high3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def high4(self):
        cname = "high4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "high4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def high4_r(self):
        cname = "high4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "high4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def high5(self):
        cname = "high5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "high5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def high5_r(self):
        cname = "high5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "high5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def hs_orange2(self):
        cname = "hs_orange2"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "hs_orange2.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def hs_orange2_r(self):
        cname = "hs_orange2_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "hs_orange2.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def l_oragnemed1(self):
        cname = "l_oragnemed1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "l_oragnemed1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def l_oragnemed1_r(self):
        cname = "l_oragnemed1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "l_oragnemed1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def l_orangemute1(self):
        cname = "l_orangemute1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "l_orangemute1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def l_orangemute1_r(self):
        cname = "l_orangemute1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "l_orangemute1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def l_orangesat1(self):
        cname = "l_orangesat1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "l_orangesat1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def l_orangesat1_r(self):
        cname = "l_orangesat1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "l_orangesat1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def l_purplowsat3(self):
        cname = "l_purplowsat3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "l_purplowsat3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def l_purplowsat3_r(self):
        cname = "l_purplowsat3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "l_purplowsat3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def l_purpmedsat3(self):
        cname = "l_purpmedsat3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "l_purpmedsat3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def l_purpmedsat3_r(self):
        cname = "l_purpmedsat3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "l_purpmedsat3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def l_purpwarm2(self):
        cname = "l_purpwarm2"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "l_purpwarm2.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def l_purpwarm2_r(self):
        cname = "l_purpwarm2_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "l_purpwarm2.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def l_red_warm1(self):
        cname = "l_red_warm1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "l_red_warm1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def l_red_warm1_r(self):
        cname = "l_red_warm1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "l_red_warm1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def l_redmuted4(self):
        cname = "l_redmuted4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "l_redmuted4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def l_redmuted4_r(self):
        cname = "l_redmuted4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "l_redmuted4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def l_redsat1(self):
        cname = "l_redsat1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "l_redsat1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def l_redsat1_r(self):
        cname = "l_redsat1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "l_redsat1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def l_turqmed2(self):
        cname = "l_turqmed2"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "l_turqmed2.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def l_turqmed2_r(self):
        cname = "l_turqmed2_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "l_turqmed2.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def l_turqsat1(self):
        cname = "l_turqsat1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "l_turqsat1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def l_turqsat1_r(self):
        cname = "l_turqsat1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "l_turqsat1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def l_yellowmed2(self):
        cname = "l_yellowmed2"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "l_yellowmed2.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def l_yellowmed2_r(self):
        cname = "l_yellowmed2_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "l_yellowmed2.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def mauve1(self):
        cname = "mauve1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "mauve1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def mauve1_r(self):
        cname = "mauve1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "mauve1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def oryell2(self):
        cname = "oryell2"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "oryell2.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def oryell2_r(self):
        cname = "oryell2_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "oryell2.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def other_outl_1(self):
        cname = "other_outl_1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "other_outl_1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def other_outl_1_r(self):
        cname = "other_outl_1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "other_outl_1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def other_outl_2(self):
        cname = "other_outl_2"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "other_outl_2.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def other_outl_2_r(self):
        cname = "other_outl_2_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "other_outl_2.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def other_outl_3(self):
        cname = "other_outl_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "other_outl_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def other_outl_3_r(self):
        cname = "other_outl_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "other_outl_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def other_outl_4(self):
        cname = "other_outl_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "other_outl_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def other_outl_4_r(self):
        cname = "other_outl_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "other_outl_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def other_outl_5(self):
        cname = "other_outl_5"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "other_outl_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def other_outl_5_r(self):
        cname = "other_outl_5_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "other_outl_5.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def other_outl_6(self):
        cname = "other_outl_6"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "other_outl_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def other_outl_6_r(self):
        cname = "other_outl_6_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "other_outl_6.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def other_outl_7(self):
        cname = "other_outl_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "other_outl_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def other_outl_7_r(self):
        cname = "other_outl_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "other_outl_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def other_outl_8(self):
        cname = "other_outl_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "other_outl_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def other_outl_8_r(self):
        cname = "other_outl_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "other_outl_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pr_mist(self):
        cname = "pr_mist"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "pr_mist.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def pr_mist_r(self):
        cname = "pr_mist_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "pr_mist.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purp2(self):
        cname = "purp2"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "purp2.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purp2_r(self):
        cname = "purp2_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "purp2.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purp_pink(self):
        cname = "purp_pink"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "purp_pink.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def purp_pink_r(self):
        cname = "purp_pink_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "purp_pink.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def red2b(self):
        cname = "red2b"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "red2b.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def red2b_r(self):
        cname = "red2b_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "red2b.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def red_1lt(self):
        cname = "red_1lt"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "red_1lt.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def red_1lt_r(self):
        cname = "red_1lt_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "red_1lt.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def redp1(self):
        cname = "redp1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "redp1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def redp1_r(self):
        cname = "redp1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "redp1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def redsun1(self):
        cname = "redsun1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "redsun1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def redsun1_r(self):
        cname = "redsun1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "redsun1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def redy3(self):
        cname = "redy3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "redy3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def redy3_r(self):
        cname = "redy3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "redy3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rpinky(self):
        cname = "rpinky"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "rpinky.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rpinky_r(self):
        cname = "rpinky_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "rpinky.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def speed_yel(self):
        cname = "speed_yel"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "speed_yel.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def speed_yel_r(self):
        cname = "speed_yel_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "speed_yel.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tempm1(self):
        cname = "tempm1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "tempm1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tempm1_r(self):
        cname = "tempm1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "tempm1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def test(self):
        cname = "test"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "test.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def test_r(self):
        cname = "test_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "test.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tr4(self):
        cname = "tr4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "tr4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tr4_r(self):
        cname = "tr4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "tr4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def turq1lt(self):
        cname = "turq1lt"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "turq1lt.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def turq1lt_r(self):
        cname = "turq1lt_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "turq1lt.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def turqw1(self):
        cname = "turqw1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "turqw1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def turqw1_r(self):
        cname = "turqw1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "turqw1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def vvlt_turq3(self):
        cname = "vvlt_turq3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "vvlt_turq3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def vvlt_turq3_r(self):
        cname = "vvlt_turq3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "vvlt_turq3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def w5m4(self):
        cname = "w5m4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "w5m4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def w5m4_r(self):
        cname = "w5m4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "w5m4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def w_ymiddle1(self):
        cname = "w_ymiddle1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "w_ymiddle1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def w_ymiddle1_r(self):
        cname = "w_ymiddle1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "w_ymiddle1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def wlteqcool(self):
        cname = "wlteqcool"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "wlteqcool.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def wlteqcool_r(self):
        cname = "wlteqcool_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "wlteqcool.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def wmutedset(self):
        cname = "wmutedset"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "wmutedset.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def wmutedset_r(self):
        cname = "wmutedset_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "wmutedset.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def yel15(self):
        cname = "yel15"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "yel15.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def yel15_r(self):
        cname = "yel15_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "yel15.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def yel3(self):
        cname = "yel3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "yel3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def yel3_r(self):
        cname = "yel3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "yel3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def yel_peach_br(self):
        cname = "yel_peach_br"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "yel_peach_br.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def yel_peach_br_r(self):
        cname = "yel_peach_br_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "yel_peach_br.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def yellowsun(self):
        cname = "yellowsun"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "yellowsun.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def yellowsun_r(self):
        cname = "yellowsun_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "yellowsun.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def yelsat100(self):
        cname = "yelsat100"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "yelsat100.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def yelsat100_r(self):
        cname = "yelsat100_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "yelsat100.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def yg1(self):
        cname = "yg1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "yg1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def yg1_r(self):
        cname = "yg1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "yg1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def yg3(self):
        cname = "yg3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "yg3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def yg3_r(self):
        cname = "yg3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "sciviz",  "yg3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_c_grey(self):
        cname = "cet_c_grey"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_c_grey.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_c_grey_r(self):
        cname = "cet_c_grey_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_c_grey.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_c_grey_15(self):
        cname = "cet_c_grey_15"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_c_grey_15.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_c_grey_15_r(self):
        cname = "cet_c_grey_15_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_c_grey_15.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_c_mrybm(self):
        cname = "cet_c_mrybm"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_c_mrybm.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_c_mrybm_r(self):
        cname = "cet_c_mrybm_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_c_mrybm.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_c_mrybm_35(self):
        cname = "cet_c_mrybm_35"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_c_mrybm_35.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_c_mrybm_35_r(self):
        cname = "cet_c_mrybm_35_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_c_mrybm_35.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_c_mygbm(self):
        cname = "cet_c_mygbm"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_c_mygbm.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_c_mygbm_r(self):
        cname = "cet_c_mygbm_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_c_mygbm.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_c_mygbm_30(self):
        cname = "cet_c_mygbm_30"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_c_mygbm_30.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_c_mygbm_30_r(self):
        cname = "cet_c_mygbm_30_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_c_mygbm_30.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_c_protanopic_deuteranopic_bwyk(self):
        cname = "cet_c_protanopic_deuteranopic_bwyk"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_c_protanopic_deuteranopic_bwyk.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_c_protanopic_deuteranopic_bwyk_r(self):
        cname = "cet_c_protanopic_deuteranopic_bwyk_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_c_protanopic_deuteranopic_bwyk.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_c_protanopic_deuteranopic_wywb(self):
        cname = "cet_c_protanopic_deuteranopic_wywb"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_c_protanopic_deuteranopic_wywb.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_c_protanopic_deuteranopic_wywb_r(self):
        cname = "cet_c_protanopic_deuteranopic_wywb_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_c_protanopic_deuteranopic_wywb.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_c_tritanopic_cwrk_4(self):
        cname = "cet_c_tritanopic_cwrk_4"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_c_tritanopic_cwrk_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_c_tritanopic_cwrk_4_r(self):
        cname = "cet_c_tritanopic_cwrk_4_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_c_tritanopic_cwrk_4.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_c_tritanopic_wrwc_7(self):
        cname = "cet_c_tritanopic_wrwc_7"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_c_tritanopic_wrwc_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_c_tritanopic_wrwc_7_r(self):
        cname = "cet_c_tritanopic_wrwc_7_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_c_tritanopic_wrwc_7.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_c_wrwbw(self):
        cname = "cet_c_wrwbw"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_c_wrwbw.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_c_wrwbw_r(self):
        cname = "cet_c_wrwbw_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_c_wrwbw.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_c_wrwbw_40(self):
        cname = "cet_c_wrwbw_40"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_c_wrwbw_40.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_c_wrwbw_40_r(self):
        cname = "cet_c_wrwbw_40_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_c_wrwbw_40.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_bkr(self):
        cname = "cet_d_bkr"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_bkr.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_bkr_r(self):
        cname = "cet_d_bkr_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_bkr.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_bky(self):
        cname = "cet_d_bky"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_bky.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_bky_r(self):
        cname = "cet_d_bky_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_bky.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_bwg(self):
        cname = "cet_d_bwg"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_bwg.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_bwg_r(self):
        cname = "cet_d_bwg_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_bwg.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_bwr(self):
        cname = "cet_d_bwr"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_bwr.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_bwr_r(self):
        cname = "cet_d_bwr_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_bwr.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_cwm_8(self):
        cname = "cet_d_cwm_8"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_cwm_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_cwm_8_r(self):
        cname = "cet_d_cwm_8_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_cwm_8.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_gkr(self):
        cname = "cet_d_gkr"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_gkr.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_gkr_r(self):
        cname = "cet_d_gkr_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_gkr.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_gwr(self):
        cname = "cet_d_gwr"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_gwr.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_gwr_r(self):
        cname = "cet_d_gwr_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_gwr.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_gwv(self):
        cname = "cet_d_gwv"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_gwv.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_gwv_r(self):
        cname = "cet_d_gwv_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_gwv.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_isoluminant_cjm(self):
        cname = "cet_d_isoluminant_cjm"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_isoluminant_cjm.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_isoluminant_cjm_r(self):
        cname = "cet_d_isoluminant_cjm_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_isoluminant_cjm.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_isoluminant_cjm1(self):
        cname = "cet_d_isoluminant_cjm1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_isoluminant_cjm1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_isoluminant_cjm1_r(self):
        cname = "cet_d_isoluminant_cjm1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_isoluminant_cjm1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_isoluminant_cjo(self):
        cname = "cet_d_isoluminant_cjo"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_isoluminant_cjo.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_isoluminant_cjo_r(self):
        cname = "cet_d_isoluminant_cjo_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_isoluminant_cjo.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_linear_bjr(self):
        cname = "cet_d_linear_bjr"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_linear_bjr.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_linear_bjr_r(self):
        cname = "cet_d_linear_bjr_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_linear_bjr.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_linear_bjy(self):
        cname = "cet_d_linear_bjy"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_linear_bjy.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_linear_bjy_r(self):
        cname = "cet_d_linear_bjy_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_linear_bjy.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_protanopic_deuteranopic_bwy(self):
        cname = "cet_d_protanopic_deuteranopic_bwy"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_protanopic_deuteranopic_bwy.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_protanopic_deuteranopic_bwy_r(self):
        cname = "cet_d_protanopic_deuteranopic_bwy_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_protanopic_deuteranopic_bwy.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_rainbow_bgymr(self):
        cname = "cet_d_rainbow_bgymr"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_rainbow_bgymr.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_rainbow_bgymr_r(self):
        cname = "cet_d_rainbow_bgymr_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_rainbow_bgymr.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_tritanopic_cwr(self):
        cname = "cet_d_tritanopic_cwr"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_tritanopic_cwr.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_d_tritanopic_cwr_r(self):
        cname = "cet_d_tritanopic_cwr_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_d_tritanopic_cwr.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_g_bw(self):
        cname = "cet_g_bw"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_g_bw.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_g_bw_r(self):
        cname = "cet_g_bw_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_g_bw.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_g_bw_minc(self):
        cname = "cet_g_bw_minc"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_g_bw_minc.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_g_bw_minc_r(self):
        cname = "cet_g_bw_minc_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_g_bw_minc.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_g_bw_minc1(self):
        cname = "cet_g_bw_minc1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_g_bw_minc1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_g_bw_minc1_r(self):
        cname = "cet_g_bw_minc1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_g_bw_minc1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_g_bw_minc_maxl(self):
        cname = "cet_g_bw_minc_maxl"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_g_bw_minc_maxl.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_g_bw_minc_maxl_r(self):
        cname = "cet_g_bw_minc_maxl_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_g_bw_minc_maxl.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_g_bw_minc_minl(self):
        cname = "cet_g_bw_minc_minl"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_g_bw_minc_minl.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_g_bw_minc_minl_r(self):
        cname = "cet_g_bw_minc_minl_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_g_bw_minc_minl.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_g_category10(self):
        cname = "cet_g_category10"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_g_category10.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_g_category10_r(self):
        cname = "cet_g_category10_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_g_category10.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_g_hv(self):
        cname = "cet_g_hv"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_g_hv.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_g_hv_r(self):
        cname = "cet_g_hv_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_g_hv.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_i(self):
        cname = "cet_i"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_i.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_i_r(self):
        cname = "cet_i_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_i.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_i_cgo(self):
        cname = "cet_i_cgo"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_i_cgo.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_i_cgo_r(self):
        cname = "cet_i_cgo_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_i_cgo.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_i_cgo1(self):
        cname = "cet_i_cgo1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_i_cgo1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_i_cgo1_r(self):
        cname = "cet_i_cgo1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_i_cgo1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_bgy(self):
        cname = "cet_l_bgy"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_bgy.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_bgy_r(self):
        cname = "cet_l_bgy_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_bgy.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_bgyw(self):
        cname = "cet_l_bgyw"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_bgyw.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_bgyw_r(self):
        cname = "cet_l_bgyw_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_bgyw.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_bgyw1(self):
        cname = "cet_l_bgyw1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_bgyw1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_bgyw1_r(self):
        cname = "cet_l_bgyw1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_bgyw1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_blue(self):
        cname = "cet_l_blue"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_blue.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_blue_r(self):
        cname = "cet_l_blue_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_blue.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_blue1(self):
        cname = "cet_l_blue1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_blue1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_blue1_r(self):
        cname = "cet_l_blue1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_blue1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_bmw(self):
        cname = "cet_l_bmw"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_bmw.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_bmw_r(self):
        cname = "cet_l_bmw_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_bmw.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_bmw1(self):
        cname = "cet_l_bmw1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_bmw1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_bmw1_r(self):
        cname = "cet_l_bmw1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_bmw1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_bmy(self):
        cname = "cet_l_bmy"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_bmy.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_bmy_r(self):
        cname = "cet_l_bmy_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_bmy.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_bmy1(self):
        cname = "cet_l_bmy1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_bmy1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_bmy1_r(self):
        cname = "cet_l_bmy1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_bmy1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_gow(self):
        cname = "cet_l_gow"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_gow.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_gow_r(self):
        cname = "cet_l_gow_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_gow.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_gow1(self):
        cname = "cet_l_gow1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_gow1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_gow1_r(self):
        cname = "cet_l_gow1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_gow1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_green(self):
        cname = "cet_l_green"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_green.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_green_r(self):
        cname = "cet_l_green_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_green.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_grey(self):
        cname = "cet_l_grey"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_grey.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_grey_r(self):
        cname = "cet_l_grey_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_grey.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_grey1(self):
        cname = "cet_l_grey1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_grey1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_grey1_r(self):
        cname = "cet_l_grey1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_grey1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_kbc(self):
        cname = "cet_l_kbc"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_kbc.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_kbc_r(self):
        cname = "cet_l_kbc_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_kbc.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_kbgyw(self):
        cname = "cet_l_kbgyw"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_kbgyw.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_kbgyw_r(self):
        cname = "cet_l_kbgyw_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_kbgyw.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_kgy(self):
        cname = "cet_l_kgy"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_kgy.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_kgy_r(self):
        cname = "cet_l_kgy_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_kgy.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_kry(self):
        cname = "cet_l_kry"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_kry.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_kry_r(self):
        cname = "cet_l_kry_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_kry.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_kry1(self):
        cname = "cet_l_kry1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_kry1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_kry1_r(self):
        cname = "cet_l_kry1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_kry1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_kry2(self):
        cname = "cet_l_kry2"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_kry2.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_kry2_r(self):
        cname = "cet_l_kry2_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_kry2.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_kryw(self):
        cname = "cet_l_kryw"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_kryw.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_kryw_r(self):
        cname = "cet_l_kryw_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_kryw.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_kryw1(self):
        cname = "cet_l_kryw1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_kryw1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_kryw1_r(self):
        cname = "cet_l_kryw1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_kryw1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_kryw2(self):
        cname = "cet_l_kryw2"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_kryw2.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_kryw2_r(self):
        cname = "cet_l_kryw2_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_kryw2.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_protanopic_deuteranopic_kbjyw(self):
        cname = "cet_l_protanopic_deuteranopic_kbjyw"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_protanopic_deuteranopic_kbjyw.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_protanopic_deuteranopic_kbjyw_r(self):
        cname = "cet_l_protanopic_deuteranopic_kbjyw_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_protanopic_deuteranopic_kbjyw.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_protanopic_deuteranopic_kbw(self):
        cname = "cet_l_protanopic_deuteranopic_kbw"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_protanopic_deuteranopic_kbw.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_protanopic_deuteranopic_kbw_r(self):
        cname = "cet_l_protanopic_deuteranopic_kbw_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_protanopic_deuteranopic_kbw.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_ternary_blue(self):
        cname = "cet_l_ternary_blue"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_ternary_blue.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_ternary_blue_r(self):
        cname = "cet_l_ternary_blue_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_ternary_blue.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_ternary_green(self):
        cname = "cet_l_ternary_green"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_ternary_green.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_ternary_green_r(self):
        cname = "cet_l_ternary_green_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_ternary_green.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_ternary_red(self):
        cname = "cet_l_ternary_red"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_ternary_red.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_ternary_red_r(self):
        cname = "cet_l_ternary_red_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_ternary_red.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_tritanopic_krjcw(self):
        cname = "cet_l_tritanopic_krjcw"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_tritanopic_krjcw.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_tritanopic_krjcw_r(self):
        cname = "cet_l_tritanopic_krjcw_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_tritanopic_krjcw.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_tritanopic_krjcw1(self):
        cname = "cet_l_tritanopic_krjcw1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_tritanopic_krjcw1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_tritanopic_krjcw1_r(self):
        cname = "cet_l_tritanopic_krjcw1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_tritanopic_krjcw1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_wcmr(self):
        cname = "cet_l_wcmr"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_wcmr.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_wcmr_r(self):
        cname = "cet_l_wcmr_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_wcmr.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_worb(self):
        cname = "cet_l_worb"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_worb.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_worb_r(self):
        cname = "cet_l_worb_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_worb.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_wyor(self):
        cname = "cet_l_wyor"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_wyor.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_l_wyor_r(self):
        cname = "cet_l_wyor_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_l_wyor.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_r_bgyr(self):
        cname = "cet_r_bgyr"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_r_bgyr.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_r_bgyr_r(self):
        cname = "cet_r_bgyr_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_r_bgyr.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_r_bgyr1(self):
        cname = "cet_r_bgyr1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_r_bgyr1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_r_bgyr1_r(self):
        cname = "cet_r_bgyr1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_r_bgyr1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_r_bgyrm(self):
        cname = "cet_r_bgyrm"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_r_bgyrm.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_r_bgyrm_r(self):
        cname = "cet_r_bgyrm_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_r_bgyrm.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_r_bgyrm1(self):
        cname = "cet_r_bgyrm1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_r_bgyrm1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cet_r_bgyrm1_r(self):
        cname = "cet_r_bgyrm1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "colorcet",  "cet_r_bgyrm1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap


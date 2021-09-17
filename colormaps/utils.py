#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .colormap import Colormap
# import matplotlib.colors as mc
import matplotlib.cm
import numpy as np


def concat(cnames, ratios=None, discrete=256, name='concat', save=False):
    """
        Concatenate two or more colormaps.

        Parameters
        ----------
        cnames : list of str or list of cmaps
            Provide the possible list of cmaps.

        ratios : list of floats
            Divide the colorbar based on the ratios. By default, divide it into the equal number of parts.
            The sum of the ratios should be 1.
        
        discrete : int
            Discrete number of levels. (Default: 256)

        name : str
            Name of the file. The file will be saved in rgb format

        save : boolean (True or False)  
            If you want to save your colomap, them use True and must provide a name.

        """
    import colormaps as cmaps

    # Two variables, one for storing string and second for cmaps
    colors_str = np.full(4, 0)

    # Starting the loop
    j = 0
    for cname in cnames:
        if ratios is None:
            # Equal ratios
            ratio = 1 / len(cnames)
        else:
            ratio = ratios[j]
        # Process for the strings
        if isinstance(cname, str):
            colors1 = eval("cmaps." + cname)
            colors1 = matplotlib.cm.get_cmap(cname)
            colors1 = colors1(np.linspace(0, 1, int(256 * ratio)))
            colors1 = Colormap(colors1, name='temp')
            colors1 = colors1.cut(0.2, 'left')
            colors1 = colors1.cut(0.2, 'right')
            colors1 = colors1.colors
            colors_str = np.vstack((colors_str, colors1))
        else:
            # Process for the cmaps
            colors1 = cname(np.linspace(0.2, 0.8,int(256 * ratio)))
            # combine them and build a new colormap
            colors_str = np.vstack((colors_str, colors1))

        j = j + 1
    
    mymap = Colormap(colors_str[1:], name=name)

    # Discrete logic (Mostly to avoid warning)
    if mymap.N < discrete:
        mymap = mymap.discrete(mymap.N - 1)
    elif mymap.N == 256:
        mymap = mymap.discrete(255)
    else:
        mymap = mymap.discrete(discrete)

    mymap.name = name

    if save is True:
        if isinstance(name, str):
            np.savetxt(name + '.rgb',
                       mymap.colors * 255, fmt='%.0f',
                       header='ncolors=' + str(len(mymap.colors)) + '\n' + 'r g b')
        else:
            raise Exception("name must be str")

    return mymap

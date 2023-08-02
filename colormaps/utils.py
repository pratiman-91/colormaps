#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .colormap import Colormap
# import matplotlib.colors as mc
import matplotlib.cm
import numpy as np
import os
from glob import glob

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
            colors1 = getattr(cmaps, cname)
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

def show_cmaps(category, cmap_list):

    import matplotlib.pyplot as plt
    import colormaps as cmaps

    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))
    
    # Create figure and adjust figure height to number of colormaps
    nrows = len(cmap_list)
    figh = 0.35 + 0.15 + (nrows + (nrows - 1) * 0.1) * 0.22
    fig, axs = plt.subplots(nrows=nrows + 1, figsize=(6.4, figh))
    fig.subplots_adjust(top=1 - 0.35 / figh, bottom=0.15 / figh,
                        left=0.2, right=0.99)
    axs[0].set_title(f'{category} colormaps', fontsize=14)

    for ax, name in zip(axs, cmap_list):
        ax.imshow(gradient, aspect='auto', cmap=eval("cmaps." + name))
        ax.text(-0.01, 0.5, name, va='center', ha='right', fontsize=10,
                transform=ax.transAxes)

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axs:
        ax.set_axis_off()

def show_cmaps_all():
    print("This may take some time... Please be patient.")
    CMAPSFILE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'colormaps')
    if CMAPSFILE_DIR is not None:
        cmapsflist = sorted(glob(os.path.join(CMAPSFILE_DIR, '**/*.rgb'), recursive = True))
        FirstTime = True
        for cmap_file in cmapsflist:
            cname = os.path.basename(cmap_file).split('.rgb')[0]
            cname_group = cmap_file.split('/')[-2]
            if FirstTime == True:
                category = cname_group
                cmap_list = [cname]
                FirstTime = False
            else:
                if category == cname_group:
                    cmap_list.append(cname)
                else:
                    show_cmaps(category=category, cmap_list=cmap_list)
                    FirstTime = True

def show_cmaps_collection(collection='cartocolors'):
    print("This may take some time... Please be patient.")
    CMAPSFILE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'colormaps')
    if CMAPSFILE_DIR is not None:
        cmapsflist = sorted(glob(os.path.join(CMAPSFILE_DIR, collection, '*.rgb')))
        if len(cmapsflist):
            FirstTime = True
            for cmap_file in cmapsflist:
                cname = os.path.basename(cmap_file).split('.rgb')[0]
                cname_group = cmap_file.split('/')[-2]
                if FirstTime == True:
                    category = cname_group
                    cmap_list = [cname]
                    FirstTime = False
                else:
                    if category == cname_group:
                        cmap_list.append(cname)
            
            show_cmaps(category=category, cmap_list=cmap_list)
        else:
            cmapsflist = sorted(glob(os.path.join(CMAPSFILE_DIR, '**/*.rgb'), recursive = True))
            FirstTime = True
            for cmap_file in cmapsflist:
                cname_group = cmap_file.split('/')[-2]
                if FirstTime == True:
                    category = cname_group
                    all_collection = [cname_group]
                    FirstTime = False
                else:
                    if category != cname_group:
                        category = cname_group
                        all_collection.append(cname_group)
            
            raise ValueError("possible collection names are " + all_collection.__str__())
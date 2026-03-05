#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .colormap import Colormap
from ._compat import get_cmap

import matplotlib.cm
import numpy as np
import os
from glob import glob

from ._version import __version__


def concat(cnames, ratios=None, trim=0.0, discrete=256, name="concat", save=False):
    """
    Concatenate two or more colormaps.

    Parameters
    ----------
    cnames : list of str, Colormap, or callable
        List of colormaps. Each element may be a string name, a Colormap
        object, or any callable that accepts a float array in [0, 1].

    ratios : list of floats, optional
        Proportion of the output each input occupies. Must sum to 1.
        Defaults to equal proportions.

    trim : float or list of float, optional
        Fraction to trim from each end of each input colormap (0–0.5).
        A scalar applies to all; a list applies per colormap.
        Default is 0.0 (no trimming).

    discrete : int
        Number of discrete color levels in the output. (Default: 256)

    name : str
        Name for the resulting colormap.

    save : bool
        If True, save the colormap to `name`.rgb.
    """
    n = len(cnames)

    if ratios is None:
        ratios = [1.0 / n] * n

    if isinstance(trim, (int, float)):
        trims = [trim] * n
    else:
        trims = list(trim)

    segments = []
    for cname, ratio, t in zip(cnames, ratios, trims):
        n_colors = max(2, int(256 * ratio))
        lo, hi = t, 1.0 - t

        if isinstance(cname, str):
            from ._compat import is_registered
            if not is_registered(cname):
                from .cmaps import Cmaps
                Cmaps()._load_colormap(cname)
            cmap = get_cmap(cname)
        else:
            cmap = cname
        segments.append(cmap(np.linspace(lo, hi, n_colors)))

    all_colors = np.vstack(segments)
    mymap = Colormap(all_colors, name=name)
    mymap = mymap.discrete(min(mymap.N - 1, discrete))
    mymap.name = name

    if save:
        if not isinstance(name, str):
            raise TypeError("name must be str")
        np.savetxt(
            name + ".rgb",
            mymap.colors * 255,
            fmt="%.0f",
            header="ncolors=" + str(len(mymap.colors)) + "\n" + "r g b",
        )

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
    fig.subplots_adjust(top=1 - 0.35 / figh, bottom=0.15 / figh, left=0.2, right=0.99)
    axs[0].set_title(f"{category} colormaps", fontsize=14)

    for ax, name in zip(axs, cmap_list):
        colors1 = getattr(cmaps, name)
        colors1 = get_cmap(name)
        ax.imshow(gradient, aspect="auto", cmap=colors1)
        ax.text(
            -0.01,
            0.5,
            name,
            va="center",
            ha="right",
            fontsize=10,
            transform=ax.transAxes,
        )

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axs:
        ax.set_axis_off()


def show_cmaps_all():
    print("This may take some time... Please be patient.")
    CMAPSFILE_DIR = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "colormaps"
    )
    if CMAPSFILE_DIR is not None:
        cmapsflist = sorted(
            glob(os.path.join(CMAPSFILE_DIR, "**/*.rgb"), recursive=True)
        )
        first_time = True
        for cmap_file in cmapsflist:
            cname = os.path.basename(cmap_file).split(".rgb")[0]
            cname_group = cmap_file.split("/")[-2]
            if first_time:
                category = cname_group
                cmap_list = [cname]
                first_time = False
            else:
                if category == cname_group:
                    cmap_list.append(cname)
                else:
                    show_cmaps(category=category, cmap_list=cmap_list)
                    first_time = True


def show_cmaps_collection(collection="cartocolors"):
    print("This may take some time... Please be patient.")
    CMAPSFILE_DIR = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "colormaps"
    )
    if CMAPSFILE_DIR is not None:
        cmapsflist = sorted(glob(os.path.join(CMAPSFILE_DIR, collection, "*.rgb")))
        if len(cmapsflist):
            first_time = True
            for cmap_file in cmapsflist:
                cname = os.path.basename(cmap_file).split(".rgb")[0]
                cname_group = cmap_file.split("/")[-2]
                if first_time:
                    category = cname_group
                    cmap_list = [cname]
                    first_time = False
                else:
                    if category == cname_group:
                        cmap_list.append(cname)

            show_cmaps(category=category, cmap_list=cmap_list)
        else:
            cmapsflist = sorted(
                glob(os.path.join(CMAPSFILE_DIR, "**/*.rgb"), recursive=True)
            )
            first_time = True
            for cmap_file in cmapsflist:
                cname_group = cmap_file.split("/")[-2]
                if first_time:
                    category = cname_group
                    all_collection = [cname_group]
                    first_time = False
                else:
                    if category != cname_group:
                        category = cname_group
                        all_collection.append(cname_group)

            raise ValueError(
                "possible collection names are " + all_collection.__str__()
            )

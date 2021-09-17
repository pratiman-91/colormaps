#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import colors


class Colormap(colors.ListedColormap):
    def __init__(self, c, name='from_list', n=None):
        # Initialization
        self._colors = c
        self._name = name
        self._N = n

        # call parent __init__
        super(Colormap, self).__init__(self._colors, name=self._name, N=self._N)

    def __getitem__(self, item):
        return Colormap(self._colors[item], name='sliced_' + self._name)

    def show(self):
        import matplotlib.pyplot as plt
        a = np.outer(np.ones(10), np.arange(0, 1, 0.001))
        plt.figure(figsize=(2.5, 0.5))
        plt.subplots_adjust(top=0.95, bottom=0.05, left=0.01, right=0.99)
        plt.subplot(111)
        plt.axis('off')
        plt.imshow(a, aspect='auto', cmap=self, origin='lower')
        plt.text(0.5, 0.5, self._name,
                 verticalalignment='center', horizontalalignment='center',
                 fontsize=12, transform=plt.gca().transAxes)
        plt.show()

    def discrete(self, ncolors):
        """
        A discrete color map that can be used in matplotlib plots.

        Parameters
        ----------
        ncolors : int
            Number of colors required in the map.
            
        """
        if ncolors >= self.N:
            import warnings
            ncolors = self.N - 1

            warnings.warn(
                "Warning: Number of levels requested is more than the number of colors. "
                "Deafulting to maximum number of colors.")

        levels = np.array(tuple(np.linspace(start=0, stop=self.N - 1, num=ncolors, dtype=int)))
        return self.__getitem__(levels)

    def shift(self, nshift):
        """
        Shifting of colormap. Possible values -1 to 1.

        Parameters
        ----------
        nshift : float
            Portion of the colormap to be shifted. Possible values are between -1 to 1.
            The negative is left and positive is right.
            
        """
        if (nshift > 1) or (nshift < -1):
            raise Exception("nshift should be between -1 and 1.")

        shift = self.N * np.abs(nshift)

        if shift >= self.N:
            shift = self.N - 1

        if nshift > 0:
            levels = np.array(tuple(np.linspace(start=shift, stop=self.N - 1, dtype=int)))
        elif nshift < 0:
            levels = np.array(tuple(np.linspace(start=0, stop=shift - 1, dtype=int)))
        elif nshift == 0:
            pass
        else:
            raise Exception("Shift only supports 'left' and 'right'.")

        return self.__getitem__(levels)

    def cut(self, ncut, loc='centre'):
        """
        Increase/Decrease the centre portion of the colormap. 
        Possible usage in the diverging colormaps.

        Parameters
        ----------
        ncut : float
            Portion of the colormap to be cut. Possible values are between -1 to 1. 
        loc : str
            Location of cut. Possible values 'left', right' or 'centre'
        """

        if (ncut > 1) or (ncut < -1):
            raise Exception("nshift should be between -1 and 1.")

        if (loc == 'left') or (loc == 'right') or (loc == 'centre'):
            pass
        else:
            raise Exception("loc should be between 'left', right' or 'centre'.")

        # Check for even/odd 
        if (self.N % 2) == 0:
            levels = np.arange(start=0, stop=self.N, dtype=int)
        else:
            levels = np.arange(start=0, stop=self.N - 1, dtype=int)
        left, right = np.array_split(levels, 2)

        if loc == 'centre':
            # Creating an offset
            offset = self.N * np.abs(ncut)
            if int(offset / 2) < 1:
                left = left[:-int(offset)]
                right = right[int(offset):]
            else:
                left = left[:-int(offset / 2)]
                right = right[int(offset / 2):]

            # Adding the offset information in the cmap
            offset = self.N - len(left) - len(right)
            if ncut > 0:
                offset_arr = np.full((offset - 1,), levels[int(len(levels) / 2)])
                levels = np.append(left, offset_arr)
                levels = np.append(levels, right)
            elif ncut < 0:
                levels = np.append(left, right)
            else:
                pass

            return self.__getitem__(levels)

        elif loc == 'left':
            # Creating an offset
            offset = int(self.N * np.abs(ncut))
            levels = levels[offset:]
            return self.__getitem__(levels)
        elif loc == 'right':
            # Creating an offset
            offset = int(self.N * np.abs(ncut))
            levels = levels[:-offset]
            return self.__getitem__(levels)
        else:
            raise Exception("Something is wrong here!")

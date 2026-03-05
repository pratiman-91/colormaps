import numpy as np
import pytest
from matplotlib.colors import ListedColormap

from colormaps.colormap import Colormap


class TestInit:
    def test_stores_colors_and_name(self):
        colors = [[1, 0, 0, 1], [0, 1, 0, 1]]
        cm = Colormap(colors, name='mymap')
        assert cm._name == 'mymap'
        assert len(cm._colors) == 2

    def test_is_listed_colormap(self):
        cm = Colormap([[0, 0, 0]], name='t')
        assert isinstance(cm, ListedColormap)

    def test_default_name(self):
        cm = Colormap([[0, 0, 0]])
        assert cm._name == 'from_list'

    def test_stores_N(self):
        colors = np.zeros((20, 4))
        cm = Colormap(colors, name='t', n=10)
        assert cm._N == 10


class TestGetitem:
    def test_slice_returns_colormap(self, sample_colormap):
        sliced = sample_colormap[2:5]
        assert isinstance(sliced, Colormap)

    def test_slice_name_prefix(self, sample_colormap):
        sliced = sample_colormap[2:5]
        assert sliced._name.startswith('sliced_')

    def test_numpy_indexing(self, sample_colormap):
        idx = np.array([0, 3, 7])
        sliced = sample_colormap[idx]
        assert isinstance(sliced, Colormap)


class TestShow:
    def test_show_called(self, sample_colormap, monkeypatch):
        called = []
        import matplotlib.pyplot as plt
        monkeypatch.setattr(plt, 'show', lambda: called.append(True))
        sample_colormap.show()
        assert called


class TestDiscrete:
    def test_fewer_colors(self, sample_colormap):
        d = sample_colormap.discrete(5)
        assert isinstance(d, Colormap)

    def test_warns_when_ncolors_ge_N(self, sample_colormap):
        with pytest.warns(UserWarning):
            d = sample_colormap.discrete(sample_colormap.N + 5)
        assert isinstance(d, Colormap)

    def test_single_color(self, sample_colormap):
        d = sample_colormap.discrete(1)
        assert isinstance(d, Colormap)


class TestShift:
    def test_positive_shift(self, sample_colormap):
        s = sample_colormap.shift(0.5)
        assert isinstance(s, Colormap)

    def test_negative_shift(self, sample_colormap):
        s = sample_colormap.shift(-0.5)
        assert isinstance(s, Colormap)

    def test_invalid_shift_raises(self, sample_colormap):
        with pytest.raises(ValueError):
            sample_colormap.shift(1.5)
        with pytest.raises(ValueError):
            sample_colormap.shift(-1.5)

    def test_boundary_plus_one(self, sample_colormap):
        s = sample_colormap.shift(1)
        assert isinstance(s, Colormap)

    def test_boundary_minus_one(self, sample_colormap):
        s = sample_colormap.shift(-1)
        assert isinstance(s, Colormap)

    def test_shift_zero(self, sample_colormap):
        s = sample_colormap.shift(0)
        assert isinstance(s, Colormap)


class TestCut:
    def test_centre_positive(self, sample_colormap):
        c = sample_colormap.cut(0.5, loc='centre')
        assert isinstance(c, Colormap)

    def test_centre_negative(self, sample_colormap):
        c = sample_colormap.cut(-0.5, loc='centre')
        assert isinstance(c, Colormap)

    def test_centre_zero(self, sample_colormap):
        c = sample_colormap.cut(0, loc='centre')
        assert isinstance(c, Colormap)

    def test_left(self, sample_colormap):
        c = sample_colormap.cut(0.3, loc='left')
        assert isinstance(c, Colormap)

    def test_right(self, sample_colormap):
        c = sample_colormap.cut(0.3, loc='right')
        assert isinstance(c, Colormap)

    def test_invalid_ncut(self, sample_colormap):
        with pytest.raises(ValueError):
            sample_colormap.cut(1.5)

    def test_invalid_loc(self, sample_colormap):
        with pytest.raises(ValueError):
            sample_colormap.cut(0.5, loc='top')

    def test_even_N(self):
        colors = np.zeros((8, 4))
        cm = Colormap(colors, name='even_test')
        c = cm.cut(0.5, loc='centre')
        assert isinstance(c, Colormap)

    def test_odd_N(self):
        colors = np.zeros((9, 4))
        cm = Colormap(colors, name='odd_test')
        c = cm.cut(0.5, loc='centre')
        assert isinstance(c, Colormap)

    def test_small_offset_branch(self):
        """When int(offset/2) < 1, uses int(offset) directly."""
        colors = np.zeros((100, 4))
        cm = Colormap(colors, name='small_offset')
        c = cm.cut(0.01, loc='centre')
        assert isinstance(c, Colormap)

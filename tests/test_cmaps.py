import importlib
import os
import uuid

import numpy as np
import pytest

_cmaps_mod = importlib.import_module('colormaps.cmaps')
Cmaps = _cmaps_mod.Cmaps
from colormaps.colormap import Colormap


class TestColtbl:
    def test_integer_format(self, int_rgb_file):
        result = Cmaps._coltbl(str(int_rgb_file))
        assert result.dtype == np.float32 or result.max() <= 1.0
        # 0-255 values should be divided by 255
        assert result.max() <= 1.0

    def test_float_format(self, float_rgb_file):
        result = Cmaps._coltbl(str(float_rgb_file))
        np.testing.assert_allclose(result[-1], [1.0, 1.0, 1.0], atol=0.01)

    def test_ncolors_header_stripped(self, int_rgb_file):
        result = Cmaps._coltbl(str(int_rgb_file))
        assert len(result) == 3

    def test_no_header(self, tmp_path):
        content = "0.0 0.0 0.0\n0.5 0.5 0.5\n1.0 1.0 1.0\n"
        f = tmp_path / "noheader.rgb"
        f.write_text(content)
        result = Cmaps._coltbl(str(f))
        assert len(result) == 3


class TestInit:
    def test_has_cache(self):
        c = Cmaps()
        assert hasattr(c, '_cache')
        assert isinstance(c._cache, dict)

    def test_has_version(self):
        c = Cmaps()
        assert hasattr(c, '__version__')

    def test_empty_cache_no_user_dir(self, monkeypatch):
        monkeypatch.setattr(_cmaps_mod, 'USER_CMAPFILE_DIR', None)
        c = Cmaps()
        assert len(c._cache) == 0


class TestLoadColormap:
    def test_returns_colormap(self):
        c = Cmaps()
        cmap = c._load_colormap('blues_dark')
        assert isinstance(cmap, (Colormap, object))

    def test_caches(self):
        c = Cmaps()
        cmap1 = c._load_colormap('blues_dark')
        cmap2 = c._load_colormap('blues_dark')
        assert cmap1 is cmap2

    def test_reversed(self):
        c = Cmaps()
        cmap = c._load_colormap('blues_dark_r')
        assert cmap.name == 'blues_dark_r'

    def test_unknown_raises(self):
        c = Cmaps()
        with pytest.raises(AttributeError):
            c._load_colormap('totally_nonexistent_xyz')


class TestLoadUserCmaps:
    def test_loads_from_dir(self, user_cmap_dir, monkeypatch):
        monkeypatch.setattr(_cmaps_mod, 'USER_CMAPFILE_DIR', str(user_cmap_dir))
        c = Cmaps()
        assert 'mymap' in c._cache
        assert 'mymap_r' in c._cache

    def test_sanitizes_digit_prefix(self, tmp_path, monkeypatch):
        content = "0.0 0.0 0.0\n1.0 1.0 1.0\n"
        (tmp_path / "9test.rgb").write_text(content)
        monkeypatch.setattr(_cmaps_mod, 'USER_CMAPFILE_DIR', str(tmp_path))
        c = Cmaps()
        # 9test.rgb -> C9test
        assert 'C9test' in c._cache
        assert 'C9test_r' in c._cache

    def test_no_dir_empty_cache(self, monkeypatch):
        monkeypatch.setattr(_cmaps_mod, 'USER_CMAPFILE_DIR', None)
        c = Cmaps()
        assert len(c._cache) == 0


class TestGetattr:
    def test_valid_name(self):
        c = Cmaps()
        cmap = c.blues_dark
        assert cmap is not None

    def test_private_raises(self):
        c = Cmaps()
        with pytest.raises(AttributeError):
            c._nonexistent

    def test_unknown_raises(self):
        c = Cmaps()
        with pytest.raises(AttributeError):
            c.absolutely_nonexistent_xyz


class TestDir:
    def test_contains_version(self):
        c = Cmaps()
        assert '__version__' in dir(c)

    def test_sorted(self):
        c = Cmaps()
        d = c.__dir__()
        assert d == sorted(d)

    def test_no_duplicates(self):
        c = Cmaps()
        d = c.__dir__()
        assert len(d) == len(set(d))

    def test_contains_registry_key(self):
        c = Cmaps()
        assert 'blues_dark' in dir(c)

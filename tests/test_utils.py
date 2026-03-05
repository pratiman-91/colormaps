import sys
import os
import importlib

import numpy as np
import pytest

from colormaps.colormap import Colormap

# colormaps.__init__ replaces sys.modules['colormaps'] with Cmaps(),
# so we need to import utils module directly via importlib
_utils_mod = importlib.import_module('colormaps.utils')
concat = _utils_mod.concat
show_cmaps_collection = _utils_mod.show_cmaps_collection
show_cmaps_all = _utils_mod.show_cmaps_all


class TestConcat:
    def test_two_string_cmaps(self):
        result = concat(['blues_dark', 'blues_light'])
        assert isinstance(result, Colormap)

    def test_cmap_objects(self):
        from colormaps.cmaps import Cmaps
        c = Cmaps()
        c1 = c._load_colormap('blues_dark')
        c2 = c._load_colormap('blues_light')
        result = concat([c1, c2])
        assert isinstance(result, Colormap)

    def test_custom_ratios(self):
        result = concat(['blues_dark', 'blues_light'], ratios=[0.3, 0.7])
        assert isinstance(result, Colormap)

    def test_custom_name(self):
        result = concat(['blues_dark', 'blues_light'], name='my_concat')
        assert result.name == 'my_concat'

    def test_save_to_file(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        result = concat(['blues_dark', 'blues_light'], name='saved_map', save=True)
        assert (tmp_path / 'saved_map.rgb').exists()

    def test_non_string_name_with_save_raises(self):
        with pytest.raises(TypeError):
            concat(['blues_dark', 'blues_light'], name=123, save=True)

    def test_trim_parameter(self):
        result = concat(['blues_dark', 'blues_light'], trim=0.2)
        assert isinstance(result, Colormap)


class TestShowCmapsCollection:
    def test_valid_collection(self, monkeypatch):
        monkeypatch.setattr(_utils_mod, 'show_cmaps', lambda **kwargs: None)
        show_cmaps_collection('cartocolors')

    def test_invalid_collection_raises(self, monkeypatch):
        monkeypatch.setattr(_utils_mod, 'show_cmaps', lambda **kwargs: None)
        with pytest.raises(ValueError):
            show_cmaps_collection('nonexistent_collection_xyz')


class TestShowCmapsAll:
    def test_runs_without_error(self, monkeypatch):
        monkeypatch.setattr(_utils_mod, 'show_cmaps', lambda **kwargs: None)
        show_cmaps_all()

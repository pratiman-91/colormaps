import uuid

import numpy as np
import pytest
from matplotlib.colors import ListedColormap

from colormaps._compat import register_cmap, get_cmap, is_registered


def _unique_name():
    return 'test_' + uuid.uuid4().hex[:8]


class TestRegisterAndGetCmap:
    def test_round_trip(self):
        name = _unique_name()
        cmap = ListedColormap([[0, 0, 0], [1, 1, 1]], name=name)
        register_cmap(name, cmap)
        result = get_cmap(name)
        assert result.name == name

    def test_is_registered_true(self):
        name = _unique_name()
        cmap = ListedColormap([[0, 0, 0]], name=name)
        register_cmap(name, cmap)
        assert is_registered(name)

    def test_is_registered_false(self):
        assert not is_registered('nonexistent_cmap_xyz_' + uuid.uuid4().hex[:8])

    def test_get_unknown_raises(self):
        with pytest.raises((KeyError, ValueError)):
            get_cmap('absolutely_nonexistent_' + uuid.uuid4().hex[:8])

import matplotlib
matplotlib.use('Agg')

import numpy as np
import pytest

from colormaps.colormap import Colormap


@pytest.fixture
def int_rgb_file(tmp_path):
    """Temp .rgb file with integer (0-255) format + ncolors header."""
    content = "ncolors=3\n0 0 0\n128 128 128\n255 255 255\n"
    f = tmp_path / "int_colors.rgb"
    f.write_text(content)
    return f


@pytest.fixture
def float_rgb_file(tmp_path):
    """Temp .rgb file with float (0-1) format + ncolors header."""
    content = "ncolors=3\n0.0 0.0 0.0\n0.5 0.5 0.5\n1.0 1.0 1.0\n"
    f = tmp_path / "float_colors.rgb"
    f.write_text(content)
    return f


@pytest.fixture
def sample_colormap():
    """Colormap with 10 known colors."""
    colors = np.zeros((10, 4))
    for i in range(10):
        v = i / 9.0
        colors[i] = [v, v, v, 1.0]
    return Colormap(colors, name='test_sample')


@pytest.fixture
def user_cmap_dir(tmp_path):
    """Temp dir with .rgb files for user cmap tests."""
    content_a = "ncolors=3\n255 0 0\n0 255 0\n0 0 255\n"
    content_b = "ncolors=2\n0.0 0.0 0.0\n1.0 1.0 1.0\n"
    (tmp_path / "mymap.rgb").write_text(content_a)
    (tmp_path / "2digit.rgb").write_text(content_b)
    return tmp_path

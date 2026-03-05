"""Build a registry mapping colormap names to .rgb file paths."""
import os
from glob import glob

CMAPSFILE_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'colormaps')

COLLECTIONS = [
    'carbonplan', 'cartocolors', 'cmasher', 'cmocean', 'colorbrewer',
    'colorcet', 'cubehelix', 'ncar_ncl', 'scientific', 'sciviz', 'tableau',
]


def _sanitize_name(name):
    if name[0].isdigit() or name.startswith('_'):
        name = 'N' + name
    return name.replace('-', '_').replace('+', '_')


def build_registry():
    registry = {}
    for collection in COLLECTIONS:
        cdir = os.path.join(CMAPSFILE_DIR, collection)
        if not os.path.isdir(cdir):
            continue
        for fpath in sorted(glob(os.path.join(cdir, '*.rgb'))):
            basename = os.path.basename(fpath).split('.rgb')[0]
            cname = _sanitize_name(basename)
            registry[cname] = fpath
            registry[cname + '_r'] = fpath
    return registry

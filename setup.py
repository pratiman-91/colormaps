from glob import glob

from setuptools import setup
import os

VERSION = '0.3.1'
CMAPSFILE_DIR = os.path.join('./colormaps/colormaps')


def write_version_py(version=VERSION, filename='colormaps/_version.py'):
    cnt = '# THIS FILE IS GENERATED FROM SETUP.PY\n' + \
          '__version__ = "%(version)s"\n'
    a = open(filename, 'w')
    try:
        a.write(cnt % {'version': version})
    finally:
        a.close()


def _listfname():
    l = {}

    l.update({'cartocolors': {
        'p': 'os.path.join(CMAPSFILE_DIR, "cartocolors", ',
        'l': sorted(glob(os.path.join(CMAPSFILE_DIR, 'cartocolors/*.rgb')))}})
    l.update({'cmocean': {
        'p': 'os.path.join(CMAPSFILE_DIR, "cmocean", ',
        'l': sorted(glob(os.path.join(CMAPSFILE_DIR, 'cmocean/*.rgb')))}})
    l.update({'colorbrewer': {
        'p': 'os.path.join(CMAPSFILE_DIR, "colorbrewer", ',
        'l': sorted(glob(os.path.join(CMAPSFILE_DIR, 'colorbrewer/*.rgb')))}})
    l.update({'cubehelix': {
        'p': 'os.path.join(CMAPSFILE_DIR, "cubehelix", ',
        'l': sorted(glob(os.path.join(CMAPSFILE_DIR, 'cubehelix/*.rgb')))}})
    l.update({'ncl': {
        'p': 'os.path.join(CMAPSFILE_DIR, "ncar_ncl", ',
        'l': sorted(glob(os.path.join(CMAPSFILE_DIR, 'ncar_ncl/*.rgb')))}})
    l.update({'scientific': {
        'p': 'os.path.join(CMAPSFILE_DIR, "scientific", ',
        'l': sorted(glob(os.path.join(CMAPSFILE_DIR, 'scientific/*.rgb')))}})
    l.update({'tableau': {
        'p': 'os.path.join(CMAPSFILE_DIR, "tableau", ',
        'l': sorted(glob(os.path.join(CMAPSFILE_DIR, 'tableau/*.rgb')))}})
    l.update({'sciviz': {
        'p': 'os.path.join(CMAPSFILE_DIR, "sciviz", ',
        'l': sorted(glob(os.path.join(CMAPSFILE_DIR, 'sciviz/*.rgb')))}})
    l.update({'colorcet': {
        'p': 'os.path.join(CMAPSFILE_DIR, "colorcet", ',
        'l': sorted(glob(os.path.join(CMAPSFILE_DIR, 'colorcet/*.rgb')))}})
    return l


def write_cmaps(template_file='./cmaps.template'):
    with open(template_file, 'rt') as f:
        c = f.read()
    l = _listfname()
    for t in l.keys():
        for cmap_file in l[t]['l']:
            cname = os.path.basename(cmap_file).split('.rgb')[0]
            # start with the number will result illegal attribute
            if cname[0].isdigit() or cname.startswith('_'):
                cname = 'N' + cname
            if '-' in cname:
                cname = cname.replace('-', '_')
            if '+' in cname:
                cname = cname.replace('+', '_')
            c += '    @property\n'
            c += '    def {}(self):\n'.format(cname)
            c += '        cname = "{}"\n'.format(cname)
            c += '        cmap_file = {} "{}")\n'.format(
                l[t]['p'], os.path.basename(cmap_file))
            c += '        cmap = Colormap(self._coltbl(cmap_file), name=cname)\n'
            c += '        if version.parse(mlp_version) >= version.parse("3.6.0"):\n'
            c += '            if cname in sorted(_colormaps):\n'
            c += '                return matplotlib.cm.get_cmap(cname)\n'
            c += '            else:\n'
            c += '                matplotlib.colormaps.register(name=cname, cmap=cmap)\n'
            c += '        else:\n'
            c += '            if cname in matplotlib.cm._cmap_registry:\n'
            c += '                return matplotlib.cm.get_cmap(cname)\n'
            c += '            else:\n'
            c += '                matplotlib.cm.register_cmap(name=cname, cmap=cmap)\n\n'
            c += '        return cmap\n\n'

            c += '    @property\n'
            c += '    def {}(self):\n'.format(cname + '_r')
            c += '        cname = "{}"\n'.format(cname + '_r')
            c += '        cmap_file = {} "{}")\n'.format(
                l[t]['p'], os.path.basename(cmap_file))
            c += '        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)\n'
            c += '        if version.parse(mlp_version) >= version.parse("3.6.0"):\n'
            c += '            if cname in sorted(_colormaps):\n'
            c += '                return matplotlib.cm.get_cmap(cname)\n'
            c += '            else:\n'
            c += '                matplotlib.colormaps.register(name=cname, cmap=cmap)\n'
            c += '        else:\n'
            c += '            if cname in matplotlib.cm._cmap_registry:\n'
            c += '                return matplotlib.cm.get_cmap(cname)\n'
            c += '            else:\n'
            c += '                matplotlib.cm.register_cmap(name=cname, cmap=cmap)\n\n'
            c += '        return cmap\n\n'

    cmapspy = './colormaps/cmaps.py'
    with open(cmapspy, 'wt') as fw:
        fw.write(c)


write_version_py()
write_cmaps()

setup(
    name='colormaps',
    author='Pratiman Patel',
    version=VERSION,
    author_email='pratiman_patel@hotmail.com',
    packages=['colormaps', ],
    package_data={'colormaps': ['colormaps/ncar_ncl/*',
                            'colormaps/cartocolors/*',
                            'colormaps/cmocean/*',
                            'colormaps/colorbrewer/*',
                            'colormaps/cubehelix/*',
                            'colormaps/scientific/*',
                            'colormaps/tableau/*',
                            'colormaps/sciviz/*',
                            'colormaps/colorcet/*'], },
    data_files=[('', ['cmaps.template', 'LICENSE']),],
    url='https://pratiman-91.github.io/colormaps/',
    license='LICENSE',
    description='A collection of colormaps or color palettes for Python',
    install_requires=['matplotlib', 'numpy'],
)

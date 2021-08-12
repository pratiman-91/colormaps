from glob import glob
import os

CMAPSFILE_DIR = os.path.join('./cmaps/colormaps')


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
    l.update({'self_defined': {
        'p': 'os.path.join(CMAPSFILE_DIR, "self_defined", ',
        'l': sorted(glob(os.path.join(CMAPSFILE_DIR, 'self_defined/*.rgb')))}})
    l.update({'scientific': {
        'p': 'os.path.join(CMAPSFILE_DIR, "scientific", ',
        'l': sorted(glob(os.path.join(CMAPSFILE_DIR, 'scientific/*.rgb')))}})
    l.update({'tableau': {
        'p': 'os.path.join(CMAPSFILE_DIR, "tableau", ',
        'l': sorted(glob(os.path.join(CMAPSFILE_DIR, 'tableau/*.rgb')))}})

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
            c += '        if cname in matplotlib.cm._cmap_registry:\n'
            c += '            return matplotlib.cm.get_cmap(cname)\n'
            c += '        cmap_file = {} "{}")\n'.format(
                l[t]['p'], os.path.basename(cmap_file))
            c += '        cmap = Colormap(self._coltbl(cmap_file), name=cname)\n'
            c += '        matplotlib.cm.register_cmap(name=cname, cmap=cmap)\n'
            c += '        return cmap\n\n'

            c += '    @property\n'
            c += '    def {}(self):\n'.format(cname + '_r')
            c += '        cname = "{}"\n'.format(cname + '_r')
            c += '        if cname in matplotlib.cm._cmap_registry:\n'
            c += '            return matplotlib.cm.get_cmap(cname)\n'
            c += '        cmap_file = {} "{}")\n'.format(
                l[t]['p'], os.path.basename(cmap_file))
            c += '        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)\n'
            c += '        matplotlib.cm.register_cmap(name=cname, cmap=cmap)\n'
            c += '        return cmap\n\n'

    cmapspy = './cmaps/cmaps.py'
    with open(cmapspy, 'wt') as fw:
        fw.write(c)


write_cmaps()

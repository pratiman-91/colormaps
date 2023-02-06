# Colormaps
<!--- {: .fs-9 } -->

Colormaps is a library of collection of colormaps or color palettes for Python. It's written in Python with matplotlib and numpy as dependencies. You can use Colormaps to customize matplotlib plots.
<!---{: .fs-6 .fw-300 } -->

Colormaps has colormaps or color palettes from:

- [cartocolors](https://pratiman-91.github.io/colormaps/docs/cartocolors) 
- [cmocean](https://pratiman-91.github.io/colormaps/docs/cmocean)
- [colorbrewer](https://pratiman-91.github.io/colormaps/docs/colorbrewer)
- [cubehelix](https://pratiman-91.github.io/colormaps/docs/cubehelix)
- [ncar ncl](https://pratiman-91.github.io/colormaps/docs/ncar_ncl)
- [scientific](https://pratiman-91.github.io/colormaps/docs/scientific)
- [tableau](https://pratiman-91.github.io/colormaps/docs/tableau)
- `may be more`

Docs: https://pratiman-91.github.io/colormaps/
---

## Getting started

### Dependencies

Python with:

- matplotlib
- numpy

### Installation

```
pip install colormaps
```

or you can also use GitHub repo

```bash
git clone https://github.com/pratiman-91/colormaps.git
cd colormaps
python setup.py install
```

### Finding Colormaps

Colormaps are pre-built and loaded at the time of importing. 

### Using Colormaps

- Importing Colormaps

```python
import colormaps as cmaps
cmaps.drought_severity
```

![brwnyl](https://pratiman-91.github.io/colormaps/assets/images/ncar_ncl/drought_severity.png)

```python
cmaps.ice
```
![ice](https://pratiman-91.github.io/colormaps/assets/images/cmocean/ice.png)

- Getting discrete number of levels

```python
cmaps.ice.discrete(10)
```

![ice_discrete](https://pratiman-91.github.io/colormaps/assets/images/demo/ice_discrete_10.png)

- Shifting the colormap

```python
cmaps.ice.shift(0.5)
```

![ice_shift](https://pratiman-91.github.io/colormaps/assets/images/demo/ice_shift_0_5.png)

- Shifting and then discrete levels

```python
cmaps.ice.shift(0.5).discrete(10)
```

![ice_shift_discrete](https://pratiman-91.github.io/colormaps/assets/images/demo/ice_shift_0_5_discrete_10.png)

- Discrete levels then cut the colormap from left side

```python
cmaps.ice.discrete(11).cut(0.25, 'left')
```

![ice_shift_discrete](https://pratiman-91.github.io/colormaps/assets/images/demo/ice_discrete_11_cut_0.25.png)

- Concatenate two or more colormaps

```python
from colormaps.utils import concat
concat1 = concat(["ice", "BkBlAqGrYeOrReViWh200"])
```

![concat_1](https://pratiman-91.github.io/colormaps/assets/images/demo/concat_1.png)

- Concatenate two or more colormaps based on ratio

```python
from colormaps.utils import concat
concat2 = concat([cmaps.ice, cmaps.BkBlAqGrYeOrReViWh200], ratios=[0.25,0.75])
```

![concat_1](https://pratiman-91.github.io/colormaps/assets/images/demo/concat_2.png)

- Matplotlib usage example

```python
import matplotlib.pyplot as plt
import colormaps as cmaps
import numpy as np

x = y = np.arange(-3.0, 3.01, 0.05)
X, Y = np.meshgrid(x, y)

sigmax = sigmay = 1.0
mux = muy = sigmaxy=0.0

Xmu = X-mux
Ymu = Y-muy

rho = sigmaxy/(sigmax*sigmay)
z = Xmu**2/sigmax**2 + Ymu**2/sigmay**2 - 2*rho*Xmu*Ymu/(sigmax*sigmay)
denom = 2*np.pi*sigmax*sigmay*np.sqrt(1-rho**2)
Z = np.exp(-z/(2*(1-rho**2))) / denom

plt.pcolormesh(X,Y,Z,cmap=cmaps.cubehelix3_16_r)
plt.colorbar()
```

![concat_1](https://pratiman-91.github.io/colormaps/assets/images/demo/matplotlib_1.png)
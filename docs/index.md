---
layout: default
title: Home
nav_order: 1
description: "Colormaps for Python"
permalink: /
---

# Colormaps
<!--- {: .fs-9 } -->

Colormaps is a library of collection of colormaps or color palettes for Python. It's written in Python with matplotlib and numpy as dependencies. You can use Colormaps to customize matplotlib plots.
<!---{: .fs-6 .fw-300 } -->

Colormaps has colormaps or color palettes from:

- [cartocolors](/colormaps/docs/cartocolors) 
- [cmocean](/colormaps/docs/cmocean)
- [colorbrewer](/colormaps/docs/colorbrewer)
- [cubehelix](/colormaps/docs/cubehelix)
- [ncar ncl](/colormaps/docs/ncar_ncl)
- [scientific](/colormaps/docs/scientific)
- [tableau](/colormaps/docs/tableau)
- `may be more`

<!---'[Get started now](#getting-started){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 } [View it on GitHub](https://github.com/pmarsceill/just-the-docs){: .btn .fs-5 .mb-4 .mb-md-0 }' -->

---

## Getting started

### Dependencies

Python with:

- matplotlib
- numpy

### Installation

```bash
git clone https://github.com/pratiman-91/colormaps.git
cd cmaps
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

![brwnyl](/assets/images/ncar_ncl/drought_severity.png)

```python
cmaps.ice
```
![ice](/assets/images/cmocean/ice.png)

- Getting discrete number of levels

```python
cmaps.ice.discrete(10)
```

![ice_discrete](/assets/images/demo/ice_discrete_10.png)

- Shifting the colormap

```python
cmaps.ice.shift(0.5)
```

![ice_shift](/assets/images/demo/ice_shift_0_5.png)

- Shifting and then discrete levels

```python
cmaps.ice.shift(0.5).discrete(10)
```

![ice_shift_discrete](/assets/images/demo/ice_shift_0_5_discrete_10.png)

- Discrete levels then cut the colormap from left side

```python
cmaps.ice.discrete(11).cut(0.25, 'left')
```

![ice_shift_discrete](/assets/images/demo/ice_discrete_11_cut_0.25.png)

- Concatenate two or more colormaps

```python
from colormaps.utils import concat
concat1 = concat(["cmocean_ice", "BkBlAqGrYeOrReViWh200"])
```

![concat_1](/assets/images/demo/concat_1.png)

- Concatenate two or more colormaps based on ratio

```python
from colormaps.utils import concat
concat2 = concat([cmaps.cmocean_ice, cmaps.BkBlAqGrYeOrReViWh200], ratios=[0.25,0.75])
```

![concat_1](/assets/images/demo/concat_2.png)

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

![concat_1](/assets/images/demo/matplotlib_1.png)
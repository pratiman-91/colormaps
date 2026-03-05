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
- [carbonplan](https://pratiman-91.github.io/colormaps/docs/carbonplan)
- [cmasher](https://pratiman-91.github.io/colormaps/docs/cmasher)
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

or using `conda`

```
conda install colormaps -c conda-forge`
```

or using `mamba`

```
mamba install colormaps
```

or you can also use GitHub repo

```bash
git clone https://github.com/pratiman-91/colormaps.git
cd colormaps
python setup.py install
```


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

- Reverse the colormap

```python
cmaps.ice_r
```

![ice_r](https://pratiman-91.github.io/colormaps/assets/images/cmocean/ice_r.png)

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

![concat_2](https://pratiman-91.github.io/colormaps/assets/images/demo/concat_2.png)

- Concatenate two or more colormaps with granular support

```python
from colormaps.utils import concat
concat3 = concat(
        ["ice", "thermal"],
        ratios=[0.4, 0.6],
        trim=[0.1, 0.05],
        discrete=128,
        name="my_concat"
    )
```

![my_concat](https://pratiman-91.github.io/colormaps/assets/images/demo/my_concat.png)

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

![matplotlib_1](https://pratiman-91.github.io/colormaps/assets/images/demo/matplotlib_1.png)

- Using concat in matplotlib

```python
# Create sample data
X = np.linspace(-np.pi, np.pi, 100)
Y = np.linspace(-np.pi, np.pi, 100)
X, Y = np.meshgrid(X, Y)
Z = np.sin(X) * np.cos(Y)

# Plot with a colormap
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Using ice colormap
im1 = axes[0].pcolormesh(X, Y, Z, cmap=cmaps.ice, shading='auto')
axes[0].set_title("Using cmaps.ice")
plt.colorbar(im1, ax=axes[0])

# Using a custom concatenated colormap
custom_cmap = concat(["thermal", "ice"], ratios=[0.4, 0.6])
im2 = axes[1].pcolormesh(X, Y, Z, cmap=custom_cmap, shading='auto')
axes[1].set_title("Using concat(['thermal', 'ice'])")
plt.colorbar(im2, ax=axes[1])
```

![matplotlib_2](https://pratiman-91.github.io/colormaps/assets/images/demo/matplotlib_2.png)

- Register maps with matplotlib

```python
_ = cmaps.ice      # registers "ice" with matplotlib
_ = cmaps.thermal  # registers "thermal" with matplotlib

X = np.linspace(-np.pi, np.pi, 100)
Y = np.linspace(-np.pi, np.pi, 100)
X, Y = np.meshgrid(X, Y)
Z = np.sin(X) * np.cos(Y)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

im1 = axes[0].pcolormesh(X, Y, Z, cmap="ice", shading='auto')
axes[0].set_title('cmap="ice" (registered by colormaps)')
plt.colorbar(im1, ax=axes[0])

im2 = axes[1].pcolormesh(X, Y, Z, cmap="thermal", shading='auto')
axes[1].set_title('cmap="thermal" (registered by colormaps)')
plt.colorbar(im2, ax=axes[1])

plt.tight_layout()
```

![matplotlib_3](https://pratiman-91.github.io/colormaps/assets/images/demo/matplotlib_3.png)

- Register collections with matplotlib

```python
# Register a single collection up front
cmaps.register_collection('cmocean')

# Now use by string name without prior attribute access
X = np.linspace(0, 1, 100)
Y = np.linspace(0, 1, 100)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.pi * X) * np.cos(np.pi * Y)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
im1 = axes[0].pcolormesh(X, Y, Z, cmap="ice", shading='auto')
axes[0].set_title('cmap="ice" via register_collection("cmocean")')
plt.colorbar(im1, ax=axes[0])

cmaps.register_all()

im2 = axes[1].pcolormesh(X, Y, Z, cmap="amber", shading='auto')
axes[1].set_title('cmap="amber" via register_all()')
plt.colorbar(im2, ax=axes[1])

plt.tight_layout()
```

![matplotlib_4](https://pratiman-91.github.io/colormaps/assets/images/demo/matplotlib_4.png)

### Finding Colormaps

Colormaps are pre-built and loaded at the time of importing. 

- Show different collections

```python
from colormaps.utils import show_cmaps_collection
show_cmaps_collection(collection='cmasher')

```

![show_cmaps_collection](https://pratiman-91.github.io/colormaps/assets/images/demo/show_cmaps_collection.png)

- Show all collections

```python
from colormaps.utils import show_cmaps_all
show_cmaps_all()
```

> This is just a sample! You will get a long list of all possible colormap collections.

![show_cmaps_all](https://pratiman-91.github.io/colormaps/assets/images/demo/show_cmaps_all.png)

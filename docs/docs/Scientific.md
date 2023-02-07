--- 
 layout: default 
 title: Scientific Colormaps
 nav_order: 6
 permalink: /docs/Scientific 
--- 

# Scientific Colormaps
{: .no_toc } 

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---
## Colormaps for Publication

https://www.nature.com/articles/s41467-020-19160-7

1. Colorbrewer
2. MPL (Matplotlib)
3. CMOcean
4. CET (Centre for Exploration Targeting)
5. Scientific

### [Colorbrewer](/colormaps/docs/collections/colorbrewer)

The Colorbrewer colour maps developed by Cynthia Brewer are provided through an online tool to manually produce and export a variety of discrete colour maps, which can, optionally, be colour-vision deficiency friendly and exported to a given a variety of formats. With the main aim being cartography, the online tool offers sequential, diverging and categorical (or in other words, qualitative) colour maps, but does not currently offer them in a continuous type.

### MPL (Matplotlib)

The MPL colour maps developed by Stéfan van der Walt and Nathaniel Smith. MPL maps aim for the most accurate perceptual uniformity with its widely applied colour maps being: **viridis, magma, plasma and inferno**. These maps have spearheaded the way towards more scientific colour mapping. The MPL colour maps are all sequential and continuous only. The MPL colour maps are openly available (currently for use with Python) and often built into software.

### [CMOcean](/colormaps/docs/collections/cmocean)

The CMOcean colour maps , developed by Kristen M. Thyng and colleagues, aim to provide the most intuitive colours for a given suite of physical parameters, while now also being perceptually uniform. A variety of continuous sequential, diverging and cyclic colour maps are provided to allow for an intuitive, true representation of a given physical parameter field. The CMOcean colour maps are available in a large variety of file formats.

### [CET (Centre for Exploration Targeting)](/colormaps/docs/collections/colorcet)

The CET colour maps, developed by Peter Kovesi, aim to offer a large choice of the most common colour combinations in a wide variety of data formats. Many of the offered colour maps feature perceptual uniformity, although not all of them to the highest standards. The CET colour maps are continuous and cover sequential, diverging, and cyclic classes.

### [Scientific](/colormaps/docs/collections/scientific) 

The Scientific colour maps are perceptually uniform (based on the underlying methodology of the CET colour maps65), perceptually ordered, colour-vision deficiency and colour-blind friendly, readable in black and white prints, and, if applied properly, also data set specific and parameter intuitive. The Scientific colour maps include sequential, diverging, and cyclic palettes, which are also provided as discrete and categorical palettes, and are available in a multitude of different file formats. They are also available through external routines and as built-in versions in a variety of software programmes. In contrast to others, the Scientific colour map package includes individual colour map diagnostics, and is versioned on a long-term online repository so individual versions can be accurately cited, which allows active developments from the community (e.g., improve their perceptual uniformity to the latest standards), and aids overall scientific reproducibility.

### [Cmasher](/colormaps/docs/collections/cmasher)

The `CMasher` provides a collection of scientific colormaps. The colormaps in CMasher are all designed to be perceptually uniform sequential using the `viscm` package; most of them are color-vision deficiency (CVD; color blindness) friendly; and they cover a wide range of different color combinations to accommodate for most applications. It offers several alternatives to commonly used colormaps, like `chroma` and `rainforest` for `jet`; `sunburst` for `hot`; `neutral` for `binary`; and `fusion` and `redshift` for `coolwarm`. 

If you use `CMasher` for your work, then please star the [repo](https://github.com/1313e/CMasher). Additionally, if you use CMasher as part of your workflow in a scientific publication, please consider citing the `CMasher` paper (van der Velden, (2020). CMasher: Scientific colormaps for making accessible, informative and 'cmashing' plots. Journal of Open Source Software, 5(46), 2004, https://doi.org/10.21105/joss.02004).
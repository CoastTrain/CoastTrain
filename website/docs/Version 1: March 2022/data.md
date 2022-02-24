---
sidebar_position: 3
---

# Data

## Access
Data may be downloaded from the Coastal and Marine Geology Data Service at [this link](https://cmgds.marine.usgs.gov/data-releases/datarelease/10.5066-P91NP87I/) (not yet live - please check back later)

## File description and contents
There are 10 data records and each record consists of a single zipped file. The zipped file contains a single csv file containing metadata for each labeled image, and a folder containing .npz format files, one per labeled image. Zipped files follow the following naming convention: {datasource}_{numberofclasses}_{threedigitdatasetversion}.zip, where 
* {datasource} is the source of the original images (for example, NAIP, Landsat 8, Sentinel 2), 
* {numberofclasses} is the number of classes used to annotate the images, and 
* {threedigitdatasetversion} is the three-digit code corresponding to the dataset version (in other words, 001 is version 1). 

All NPZ files can be extracted using the utilities available in Doodler (Buscombe, 2022; https://doi.org/10.5066/P9YVHL23) - see below for more details. An individual NPZ file is named after the image that it represents and contains the following variables

| Variable   |      Description   |
|----------|:-------------:|
| ‘image’ |  Image used by the Doodler program. This is the first 3 bands of ‘orig_image’|
| ‘orig_image’ |    Original 8-bit unsigned integer image read by the Doodler program, that may contain 4 bands.    |
| ‘label’ | One-hot-encoded label image (2D raster) in 8-bit unsigned integer. Each integer encodes a class label, incrementing through `classes` starting at zero.   |
| ‘color_label’ |  8-bit unsigned integer 3D (RGB) version of ‘label’ colorized according to a discrete colormap|
| ‘color_doodles’ |  8-bit unsigned integer 3D (RGB) raster of doodles colorized according to a discrete colormap|
| ‘doodles’ |  8-bit unsigned integer 2D raster of doodles. It is possible to use Doodler utilities to reconstruct ‘label’ from ‘doodles’ and values listed in ‘settings’|
| ‘settings’ |  List of settings used internally by the program, including the final values of the hyperparameters that may have been modified by the labeler|
| ‘classes’ | List of strings, each string a class name|
| 0-prefix |  The variables ‘label’, ‘doodles’, and ‘color_doodles’ may have one or several prefix zeros, the number of which indicate the order of the previous trial. Variables without a zero prefix are always the final versions.|

We provide codes to extract all images and labels and other information using utility scripts packaged with  the Doodler program. Labels are reproducible; it is possible to use Doodler to reconstruct all the labeled imagery from the original sparse annotations (or ‘doodles’) that are recorded to file. 

## Unpacking NPZ file contents
The following instructions will allow you to unpack the contents of each .npz file to visualize the imagery, label imagery, and sparse annotations of `doodles` that made the labels, as jpeg format files viewable on your desktop.

To do this we need the software [Doodler](https://github.com/Doodleverse/dash_doodler). Check out the installation guide on the [Doodler website](https://doodleverse.github.io/dash_doodler/).

In a nutshell, download the code

```
git clone --depth 1 https://github.com/dbuscombe-usgs/dash_doodler.git
```

Make a conda environment

```
conda env create --file install/dashdoodler-clean.yml
conda activate dashdoodler
```

```
cd utils
python gen_images_and_labels.py
```

The program will prompt you to `Select directory of results (annotations)` which is the folder of npz files. For each npz file, it will create a jpeg file `_label.jpg` showing the greyscale label, an overlay `_overlay.png` file showing the image overlain with a color label mask, and color sparse annotations or doodles `_doodles.png`.

The images and greyscale label images can be used with [Segmentation Gym](https://github.com/Doodleverse/segmentation_gym) to create deep-learning-based image segmentation models.

## Metadata

You may examine the contents of the Coast Train version 1 programmatically using a collections of python scripts and ipython notebooks hosted in [this github repository](https://github.com/dbuscombe-usgs/CoastTrainMetaPlots)


## Citation

If you find the dataset useful please consider citing our work:

Buscombe, D., Wernette, P.A.,Fitzpatrick, S., Favela, J., Goldstein E.B., and Enwright, N.M. 2022, A 1.2 Billion Pixel Human-Labeled Dataset for Data-Driven Classification of Coastal Environments. Intended for Scientific Data

Wernette, P.A., Buscombe, D.D., Favela, J., Fitzpatrick, S., and Goldstein E., 2022, Coast Train--Labeled imagery for training and evaluation of data-driven models for image segmentation: U.S. Geological Survey data release, https://doi.org/10.5066/P91NP87I
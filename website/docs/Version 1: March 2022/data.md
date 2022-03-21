---
sidebar_position: 3
---

# Data

## Access
Data may be downloaded from the Coastal and Marine Geology Data Service at [this link](https://cmgds.marine.usgs.gov/data-releases/datarelease/10.5066-P91NP87I/)

#### Data file links:
Here are links to each individual data set:

* [Landsat8_11_001.zip](https://cmgds.marine.usgs.gov/data-releases/media/2022/10.5066-P91NP87I/781710b1938b4325893c06b49ecd62a0/Landsat8_11_001.zip) - 611.3 MB
* [Landsat8_12_001.zip](https://cmgds.marine.usgs.gov/data-releases/media/2022/10.5066-P91NP87I/1bbac87e1b004f81a18ad6660665804b/Landsat8_12_001.zip) - 12.2 MB
* [NAIP_11_001.zip](https://cmgds.marine.usgs.gov/data-releases/media/2022/10.5066-P91NP87I/027742f5a4ff43f79e25709578e01ebc/NAIP_11_001.zip) - 4.0 GB
* [NAIP_6_001.zip](https://cmgds.marine.usgs.gov/data-releases/media/2022/10.5066-P91NP87I/959fb3494be14be7acc653c3434fd1d1/NAIP_6_001.zip) - 141.1 MB
* [Orthophoto_12_001.zip](https://cmgds.marine.usgs.gov/data-releases/media/2022/10.5066-P91NP87I/32a2d56bfe7443528103015d8a933407/Orthophoto_12_001.zip) - 501.4 MB
* [Orthophoto_8_001.zip](https://cmgds.marine.usgs.gov/data-releases/media/2022/10.5066-P91NP87I/62ab99be95f3446aa4401e5f08854d76/Orthophoto_8_001.zip) - 1.3 GB
* [Orthophoto_9_001.zip](https://cmgds.marine.usgs.gov/data-releases/media/2022/10.5066-P91NP87I/ff925cad3f6e4f92821fd529cf76dd80/Orthophoto_9_001.zip) - 1.5 GB
* [Quadrangles_7_001.zip](https://cmgds.marine.usgs.gov/data-releases/media/2022/10.5066-P91NP87I/88bc6ad30c9d4def8a0c737af1f6692c/Quadrangles_7_001.zip) - 326.4 MB
* [Sentinel2_11_001.zip](https://cmgds.marine.usgs.gov/data-releases/media/2022/10.5066-P91NP87I/bdc18f4f38004538af974aa0540d468c/Sentinel2_11_001.zip) - 361.6 MB
* [Sentinel2_4_001.zip](https://cmgds.marine.usgs.gov/data-releases/media/2022/10.5066-P91NP87I/60838f0cb7dd41fcbb8a5632c1821557/Sentinel2_4_001.zip) - 100.8 MB

Wget commands:

```
wget https://cmgds.marine.usgs.gov/data-releases/media/2022/10.5066-P91NP87I/781710b1938b4325893c06b49ecd62a0/Landsat8_11_001.zip
wget https://cmgds.marine.usgs.gov/data-releases/media/2022/10.5066-P91NP87I/1bbac87e1b004f81a18ad6660665804b/Landsat8_12_001.zip
wget https://cmgds.marine.usgs.gov/data-releases/media/2022/10.5066-P91NP87I/027742f5a4ff43f79e25709578e01ebc/NAIP_11_001.zip
wget https://cmgds.marine.usgs.gov/data-releases/media/2022/10.5066-P91NP87I/959fb3494be14be7acc653c3434fd1d1/NAIP_6_001.zip
wget https://cmgds.marine.usgs.gov/data-releases/media/2022/10.5066-P91NP87I/32a2d56bfe7443528103015d8a933407/Orthophoto_12_001.zip
wget https://cmgds.marine.usgs.gov/data-releases/media/2022/10.5066-P91NP87I/62ab99be95f3446aa4401e5f08854d76/Orthophoto_8_001.zip
wget https://cmgds.marine.usgs.gov/data-releases/media/2022/10.5066-P91NP87I/ff925cad3f6e4f92821fd529cf76dd80/Orthophoto_9_001.zip
wget https://cmgds.marine.usgs.gov/data-releases/media/2022/10.5066-P91NP87I/88bc6ad30c9d4def8a0c737af1f6692c/Quadrangles_7_001.zip
wget https://cmgds.marine.usgs.gov/data-releases/media/2022/10.5066-P91NP87I/bdc18f4f38004538af974aa0540d468c/Sentinel2_11_001.zip
wget https://cmgds.marine.usgs.gov/data-releases/media/2022/10.5066-P91NP87I/60838f0cb7dd41fcbb8a5632c1821557/Sentinel2_4_001.zip
```

This csv lists all files:

* [CoastTrain_imagery_details.csv](https://cmgds.marine.usgs.gov/data-releases/media/2022/10.5066-P91NP87I/bc506d1667674d5fa183ec30637d6db7/CoastTrain_imagery_details.csv) - 1.2 MB

#### Metadata file links:

* [CoastTrain_imagery_details_metadata.xml](https://cmgds.marine.usgs.gov/data-releases/media/2022/10.5066-P91NP87I/475f6af324954ef49b53393f4143b2b0/CoastTrain_imagery_details_metadata.xml) - 41.5 KB
* [CoastTrain_imagery_details_metadata.txt](https://cmgds.marine.usgs.gov/data-releases/media/2022/10.5066-P91NP87I/475f6af324954ef49b53393f4143b2b0/CoastTrain_imagery_details_metadata.txt) - 41.5 KB


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

## Programmatic workflows to examine dataset

You may examine the contents of the Coast Train version 1 programmatically using a collections of python scripts and ipython notebooks hosted in [this github repository](https://github.com/dbuscombe-usgs/CoastTrainMetaPlots). There are 4 notebooks:

1. [plot_class_distribution.ipynb](https://github.com/dbuscombe-usgs/CoastTrainMetaPlots/tree/main/notebooks)

Allows analysis of the class-image distributions for each data record in turn and overall. Generates the following plots:


2. [plot_geographic_distribution.ipynb](https://github.com/dbuscombe-usgs/CoastTrainMetaPlots/tree/main/notebooks)

Allows analysis of the geographic-image distributions for each data record in turn and overall. Generates the following plots:


3. [plot_user_distribution.ipynb](https://github.com/dbuscombe-usgs/CoastTrainMetaPlots/tree/main/notebooks)

Allows analysis of the anonymized labeler-image distributions for each data record in turn and overall. Generates the following plots:

4. [plot_image_locations.ipynb](https://github.com/dbuscombe-usgs/CoastTrainMetaPlots/tree/main/notebooks)

This notebook simply allows you to visualize where each image is located on a map, one by one


## Remapping classes
Classes in the labeled imagery can optionally be remapped. Datasets for image segmentation come with labels from pre-determined class sets. Those classes may be merged, split or otherwise remapped from one set of classes to another, depending on the intended application. For example, if the integer 1 is used to encode the class label `ocean', and the integer 2 is used to denote `river', those two classes might be merged such that integers 1 and 2 both denote a third common class, `water'.

We provide [this script](https://github.com/Doodleverse/dash_doodler/blob/main/utils/gen_remapped_images_and_labels.py) within the Doodler software program for carrying out class remapping of the data


## Citation

If you find the dataset useful please consider citing our work:

Buscombe, D., Wernette, P.A.,Fitzpatrick, S., Favela, J., Goldstein E.B., and Enwright, N.M. (in review). A 1.2 Billion Pixel Human-Labeled Dataset for Data-Driven Classification of Coastal Environments. Intended for Scientific Data

Wernette, P.A., Buscombe, D.D., Favela, J., Fitzpatrick, S., and Goldstein E. (2022). Coast Train--Labeled imagery for training and evaluation of data-driven models for image segmentation: U.S. Geological Survey data release, https://doi.org/10.5066/P91NP87I
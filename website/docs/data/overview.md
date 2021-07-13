---
sidebar_position: 2
---

# Overview

While there are many potential types of imagery we could use, the Coast Train project has settled on the following types of imagery because they collectively represent a majority of use-cases and scales.

## Geospatial

1. NAIP

The dataset consists of 1-m NAIP imagery from 8736 chunks, within 237 sites across the United States. Images are either 3-band (RGB) or 1-band (near-infrared) of the same extent. For each jpg file, there is a .wld file (ESRI world file format) and a aux.xml file containing all relevant coordinate system reference information for that image.


2. Orthomosaics

The dataset consists of  <= 1-m orthomosaics derived from SfM processing, with variable coverage and resolution. Large orrhomosaics have been tiled into 1024x1024x3 pixel images in jpeg format. For each jpg file, there is a .wld file (ESRI world file format) and a aux.xml file containing all relevant coordinate system reference information for that image.


3. Satellite imagery

10-m Sentinel-2

Each image band for every tile extent was downloaded as a separate 1-band geoTIFF image, then R, G, and B bands are merged

4. Quads

USGS Digital Ortho Quadrangle imagery of coastal wetlands in the Gulf. See [here](https://www.usgs.gov/faqs/what-a-digital-orthophoto-quadrangle-doq-or-orthoimage?qt-news_science_products=0#qt-news_science_products)


## Non- Geospatial  

Oblique snapshots of coasts from airplanes have variable coverage and resolution

1. PlaneCam
Images collected by aircraft for the USGS Remote Sensing Coastal Change project. See [here](https://www.usgs.gov/centers/pcmsc/science/remote-sensing-coastal-change?qt-science_center_objects=0#qt-science_center_objects)

2. NOAA
NOAA's post-hurricane reconnaissance imagery. See [here](https://www.nhc.noaa.gov/recon.php)

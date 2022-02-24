---
sidebar_position: 1
---

# Coast Train: A Library of Labeled Coastal Images to Train Machine Learning Models

Scientists who study coastal ecosystems and hazards such as hurricanes, flooding, and cliff failure collect lots of photographs of coastal environments from airplanes and drones. A large area can be surveyed at high resolution and low cost. Additionally, satellites such as Landsat have provided imagery of the Nation’s coastlines every few days for decades. 

Scientist’s ability to understand coastal hazards would be greatly improved if this wealth of imagery could be ‘mined’ automatically by computers. We want to automate the process of identifying and labelling each region of the image from a set of categories (e.g. bare land, water, woody vegetation, herbaceous vegetation). We need to train a computer to recognize the same things that a human can and that will require a very large number of labeled images.

## Why do we need Coast Train?

We define the information need met by Coast Train as:
1. Pixel-level discrete classification of a variety of publicly available geospatial imagery that are commonly used for coastal and other Earth surface processes research.
2. Statistics describing agreement that might be used to define uncertainty in labeled data. This uncertainty could be interpreted as the irreducible error
3. A fully reproducible workflow, facilitating end-user-defined accuracy assessments and quality control procedures. 
4. An extensible and open dataset, that might be actively contributed to by others.

The coastlines of the world are spatially highly variable coupled-human-natural systems that comprise a nested hierarchy of component landforms, ecosystems, and human interventions, each interacting over a range of space and time scales. Understanding and predicting coastline dynamics necessitates frequent observation from imaging sensors on remote sensing platforms. Machine Learning models that carry out supervised (i.e. human-guided) pixel-based classification, or image segmentation, have transformative applications in spatio-temporal mapping of dynamic environments, including transient coastal landforms, sediments, habitats, waterbodies, and water flows. However, these models require large and well-documented training and testing datasets consisting of labeled imagery. 

Coast Train provides researchers working in coastal environments (including but not limited to deltas, estuaries, barrier islands, salt marshes, developed and undeveloped coastlines including low energy and high energy coastal environments) with a training set that has until now been missing, allowing them to overcome a significant challenge to applying supervised and semi-supervised ML algorithms to the segmentation of high- and medium-resolution imagery. The library will allow us to train generic image segmentation models for satellite and high-resolution orthomosaics that will classify imagery into feature classes commonly used to categorize Earth surface composition (for example, water bodies, substrates, surficial geology, vegetation types, coastal infrastructure, development, and other landcover classes).

We anticipate that the datasets could be useful for training models for image segmentation of coastal and other natural environments. This labeled image library can be used either in their intended environments (i.e., the coastal waters of the conterminous United States) or used to train models that serve as starting points for training models for similar environments (e.g., other coastal regions, rivers, mountains, and lakes) with less data than would otherwise be needed — a concept known in ML as Transfer Learning.

## Project Manifesto

### For quantifying coastal change
Coast Train is for generating data (and models) for segmenting landscapes for the purposes of detecting and quantifying coastal change. By providing a means to segment imagery into broad classes, we are aware of the compromise between a) class specificity demanded by specific novel science objectives, and b) class generality demanded by the discipline as a whole. At study sites across CONUS, Coast Train will provide labeled data on a number of typical datasets and classes used and useful for coastal research.

### For basic stand-alone information, and use in ML model cascades
Classes are necessarily specific to the dataset. We will try to overlapping class sets where possible, but the overarching goal is to generate a broad set of classes that can respond to the challenge over the compromise mentioned above. Broad classes can be used for different multi-use purposes.

A ML model cascade is a series of models where the outputs of one are the inputs to the next, for stepwise prediction. For image segmentation, it is often a process of elimination; narrow down the problem by removing all classes not of interest, which makes a subsequent model (perhaps for more detailed classes) more tractable.

### Exemplifying coastal data science
We are, in addition to targeting important questions about phenomena, organizing our activities around important questions around coastal data science, which I would define as the activities around building modeling infrastructure and useful, unbiased datasets with known errors, in support of coastal science. We are contributing to an emerging subfield within our discipline, so we’re also interested in questions to do with transferability, question framing, “opinionated” class sets, etc.

### The Doodleverse: a community of tools for end-to-end model development and deployment
Coast Train is supported by a parallel effort called the [Doodleverse](https://github.com/Doodleverse/), containing tools for data labeling called [Doodler](https://dbuscombe-usgs.github.io/dash_doodler/), and one for building and training models to use Coast Train data for its intended purpose. The latter is a modeling suite under development called [Segmentation Gym](https://github.com/dbuscombe-usgs/segmentation_gym) that is based around a family of fully convolutional U-Net models.


## The Coast Train team

We are scientists working in coastal environments on topics in coastal conservation and ecology, hazards, mapping, physical oceanography, geography, and coastal geomorphology, with practical and research experience in image labeling, ML, and scientific applications.

• [Daniel Buscombe](https://scholar.google.com/citations?user=bwVl0NwAAAAJ&hl=en), Contractor, USGS Pacific Coastal and Marine Science Center

• [Evan Goldstein](https://ebgoldstein.wordpress.com/), Research Scientist, Institute for Data Evaluation and Analytics, University of North Carolina at Greensboro

• [Sharon Fitzpatrick](https://www.linkedin.com/in/sharon-fitzpatrick-9088b31b3), Contractor, USGS Pacific Coastal and Marine Science Center

• [Jaycee Favela](https://orcid.org/0000-0001-9175-8324), Contractor, USGS Pacific Coastal and Marine Science Center

• [Phillipe Wernette](https://www.usgs.gov/staff-profiles/phillipe-a-wernette?qt-staff_profile_science_products=3#qt-staff_profile_science_products), Research Geologist, USGS Pacific Coastal and Marine Science Center

• [Nicholas Enwright](https://www.usgs.gov/staff-profiles/nicholas-m-enwright?qt-staff_profile_science_products=0#qt-staff_profile_science_products), Geographer, USGS Wetland and Aquatic Research Center


## The Coast Train expert panel
• [Christopher Sherwood](https://www.usgs.gov/staff-profiles/christopher-sherwood?qt-staff_profile_science_products=0#qt-staff_profile_science_products), Research Oceanographer, USGS Woods Hole Coastal and Marine Science Center

• [Sara Zeigler](https://www.usgs.gov/staff-profiles/sara-l-zeigler?qt-staff_profile_science_products=0#qt-staff_profile_science_products), Research Geographer, USGS St. Petersburg Coastal and Marine Science Center

• [Kristin Byrd](https://www.usgs.gov/staff-profiles/kristin-byrd?qt-staff_profile_science_products=0#qt-staff_profile_science_products), Research Physical Scientist, Western Geographical Science Center

• [Zafer Defne](https://www.usgs.gov/staff-profiles/zafer-defne?qt-staff_profile_science_products=0#qt-staff_profile_science_products), Oceanographer, USGS Woods Hole Coastal and Marine Science Center

• [Nate Herold](https://coast.noaa.gov/digitalcoast/data/ccapregional.html), Physical Scientist / Land Cover Mapping Lead, NOAA Office of Coastal Management

• [Mara Orescanin](https://nps.edu/faculty-profiles/-/cv/msoresca), Assistant Professor, Naval Postgraduate School, Monterey

• [Andy Ritchie](https://www.usgs.gov/staff-profiles/andy-ritchie?qt-staff_profile_science_products=0#qt-staff_profile_science_products), Geomorphologist, USGS Pacific Coastal and Marine Science Center

• [Sean Vitousek](https://www.usgs.gov/staff-profiles/sean-vitousek?qt-staff_profile_science_products=3#qt-staff_profile_science_products), Research Oceanographer, USGS Pacific Coastal and Marine Science Center

• [Jonathan Warrick](https://www.usgs.gov/staff-profiles/jonathan-warrick?qt-staff_profile_science_products=0#qt-staff_profile_science_products), Research Geologist, USGS Pacific Coastal and Marine Science Center



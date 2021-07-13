---
sidebar_position: 1
---

# Coast Train: Building a Massive Library of Labeled Coastal Images to Train Machine Learning for Coastal Hazards and Resources

Scientists who study coastal ecosystems and hazards such as hurricanes, flooding, and cliff failure collect lots of photographs of coastal environments from airplanes and drones. A large area can be surveyed at high resolution and low cost. Additionally, satellites such as Landsat have provided imagery of the Nation’s coastlines every few days for decades. Scientist’s ability to understand coastal hazards would be greatly improved if this wealth of imagery could be ‘mined’ automatically by computers. We want to automate the process of identifying and labelling each region of the image from a set of categories (e.g. bare land, water, woody vegetation, herbaceous vegetation). We need to train a computer to recognize the same things that a human can and that will require a very large number of labeled images.

## Why do we need Coast Train?

Coast Train will provide researchers working in coastal environments (including but not limited to deltas, estuaries, barrier islands, salt marshes, developed and undeveloped coastlines including low energy and high energy coastal environments) with a training set that heretofore has been missing, allowing them to overcome a significant challenge to applying supervised and semi-supervised ML algorithms to the segmentation of high- and medium-resolution imagery. The library will allow us to train generic image segmentation models for satellite and high-resolution orthomosaics that will classify imagery into feature classes commonly used to categorize Earth surface composition (for example, water bodies, substrates, surficial geology, vegetation types, coastal infrastructure, development, and other landcover classes).

We anticipate that the datasets will be used by numerous groups both nationally and internationally to help train models for image segmentation of coastal and other natural environments. This labeled image library can be used either in their intended environments (i.e., the coastal waters of the conterminous United States) or used to train models that serve as starting points for training models for similar environments (e.g., other coastal regions, rivers, mountains, and lakes) with less data than would otherwise be needed — a concept known in ML as Transfer Learning. Therefore, the likely positive impact of the Coast Train dataset would extend beyond both coasts, the USGS, and the United States.

## Project Manifesto

### For quantifying coastal change
Coast Train is for generating data (and models) for segmenting landscapes for the purposes of detecting and quantifying coastal change. By providing a means to segment imagery into broad classes, we are aware of the compromise between a) class specificity demanded by specific novel science objectives, and b) class generality demanded by the discipline as a whole. At study sites across CONUS, Coast Train will provide labeled data on a number of typical datasets and classes used and useful for coastal research.

### For basic stand-alone information, and use in ML model cascades
Classes are necessarily specific to the dataset. We will try to overlapping class sets where possible, but the overarching goal is to generate a broad set of classes that can respond to the challenge over the compromise mentioned above. Broad classes can be used for different multi-use purposes.

A ML model cascade is a series of models where the outputs of one are the inputs to the next, for stepwise prediction. For image segmentation, it is often a process of elimination; narrow down the problem by removing all classes not of interest, which makes a subsequent model (perhaps for more detailed classes) more tractable.

### Exemplifying coastal data science
We are, in addition to targeting important questions about phenomena, organizing our activities around important questions around coastal data science, which I would define as the activities around building modeling infrastructure and useful, unbiased datasets with known errors, in support of coastal science. We are contributing to an emerging subfield within our discipline, so we’re also interested in questions to do with transferability, question framing, “opinionated” class sets, etc.

### End-to-end tools
Coast Train is supported by two parallel efforts, one for data labeling called [Doodler](https://dbuscombe-usgs.github.io/dash_doodler/), and one for building and training models to use Coast Train data for its intended purpose. The latter is a modeling suite under development called [Segmentation Zoo](https://github.com/dbuscombe-usgs/segmentation_zoo) that is based around the residual U-Net model.


## The Coast Train team

We are scientists working in coastal environments on topics in coastal conservation and ecology, hazards, mapping, physical oceanography, geography, and coastal geomorphology, with practical and research experience in image labeling, ML, and scientific applications.

• [Phillipe Wernette](https://www.usgs.gov/staff-profiles/phillipe-a-wernette?qt-staff_profile_science_products=3#qt-staff_profile_science_products), Research Geologist, USGS Pacific Coastal and Marine Science Center

• [Sara Zeigler](https://www.usgs.gov/staff-profiles/sara-l-zeigler?qt-staff_profile_science_products=0#qt-staff_profile_science_products), Research Geographer, USGS St. Petersburg Coastal and Marine Science Center

• [Daniel Buscombe](https://scholar.google.com/citations?user=bwVl0NwAAAAJ&hl=en), Contractor, USGS Pacific Coastal and Marine Science Center

• [Nicholas Enwright](https://www.usgs.gov/staff-profiles/nicholas-m-enwright?qt-staff_profile_science_products=0#qt-staff_profile_science_products), Geographer, USGS Wetland and Aquatic Research Center

• [Christopher Sherwood](https://www.usgs.gov/staff-profiles/christopher-sherwood?qt-staff_profile_science_products=0#qt-staff_profile_science_products), Research Oceanographer, USGS Woods Hole Coastal and Marine Science Center

• [Evan Goldstein](https://ebgoldstein.wordpress.com/), Research Scientist, Institute for Data Evaluation and Analytics, University of North Carolina at Greensboro

• [Jonathan Warrick](https://www.usgs.gov/staff-profiles/jonathan-warrick?qt-staff_profile_science_products=0#qt-staff_profile_science_products), Research Geologist, USGS Pacific Coastal and Marine Science Center


## The Coast Train expert panel

• [Kristin Byrd](https://www.usgs.gov/staff-profiles/kristin-byrd?qt-staff_profile_science_products=0#qt-staff_profile_science_products), Research Physical Scientist, Western Geographical Science Center

• [Zafer Defne](https://www.usgs.gov/staff-profiles/zafer-defne?qt-staff_profile_science_products=0#qt-staff_profile_science_products), Oceanographer, USGS Woods Hole Coastal and Marine Science Center

• [Nate Herold](https://coast.noaa.gov/digitalcoast/data/ccapregional.html), Physical Scientist / Land Cover Mapping Lead, NOAA Office of Coastal Management

• [Mara Orescanin](https://nps.edu/faculty-profiles/-/cv/msoresca), Assistant Professor, Naval Postgraduate School, Monterey

• [Andy Ritchie](https://www.usgs.gov/staff-profiles/andy-ritchie?qt-staff_profile_science_products=0#qt-staff_profile_science_products), Geomorphologist, USGS Pacific Coastal and Marine Science Center

• [Sean Vitousek](https://www.usgs.gov/staff-profiles/sean-vitousek?qt-staff_profile_science_products=3#qt-staff_profile_science_products), Research Oceanographer, USGS Pacific Coastal and Marine Science Center


### June 17 Coast Train expert panel meeting 1

#### “What coastal science questions/topics could be immediately addressed using the Coast Train dataset?”
Participants were encouraged to answer this question in light of other known datasets and initiatives like C-CAP. A summary of identified and discussed topics are listed below

* Mudflats and marshes - shoreline change, and changes in bare area. Mangrove expansion into marshes.
* Beaches and dunes - capturing any change such as after storm events and restoration efforts
* Habitat succession, heterogeneity, and complexity
* Ghost forests - saltwater intrusion and dieback

The group collectively agreed that consensus is key in any scientific application: errors must be minimal, therefore categories should be broad. Also, there was a consensus that a basic utility of Coast Train will be to generate gridded info for input or validation for numerical simulations of, for example, flooding, roughness, erodability, or vegetation change.

#### "What set of classes/labels best collectively serve the identified science questions/topics?"

Numerous class sets were discussed and those suggestions collectively informed the class sets listed on this site for use with specific data sets/types. A number of over-arching recommendations were also made with respect to class set determination, which are summarized in brief below

* Time scale is very important to the science question
* Consequently, feasibility in usage of map-based products for science are focused on imagery temporal and spatial resolution
* Change itself can be a driver in science questions; unexpected categories (presence or absence of classes); unexpected class boundaries
* Higher resolution datasets are important to consider even if working at the moderate resolution
* Detecting storm impacts could be problematic since areas different than from a non-disturbed point in time.
* High-resolution imagery has fewer mixed pixels and resolves transition areas better, so labeling with the highest resolution is good, but not all categories transfer to lower-resolution imagery


#### List of design criteria established as a result of the meeting

1. Context is important: images should be viewed in time-series where possible, and GIS and base imagery (Google Earth, etc) should be used for context
2. Label what we are confident about (only), to maximize true positives in the training data
3. Use a short list of simple (broad/elemental) classes – start simple and build complexity later (a hierarchical labeling approach)
4. There should be a probability sink (unknown/uncertain) class; if multilabel, it could encode candidate classes
5. Consider a ‘unusual’ class – things that are not in the class set but occasionally appear in the scene
6. Where possible, labels at high-resolution could be transferred to lower resolution imagery, to catalogue mixed pixels for lower-res. Imagery
7. Splitting classes harder/less consensus than lumping classes, in general
8. Avoid ordinal classes, but vegetation presence/absence requires making a call based on sparseness – develop a visual guide (manual) to help with consistency
9. Higher resolution datasets are important to consider even if working at the moderate resolution; aggregate to large spatial scales where appropriate
10. Develop a consistent strategy for ‘developed open spaces’ like agricultural land, golf courses, waterparks, etc – these are land cover, not land use.

The class sets that were determined as a result of this fruitful discussion are found in the `Classes' tab of the sidepane.

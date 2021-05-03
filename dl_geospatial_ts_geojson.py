# Written by Dr Daniel Buscombe, Marda Science LLC
# for the USGS Coastal Change Hazards Program
#
# MIT License
#
# Copyright (c) 2020,2021, Marda Science LLC
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# For a list of polygons in a geojson file

# 1. download all the 1-m NAIP imagery between 2010 and 2020. Bands downloaded separately and as a multiband geotiff
# 1a. If the imagery is larger than an allowable GEE data packet (33MB), region is quartered and each quarter

import geemap,ee, reverse_geocoder
import os, json  #shutil
from ipyleaflet import GeoJSON
import numpy as np
from glob import glob
from area import area
from joblib import Parallel, delayed

from shapely.geometry import LineString, MultiPolygon, Polygon
from shapely.ops import split

# read in coast train master sites
with open('coastTrain_sites.geojson') as f:
    json_data = json.load(f)
features = json_data['features']


start_date = '2010-01-01'
end_date = '2020-12-31'

MAXCLOUD = 5  #percentage maximum cloud cover tolerated



##============================

L=[]; LL=[]
for feature,site in zip(features, np.arange(1,1+len(features))):
    coordinates = feature['geometry']['coordinates']
    lng, lat = np.mean(coordinates[0], axis=0)
    #print((lng, lat))
    LL.append(lng); L.append(lat)

coordinates = [tuple((a,b)) for a,b in zip(L,LL)]
geocodes = reverse_geocoder.search(coordinates)

N = []; A1 = []; A2 = []
for g in geocodes:
    N.append(g['name'])
    A1.append(g['admin1'])
    A2.append(g['admin2'])

np.savetxt("site_locs.csv", np.vstack((LL,L)).T, delimiter=",")
np.savetxt("site_names.csv", np.vstack((N,A1,A2)).T, delimiter=",", fmt='%s')



###=================================================
############### NAIP #########################
###=================================================
gee_collection = 'USDA/NAIP/DOQQ'

OUT_RES_M = 1

try:
    os.mkdir('naip')
except:
    pass


# site = 1
# for feature in features:
def func(feature, site, nx=4, ny=4):
    try:
        os.mkdir('naip'+os.sep+'site'+str(site))
    except:
        pass

    # initialize Earth Engine
    ee.Initialize()

    coordinates = feature['geometry']['coordinates']
    lng, lat = np.mean(coordinates[0], axis=0)
    print((lng, lat))
    area_sqkm = area(feature['geometry'])/1e6
    #print(area_sqkm)

    collection = ee.ImageCollection(gee_collection)

    polygon = Polygon([tuple(c) for c in coordinates[0]])
    minx, miny, maxx, maxy = polygon.bounds

    #nx, ny = 12,12 #4, 4  # number of columns and rows

    dx = (maxx - minx) / nx  # width of a small part
    dy = (maxy - miny) / ny  # height of a small part
    horizontal_splitters = [LineString([(minx, miny + i*dy), (maxx, miny + i*dy)]) for i in range(ny)]
    vertical_splitters = [LineString([(minx + i*dx, miny), (minx + i*dx, maxy)]) for i in range(nx)]
    splitters = horizontal_splitters + vertical_splitters

    result = polygon
    for splitter in splitters:
        result = MultiPolygon(split(result, splitter))
    parts = [list(part.exterior.coords) for part in result.geoms]

    counter = 1
    for part in parts:

        try:
            os.mkdir('naip'+os.sep+'site'+str(site)+os.sep+'chunk'+str(counter))
        except:
            pass

        print(area({'type':'Polygon','coordinates': [[list(p) for p in part]]})/1e6)
        collection = ee.ImageCollection(gee_collection)

        polys = ee.Geometry.Polygon(part)

        centroid = polys.centroid()
        lng, lat = centroid.getInfo()['coordinates']
        #print("lng = {}, lat = {}".format(lng, lat))

        #lng_lat = ee.Geometry.Point(lng, lat)
        collection = collection.filterBounds(polys)
        collection = collection.filterDate(start_date, end_date).sort('system:time_start', True)
        count = collection.size().getInfo()
        #print("Number of cloudy scenes: ", count)
        img_lst = collection.toList(1000)

        N = []
        for i in range(0, count):
            image = ee.Image(img_lst.get(i))
            name = image.get('system:index').getInfo()
            N.append(name)

        for n in N:
            image = ee.Image('USDA/NAIP/DOQQ/'+n)
            #geemap.ee_export_image(image, os.getcwd()+os.sep+'site_'+str(site)+'_'+n+'_part_'+str(counter)+'_of_'+str(len(parts))+'.tif', scale=OUT_RES_M, region=polys, file_per_band=True)
            geemap.ee_export_image(image, os.getcwd()+os.sep+'naip'+os.sep+'site'+str(site)+os.sep+'chunk'+str(counter)+os.sep+'chunk'+str(counter)+'_'+n+'.tif', scale=OUT_RES_M, region=polys, file_per_band=True)
            geemap.ee_export_image(image, os.getcwd()+os.sep+'naip'+os.sep+'site'+str(site)+os.sep+'chunk'+str(counter)+os.sep+'chunk'+str(counter)+'_'+n+'_multiband.tif', scale=OUT_RES_M, region=polys, file_per_band=False)

        counter += 1

    # site += 1


## call the above in parallel
## nx = ny = 4
# w = Parallel(n_jobs=-1, verbose=1)(delayed(func)(feature,site) for feature,site in zip(features, np.arange(1,1+len(features))))

## nx = ny = 4
# 74,75,77,79,80,81,83,84,85,88

# nx = ny = 12
# w = Parallel(n_jobs=-1, verbose=1)(delayed(func)(feature,site,nx,ny) for feature,site in zip(features[55:74], np.arange(55,75)))

## nx = ny = 12
#76,78,82,86,87

## nx = ny = 4
#w = Parallel(n_jobs=-1, verbose=1)(delayed(func)(feature,site) for feature,site in zip(features[100:], np.arange(100,1+len(features))))


# nx = ny = 12
# w = Parallel(n_jobs=-1, verbose=1)(delayed(func)(feature,site,nx,ny) for feature,site in zip(features[89:99], np.arange(89,100)))


nx = ny = 4
w = Parallel(n_jobs=-1, verbose=1)(delayed(func)(feature,site,nx,ny) for feature,site in zip(features[100:121], np.arange(100,122)))


nx = ny = 4
w = Parallel(n_jobs=-1, verbose=1)(delayed(func)(feature,site,nx,ny) for feature,site in zip(features[122:129], np.arange(122,130)))

nx = ny = 6
w = Parallel(n_jobs=-1, verbose=1)(delayed(func)(feature,site,nx,ny) for feature,site in zip(features[130:158], np.arange(130,159)))


nx = ny = 4
w = Parallel(n_jobs=-1, verbose=1)(delayed(func)(feature,site,nx,ny) for feature,site in zip(features[174:226], np.arange(174,227)))

nx = ny = 8
site=158; feature = features[site]; func(feature,site,nx,ny);
##99, 121, 159, 167, 168, 169, 170, 172, 173

nx = ny = 8
site=121; feature = features[site]; func(feature,site,nx,ny); site=159; feature = features[site]; func(feature,site,nx,ny)

site=167; feature = features[site]; func(feature,site,nx,ny); site=168; feature = features[site]; func(feature,site,nx,ny)

site=169; feature = features[site]; func(feature,site,nx,ny); site=170; feature = features[site]; func(feature,site,nx,ny)


site=172; feature = features[site]; func(feature,site,nx,ny); site=173; feature = features[site]; func(feature,site,nx,ny)


nx = ny = 12
site=216; feature = features[site]; func(feature,site,nx,ny);

nx = ny = 8
site=129; feature = features[site]; func(feature,site,nx,ny);

nx = ny = 4
site=0; feature = features[site]; func(feature,site,nx,ny);


# cmd = 'for file in *.tif; do gdal_translate -of JPEG -scale -co worldfile=yes $file "${file%.tif}.jpg"; done'
# os.chdir()
# os.command(cmd)

###=================================================
############### NLCD #########################
###=================================================

gee_collection = 'USGS/NLCD_RELEASES/2016_REL'
OUT_RES_M = 30


try:
    os.mkdir('nlcd')
except:
    pass


# collection = ee.ImageCollection(gee_collection)
#
# polys = ee.Geometry.Polygon(coordinates)
# centroid = polys.centroid()
# lng, lat = centroid.getInfo()['coordinates']
# # print("lng = {}, lat = {}".format(lng, lat))
#
# lng_lat = ee.Geometry.Point(lng, lat)
# collection = collection.filterBounds(polys)
# collection = collection.filterDate(start_date, end_date).sort('system:time_start', True)
# count = collection.size().getInfo()
# print("Number of cloudy scenes: ", count)
#
#
# img_lst = collection.toList(1000)
#
# N = []
# for i in range(0, count):
#     image = ee.Image(img_lst.get(i))
#     name = image.get('system:index').getInfo()
#     N.append(name)
#
# for n in N:
#         image = ee.Image('USGS/NLCD_RELEASES/2016_REL/'+n)
#         geemap.ee_export_image(image, os.getcwd()+os.sep+'nlcd'+os.sep+n+'.tif', scale=OUT_RES_M, region=polys)
#


# site = 1
# for feature in features:
def func(feature, site):
    try:
        os.mkdir('nlcd'+os.sep+'site'+str(site))
    except:
        pass

    # initialize Earth Engine
    ee.Initialize()

    coordinates = feature['geometry']['coordinates']
    lng, lat = np.mean(coordinates[0], axis=0)
    #print((lng, lat))
    area_sqkm = area(feature['geometry'])/1e6
    #print(area_sqkm)

    collection = ee.ImageCollection(gee_collection)

    polygon = Polygon([tuple(c) for c in coordinates[0]])
    minx, miny, maxx, maxy = polygon.bounds

    nx, ny = 4, 4  # number of columns and rows

    dx = (maxx - minx) / nx  # width of a small part
    dy = (maxy - miny) / ny  # height of a small part
    horizontal_splitters = [LineString([(minx, miny + i*dy), (maxx, miny + i*dy)]) for i in range(ny)]
    vertical_splitters = [LineString([(minx + i*dx, miny), (minx + i*dx, maxy)]) for i in range(nx)]
    splitters = horizontal_splitters + vertical_splitters

    result = polygon
    for splitter in splitters:
        result = MultiPolygon(split(result, splitter))
    parts = [list(part.exterior.coords) for part in result.geoms]

    counter = 1
    for part in parts:

        try:
            os.mkdir('naip'+os.sep+'site'+str(site)+os.sep+'chunk'+str(counter))
        except:
            pass

        #print(area({'type':'Polygon','coordinates': [[list(p) for p in part]]})/1e6)
        collection = ee.ImageCollection(gee_collection)

        polys = ee.Geometry.Polygon(part)

        centroid = polys.centroid()
        lng, lat = centroid.getInfo()['coordinates']
        #print("lng = {}, lat = {}".format(lng, lat))

        #lng_lat = ee.Geometry.Point(lng, lat)
        collection = collection.filterBounds(polys)
        collection = collection.filterDate(start_date, end_date).sort('system:time_start', True)
        count = collection.size().getInfo()
        #print("Number of cloudy scenes: ", count)
        img_lst = collection.toList(1000)

        N = []
        for i in range(0, count):
            image = ee.Image(img_lst.get(i))
            name = image.get('system:index').getInfo()
            N.append(name)

        for n in N:
            image = ee.Image('USDA/NAIP/DOQQ/'+n)
            #geemap.ee_export_image(image, os.getcwd()+os.sep+'site_'+str(site)+'_'+n+'_part_'+str(counter)+'_of_'+str(len(parts))+'.tif', scale=OUT_RES_M, region=polys, file_per_band=True)
            geemap.ee_export_image(image, os.getcwd()+os.sep+'naip'+os.sep+'site'+str(site)+os.sep+'chunk'+str(counter)+os.sep+'chunk'+str(counter)+'_'+n+'.tif', scale=OUT_RES_M, region=polys, file_per_band=True)
            geemap.ee_export_image(image, os.getcwd()+os.sep+'naip'+os.sep+'site'+str(site)+os.sep+'chunk'+str(counter)+os.sep+'chunk'+str(counter)+'_'+n+'_multiband.tif', scale=OUT_RES_M, region=polys, file_per_band=False)

        counter += 1

    site += 1


## call the above in parallel
w = Parallel(n_jobs=-1, verbose=1)(delayed(func)(feature,site) for feature,site in zip(features, np.arange(1,1+len(features))))














###=================================================
############### SENTINEL-2 #########################
###=================================================

gee_collection = 'COPERNICUS/S2_SR'
OUT_RES_M = 10 #output pixel size in m (10m for sentinel visisble band)

collection = ee.ImageCollection(gee_collection)

polys = ee.Geometry.Polygon(coordinates)
centroid = polys.centroid()
lng, lat = centroid.getInfo()['coordinates']
# print("lng = {}, lat = {}".format(lng, lat))

lng_lat = ee.Geometry.Point(lng, lat)
collection = collection.filterBounds(polys)
collection = collection.filterDate(start_date, end_date)
count = collection.size().getInfo()
print("Number of cloudy scenes: ", count)

collection = collection.filter('CLOUDY_PIXEL_PERCENTAGE < '+str(MAXCLOUD))

count = collection.size().getInfo()
print("Number of non-cloudy scenes: ", count)

img_lst = collection.toList(1000)

N = []
for i in range(0, count):
    image = ee.Image(img_lst.get(i))
    name = image.get('system:index').getInfo()
    N.append(name)

for n in N:
    print(n)
    image = ee.Image(gee_collection+'/'+n).select(['B4', 'B3', 'B2'])
    try:
        os.remove(os.getcwd()+os.sep+n+'.tif')
    except:
        pass
    geemap.ee_export_image(image, os.getcwd()+os.sep+n+'.tif', scale=OUT_RES_M, region=polys) #, file_per_band=True)

    image = ee.Image(gee_collection+'/'+n).select(['B8'])
    try:
        os.remove(os.getcwd()+os.sep+n+'_ir.tif')
    except:
        pass
    geemap.ee_export_image(image, os.getcwd()+os.sep+n+'_ir.tif', scale=OUT_RES_M, region=polys) #, file_per_band=True)


try:
    os.mkdir('sentinel2')
except:
    pass


for f in glob(os.getcwd()+os.sep+'*.tif'):
    print(f)
    shutil.move(f,os.getcwd()+os.sep+'sentinel2')



###=================================================
############### LANDSAT-8 #########################
###=================================================






###=================================================



# for f in glob(os.getcwd()+os.sep+'*.tif'):
#     print(f)
#     shutil.move(f,os.getcwd()+os.sep+'nlcd')
#



    # polys = ee.Geometry.Polygon(coordinates) #part)
    # centroid = polys.centroid()
    # lng, lat = centroid.getInfo()['coordinates']
    # #print("lng = {}, lat = {}".format(lng, lat))
    #
    # #lng_lat = ee.Geometry.Point(lng, lat)
    # collection = collection.filterBounds(polys)
    # collection = collection.filterDate(start_date, end_date).sort('system:time_start', True)
    # count = collection.size().getInfo()
    # #print("Number of cloudy scenes: ", count)
    # img_lst = collection.toList(1000)
    #
    # N = []
    # for i in range(0, count):
    #     image = ee.Image(img_lst.get(i))
    #     name = image.get('system:index').getInfo()
    #     N.append(name)
    #
    # for n in N:
    #     image = ee.Image('USDA/NAIP/DOQQ/'+n)
    #     #geemap.ee_export_image(image, os.getcwd()+os.sep+'site_'+str(site)+'_'+n+'_part_'+str(counter)+'_of_'+str(len(parts))+'.tif', scale=OUT_RES_M, region=polys, file_per_band=True)
    #     geemap.ee_export_image(image, os.getcwd()+os.sep+'naip'+os.sep+'site'+str(site)+os.sep+'site_'+str(site)+'_'+n+'.tif', scale=OUT_RES_M, region=polys, file_per_band=True)
    #     geemap.ee_export_image(image, os.getcwd()+os.sep+'naip'+os.sep+'site'+str(site)+os.sep+'site_'+str(site)+'_'+n+'_multiband.tif', scale=OUT_RES_M, region=polys, file_per_band=False)
    #
    # files = glob(os.getcwd()+os.sep+'naip'+os.sep+'site'+str(site)+os.sep+'*.tif')

    #if len(files)==0:

    #counter += 1

    # for f in glob(os.getcwd()+os.sep+'*.tif'):
    #     #print(f)
    #     shutil.move(f,os.getcwd()+os.sep+'naip'+os.sep+'site'+str(site))

    #
    #
    # for f in glob(os.getcwd()+os.sep+'*.tif'):
    #     print(f)
    #     shutil.move(f,os.getcwd()+os.sep+'naip/site'+str(site))

#
#
#
# to_merge = glob('/media/marda/TWOTB/USGS/SOFTWARE/Projects/CoastTrain/naip/site1/2011/*.tif')
# to_merge = " ".join(to_merge)
# print(to_merge)
#
# command = "gdal_merge.py -n 0 -a_nodata 0 -co PHOTOMETRIC=RGB -o merge_site1_2011.tif -of gtiff " + to_merge
# print(os.popen(command).read())


#
# json_data = {
#   "type": "FeatureCollection",
#   "features": [
#     {
#       "type": "Feature",
#       "properties": {},
#       "geometry": {
#         "type": "Polygon",
#         "coordinates": [
#           [
#             [
#               -75.76772689819336,
#               36.161646806872
#             ],
#             [
#               -75.73468208312988,
#               36.161646806872
#             ],
#             [
#               -75.73468208312988,
#               36.2003043685443
#             ],
#             [
#               -75.76772689819336,
#               36.2003043685443
#             ],
#             [
#               -75.76772689819336,
#               36.161646806872
#             ]
#           ]
#         ]
#       }
#     }
#   ]
# }
#
# coordinates = json_data['features'][0]['geometry']['coordinates']
#
# lng, lat = np.mean(coordinates[0], axis=0)
# print((lng, lat))

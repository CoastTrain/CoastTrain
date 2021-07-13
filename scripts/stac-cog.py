#http://www.acgeospatial.co.uk/stac-cog-python-and-qgis/

###===================================================
###=========== imports  ======================

#pip install sat-search
from satsearch import Search
import geopandas as gpd
import rasterio, os, json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

###===================================================
###=========== functions ======================

def get_thumbnail(file_url):
    with rasterio.open(file_url) as src:
       # List of overviews from biggest to smallest
       oviews = src.overviews(1)
       # Retrieve the smallest thumbnail
       oview = oviews[-1]
       # NOTE this is using a 'decimated read' (http://rasterio.readthedocs.io/en/latest/topics/resampling.html)
       thumbnail = src.read(1, out_shape=(1, int(src.height // oview), int(src.width // oview)))
    return thumbnail

def get_rgb_thumbnail(index):
    file_url = items[index].asset('B04')['href']
    r = get_thumbnail(file_url)
    file_url = items[index].asset('B03')['href']
    g = get_thumbnail(file_url)
    file_url = items[index].asset('B02')['href']
    b = get_thumbnail(file_url)
    rgb = np.dstack((r,g,b))
    rgb = (255*(rgb/np.max(rgb))).astype('uint8')
    return rgb

def get_bigraster(file_url):
    with rasterio.open(file_url) as src:
       bigraster = src.read(1, out_shape=(1, int(src.height), int(src.width)))
       profile = src.profile
    return bigraster, profile

def get_rgb_bigraster(index):
    file_url = items[index].asset('B04')['href']
    r, profile = get_bigraster(file_url)
    file_url = items[index].asset('B03')['href']
    g, gprofile = get_bigraster(file_url)
    file_url = items[index].asset('B02')['href']
    b, bprofile = get_bigraster(file_url)
    #rgb = np.dstack((r,g,b))
    #rgb = (255*(rgb/np.max(rgb))).astype('uint8')
    return r,g,b, profile, file_url

###===================================================
###=========== user inputs ======================

geojson_file = 'sandiego.geojson'
collection = 'sentinel-s2-l2a-cogs' #sentinel2 COGS
period = '2010-01-01/2020-12-31'
url = 'https://earth-search.aws.element84.com/v0'
# url = 'https://landsatlook.usgs.gov/stac-browser/collection02/level-2/standard/etm/'
###===================================================
gdf = gpd.read_file(geojson_file)
bounds = gdf.bounds
boundary = bounds.values.tolist()


search = Search(bbox=boundary[-1], datetime=period, collections=[collection], url=url)
print('bbox search: %s items' % search.found())

items = search.items()
print(items.summary(['date', 'id', 'eo:cloud_cover']))

print(items[0].assets.keys())

print(items[0].asset('visual'))

print(items[0].asset('visual')['href'])


# rb = get_rgb_thumbnail(9)
# plt.imshow(rgb)
# plt.colorbar()
# plt.show()
#
# print(rgb.shape)

index = 8

r,g,b, profile, file_url = get_rgb_bigraster(index)

print(r.shape)

profile['count']=1
profile['driver']='COG'
profile['compress']='lzw'

name = '_'.join(file_url.split('/')[-2:])

with rasterio.Env():
    with rasterio.open(name+'_R.tif', 'w', **profile) as dst:
        dst.write(np.expand_dims(r,axis=0))
    with rasterio.open(name+'_G.tif', 'w', **profile) as dst:
        dst.write(np.expand_dims(g,axis=0))
    with rasterio.open(name+'_B.tif', 'w', **profile) as dst:
        dst.write(np.expand_dims(b,axis=0))

cmd = 'gdal_merge.py -separate -o '+name+'_RGB.tif -co PHOTOMETRIC=MINISBLACK '+name+'_R.tif '+name+'_G.tif '+name+'_B.tif'
os.system(cmd)

# cmd = 'gdal_translate '+name+'_RGB.tif '+name+'_RGB_cog.tif -co TILED=YES -co COPY_SRC_OVERVIEWS=YES -co COMPRESS=LZW'
# os.system(cmd)

width, height = rgb.shape
tilesize=1024
file = name+'_RGB.tif'

for i in range(0, width, tilesize):
    for j in range(0, height, tilesize):
        window = rasterio.windows.Window(i,j,tilesize, tilesize)

        with rasterio.open(file) as src:
            profile = src.profile
            orig = src.read(window=window).squeeze()
        orig = orig.T
        orig = 255*(orig/np.max(orig))
        orig = orig.astype('uint8')
        plt.imshow(orig); plt.show()


#
# with open('sandiego.geojson') as f:
#     json_data = json.load(f)
#
# features = json_data['features']
#
# features[0]['geometry']
#
# search = Search(bbox=features[0]['geometry']['coordinates'], datetime=period, collections=[collection], url=url)
# print('bbox search: %s items' % search.found())

    #
    # coordinates = feature['geometry']['coordinates']
    # lng, lat = np.mean(coordinates[0], axis=0)
    # print((lng, lat))
    # area_sqkm = area(feature['geometry'])/1e6
    # #print(area_sqkm)
    #
    # collection = ee.ImageCollection(gee_collection)
    #
    # polygon = Polygon([tuple(c) for c in coordinates[0]])
    # minx, miny, maxx, maxy = polygon.bounds
    #
    # #nx, ny = 12,12 #4, 4  # number of columns and rows
    #
    # dx = (maxx - minx) / nx  # width of a small part
    # dy = (maxy - miny) / ny  # height of a small part
    # horizontal_splitters = [LineString([(minx, miny + i*dy), (maxx, miny + i*dy)]) for i in range(ny)]
    # vertical_splitters = [LineString([(minx + i*dx, miny), (minx + i*dx, maxy)]) for i in range(nx)]
    # splitters = horizontal_splitters + vertical_splitters
    #
    # result = polygon
    # for splitter in splitters:
    #     result = MultiPolygon(split(result, splitter))
    # parts = [list(part.exterior.coords) for part in result.geoms]

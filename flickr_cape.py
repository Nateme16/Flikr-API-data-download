# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 13:38:02 2015

@author: nmerri02
"""

##Python script to download Flikr data from API
##Author: Nate Merrill
##Started 11/9/2015

import flickrapi
import numpy

#logs into flikr API 
api_key = u'ce2f76d42f363d6199b9fa0d55b6869f'
api_secret = u'cf32baacaa9132e2'
flickr = flickrapi.FlickrAPI(api_key, api_secret,format='parsed-json')
woeid='12588700'

#get photos by woeid for Cape Cod
cape2=flickr.places.getInfo(woe_id=woeid) #gets place info
cape3=flickr.photos.search(woe_id=woeid) #gets info all photos taken on Cape


#this retreives location (woeid) of all photos on the cape after datemin
flickr = flickrapi.FlickrAPI(api_key, api_secret,format='etree') #has to be in etree format for some reason

datemin= '2015-11-01'
def pcape(datemin,woeid):
    results2=list()
    lat=list()
    lon=list()
    accur=list()
    for photo in flickr.walk(woe_id=woeid,min_taken_date=datemin, per_page=250, privacy_filter="1"):
        results2.append(photo.get('id'))
        loc=flickr.photos_geo_getLocation(photo_id=photo.get('id'))
        lat.append(loc[0][0].attrib['latitude'])
        lon.append(loc[0][0].attrib['longitude'])
        accur.append(loc[0][0].attrib['accuracy'])
        print photo
    return results2,lat,lon, accur
    
r2=pcape(datemin,woeid)
locmat=numpy.array(r2)


    



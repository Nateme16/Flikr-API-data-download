# -*- coding: utf-8 -*-
"""
Python script to download Flikr location data from API
Created on Mon Nov 16 13:38:02 2015

@author: nmerri02
"""
import flickrapi
import numpy
import pickle

#logs into flikr API 
api_key = u'ce2f76d42f363d6199b9fa0d55b6869f'
api_secret = u'cf32baacaa9132e2'
woeid='12588700' #got this through search, but the API search for flickr is clumsy, so its hardcoded

#this retreives location of all photos on the cape (woeid for Barnstable County) after datemin
flickr = flickrapi.FlickrAPI(api_key, api_secret,format='etree') #has to be in etree format for some reason
datemin= '2015-07-01' #minimum date 
datemax= '2015-08-01'

def pcape(datemin,woeid,datemax):
    results2=list()
    lat=list()
    lon=list()
    accur=list()
    for photo in flickr.walk(woe_id=woeid,min_taken_date=datemin, max_taken_date=datemax, per_page=250, privacy_filter="1"):
        results2.append(photo.get('id'))
        loc=flickr.photos_geo_getLocation(photo_id=photo.get('id'))
        lat.append(loc[0][0].attrib['latitude'])
        lon.append(loc[0][0].attrib['longitude'])
        accur.append(loc[0][0].attrib['accuracy'])
        
        #print photo
    return results2,lat,lon, accur
    
r2=pcape(datemin,woeid,datemax)
locmat=numpy.array(r2)

#this saves the data to a file
fileobject=open('locationdata','wb')
pickle.dump(r2,fileobject)
fileobject.close()

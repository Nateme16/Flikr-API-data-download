# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 13:38:02 2015

@author: nmerri02
"""

##Python script to download Flikr data from API
##Author: Nate Merrill
##Started 11/9/2015

import flickrapi
import pickle

#logs into flikr API 
api_key = u'ce2f76d42f363d6199b9fa0d55b6869f'
api_secret = u'cf32baacaa9132e2'
flickr = flickrapi.FlickrAPI(api_key, api_secret,format='parsed-json')
#sets format for return

#uses API functions
photos = flickr.photos.search(user_id='73509078@N00', per_page='100',has_geo='1') #searches for 1 user

photos['photos']['photo'][1]['id']

photo2=photos['photos']['photo'] 

#function for getting id list of photos that met API query
def plist(photo2):
	results=list()
	for i in photo2:
		results.append(i['id'])
	return results

r=plist(photo2)
                        
print r

#get photos by woeid for Cape Cod

capewo=flickr.places.find(query='Barnstable') #gets id for the Cape
cape2=flickr.places.getInfo(woe_id='12588700') #gets place info
cape3=flickr.photos.search(woe_id='12588700') #gets info all photos taken on Cape

#flickr = flickrapi.FlickrAPI(api_key, api_secret,format='etree')

#this retreives all photos on the cape after datemin
flickr = flickrapi.FlickrAPI(api_key, api_secret,format='etree') #has to be in etree format for some reason

datemin= '2015-11-10'
def pcape(datemin):
    results2=list()
    lat=list()
    lon=list()
    accur=list()
    for photo in flickr.walk(woe_id='12588700',min_taken_date=datemin, per_page=250, privacy_filter="1"):
        results2.append(photo.get('id'))
        loc=flickr.photos_geo_getLocation(photo_id=photo.get('id'))
        lat.append(loc[0][0].attrib['latitude'])
        lon.append(loc[0][0].attrib['longitude'])
        accur.append(loc[0][0].attrib['accuracy'])
    return results2,lat,lon, accur

r2=pcape(datemin)

#This saves it to a file to be opened later
fileobject=open('locationdata','wb')
pickle.dump(r2,fileobject)
fileobject.close()




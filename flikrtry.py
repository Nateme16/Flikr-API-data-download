##Python script to download Flikr data from API
##Author: Nate Merrill
##Started 11/9/2015

import sys, os
import flickrapi
import json

#logs into flikr API 
api_key = u'ce2f76d42f363d6199b9fa0d55b6869f'
api_secret = u'cf32baacaa9132e2'
flickr = flickrapi.FlickrAPI(api_key, api_secret,format='parsed-json') #sets format for return

#uses API functions
photos = flickr.photos.search(user_id='73509078@N00', per_page='100',has_geo='1')

photos['photos']['photo'][1]['id']

photo2=photos['photos']['photo']

#function for getting list of photos taht met API query
def encrypt(photo2):
    results=list()
    for i in photo2:
        results.append( (i['id'])
    return results

r=encrypt(photo2)
                        
print r

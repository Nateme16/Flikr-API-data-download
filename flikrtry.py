#Python script to download Flikr data from API
#Author: Nate Merrill
#Started 11/9/2015

import sys, os
import flickrapi

api_key = u'ce2f76d42f363d6199b9fa0d55b6869f'
api_secret = u'cf32baacaa9132e2'

flickr = flickrapi.FlickrAPI(api_key, api_secret)
photos = flickr.photos.search(user_id='73509078@N00', per_page='100',has_geo='1')

for child in photos.iter():
    print child.tag, child.attrib
    

photocheck=flickr.photos.getInfo(photo_id='8560608555')

# -*- coding: utf-8 -*-
"""
Python script to create point shapefile from locations in 'locationdata'

Created on Wed Nov 18 16:42:16 2015

@author: nmerri02
"""

import pickle
import arcpy
import numpy

#opens file with the lat/lon and data from flickr_cape.py
fileObject = open('locationdata','r')
b=pickle.load(fileObject) 

#creates point geometry with lat/lon
pts=numpy.array(b).T
pt=arcpy.Point()
ptGeoms=[]
for i in range(len(pts)):
    print pts[i,1]
    print pts[i,2]
    pt.Y=pts[i,1]
    pt.X=pts[i,2]
    ptGeoms.append(arcpy.PointGeometry(pt))
    
#saves the data as a shapfile with points
sr = arcpy.SpatialReference(4269) #this is the code for the projection
arcpy.CopyFeatures_management(ptGeoms, r"C:\Users\nmerri02\Desktop\test2\test2.shp")
arcpy.DefineProjection_management(r"C:\Users\nmerri02\Desktop\test2\test2.shp", sr)


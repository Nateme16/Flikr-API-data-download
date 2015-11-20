# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 16:42:16 2015

@author: nmerri02
"""
#This creates point shapefile from locations in 'locationdata'
import pickle
import arcpy
import numpy

fileObject = open('locationdata','r')

b=pickle.load(fileObject) 

ptList1=map(float,b[1])
ptList2=map(float,b[2])
c=[ptList1,ptList2]

pt=arcpy.Point()
ptloc= []

for r in e.T:
    print c[r]
    pt.X= r
    ptloc.append(arcpy.PointGeometry(pt))

        
        
#saves it to a file "test"
arcpy.CopyFeatures_management(ptloc, r"C:\Users\nmerri02\Desktop\test.shp")
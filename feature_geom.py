from urllib.request import urlopen
from shapely.geometry import LineString,Point, shape
import math
        


class VFeature:
    """
    Create a VFeature class for a geometry feature object
    Parameter
    ----------
    feature (geometry dict)
   {
          'type': [geometry_type],
          'coordinates': [
            [
              lon,
              lat
            ],
            [
              lon,
              lat
            ],
            [
              lon,
              lat
            ]
          ]
    }
    Where : 
        [geometry_type] - geometry type : LineString/MultiLineString/MultiPolygon
        [lon, lat] - corresponding longitude and latitude coordinates
    """
    def __init__(self, feature):
        #Init VFeature with a geometry dict : 
        # e.g {'type':'LineString', 'geometry':{'type':'LineString', 'coordinates':[]}}
        self.feature = feature
        self.shape = shape(self.feature)

    @property
    def feature(self):
        """Return feature"""
        return self._feature
    
    @feature.setter
    def feature(self, feature):
        """Set feature. """
        if 'type' not in feature or 'coordinates' not in feature:
            raise ValueError('Initial feature must be a geometry dict with a type and geometry ')
        self._feature = feature
    
    def __repr__(self):
        """Return VFeature string for repr()"""
        feature_type = self.feature['type']
        coordinates = self.feature['coordinates']
        return (f'Feature.type = {feature_type}, coordinates = {coordinates}')
    def __str__(self):
        """Return VFeature string for print() method"""
        feature_type = self.feature['type']
        coordinates = self.feature['coordinates']
        return (f'Feature.type = {feature_type}, coordinates = {coordinates}')
        
    def mid_point(self):
        # call _points_along_line with a fration = 0.5 to get the midpoint
        return self._points_along_line(0.5)[0]
    
    def _points_along_line(self, a_fraction):
        """
        Private function to return a point list along line base on a_fraction
        Parameter
        ----------
        a_fraction = a fraction of the geometric object length, value from 0 to 1
        
        Return 
        ---------
        point_list : list of the points along line exclude begin and end point
        
        """
        point_list = []
        if self.shape.geom_type =='LineString':
            # Handle cases divide by 0 and fraction >1
            if a_fraction <=0 or a_fraction>=1:
                return point_list
            #Calculate number points along line from a fraction
            num_point = int(math.ceil(1 / a_fraction))
            #using Shapely interpolate with normalized = true to build a Points list
            # exclude start point and end points (0 and n )          
            points = [self.shape.interpolate(a_fraction*n, normalized=True) for n in range(1,num_point)]
            for point in points:
                x,y = point.xy
                xy = [x[0],y[0]]
                point_list.append(xy)
            return point_list
            
        # raise exception for other type of geometry
        else:
            raise ValueError('Geometry type unhandled' )        


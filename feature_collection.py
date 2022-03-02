#feature_collection.py
from feature_geom import VFeature


class VFeaturesCollection:
    """
    Create a VFeatureCollection for featurecollections jsonobject
    Parameter
    ----------
    feature_collection (feature collection dict)

    {
    'type': 'FeatureCollection',
    'features': [
      
      {
        'type': 'Feature',
        'properties': {},
        'geometry': {
          'type': 'LineString',
          'coordinates': [
            [
              -87.66531944274902,
              41.82314153997187
            ],
            [
              -87.66583442687988,
              41.837659178457336
            ],
            [
              -87.72359848022461,
              41.80247860815289
            ]
          ]
        }
      }
    ]
  }

    """
    def __init__(self, feature_collection):
        """Initialize feature Collection"""
        self.feature_collection = feature_collection
        self._vfeature_list = []
        # Initialize _feature_list
        for feature in self.feature_collection['features']:
            v_feature = VFeature(feature['geometry'])
            self._vfeature_list.append(v_feature)


    @property
    def feature_collection(self):
        return self._feature_collection
    
    @feature_collection.setter
    def feature_collection(self, feature_collection):
        """Set feature collection """
        if 'type' not in feature_collection or 'features' not in feature_collection:
            raise ValueError('Initial features collection must be a featurecollection dict type = featurecollection  and a list of features')
        self._feature_collection = feature_collection

    def mid_points(self):
        # return a list of mid points of lineString collections
        midpoints = []
        for vfeature in self._vfeature_list:
            mid_point = vfeature.mid_point()
            midpoints.append(list(mid_point))
        return midpoints

    def __str__(self):
        """Return a string of feature collection"""
        feature_collection_type = self.feature_collection['type']
        features = self.feature_collection['features']
        return (f'FeatureCollection.type = {feature_collection_type}, features = {features}')





import argparse
from enum import Enum
from app_arguments import ArgParser
from feature_collection import VFeaturesCollection
from utils import *


class SourceType(Enum):
    FILE = 0
    HTTP = 1

def _get_source_type(source):
    pos = source.find('://')
    if source[:pos] == 'http' or source[:pos] == 'https' :
        source_type = SourceType.HTTP
    else:
        source_type = SourceType.FILE
    return source_type


if __name__ == "__main__":
    parser = ArgParser(formatter_class=argparse.RawTextHelpFormatter,
                      description='Perform midpoint(s) of a LineString feature collections \n'
                                  'return list midpoints  coords= [[lon,lat], [lon, lat]]\n')
    parser.add_argument('--source', type=str, required=True,
                        help='Path to the source local file system or from an url json data.\n'
                             'Examples:\n'
                             '  sample.json \n'
                             '  https://gitlab.com/florin.alexandrescu/interview-json/-/raw/main/chicago.json')

    opt = parser.parse_args()
    source_type = _get_source_type(opt.source)
    json_data = {}
    mid_points = []
    if source_type == SourceType.FILE:
        json_data = read_json_file(opt.source)
    else:
        json_data = read_json_url(opt.source)
    
    feature_collection = VFeaturesCollection(json_data)
    mid_points = feature_collection.mid_points()
    print(f'list of mid_point(s) : {mid_points}')


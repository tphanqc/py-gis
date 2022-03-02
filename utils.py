import json
from urllib.request import urlopen


def read_json_file(file_path):
    """
    :param file_path:absolute_path
    """
    with open(file_path, 'r') as f:
        json_data = json.load(f)
        return json_data
       
def read_json_url(url):
    """
    :param url: source  
       e.g https://gitlab.com/florin.alexandrescu/interview-json/-/raw/main/chicago.json
    """
    try:
        # get the response from opening a URL
        response = urlopen(url) 
        # read JSON response in string and load into a dict 
        data_json = json.loads(response.read())
        return data_json
    except IOError:
        # IOError handler 
        print('Faile to open URL')        

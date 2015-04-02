# -*- coding: utf-8 -*-
"""
Titel: geocoder
Purpose: Request and fetch geocoding data from Mapquest's Open Geocoding Service
Author: Thomas Treml (datadonk23@gmail.com)
Date: September 2014
"""

import os, sys
import requests
import json

def geocodeMQ(req_location):
    """ Return Lat and Long of requested location by parsing MapQuest Open
        Geocoding API. Data based OpenStreetMaps.
        
        Parameter -
        req_location: location query (str)
    """
    
    try:
        os.environ["MAPQUEST_API_KEY"]
    except:
        print("Missing API KEY. Set MAPQUEST_API_KEY in environ. variables")
        sys.exit(1)

    # request parameters
    req_loc = req_location    
    key = os.environ.get("MAPQUEST_API_KEY")
    api = "http://open.mapquestapi.com/geocoding/v1/address?key="
    format_req = "&inFormat=kvp" # change if necessary
    format_out = "&outFormat=json" # change if necessary
    loc = "&location=" + req_loc 
    max_results = "&maxResults=1" # change if necessary

    # request to MapQuest
    req_url = api + key + format_req + format_out + loc + max_results
    req = requests.get(req_url)
    raw_data = json.loads(req.text)['results']
    
    # extract lat and long
    geo_location = (raw_data[0]["locations"][0]["latLng"]["lat"],
                    raw_data[0]["locations"][0]["latLng"]["lng"])
                    
    return geo_location

#!/usr/bin/env python3

"""Returning the location of the ISS in latitude/longitude"""

import requests
import datetime
import reverse_geocoder as rg

URL= "http://api.open-notify.org/iss-now.json"

def main():

    resp = requests.get(URL).json()
    
    lon = resp["iss_position"]["longitude"]
    lat = resp["iss_position"]["latitude"]
    timestamp = resp["timestamp"]
    timestamp = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    coords_tuple = (lat, lon)
    results = rg.search(coords_tuple)
    city = results[0]["name"]
    country = results[0]["cc"]

    print(f"Current location of the ISS:\nTimestamp: {timestamp}\nLon: {lon}\nLat: {lat}\nCity/Country: {city}, {country}")


if __name__ == "__main__":
    main()

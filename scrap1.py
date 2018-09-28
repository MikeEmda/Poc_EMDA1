from urllib import urlopen
from bs4 import BeautifulSoup
import re
open('output-2018.csv', 'w').close()
open('headlines.txt', 'w').close()
g= open("headlines.txt","a+")
source  = urlopen('http://www.standard.co.uk/news/crime/rss').read()
#print source
title = re.compile('<title>(.*)</title>')
link = re.compile('<link>(.*)</link>')
description = re.compile('<description>(.*)</description>')
pubDate = re.compile('<pubDate>(.*)</pubDate>')
find_title = re.findall(title, source)
find_link = re.findall(link, source)
find_description = re.findall(description, source)
find_pubDate = re.findall(pubDate, source)
find_title.pop(0)
find_link.pop(0)
find_description.pop(0)
for f in range(len(find_title)):
    print find_title[f]
    s = str(find_title[f]).replace("&amp;apos;", "'")
    g.write(str(s)+"\n")
    print find_link[f]
    print find_description[f]
    print find_pubDate[f]
    print

source  = urlopen('http://www.independent.co.uk/news/uk/rss').read()
#print source
title = re.compile('<title>(.*)</title>')
link = re.compile('<link>(.*)</link>')
description = re.compile('<description>(.*)</description>')
pubDate = re.compile('<pubDate>(.*)</pubDate>')
find_title = re.findall(title, source)
find_link = re.findall(link, source)
find_description = re.findall(description, source)
find_pubDate = re.findall(pubDate, source)
find_title.pop(0)
find_link.pop(0)
find_description.pop(0)
for f in range(len(find_title)):
    print find_title[f]
    s = str(find_title[f]).replace("&amp;apos;", "'")
    g.write(str(s)+"\n")
    print find_link[f]
    print find_description[f]
    print find_pubDate[f]
    print
g.close()

'''
source  = urlopen('http://feeds.bbci.co.uk/news/uk/rss.xml?edition=uk').read()
#print source
title = re.compile('<title>(.*)</title>')
link = re.compile('<link>(.*)</link>')
description = re.compile('<description>(.*)</description>')
pubDate = re.compile('<pubDate>(.*)</pubDate>')
find_title = re.findall(title, source)
find_link = re.findall(link, source)
find_description = re.findall(description, source)
find_pubDate = re.findall(pubDate, source)
find_title.pop(0)
find_title.pop(0)
find_link.pop(0)
find_link.pop(0)
find_description.pop(0)
for f in range(len(find_title)):
    print find_title[f]
    g.write(str(find_title[f])+"\n")
    print find_link[f]
    print find_description[f]
    print find_pubDate[f]
    print
'''

l1 = ['Attack',
'Attacked',
'Attacks',
'Violent',
'Assault',
'Fight',
'Incident',
'Sudden',
'Beaten',
'Assaulted',
'Assault'
]
l5 = [
'Terror',
'Terrorist',
'Suicide bomber',
'Isis',
'IED',
'Vehicle Ramming',
'Lone Wolf',
'Suicide Bomber',
'Acid Attack',
'Explosive Device',
'Terrorism'
]
l9 = [
'Disaster',
'Fire',
'Earthquake',
'Tornado',
'Flood',
'Hurricane',
'Collapsed Building',
'Trapped',
'Collapsed'
]
l2 = [
'Protest',
'Protesting', 
'Protests',
'Demonstration',
'Revolt'
]
l6 = [
'Robbery',
'Robbing',
'Rob',
'Robberies',
'Robbed',
'Theft',
'Stolen',
'Burglar',
'Burglary'
]
l10 = [
'Crash',
'Accident',
'Emergency',
'Disaster',
'Hazard',
'Mishap'
]
l3 = [
'Stab',
'Stabbed',
'Stabbing',
'Knifed',
'Knife',
'Knives'
]
l7 = [
'Explosion',
'Exploded',
'Explode',
'Bomb',
'Bombing', 
'Bomber'
]
l11 = [
'murder',
'Deadly',
'Massacre',
'Execution',
'Homicide',
'slaughter'
]
l4 = [
'Shoot',
'Shot',
'Shooting',
'Active Shooter',
'Gunmen',
'Gunman'
]
l8 = [
'Rape',
'Raped',
'Raping'
]
l12 = [
'Heart Attack',
'MVA',
'CVA',
'Cardiac arrest',
'Wounded',
'Chest wound',
'Medical Emergency'
]

f=open("headlines.txt", "r")
if f.mode == 'r':
    contents =f.read()
f.close()
f=open("streetnames.txt", "r")
if f.mode == 'r':
    streets =f.read()
f.close()
streets = streets.split('\r\n')
#print streets
contents = [s.strip() for s in contents.splitlines()]
addresses = []
for s in contents:

    print str(s)
    check = 0
    m = str(s)
    #print type(k)
    #print len(k)
    m = m.split()
    m = map(lambda x: x.lower(), m)
    for i in range(len(m)):
        m[i] = re.sub('[^A-Za-z0-9]+', '', m[i])
    print m
    c = 0
    tt = 0
    for k in l1:
        if k.lower() in m and check == 0:
            print "Icon : icon 1 " + str(k)
            tt = 1
            check = 1
    for k in l2:
        if k.lower() in m and check == 0:
            print "Icon : icon 2 " + str(k)
            tt = 1
            check = 1
    for k in l3:
        if k.lower() in m and check == 0:
            print "Icon : icon 3 " + str(k)
            tt = 1
            check = 1
    for k in l4:
        if k.lower() in m and check == 0:
            print "Icon : icon 4 " + str(k)
            tt = 1
            check = 1
    for k in l5:
        if k.lower() in m and check == 0:
            print "Icon : icon 5 " + str(k)
            tt = 1
            check = 1
    for k in l6:
        if k.lower() in m and check == 0:
            print "Icon : icon 6 " + str(k)
            tt = 1
            check = 1
    for k in l7:
        if k.lower() in m and check == 0:
            print "Icon : icon 7 " + str(k)
            tt = 1
            check = 1
    for k in l8:
        if k.lower() in m and check == 0:
            print "Icon : icon 8 " + str(k)
            tt = 1
            check = 1
    for k in l9:
        if k.lower() in m and check == 0:
            print "Icon : icon 9 " + str(k)
            tt = 1
            check = 1
    for k in l10:
        if k.lower() in m and check == 0:
            print "Icon : icon 10 " + str(k)
            tt = 1
            check = 1
    for k in l11:
        if k.lower() in m and check == 0:
            print "Icon : icon 11 " + str(k)
            tt = 1
            check = 1
    for k in l12:
        if k.lower() in m and check == 0:
            print "Icon : icon 12 " + str(k)
            tt = 1
            check = 1
    if tt == 1:
        for k in streets:
            if k.lower() in m:
                print "Location : "+str(k) + " Street"
                addresses.append(str(k)+ " Street, London")
                c = 1

    if c==0 and tt == 1:
        print "Location : Not Detected"
        
    print
    print


import pandas as pd
import requests
import logging
import time

logger = logging.getLogger("root")
logger.setLevel(logging.DEBUG)
# create console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)

API_KEY = 'AIzaSyDcQlwTnrKhgtV5CJ2g21EKdOv_JgqbgpY'

BACKOFF_TIME = 30

output_filename = 'output-2018.csv'

address_column_name = "Address"

RETURN_FULL_RESULTS = False




#------------------ FUNCTION DEFINITIONS ------------------------

def get_google_results(address, api_key=None, return_full_response=False):

    geocode_url = "https://maps.googleapis.com/maps/api/geocode/json?address={}".format(address)
    if api_key is not None:
        geocode_url = geocode_url + "&key={}".format(api_key)
        
    # Ping google for the reuslts:
    results = requests.get(geocode_url)
    # Results will be in JSON format - convert to dict using requests functionality
    results = results.json()
    
    # if there's no results or an error, return empty results.
    if len(results['results']) == 0:
        output = {
            "formatted_address" : None,
            "latitude": None,
            "longitude": None,
            "accuracy": None,
            "google_place_id": None,
            "type": None,
            "postcode": None
        }
    else:    
        answer = results['results'][0]
        output = {
            "formatted_address" : answer.get('formatted_address'),
            "latitude": answer.get('geometry').get('location').get('lat'),
            "longitude": answer.get('geometry').get('location').get('lng'),
            "accuracy": answer.get('geometry').get('location_type'),
            "google_place_id": answer.get("place_id"),
            "type": ",".join(answer.get('types')),
            "postcode": ",".join([x['long_name'] for x in answer.get('address_components') 
                                  if 'postal_code' in x.get('types')])
        }
        
    # Append some other details:    
    output['input_string'] = address
    output['number_of_results'] = len(results['results'])
    output['status'] = results.get('status')
    if return_full_response is True:
        output['response'] = results
    
    return output



# Ensure, before we start, that the API key is ok/valid, and internet access is ok
test_result = get_google_results("London, England", API_KEY, RETURN_FULL_RESULTS)
if (test_result['status'] != 'OK') or (test_result['formatted_address'] != 'London, UK'):
    logger.warning("There was an error when testing the Google Geocoder.")
    raise ConnectionError('Problem with test results from Google Geocode - check your API key and internet connection.')

# Create a list to hold results
results = []
# Go through each address in turn
for address in addresses:
    # While the address geocoding is not finished:
    geocoded = False
    while geocoded is not True:
        # Geocode the address with google
        try:
            geocode_result = get_google_results(address, API_KEY, return_full_response=RETURN_FULL_RESULTS)
        except Exception as e:
            logger.exception(e)
            logger.error("Major error with {}".format(address))
            logger.error("Skipping!")
            geocoded = True
            
        # If we're over the API limit, backoff for a while and try again later.
        if geocode_result['status'] == 'OVER_QUERY_LIMIT':
            logger.info("Hit Query Limit! Backing off for a bit.")
            time.sleep(BACKOFF_TIME * 60) # sleep for 30 minutes
            geocoded = False
        else:
            # If we're ok with API use, save the results
            # Note that the results might be empty / non-ok - log this
            if geocode_result['status'] != 'OK':
                logger.warning("Error geocoding {}: {}".format(address, geocode_result['status']))
            logger.debug("Geocoded: {}: {}".format(address, geocode_result['status']))
            results.append(geocode_result)           
            geocoded = True

    # Print status every 100 addresses
    if len(results) % 100 == 0:
        logger.info("Completed {} of {} address".format(len(results), len(addresses)))
            
    # Every 500 addresses, save progress to file(in case of a failure so you have something!)
    if len(results) % 500 == 0:
        pd.DataFrame(results).to_csv("{}_bak".format(output_filename))

# All done
logger.info("Finished geocoding all addresses")
# Write the full results to csv using the pandas library.
pd.DataFrame(results).to_csv(output_filename, encoding='utf8')
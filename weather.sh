#!/bin/sh

# This is a simple script that downloads current weather conditions and zone
# forecast from the National Weather Service and displays them.
# 
# This script is preconfigured for the Newark, NJ area.
# It is biased toward the US, as it gets its data from the NWS.
# 
# To change the observations site, replace KTUL with another observations site.
# See <http://weather.noaa.gov/pub/data/observations/metar/decoded/> for a list.
# For the bare, unparsed METAR, replace "decoded" in the URI with "stations".
# 
# To change the forecast zone, replace nj/njz003 with another forecast zone.
# See <http://weather.noaa.gov/pub/data/forecasts/zone/> for a list.

echo "********** CURRENT CONDITIONS **********"
wget -q -O- http://weather.noaa.gov/pub/data/observations/metar/decoded/KEWR.TXT
echo
echo "********** NWS ZONE FORECAST **********"
wget -q -O- http://weather.noaa.gov/pub/data/forecasts/zone/nj/njz003.txt

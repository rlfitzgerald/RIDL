import requests
## script
"""1. Alexa, load a map of {long beach}
2a. Alexa show me the port area
2b. Alexa show me an outline of the port of long beach
2c. Alexa show me the port of long beach
3.  Alexa what dataset do you have for this area
3. Alexa overlay data for marine radar.
	R.  For what dates
	R.  From Feb 10-Feb 13 2014
4. Alexa whats AIS"""

requests.get("http://localhost:5000/maps/33.74,-118.23") 
 
 

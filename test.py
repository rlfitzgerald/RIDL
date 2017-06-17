import requests

## question 1
proxies = {
  'http': 'http://28435:Sunday@proxy-west.aero.org:8080/',
  'https': 'https://28435:Sunday@proxy-west.aero.org:8080/',
}
def q1():
	lb_map = "http://localhost:5000/map/33.74,-118.23"
	x = requests.get(lb_map,proxies=proxies)
	print x	
print q1() 

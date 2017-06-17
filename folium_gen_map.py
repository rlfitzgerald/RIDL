import folium
import pdb
def _gen_map(lat,lon,markers,geojson,filename="default.html"):
	map_osm = folium.Map(location=[lat,lon])
	if geojson != None:
		G=folium.GeoJson(open(geojson))
		G.add_to(map_osm) 
	if markers != None:
		pass		
	map_osm.save(filename)
	return map_osm,filename


def mmap(lat,lon,geojson=None):
	map_file,filename=_gen_map(lat,lon,markers=None,geojson=geojson)
	f = " ".join(open(filename).readlines())
	print f	
	return f	
#	div,script=get_div_script(map_file)
#	div_string = str(div)	
#	script_string = str(script)	
#	return  div_string+script_string
def test():
	lat=33.734
	lon=-118.2373
	maps = mmap(lat,lon,geojson="/tmp/x.geojson")
	print maps

#test()

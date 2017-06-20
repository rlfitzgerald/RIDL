from bs4 import BeautifulSoup as bs


inputFileName = "ais.html"

ais_page = open(str(inputFileName), 'r')

soup = bs(ais_page, 'html.parser')
table = soup.find_all('td')
tableSoup = bs(str(table), 'html.parser')
tableLinks = tableSoup.find_all('a')

tableRef = []
for link in tableLinks:
    ref = link.get('href')
    if "center" in ref:
        tableRef.append(ref)
    
coordinates = []

#import pdb; pdb.set_trace()
for ref in tableRef:
    refParts = ref.split('/')
    x = 0
    y = 0
    for part in refParts:
        if "centerx" in part:
            xpart = part.split(':')
            x = float(xpart[1])
            print "x: " + str(x)
        if "centery" in part:
            ypart = part.split(':')
            y = float(ypart[1])
            print "y: " + str(y)
        if (x is not 0) and (y is not 0):
            coordinates.append([x, y])
            x = 0
            y = 0

print "coordinates:"
print coordinates 

import urllib2
from bs4 import BeautifulSoup


# hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
#        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#        'Accept-Encoding': 'none',
#        'Accept-Language': 'en-US,en;q=0.8',
#        'Connection': 'keep-alive'}

hdr2 = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

def rottenTomatoes():
    site = "http://www.rottentomatoes.com/movie/box-office/"
    req = urllib2.Request(site, headers=hdr2) 
    try:
        page = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print e.fp.read()
    
    content = page.read()
    soup = BeautifulSoup(content)
    # target="_top"
    results = soup.findAll("a", {"target" : "_top", "class" : "", "data-ga-event" : "", "title" : ""})
    # results_utf = [x.encode('utf-8') for x in results]
    boxOfficeList = []
    
    for result in results:
        # print result.text
        boxOfficeList.append(str(result.text))
    
    return boxOfficeList


def imdb():
    site = "http://www.imdb.com/chart/?ref_=hm_cht_sm"
    req = urllib2.Request(site, headers=hdr2) 
    try:
        page = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print e.fp.read()
    
    content = page.read()
    soup = BeautifulSoup(content)
    # target="_top"
    results = soup.findAll("td", {"class" : "titleColumn"})
    
    # results_utf = [x.encode('utf-8') for x in results]
    boxOfficeList = []
    
    for result in results:
        movie = result.find("a")
        boxOfficeList.append(str(movie.text))
    
    return boxOfficeList


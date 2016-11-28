from HTMLParser import HTMLParser
import urllib2

class CHTMLParser(HTMLParser):
    def __init__(self):
	HTMLParser.__init__(self)
	self.artefacts = []

    def handle_starttag(self, tag, attrs):
	if tag=='a' and "href" in attrs[0] and "NEWHM" in attrs[0][1]:
	    self.artefacts.append(attrs[0][1])

def getUrlOfArtefactImages():    
    # Get html
    req = urllib2.Request('http://homepages.cs.ncl.ac.uk/matthew.forshaw/teaching/csc8622/cswk/images/')
    res = urllib2.urlopen(req)
    html = res.read()
    # instantiate the parser and fed it some HTML
    parser = CHTMLParser()
    parser.feed(html)
    return parser.artefacts

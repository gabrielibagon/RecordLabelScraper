from bs4 import BeautifulSoup
import urllib2
import csv

Base_URL = "https://www.cc-seas.columbia.edu/wkcr/playlist"
labels={}

def getPageLinks(page):
	for i in range(64):
		link = "https://www.cc-seas.columbia.edu/wkcr/playlist?page=" + str(i)
		getProgramLinks(link)


# this method gets all of the links to the program playlists present on 
# one page of the playlists tab
def getProgramLinks(playLists_url):
	html = urllib2.urlopen(playLists_url).read() #opens the URL
	soup = BeautifulSoup(html, "lxml") #creates a soup object, parses with lxml
	tbody = soup.findAll('tbody')
	for a in tbody:
		programLinks = a.findAll('a')
	for link in programLinks:
		print "https://www.cc-seas.columbia.edu/" + link.get('href')
		getLabel("https://www.cc-seas.columbia.edu/" + link.get('href'))
	#getLabel("https://www.cc-seas.columbia.edu/wkcr/program/tennessee-border-show/tennessee-border-show-playlist-01242016")

def getLabel(programURL):
	html = urllib2.urlopen(programURL).read() #opens the URL
	soup = BeautifulSoup(html, "lxml") #creates a soup object, parses with lxml
	tbody = soup.findAll('tbody') 
	#go through all of the record labels in one program
	for label in soup.findAll('td',{'class':'views-field views-field-label'}):
		if len(''.join(label.findAll(text=True)))>2:
			recordLabel = ''.join(label.findAll(text=True)).strip().encode('UTF-8')
		else:
			recordLabel = None
		# else:
		# 	album = soup.findPreviousSibling(label)
		# 	print album
		# 	recordLabel = searchInformation(album)
		
		#add to map of labels
		if not labels.get(recordLabel):
			labels[recordLabel] = 1;
		else:
			labels[recordLabel] = labels[recordLabel]+1

def printResult():
	for label in labels:
		print label, labels[label]

def output():
	writer = csv.writer(open('playlists.csv','wb'))
	for key,value in labels.items():
		writer.writerow([key,value])

def searchInformation(album):
	#TODO: search the album information online for potential record label
	print "hello"


getPageLinks(Base_URL)
output()


import urllib2
import urllib
import os
import csv
from time import sleep
import random



# def append_new_row(filepath, text):
#     with open(filepath, 'a') as f:
#         mycsv = csv.writer(f, delimiter=',', lineterminator='\n')
#         mycsv.writerow(text)





### the class Serp
###    it is about a single Serp (10 results for a query)
###    as input it has the url (http://www.google.de/search?hl=de&q=kontaktlinsen)
###    as instance variable has url, html, http_header_response, links
###	   as functions:
###		 - htmlcrawler, just get the html and send it to the self.html variable
###      - findlinks, send the links to self.links
###		 - show, write the links on the console & on a csv - for testing
###		 - shooter, for testing, it shoot all those functions

###	to do:
###		adding SEM links, adding shopping, images
### IMPORTANT:
### I NEED TO LAUNCH THE HTML CRAWLER JUST ONCE PER QUERY. IT IS LAUNCHED ON __INIT__


class Serp:

	def __init__ (self, url):
		self.html = ''
		self.http_header_response = ''
		self.url = url
		self.links = []
		self.htmlcrawler()


	def htmlcrawler (self):

		# I NEED TO LAUNCH THE HTML CRAWLER JUST ONCE PER QUERY. IT IS LAUNCHED ON __INIT__
		#print self.url
			
		# create a random sleep time between 0.5 secs and 1.5
		randomfloat = random.uniform(0.5, 1.5)
		sleep(randomfloat)
			
		request = urllib2.Request(self.url)
		request.add_header("User-Agent", "My Python Crawler")
		opener = urllib2.build_opener()
		response = opener.open(request)
		self.html = response.read()
		self.http_header_response = response.info()


	def findlinks (self):

	

		# splitting the html code in order to get the clean links
		
		links = self.html.split('<li class="g">')

		for link in links[1:]:
			subitem = link.split('<a href="')
			subsubitem = subitem[1].split('&amp')

		
		# cleaning the response, changing weird urls for utf8

			s = subsubitem[0].replace('/url?q=', '')
			s = urllib.unquote(s).decode('utf8')

		# sending the links to the list self.links	
			self.links.append(s)

	def returnRanking (self, website):

		if self.findlinks() == []:
			self.findlinks()

		i = 1
		for link in self.links:

			if website in link:

				ranking = i

				return ranking

				break

			i = i + 1
	
		
	
	def returnLandingPage(self, website):
		
		if self.findlinks() == []:
			self.findlinks()

		for link in self.links:

			if website in link:

				return link

				break

	def returnLinks(self):

		if self.findlinks() == []:
			self.findlinks()

		print self.links
		return links



# a = Serp('http://www.google.de/search?hl=de&q=kontaktlinsen')	
# a.returnRanking('misterspex')
#crawlurl('http://www.google.de/search?hl=de&q=kontaktlinsen')
#print html




				









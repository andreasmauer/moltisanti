#function that crawls a sitemap and create html files with it
#next step is to crawl the next pages

import urllib2
import urllib
import os
import csv
from time import sleep
import random



def append_new_row(filepath, text):
    with open(filepath, 'a') as f:
        mycsv = csv.writer(f, delimiter=',', lineterminator='\n')
        mycsv.writerow(text)





#import httplib


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
###		

class Serp:

	def __init__ (self, url):
		self.html = ''
		self.http_header_response = ''
		self.url = url
		self.links = []

	def htmlcrawler (self):

		# #open the sitemap file
		# f = open(sitemap, 'r+')
		# lines = f.readlines()


		# #read line to line of the sitemap
		# for item in lines:
		
		print self.url
			
		# create a random sleep time between 0.5 secs and 1.5
		randomfloat = random.uniform(0.5, 1.5)
		sleep(randomfloat)
			
		request = urllib2.Request(self.url)
		request.add_header("User-Agent", "My Python Crawler")
		opener = urllib2.build_opener()
		response = opener.open(request)
		self.html = response.read()
		self.http_header_response = response.info()



		# print self.html


		# print self.http_header_response





	def findlinks (self):

		# self.htmlcrawler()
		links = self.html.split('<li class="g">')

		for link in links[1:]:
			subitem = link.split('<a href="')
			

			
			subsubitem = subitem[1].split('&amp')

			#trying to decode the amazon url from utf-8 but didnt work out
			# h = HTMLParser.HTMLParser()




			s = subsubitem[0].replace('/url?q=', '')
			# print h.unescape(s)
			# sencoded = urllib.urlencode(s)

			s = urllib.unquote(s).decode('utf8')
			self.links.append(s)

			
		# for link in links[1:]:
		# 	print link
		# 	print '--------------------------'

	def show (self):

		print self.links

		for element in self.links:
			with open('test.csv', 'a') as f:
				f.write(element)
				f.write('\n')
				f.close()





	def shooter (self):
		self.htmlcrawler()
		self.findlinks()
		self.show()



a = Serp('http://www.google.de/search?hl=de&q=kontaktlinsen')	
a.shooter()
#crawlurl('http://www.google.de/search?hl=de&q=kontaktlinsen')
#print html




				









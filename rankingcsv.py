import os
import csv
import serp
import urllib



class Ranking_csv:

	def __init__ (self):

		self.website = ''
		self.url = ''
		self.website_with_ranking = []
		#open the sitemap file
		self.url = raw_input('define the google url (http://www.google.de/search?hl=de&q=):' )
		if self.url == '':
			self.url = 'http://www.google.de/search?hl=de&q='

		
		self.website = raw_input('define the website to check the rankings:')
		if self.website == '':
			print "a website needs to be included"
			sys.exit()

		self.write_rankings()






	
	def write_rankings(self):

		f = open('list_of_keywords.txt', "r+")
		lines = f.readlines()
		
		for keyword in lines:
			
			# if the line is empty, it jumps to the next
			if keyword == '':
				continue

			# clean the free spaces from the txt & convert to nice-for-urls
			keyword = keyword.rstrip('\r\n')
			keyword = urllib.quote(keyword)
			print keyword
			
			# for each keyword I create a Serp object and get the rankings for a website
			completeUrl = self.url + keyword
			aSerp = serp.Serp(completeUrl)
			ranking = aSerp.returnRanking(self.website)
			landingPage = aSerp.returnLandingPage(self.website)

			# now the keyword is again a nice one not for URLs
			keyword = urllib.unquote(keyword)

			website_with_ranking_to_list = [keyword, ranking, landingPage]
			self.website_with_ranking.append(website_with_ranking_to_list)

		print self.website_with_ranking

		

		for element in self.website_with_ranking:

			with open('ranking_report.csv', 'ab') as f:
				mycsv = csv.writer(f, delimiter=',', lineterminator='\n')
				mycsv.writerow(element)




a = Ranking_csv()




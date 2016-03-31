from bs4 import BeautifulSoup
from urllib2 import urlopen
import csv
from HTMLParser import HTMLParser


def get_page_links(section_url,depth):
	counter = 1
	html=urlopen(section_url).read()
	soup = BeautifulSoup(html,"lxml")
	print soup
	#raw_input("Enter maaro ji")
	print soup.prettify()
	#raw_input("Firse enter maaro ji")
	boccat = soup.findAll("p")
	#print type(boccat)
	#raw_input("Enter string")
	# category_links = [p.a["href"] for dd in boccat.findAll("p")]
	#category_links = []
	if depth==0:
		try:
			for dd in boccat:
				if dd.find("a"):
					temp= dd.find('a')
					print type(temp['href'])
					if 'http' in temp['href'].split(':'):
						#pass
						#raw_input("redirecting")
						get_page_links(temp['href'],1)
					else:
						#pass
						#raw_input("Redirecting with addition")
						get_page_links(section_url + temp['href'],1)
					#raw_input("redirecting")
					#get_page_links(temp['href'],1)

					if temp['href']=="jun98.html":
						return
					
				#raw_input("Hit Enter")
				# print counter
				counter+=1
				#category_links.append(p.a["href"])
		except:
			print counter
	elif depth==1:
		#b = open("data.csv")
		#csvWrite = csv.writer(b,"w")



		dates = soup.findAll("b")
		lists = soup.findAll("ul")
		findLastPoint = soup.findAll("hr")
		diffSoup = BeautifulSoup('<b>Programs</b>',"lxml")
		tag=diffSoup.b
		print (tag.string)
		lineTracker = 0
		#print lists
		#print dates
		# for line in enumerate(soup.prettify()):
		# 	lineTracker+=1
		# 	#print line[0]
		# 	if '<b>Programs</b>' in soup.prettify()[line[0]].findAll("b"):
		# 		print lineTracker
		date_tags=[]
		for item in enumerate(dates):
			date_tags.append(item)
			if item=='<b>Programs</b>':
				break
				#print item

		for item in date_tags:
			print item[1].get_text()
			firstColumn = item[1].get_text()
			for ulItem in lists:
				liInstances = ulItem.findAll("li")
				for liItem in liInstances:
					x = liItem.find("a")
					print x['href']
					print "********"
					print x.get_text()
					print "********"
					print (((liItem.br.next_sibling.strip()).encode('ascii','ignore')).split('('))[0]
					# contents[2].strip()
					#print liInstances
					#raw_input("ailfnealifnalfin")
			#raw_input("Hi Enter")



	#return category_links


if __name__ == '__main__':
	BASE_URL = raw_input("Please enter urlopen")
	#output = get_page_links('http://nber.org/new_archive/2015.html',1)
	output = get_page_links('http://nber.org/new_archive/',0)
	
	print output

from bs4 import BeautifulSoup
from urllib2 import urlopen
import csv
from HTMLParser import HTMLParser
import copy
if __name__ == '__main__':
	# html=urlopen('../sample.html').read()
	soup = BeautifulSoup(open('sample.html'),"lxml")
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
		#print item
		#raw_input("see this")
		# if item[1]=='<b>Programs</b>':
		if '<b>Programs</b>' in item[1]:
			#raw_input("lets wait")
			break
			#print item
	list_final = []
	for item in date_tags:
		print item[1].get_text()
		#raw_input("wait")
		firstColumn = item[1].get_text()
		if firstColumn=='Programs':
			break
		for ulItem in lists:
			liInstances = ulItem.findAll("li")
			for liItem in liInstances:
				x = liItem.find("a")
				location = 'ok'
				try:
					print x['href']
					location = x['href']

				except:
					print x['hrvef']
					location = x['hrvef']
				final_location = 'ok'
				if 'http' in location.split(':'):
					final_location = copy.deepcopy(location)
				else:
					final_location = 'http://nber.org/' + location
				print "********"
				print x.get_text()
				print "########"
				
				if liItem.br is None:
					#tempy = (liItem.find('</br>'))
					#tempy.extract()
					print ((((liItem.a.next_sibling).strip()).encode('ascii','ignore')).split('('))[0]
					list_final.append([firstColumn.encode('ascii','ignore'),final_location,x.get_text().encode('ascii','ignore'),((((liItem.a.next_sibling).strip()).encode('ascii','ignore')).split('('))[0]])
					#str(liItem).replace("</br>", "<br>")
					#print liItem.prettify()
					#raw_input("")
				else:
					temporary = liItem.br.next_sibling
					if liItem.br.next_sibling is None:
						print ((((liItem.a.next_sibling).strip()).encode('ascii','ignore')).split('('))[0]
						list_final.append([firstColumn.encode('ascii','ignore'),final_location,x.get_text().encode('ascii','ignore'),((((liItem.a.next_sibling).strip()).encode('ascii','ignore')).split('('))[0]])
					else:
						print (((liItem.br.next_sibling.strip()).encode('ascii','ignore')).split('('))[0]
						list_final.append([firstColumn.encode('ascii','ignore'),final_location,x.get_text().encode('ascii','ignore'),(((liItem.br.next_sibling.strip()).encode('ascii','ignore')).split('('))[0]])
	
from bs4 import BeautifulSoup
from urllib2 import urlopen
import csv
from HTMLParser import HTMLParser
import copy
import sys, os


def get_page_links(section_url,depth):
	counter = 1
	html=urlopen(section_url).read()
	soup = BeautifulSoup(html,"lxml")
	#print soup
	#raw_input("Enter maaro ji")
	#print soup.prettify()
	#raw_input("Firse enter maaro ji")
	boccat = soup.findAll("p")
	list_papers = []
	#print type(boccat)
	#raw_input("Enter string")
	# category_links = [p.a["href"] for dd in boccat.findAll("p")]
	#category_links = []
	if depth==0:
		try:
			for dd in boccat:
				if dd.find("a"):
					temp= dd.find('a')
					#print type(temp['href'])
					if 'http' in temp['href'].split(':'):
						#pass
						#raw_input("redirecting")
						temp_list = get_page_links(temp['href'],1)
						list_papers.append(temp_list)
					else:
						#pass
						#raw_input("Redirecting with addition")
						temp_list = get_page_links(section_url + temp['href'],1)
						list_papers.append(temp_list)
					#raw_input("redirecting")
					#get_page_links(temp['href'],1)

					if temp['href']=="jun98.html":
						raw_input('Hey')
						return list_papers
					
				#raw_input("Hit Enter")
				# print counter
				counter+=1
				#category_links.append(p.a["href"])
		except Exception as e: 
			
		    
		    
		    # top = traceback.extract_stack()[-1]
		    # print ', '.join([type(e).__name__, os.path.basename(top[0]), str(top[1])])
			exc_type, exc_obj, exc_tb = sys.exc_info()
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			print(exc_type, fname, exc_tb.tb_lineno)
			print str(e)
			raw_input("Exception")
			print counter
			return list_papers
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
		tracker_counter = 0
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
		# for item in date_tags:
			#print item[1].get_text()
			#raw_input("wait")
			#firstColumn = item[1].get_text()
			# if firstColumn=='Programs':
			# 	break
		for ulItem in lists:
			firstColumn = date_tags[tracker_counter][1].get_text()
			while firstColumn == 'Latest NBER Working Papers' or firstColumn=='Chapters for Forthcoming NBER Books':
				tracker_counter+=1
				firstColumn = date_tags[tracker_counter][1].get_text()
			if firstColumn=='Programs':
				break
			tracker_counter+=1
			liInstances = ulItem.findAll("li")
			for liItem in liInstances:
				x = liItem.find("a")
				if x.has_key('name'):
					break
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
				try:
					if liItem.br is None or liItem.br.next_sibling is None:
					# 	print ((((liItem.a.next_sibling).strip()).encode('ascii','ignore')).split('('))[0]
					# 	list_final.append([firstColumn.encode('ascii','ignore'),final_location,x.get_text().encode('ascii','ignore'),((((liItem.a.next_sibling).strip()).encode('ascii','ignore')).split('('))[0]])
					# temporary = liItem.br.next_sibling
					# if liItem.br.next_sibling is None:
						print ((((liItem.a.next_sibling).strip()).encode('ascii','ignore')).split('('))[0]
						list_final.append([firstColumn.encode('ascii','ignore'),final_location,x.get_text().encode('ascii','ignore'),((((liItem.a.next_sibling).strip()).encode('ascii','ignore')).split('('))[0]])
					else:
						print (((liItem.br.next_sibling.strip()).encode('ascii','ignore')).split('('))[0]
						list_final.append([firstColumn.encode('ascii','ignore'),final_location,(x.get_text().encode('ascii','ignore'))[1:],(((liItem.br.next_sibling.strip()).encode('ascii','ignore')).split('('))[0]])
				except Exception as e:
					exc_type, exc_obj, exc_tb = sys.exc_info()
					fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
					print(exc_type, fname, exc_tb.tb_lineno)
					print str(e)
					raw_input("Exception Inside")
			# break		

					#print list_final
					#raw_input(".")

		# for item in list_final:
		# 	print item

		return list_final

		#raw_input("Please view. Press Enter afterwards.")
					# contents[2].strip()
					#print liInstances
					#raw_input("ailfnealifnalfin")
			#raw_input("Hi Enter")



	#return category_links


if __name__ == '__main__':
	BASE_URL = raw_input("Please enter urlopen")
	#output = get_page_links('http://nber.org/new_archive/2015.html',1)
	output = get_page_links('http://nber.org/new_archive/',0)
	# for item in output:
	# 	print item
	with open("output.csv", "wb") as f:
	    writer = csv.writer(f)
	    for item in output:
	    	writer.writerows(item)

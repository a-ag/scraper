from bs4 import BeautifulSoup
from urllib2 import urlopen



def get_page_links(section_url):
	counter = 1
	html=urlopen(section_url).read()
	soup = BeautifulSoup(html,"lxml")
	print soup.prettify()[0:1000]
	boccat = soup.findAll("p")
	print type(boccat)
	#raw_input("Enter string")
	# category_links = [p.a["href"] for dd in boccat.findAll("p")]
	category_links = []
	try:
		for dd in boccat:
			if dd.find("a"):
				temp= dd.find('a')
				print temp['href']
			raw_input("Hit Enter")
			# print counter
			counter+=1
			#category_links.append(p.a["href"])
	except:
		print counter

	return category_links


if __name__ == '__main__':
	BASE_URL = raw_input("Please enter url")
	output = get_page_links(BASE_URL)
	print output

from html.parser import HTMLParser
from urllib import parse

# This file is reponsible for finding all the links in a page (identified by 'href' tag and 'wiki'
# in that). All other links are discarded (images/videos). These links are then returned to the
# spider file.

class LinkFinder(HTMLParser):
	def __init__(self, base_url, page_url):
		super().__init__()
		self.base_url = base_url
		self.page_url = page_url
		self.links = set()

	def handle_starttag(self, tag, attrs):
		if tag == 'a':
			for (attribute, value) in attrs:				
				if attribute == 'href':
					temp_list = value.split('/')
					if len(temp_list) == 3 and temp_list[1] == 'wiki':
						url = parse.urljoin(self.base_url, value)  #only appends if base_url is not present
						self.links.add(url)

	def page_links(self):
		return self.links

	def error(self, message):
		pass

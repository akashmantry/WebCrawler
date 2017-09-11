from urllib.request import urlopen
from link_finder import LinkFinder
from domain import *
from general import *
import os
 
class Spider():

    #class variable shared among all spiders
    project_name  = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    out_links_file = ''
    queue = set()
    crawled = set()
    graph_out_dict = dict()
    graph_in_dict = dict()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        Spider.out_links_file = Spider.project_name + '/out_links.json'

        self.boot()
        self.crawl_page('First spider', Spider.base_url)

    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print (thread_name + ' crawling ' + page_url)
            print ('Queue ' + str(len(Spider.queue)) + ' | Crawled ' + str(len(Spider.crawled)))

            links = Spider.gather_links(page_url)
            Spider.add_links_to_queue(links)
            Spider.add_out_links_to_dict(page_url, links)
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)

            dict_temp = dict(Spider.graph_out_dict)
            Spider.update_files(dict_temp)

    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode('utf-8')
                save_name = page_url.replace('/', '.')
                name = Spider.project_name+'/'+save_name+'.txt'
                if not os.path.isfile(name):
                    write_file(name, page_url+'\n'+html_string)
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            print (str(e))
            return set()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue or url in Spider.crawled:
                continue
            if Spider.domain_name not in url:
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_files(dict_temp):
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
        dict_to_file(dict_temp, Spider.out_links_file)


    @staticmethod
    def add_out_links_to_dict(base_url, links):
        if base_url not in Spider.graph_out_dict:
            Spider.graph_out_dict[base_url] = []
        for url in links:
            Spider.graph_out_dict[base_url].append(url)



    







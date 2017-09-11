import os
import json

# This file contains the general functions used everywhere in the module.

def create_project_dir(directory):
	if not os.path.exists(directory):
		print ('Creating directory ' + directory)
		os.makedirs(directory)


def create_data_files(project_name, base_url):
	queue = project_name + '/queue.txt'
	crawled = project_name + '/crawled.txt'
	out_links_file = project_name + '/out_links.json'

	if not os.path.isfile(queue):
		write_file(queue, base_url)
	if not os.path.isfile(crawled):
		write_file(crawled, '')
	if not os.path.isfile(out_links_file):
		write_file(out_links_file, '')

	
def create_data_file_index(project_name):
	index = project_name + '/index.json'
	
	if not os.path.isfile(index):
		write_file(index, '')

def write_file(path, data):
	f = open(path, 'w')
	f.write(data)
	f.close()

def append_to_file(path, data):
	with open(path, 'a') as file:
		file.write(data + '\n')


def delete_file_contents(path):
	with open(path, 'w'):
		pass

#read a file and convert each line to set items
def file_to_set(file_name):
	results = set()
	with open(file_name, 'rt') as f:             
		for line in f:
			results.add(line.replace('\n', ''))
	return results

#convert set to a file
def set_to_file(links, file):
	delete_file_contents(file)                     #we don't want to appned, links has the new data
	for link in sorted(links):
		append_to_file(file, link)

def file_to_dict(file_name):
	results = dict()
	with open(file_name) as data_file:
		if os.stat(file_name).st_size == 0:
			return results
		results = json.load(data_file) 
	return results

def dict_to_file(words, file):
	delete_file_contents(file)                     #we don't want to appned, links has the new data
	with open(file, 'w') as fp:
		json.dump(words, fp, indent = 1)

def file_to_list(file_name):
	results = []
	results = open(file_name).read().split("\n")
	return results
	


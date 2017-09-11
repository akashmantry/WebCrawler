# WebCrawler
The goal of this project is to implement a simple web crawler in Python.

1. This is a multi-threaded web crawler that starts from a seed page (http://en.wikipedia.org) and goes to a depth of 3.
2. The crawler doesn't crawl the same pages and doesn't go outside the wikipedia domain. 
3. The crawler also creates an out_links file which maps url to its out links. This is used while implmenting PageRank which is used in this project [FolfoxSearch](https://github.com/akashmantry/FolfoxSearch).
4. The crawler was also deployed on an AWS EC2 instance and the results were stored in S3 file storage system.

import os
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from urllib import request
from pyvirtualdisplay import Display 

browserPath = '/home/tulip/python/phantomjs-2.1.1-linux-x86_64/bin/phantomjs'
homePage    = "http://www.sehuba3.com/videos/10940/play.html?10940-1-1"

parser      = 'html.parser'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
page        = request.Request(homePage,headers=headers)
page_source = request.urlopen(page).read()
bsObj = BeautifulSoup(page_source, parser)

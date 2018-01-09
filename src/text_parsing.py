# ========================================================================
# Copyright 2018 Emory University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ========================================================================
import os
import glob
import bibtexparser
from urllib.request import urlopen

import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

__author__ = 'Jinho D. Choi'


from bs4 import BeautifulSoup
from selenium import webdriver


url = 'http://nlp.mathcs.emory.edu'

driver = webdriver.Firefox()
driver.get(url)
# WebDriverWait(driver, 10000).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "schedule-landing-page"))) # waits till the element with the specific id appears

# html = driver.page_source
#
# fout = open('qtm-spring-2018.html', 'w')
# fout.write(html)




#
# def read_bibs(dirpath):
#     filenames = glob.glob(os.path.join(dirpath, '*.bib'))
#     entries = []
#
#     for filename in filenames:
#         fin = open(filename)
#         bib = bibtexparser.loads(fin.read())
#         ent = [entry for entry in bib.entries if 'author' in entry]
#         entries.extend(ent)
#
#     print('Read: %s (%d files, %d entries)' % (dirpath, len(filenames), len(entries)))
#     return entries
#
#
#
#
# # constants
# BIB_DIR = '/Users/jdchoi/Desktop/bibs/'
#
# # read bib file
# # read_bibs(BIB_DIR)
#
#
#
# def comment_threads_list_by_video_id(client, **kwargs):
#   # See full sample for function
#   kwargs = remove_empty_kwargs(**kwargs)
#
#   response = client.commentThreads().list(
#     **kwargs
#   ).execute()
#
#   return print_response(response)
#
# comment_threads_list_by_video_id(client,
#     part='snippet,replies',
#     videoId='m4Jtj2lCMAA')
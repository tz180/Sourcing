
from bs4 import BeautifulSoup
import socket
import mechanize
import sys
from unidecode import unidecode
from bs4.diagnose import diagnose
import urllib2
import unicodedata
from PIL import Image
import glob
import os
import re

def main():


	toURL = "http://fortune.com/2017/10/09/term-sheet-monday-october-9/"
	print "toURL: %s" %(toURL)
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	response = opener.open(toURL)
	soup = BeautifulSoup(response, "html.parser")
	text_parts = soup.findAll(text=True)
	text = ''.join(text_parts)

	data = soup.findAll('p')
	stringConvert = []
	see = []
	url_list = []
	for i in range(len(data)):
		data_j = str(data[i]).decode('unicode_escape').encode('ascii','ignore')
		stringConvert.append(strip_accents(unicode(data_j)))

		 #convert tagged information from site to strin
	#substr = long_substr(stringConvert)

	for i in range(len(stringConvert)):
		step1 = (stringConvert[i].replace('<p class="medium-offset-1 text size-1x-large line-height-large _10M0Ygc4"', ""))
		step2 = step1.replace("react-text", "")
		step3 = step2.replace('data-reactid="', "")
		step4 = step3.replace('-->  <!-- / --><a', "")
		step5 = step4.replace('rel=" noopener noreferrer" target="_blank"><strong ', "")
		step6 = step5.replace('rel=" noopener noreferrer" target="_blank"><!-- : ', "")
		step7 = step6.replace(' <!-- / --><a ', "")
		step8 = step7.replace('<!-- / --></p>', "")
		step9 = step8.replace('</strong></a><!-- : ', "")
		step10 = step9.replace('<!-- / --><strong ',"")
		step11 = step10.replace('"><!-- : ', "")
		step12 = step11.replace('<!-- / --></a><!-- : ', "")
		step13 = step12.replace('</strong><!-- : ', "")
		step14 = step13.replace('</strong></a><strong ', "")
		step15 = step14.replace('-->', "")
		step16 = step15.replace('.<!-- / </a></p>', "")
		step17 = step16.replace('<!-- / <em', "")
		step18 = step17.replace('</em><!-- : ',"")
		step19 = step18.replace('ong>', "")
		step20 = step19.replace('</a></p>', "")
		step21 = step20.replace('</str', "")
		step22 = step21.replace('</str</a><str', "")
		step23 = step22.replace('</a>', "")

		print step22
		see.append(step22)

	stripped_list = []

	for i in range(len(see)):
		stripped_list.append(see[i][8:])


		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', see[i]) #add urls to list
		url_list = url_list+urls

	print stripped_list
	for i in stripped_list:
		print
		print i.encode('ascii', 'ignore')
		print

	print text

	#for i in range(len(stringConvert)):
	#	for ch in ['<p class="medium-offset-1 text size-1x-large line-height-large _10M0Ygc4"', 'react-text', 'data-reactid="']:
	#		if ch in stringConvert[i]:
		#		new = stringConvert[i].replace(ch, "")
		#		print new
		#if 'raised' in stringConvert[i]: #if data is housed within this tag add it to see
			#see.append(stringConvert[i])
	"""for i in range(len(see)):
		print 
		print see[i]
		print"""

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def common_start(sa, sb):
    """ returns the longest common substring from the beginning of sa and sb """
    def _iter():
        for a, b in zip(sa, sb):
            if a == b:
                yield a
            else:
                return

    return ''.join(_iter())

def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and is_substr(data[0][i:i+j], data):
                    substr = data[0][i:i+j]
    return substr

def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True

main()
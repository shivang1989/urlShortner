'''
Description : Script used to shorten the url
Author : Shivang Desai

'''

import requests
import sys

url_name = str(sys.argv[1])

if url_name == " ":
	print "Please provide the url"
	sys.exit(0)


r = requests.get('http://tinyurl.com/create.php?source=indexpage&url=' + url_name + '&submit=Make+TinyURL!&alias=')

res = r.text

content  = res.split('\r\n')

file_obj = open('url-response.txt','w')
for item in content:	
	file_obj.write(item)
file_obj.close()

file_obj = open('url-response.txt','r')
file_content = file_obj.read()
line_numb = file_content.index('window.clipboardData.setData("Text"')

remaining_content = file_content[line_numb:]

second_index = remaining_content.index("')")

required_string = remaining_content[len('window.clipboardData.setData("Text",') + 1:second_index]

print "The Shortened URL is : " + required_string


import feedparser
import textwrap
import PIL
import configparser
import subprocess
import time
import os
from os.path import expanduser
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from datetime import datetime
"""
Author - Greg McCoy

Date - June 28th 2015

Description - pulls verse from bible gateway RSS feed.
Uses PIL to apply text to an image. Draws varaibles from
the conf file.
"""
config = configparser.ConfigParser()
home = expanduser("~")

def parseHTML(line):
	try:
		line = line.decode('utf-8')
		line = line.replace("&quot;", "\"")
		line = line.replace("&apos;", "'")
		line = line.replace("&amp;", "&")
		line = line.replace("&lt;", "<")
		line = line.replace("&gt;", ">")
		line = line.replace("&laquo;", "<<")
		line = line.replace("&raquo;", ">>")
		line = line.replace("&#039;", "'")
		line = line.replace("&#8220;", "\"")
		line = line.replace("&#8221;", "\"")
		line = line.replace("&#8216;", "\'")
		line = line.replace("&#8217;", "\'")
		line = line.replace("&#9632;", "")
		line = line.replace("&#8226;", "-")
		line = line.replace("&ldquo;", "")
		line = line.replace("&rdquo;", "")
		line = line.replace("&#8212;", "—")
	except Exception as e:
		print("Exception - " + str(e))
	
	return(line)

def getVerse():
	rssVerse = "https://www.biblegateway.com/votd/get/?format=atom"
	feed = feedparser.parse( rssVerse )
	for item in feed["entries"]:
		title = "\n" + item["title"]
		verse = item["summary"]
	
		return(verse + " - " + title)

def writeImage(quote):
	quote = parseHTML(quote)
	quote = textwrap.fill(quote, 50)
	text = quote.split('\n')
	print(quote)
	f = Image.open(readConf('input_image'))
	font = ImageFont.truetype(home + "/.versebg/" + readConf('font'),int(readConf('font_size')))
	draw = ImageDraw.Draw(f)
	(width, height) = f.size
	#Needs to be based on amount of new lines
	width = width / 2
	height = height / 2 + 50
	for s in reversed(text):
		draw.text((width - 500, height),s,(int(readConf('red')),int(readConf('green')),int(readConf('blue'))),font=font)
		height = height - 60
	draw = ImageDraw.Draw(f)
	draw = ImageDraw.Draw(f)
	
	f.save(readConf('output_url'))
	f.close();
	os.chmod(readConf('output_url'), 0o777)

def readConf(option):
	config.read(home + "/.versebg/versebg.conf")
	value = config['DEFAULT'][option]
	value = value.replace("~", home) 
	return(value)

def update():
	writeImage(getVerse())
	#Now uses crontab
	cmd = "sh " + home + "/.versebg/" + readConf('exec')
	os.system(cmd)
	#print(cmd)
	
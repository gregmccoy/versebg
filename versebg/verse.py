import feedparser
import textwrap
import PIL
import configparser
import subprocess
import schedule
import time
import os
from os.path import expanduser
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

"""
Author - Greg McCoy

Date - June 28th 2015

Description - pulls verse from bible gateway RSS feed.
Uses PIL to apply text to an image. Draws varaibles from
the conf file.
"""
config = configparser.ConfigParser()
home = expanduser("~")

def getVerse():
	rssVerse = "https://www.biblegateway.com/votd/get/?format=atom"
	feed = feedparser.parse( rssVerse )
	for item in feed["entries"]:
		title = item["title"]
		verse = item["summary"].replace("&ldquo;", "\"")
		verse = verse.replace("&rdquo;", "\"")
		verse = verse.replace("&#8212;", "—")
		return(verse + "\n" + title)

def writeImage(quote):
	quote = textwrap.fill(quote, 50)
	text = quote.split('\n')
	f = Image.open(home + "/.versebg/" + readConf('input_image'))
	font = ImageFont.truetype(home + "/.versebg/" + readConf('font'),int(readConf('font_size')))#needs to use conf
	draw = ImageDraw.Draw(f)
	(width, height) = f.size
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
	return(value)

def update():
	writeImage(getVerse())
	cmd = "sh " + home + "/.versebg/" + readConf('exec')
	os.system(cmd)
	print(cmd)
	
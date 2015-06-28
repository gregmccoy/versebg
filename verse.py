import feedparser
import textwrap
import PIL
import configparser
import subprocess
import schedule
import time
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


config = configparser.ConfigParser()

def getVerse():
	rssVerse = "https://www.biblegateway.com/votd/get/?format=atom"
	feed = feedparser.parse( rssVerse )
	for item in feed["entries"]:
		title = item["title"]
		verse = item["summary"].replace("&ldquo;", "\"")
		verse = verse.replace("&rdquo;", "\"")
		return(verse + "\n" + title)

def writeImage(quote):
	quote = textwrap.fill(quote, 50)
	text = quote.split('\n')
	f = Image.open(readConf('input_image'))
	font = ImageFont.truetype("font/DejaVuSans.ttf",45)#needs to use conf
	draw = ImageDraw.Draw(f)
	(width, height) = f.size
	width = width / 2
	height = height / 2 + 50
	for s in reversed(text):
		draw.text((width - 500, height),s,(255,255,255),font=font)
		height = height - 60
	draw = ImageDraw.Draw(f)
	draw = ImageDraw.Draw(f)
	
	f.save(readConf('output_url'))
	f.close();

def readConf(option):
	config.read("versebg.conf")
	value = config['DEFAULT'][option] 
	return(value)

def update():
	writeImage(getVerse())
	subprocess.call(['./scripts/' + readConf('exec')])

update()
schedule.every().day.at("23:00").do(update)
while True:
	schedule.run_pending()
	time.sleep(60)
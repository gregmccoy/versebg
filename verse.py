import feedparser
import textwrap
import PIL
import html
import re
import requests
import shutil
import argparse
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
"""
Author - Greg McCoy

Date - June 28th 2015

Description - pulls verse from bible gateway RSS feed.
Uses PIL to apply text to an image.
"""

parser = argparse.ArgumentParser()
parser.add_argument("-o", dest='output', help="Location to save image")
args = parser.parse_args()

def dailyPhoto():
    path = "http://www.gfa.ca/dailyphoto/"
    response = requests.get(path)
    results = re.search("www.gfamedia.org/u/convertible/circadian_photograph/gospelforasia.+(?=\.)", response.text)
    url = results.group(0)
    url = "http://" + url.rsplit("-", 1)[0] + ".jpg"
    url = url.replace("convertible/", "")
    img = requests.get(url, stream=True)
    if img.ok:
        with open("verse_background.png", 'wb+') as f:
            for block in img.iter_content(1024):
                f.write(block)

def getVerse():
    rssVerse = "https://www.biblegateway.com/votd/get/?format=atom"
    feed = feedparser.parse( rssVerse )
    for item in feed["entries"]:
        title = "\n" + item["title"]
        verse = item["summary"]
        return(verse + " - " + title)

def writeImage(quote, output):
    quote = html.unescape(quote)
    quote = textwrap.fill(quote, 50)
    text = quote.split('\n')

    dailyPhoto()
    f = Image.open("verse_background.png")

    # Darken image
    f = f.point(lambda x: x*0.4)

    font = ImageFont.truetype('DejaVuSans.ttf', 45)
    draw = ImageDraw.Draw(f)
    (width, height) = f.size

    #Needs to be based on amount of new lines
    width = width / 2
    height = height / 2 + 50
    for s in reversed(text):
        draw.text((width - 500, height),s, (255, 255, 255), font=font)
        height = height - 60
    draw = ImageDraw.Draw(f)
    f.save(output)
    f.close()

def update(args):
    if args.output:
        if args.output[:1] != "/":
            args.output += "/"
        output = args.output + "verse_background.png"
    else:
        output = "verse_background.png"
    writeImage(getVerse(), output)

update(args)

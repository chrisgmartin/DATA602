# This assignment will give you a chance to do a few important analytical tasks.
# As with Homework 3, I am looking for complete program.
# There are two parts below, do them both.

# 1 Design and implement a system that takes a webpage URL as input.
# The program will read the page and extract the important text, news story, blog post, etc from the pages source.
# Writing a program that can do this for any webpage is a major undertaking, so we will just focus on a single page.
# You can hard-code the link into the program.
# Basically, you want to turn something like this:
# Webpage (image with text)
# into this:
# "Anyone wanting to stream YouTube videos through a Chromecast currently has to visit YouTube's website or run one of its mobile apps.
# viewers may soon have more options, though, as Google has confirmed to GigaOM that it's publicly testing Chromecast support for
# embedded YouTube clips on third-party web pages. Right now, access is random at best -- the "send to" button only appears some of
# the time, and might not be available to everyone. The company says it's monitoring feedback from these experiments,
# however, and it could offer embedded video support to more Chromecast owners if all goes well."

# Take this text and store it in the program to use in the next step.

import urllib
from bs4 import BeautifulSoup

def get_text(urlname):
    try:
        sock = urllib.urlopen(urlname).read()
    except:
        print "Error with %s, please retry using another url object" % urlname
    soup = BeautifulSoup(sock, 'html.parser')
    soup.prettify()
    return soup.p.text

my_url = "https://www.engadget.com/2013/09/16/youtube-tests-chromecast-support-for-embedded-videos/"
my_text = get_text(my_url)
my_text


# 2 Take the important text that you extracted from the page and submit it to the Alchemy API for analysis.
# Specifically, obtain the Ranked Keywords.  Once you have the keywords, print to the console the top ten results.
# Below are the detailed steps:
# 1.Get an API key from Alchemy.
# 2.Download the Python SDK from the site.
# 3.Look at the example provided in the SDK.
# 4.Import the Alchemy module into your code.
# 5.Call the function to get Ranked Keywords.
# 6.The result will be in XML.  Process that XML and get the top ten keywords, and their relevance.
# 7.Print those results to the console.

from watson_developer_cloud import AlchemyLanguageV1 as alc
alchemy_language = alc(api_key='194aa7702b99d164213259c1d835cfdccb97b8ad')
keyrank = json.dumps(alchemy_language.keywords(max_items=10, text=my_text), indent=2)

import json
parsed_keyrank = json.loads(keyrank)
keywordlist = str(parsed_keyrank['keywords'])

print parsed_keyrank['keywords'][1]['text']


for i in parsed_keyrank['keywords']:
    print('Keyword: ' + str(i['text']) + '; Relevance: ' + i['relevance'])
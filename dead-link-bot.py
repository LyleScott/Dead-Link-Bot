"""
Lyle Scott III
lyle@digitalfoo.net
"""
import re
import sys
import urllib


START_URL = 'http://digitalfoo.net'

# links regex to look for
_LINK_RE = ["""href=['\|"]([^"]+digitalfoo[^"]+)['|"]""",]
LINK_RE = re.compile(r'|'.join(_LINK_RE))

# protocol regex to look for (if not relative URL)
PROTO_RE = re.compile(r"""[A-Za-z]+://([^"])""")

# link regex to ignore
_LINK_IGNORE_RE = ['google',
                   'statcounter',
                   'wikipedia',
                   'github',
                   'freebsd',
                   'pcengines',
                   'sourceforge',]
LINK_IGNORE_RE = re.compile(r'|'.join(_LINK_IGNORE_RE))


def getHtml(url):
    """get the html source of a url"""
    try:
        if not re.search(PROTO_RE, url):
            url = '%s/%s' % (START_URL, url,)
        urlcon = urllib.urlopen(url)
    except:
        sys.stderr.write ('ERROR connecting to %s\n' % url)
        return None
    return urlcon.read()
        
def extractUrls(html):
    """extract links that we care about from html source"""
    try:
        return re.findall(LINK_RE, html)
    except TypeError :
        return []

def keepUrl(url):
    """figure out if we care about the url hat was found"""
    if re.search(LINK_IGNORE_RE, url):
        return False
    if re.search(PROTO_RE, url) and re.search(LINK_RE, url):
        return False
    return True

def main():
    """main logic"""
    urls = [START_URL]
    crawled = []
    while urls:
        url = urls[0]
        urls = urls[1:]
        html = getHtml(url)
        for new_url in extractUrls(html):
            if new_url not in crawled and new_url not in urls and keepUrl(new_url):
                print new_url
                urls.append(new_url)
        crawled.append(url)
        
if __name__ == '__main__':
    main()
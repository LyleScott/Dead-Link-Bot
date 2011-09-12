import re
import sys
import urllib

#START_URL = 'http://digitalfoo.net'
START_URL = 'http://dsfsdf.com'
LINK_RE = re.compile(r'.*digitalfoo.net.*')


def getHtml(url):
    """get the html source of a url"""
    try:
        urlcon = urllib.urlopen(url)
    except:
        print sys.stderr.write('ERROR connecting to %s\n' % url)
        return None
    return urlcon.read()
        
def extractUrls(html):
    """extract links that we care about from html source"""
    #re.search(
    pass

def main():
    urls = [START_URL]
    while urls:
        url = urls.pop()
        html = getHtml(url)
        print html
        #more_urls = extractUrls(html)
        
    
    

if __name__ == '__main__':
    main()

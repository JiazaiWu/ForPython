# gethtml.py
# -*- coding: utf-8 -*-

import urllib
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.mdatalist = []
        self.mdatadic = {'start_time':False, 'end_time':False, 'event-location':False, 'event-title':False}

    def handle_starttag(self, tag, attrs):
        print('<%s %s>' % (tag, attrs))
        if len(attrs) != 0:
            if 'event-location' in attrs[0]:
                self.mdatadic['event-location'] = True
            if 'datetime' in attrs[0]:
                self.mdatadic['start_time'] = True
                self.mdatadic['end_time'] = True
            if 'event-title' in attrs[0]:
                self.mdatadic['event-title'] = True

    def handle_endtag(self, tag):
        #print('</%s>' % tag)
        pass

    def handle_startendtag(self, tag, attrs):
        #print('<%s %s/>' % (tag, attrs))
        pass

    def handle_data(self, data):
        print 'data %s' %data
        if self.mdatadic['start_time']:
            self.mdatalist.append(('start time', data))
            self.mdatadic['start_time'] = False
        elif self.mdatadic['end_time']:
            self.mdatalist.append(('end time', data))
            self.mdatadic['end_time'] = False
        if self.mdatadic['event-location']:
            self.mdatalist.append(('event-location', data))
            self.mdatadic['event-location'] = False
        if self.mdatadic['event-title']:
            self.mdatalist.append(('event-title', data))
            self.mdatadic['event-title'] = False

    def handle_comment(self, data):
        #print('<!-- %s -->' % data)
        pass

    def handle_entityref(self, name):
        #print('&%s;' % name)
        pass

    def handle_charref(self, name):
        #print('&#%s;' % name)
        pass

if __name__ == '__main__':
    web_page = urllib.urlopen('https://www.python.org/events/python-events/')
    html_page = web_page.read()
    parser = MyHTMLParser()
    parser.feed(html_page)
    print parser.mdatalist
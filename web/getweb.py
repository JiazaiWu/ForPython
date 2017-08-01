# getweb.py
# -*- coding: utf-8 -*-

import urllib
from xml.parsers.expat import ParserCreate

class xml_handler(object):
	def __init__(self):
		self.datalist = []
		self.flag = False
		self.datefilter = ['currentCity', 'date', 'weather', 'wind', 'temperature']

	def start_element(self, name, attr):
		if name in self.datefilter:
			print name
			self.flag = True

	def end_element(self, name):
		self.flag = False

	def char_data(self, text):
		if self.flag:
			self.datalist.append(text)

	def get_weather(self):
		weather_str = ''
		for str in self.datalist:
			weather_str += str.encode('utf-8')
		return weather_str


if __name__ == '__main__':
	handler = xml_handler()
	mparser = ParserCreate()
	mparser.returns_unicode = True
	mparser.StartElementHandler = handler.start_element
	mparser.EndElementHandler = handler.end_element
	mparser.CharacterDataHandler = handler.char_data
	web_page = urllib.urlopen('http://api.map.baidu.com/telematics/v2/weather?location=%E4%B8%8A%E6%B5%B7&ak=B8aced94da0b345579f481a1294c9094')
	data = web_page.read()
	mparser.Parse(data)
	print handler.get_weather()
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request
import re
__author__ = 'Ly'


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')


# 作业
class MyParser(HTMLParser):
    flag = 0
    res = []
    current_data =None

    def handle_starttag(self, tag, attrs):
        if tag == 'ul':
            for attr in attrs:
                if re.match(r'list-recent-events', attr[1]):
                    self.flag = 1

        if self.flag and tag == 'a':
            self.current_data = 'title'
        if self.flag and tag == 'time':
            self.current_data = 'time'
        if self.flag and tag == 'span':
            self.current_data = 'addr'

    def handle_endtag(self, tag):
        if self.flag == 1 and tag == 'ul':
            self.flag = 0
        if self.current_data:
            self.current_data = None

    def handle_data(self, data):
        if self.flag and self.current_data:
            if self.current_data =='title':
                self.res.append({self.current_data: data})
            else:
                self.res[len(self.res) - 1][self.current_data] = data

            self.current_data = None


def my_html_parser(url):
    with request.urlopen(url) as fget:
        parser_str = fget.read().decode('utf-8')
        parser = MyParser()
        parser.feed(parser_str)
        for i in parser.res:
            for j in i:
                print('%s: %s' % (j, i[j]))
            print()


my_html_parser('https://www.python.org/events/python-events/')
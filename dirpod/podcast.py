# -*- coding: utf-8 -*-
from episode import Episode  # change this to .episode when it's a package
import arrow
from urllib import quote
from cgi import escape


class Podcast():

    """docstring for Podcast"""

    def __init__(self, metadata, files):
        # Input variables
        self.metadata = metadata
        self.files = files

        # Output variable
        self.episodes = []
        self.channel = dict()

        # Initialization
        self.addChannel()
        self.addItems()

    def addChannel(self):
        self.channel['title'] = escape(self.metadata['title'])
        self.channel['link'] = self.metadata['url']
        self.channel['language'] = self.metadata['language']
        self.channel['description'] = escape(self.metadata['description'])
        self.channel['itunes:subtitle'] = escape(self.metadata['subtitle'])
        self.channel['itunes:author'] = escape(self.metadata['author'])
        self.channel['itunes:summary'] = escape(self.metadata['description'])
        self.channel['itunes:category'] = []
        metacategories = self.metadata["categories"]
        if not isinstance(metacategories, list):
            metacategories = [metacategories]
        for category in metacategories:
            self.channel['itunes:category'].append(escape(category))
        self.channel['itunes:image'] = self.metadata["base_url"] + quote(self.metadata['image_url'])
        self.channel['pubDate'] = arrow.utcnow().format(
            'ddd, D MMM YYYY hh:mm:ss') + ' GMT'

    def addItems(self):
        for afile in self.files:
            self.episodes.append(Episode(afile, self.metadata).toXml())

    def toXml(self):
        podcastXml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>" \
                     "<rss xmlns:itunes=\"http://www.itunes.com/" \
                     "dtds/podcast-1.0.dtd\" version=\"2.0\"><channel>"
        for prop in self.channel:
            if prop == 'itunes:image':
                podcastXml += '<%s href="%s" />' % (prop, self.channel[prop])
            elif prop == 'itunes:category':
                for category in self.channel[prop]:
                    podcastXml += '<%s text="%s" />' % (prop, category)
            else:
                podcastXml += '<%s>%s</%s>' % (prop, self.channel[prop], prop)
        for episode in self.episodes:
            podcastXml += episode
        podcastXml += "</channel></rss>"
        return podcastXml

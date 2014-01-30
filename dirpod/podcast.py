# -*- coding: utf-8 -*-
import dicttoxml
from episode import Episode  # change this to .episode when it's a package


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
        self.channel['title'] = self.metadata['title']
        self.channel['link'] = self.metadata['url']
        self.channel['language'] = self.metadata['language']
        self.channel['description'] = self.metadata['description']
        self.channel['itunes:subtitle'] = self.metadata['subtitle']
        self.channel['itunes:author'] = self.metadata['author']
        self.channel['itunes:summary'] = self.metadata['description']
        self.channel['itunes:image'] = self.metadata['image_url']

    def addItems(self):
        for afile in self.files:
            self.episodes.append({"item": Episode(afile, self.metadata)})
            #self.episodes.append({"item": Episode(afile, self.metadata).toDict()})

    def xml(self):
        # Output <rss> shit
        # dicttoxml channel shit
        # dicttoxml each self.episodes
        # output trailing </rss> shit
        pass

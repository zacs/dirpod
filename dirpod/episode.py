# -*- coding: utf-8 -*-
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen._id3util import ID3NoHeaderError
import arrow
import os.path
import time
import logging


class Episode:
    """
    Episode class, for a single episode of a podcast. This class should really
    only be called from the Podcast class. Class should be instantiated with
    2 variables: a path to an mp3 and [optionally] a dict of metadata.

    The dict of metadata should be used to either fill in gaps or override
    values divined from the mp3's ID3 tag data.
    """

    def __init__(self, path, metadata):
        # Initialization vars
        self.path = path
        self.metadata = metadata

        # Internal vars
        self.title = ""
        self.artist = ""
        self.categories = []
        self.date = arrow.now()
        self.duration = None

        # Instantiate the class
        self.addDataFromTags()

    def addDataFromTags(self):
        try:
            mp3info = EasyID3(self.path)
        except ID3NoHeaderError:
            print "no ID3 data present"
            mp3info = None
        except:
            print "unknown error loading ID3 data"

        mp3file = MP3(self.path)
        # should probably clear the track number if we're okay writing to the mp3

        # Get the author from the MP3's artist tag; fallback to metadata author
        try:
            self.author = mp3info["artist"][0]
        except:
            print "no id3 artist, pull author from channel.json"
            self.author = self.metadata["author"]

        # Add the categories specified in the input metadata
        try:
            metacategories = self.metadata["categories"]
            if not isinstance(metacategories, list):
                metacategories = [metacategories]
                print "sup"
            for category in metacategories:
                print "%s: %s" % (self.path, category)
                self.categories.append(category)
        except Exception as e:
            print "no categories in json: %s" % str(e)

        # Now also add the genre as a category
        try:
            self.categories.append(mp3info["genre"][0])
        except:
            print "No genre present in ID3, not adding anything."

        # Get date from file creation time; fallback to current time
        try:
            self.date = arrow.get(os.path.getctime(self.path))
        except:
            self.date = arrow.now('US/Central')
            print "Unable to get file creation time. Using 'now' as fallback."

        # Get title from ID3; fallback to "Show Name (Date)"
        try:
            self.title = mp3info["title"][0]
        except:
            print "no id3 title"
            self.title = "%s (%s)" % (self.metadata["title"], self.date.format('MMM D, YYYY'))

        try:
            self.duration = time.strftime('%H:%M:%S', time.gmtime(mp3file.info.length))
        except:
            self.duration = None

        #print mp3info.items()
        #print mp3file.info.length
        pass

    def episodeToDict(self):
        print self.title
        print self.author
        print self.categories
        print self.date
        print self.duration
        pass

if __name__ == '__main__':
    print "Probably shouldn't be calling Episode on its own"

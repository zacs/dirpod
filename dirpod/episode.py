# -*- coding: utf-8 -*-
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import arrow
import os.path
import time


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
        mp3info = EasyID3(self.path)
        mp3file = MP3(self.path)

        try:
            self.author = mp3info["artist"][0]
        except:
            print "no id3 artist, pull author from channel.json"

        try:
            self.categories.append(mp3info["genre"][0])
        except KeyError:
            print "no id3 genre"
            # Use static genre from the channel.json
        else:
            # apparently no genres in channel.json -- set to blank
            pass

        try:
            self.date = arrow.get(os.path.getctime(self.path))
        except:
            print "just use today's date, as a weird fallback"

        try:
            self.title = mp3info["title"][0]
        except:
            print "no id3 title"
            # Use static title (show name + date) from the channel.json

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

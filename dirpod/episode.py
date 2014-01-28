# -*- coding: utf-8 -*-
from mutagen.easyid3 import EasyID3
import arrow
import os.path


class Episode:
    """
    Episode class, for a single episode of a podcast. This class should really
    only be called from the Podcast class. Class should be instantiated with
    2 variables: a path to an mp3 and [optionally] a dict of metadata.

    The dict of metadata should be used to either fill in gaps or override
    values divined from the mp3's ID3 tag data.
    """

    def __init__(self, path, metadata=""):
        # Initialization vars
        self.path = path
        self.metadata = metadata

        # Internal vars
        #self.date = arrow()
        self.title = ""
        self.album = ""
        self.artist = ""
        self.genre = ""
        self.date = arrow.now()

        # Instantiate the class
        self.addTagData()

    def addTagData(self):
        mp3info = EasyID3(self.path)

        try:
            self.title = mp3info["title"]
        except:
            print "no id3 title"
            # Use static title from the channel.json

        try:
            self.artist = mp3info["artist"]
        except:
            print "no id3 artist"
            # Use static artist from the channel.json

        try:
            self.album = mp3info["album"]
        except:
            print "no id3 album"
            # Use static album from the channel.json

        try:
            self.genre = mp3info["genre"]
        except KeyError:
            print "no id3 genre"
            # Use static genre from the channel.json
        else:
            # apparently no genres in channel.json -- set to blank
            pass

        try:
            self.date = mp3info["date"]
        except KeyError:
            self.date = arrow.get(os.path.getctime(self.path))
            print "no id3 date, let's use file creation time"
            # Use static title from the channel.json
        else:
            # Use the date that was set at instantiation time ("now")
            print "just use today's date, as a final fallback"
            pass

        print mp3info.items()
        pass

    def episodeToDict(self):
        print self.title
        print self.album
        print self.artist
        print self.genre
        print self.date
        print self.date.humanize()
        pass

if __name__ == '__main__':
    foo = Episode("/Users/zac/Code/scratch/groce_sample.mp3")
    foo.episodeToDict()

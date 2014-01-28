# -*- coding: utf-8 -*-
from glob import glob


allEps = []
for filename in glob('/home/jon/Downloads/*.mp3'):
    # now sort the array by their dates
    allEps.append(Episode(filename))

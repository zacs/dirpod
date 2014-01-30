# -*- coding: utf-8 -*-
from glob import glob
import json
import dicttoxml
import os.path
from episode import Episode # change this to .episode when it's a package

allEps = []
podcastMetadata = json.loads(open('/Users/zac/Code/scratch/fake_pod/channel.json').read())

for filename in glob('/Users/zac/Code/scratch/fake_pod/*.mp3'):
    allEps.append(Episode(filename, podcastMetadata))
# now sort the array by their dates
print "=================================="
for ep in allEps:
    ep.episodeToDict()
    print "---------------------------"

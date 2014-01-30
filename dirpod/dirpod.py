from podcast import Podcast
import os.path
import json
from glob import glob
from pprint import pprint
# first validate the path given
# second validate the channel.json
# third load the json, add the channel-wide valus to a dict
# fourth iter through files, add them to dict.items or whatever
# fifth write the dict to the path using dicttoxml
files = []
podcastMetadata = json.loads(open('/Users/zac/Code/scratch/fake_pod/channel.json').read())
for filename in glob('/Users/zac/Code/scratch/fake_pod/*.mp3'):
    files.append(filename)
temp = Podcast(podcastMetadata, files)

#for ep in temp:
print temp
pprint (vars(temp))

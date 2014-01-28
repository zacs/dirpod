# dirpod

Pronounced derp-odd.

dirpod is a command-line utility, written in Python, which allows one to generate a podcast based upon two things: a directory full of mp3s, and a JSON file which stores some necessary pieces of the podcast metadata.

In order to run, you need to define the path in which both the mp3s and the `channel.json` file stay. These should all be in the same directory (and not in subdirectories). Run it like so:

   dirpod /home/user1/dirwithmp3s

This will generate the RSS file, which will be output into that same `dirwithmp3s`.

## Configuration via `channel.json`

The `channel.json` file is the only place to specify configuration information, some of which is mandatory. See `samples/channel.json` for a fully documented example of the config.

### Require Config Values

It is required to at least specify a few values in the `channel.json`. They are the following:

    "title": "Your Podcast Title",
    "subtitle": "A few short words about this podcast."
    "author": "Firstname Lastname",
    "description": "This podcast is about foos and bars, and more!"

As long as those properties are specified, the podcast will generate correctly. There are of course some other config values which are highly recommended, especially if you plan on trying to find new listeners via iTunes' search functionality, etc.

### Relative Links

By default, the utility will assume that all links are relative. For example, the `enclosure` elements will simply specify 'some_episode.mp3' as the URL, instead of `http://mydomain.com/podcast/some_episode.mp3`.

In order to define a static root for the enclosures, just set the `enclosures_url` property in the `channel.json`.


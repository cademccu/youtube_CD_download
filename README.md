# youtube_CD_download
This repository contains python3 scripts designed to fetch and download audio files from youtube video URL's and playlist URL's.

### WARNING
This code is designed to occasially make custom CD's formyself, and no download of any music is sold or used in any way other than personal
enjoyment. This should only be used for the occasional creation of a custom CD, and should not replace streaming services. This script should **NOT**
be used to redistrubute, sell, or profit off other's works in any way. The technology for actually downloading the videos is provided by outside 
libraries and sources, and I only manage the files once they are created. This code serves as a command line utility for those libraries.

### Intent of this project
The intent of this project was to write a program to fit my music dowload needs. Using a YouTube converter for one URL at a time,
that often failed to get the final product, then manually move each video from the Downloads directory to a specific, nested directory 
made creating a custom CD or downloading an entire album a 20 plus minute process. 

What I wanted is a portable script that I can place on my path, that gives me the ability to do a few things:
* Give a URL, or a file containing a URL(s) and download to my current place in the filesystem.
* Provide a file with a list of URLs, perhaps individual videos of a custom playlist, to all be downloaded to the same location.
* Provide a location to be created or written to.


### Features

```
usage: get_audio [-h] [-u URL] [-l LOCATION] [--make-directory] [-f FILE] [-c] [--location-file LOCATION_FILE] [-a AUDIO_FORMAT]

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Specify the URL of a video or playlist.
  -l LOCATION, --location LOCATION
                        Specify a location for the files to download to.
  --make-directory      If location is specified, make the directory with the specified path.
  -f FILE, --file FILE  Specify a file name/path of a textfile with a single URL on each line.
  -c, --clear           Clear youtube-dl's cache
  --location-file LOCATION_FILE
                        Give a .csv file with <URL,location,make-directory> where make-directory is <True|False>. If not specified, defaults to False.
  -a AUDIO_FORMAT, --audio-format AUDIO_FORMAT
                        Audio format to write to. Defaults to 'best' which is .opus on most systems. Other options are: aac, alac, flac, m4a, mp3, opus, vorbis, wav
```


### TODO list
* DONE arg to specify the target directory.
* DONE arg to CREATE a target directory.
* if not mkdirs, then cancel if not exists
* naming conventions for files.
* script to start and run brasero with specific directory (bash probably)
* run brasero with directory given from script? might be too much
* check that command line arg is surrounded with quotes
* give naming convention options?
* sanatize inputs with quotes
* specify quality of sound? or make better


### Usage
Remember to put quotes ( " ) around command line arg strings.


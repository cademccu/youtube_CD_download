# youtube_CD_download
This repository contains python3 scripts designed to fetch and download audio files from youtube video URL's and playlist URL's.

### WARNING
This code is designed to occasially make custom CD's for myself, and no download of any music is sold or used in any way other than personal
enjoyment. This should only be used for the occasional creation of a custom CD, and should not replace streaming services or purchasing CDs when possible. This script should **NOT**
be used to redistrubute, sell, or profit off other's works in any way. The technology for actually downloading the videos is provided by outside 
libraries and sources, and I only manage the files once they are created. This code serves as a command line utility for those libraries.

### Intent of this project
The intent of this project was to write a program to fit my music download needs. Using a YouTube converter for one URL at a time,
that often failed to get the final product, then manually move each video from the Downloads directory to a specific, nested directory 
made creating a custom CD or an entire album a 20 plus minute process. 

What I wanted is a portable script that I can place on my path, that gives me the ability to do a few things:
* Give a URL, or a file containing a URL(s) and download to my current place in the filesystem.
* Provide a file with a list of URLs, perhaps individual videos of a custom playlist, to all be downloaded to the same location.
* Provide a location to be created or written to.


### Current Features

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
  --name-file NAME_FILE
                        Give a .csv file with <URL,location,file-name,make-directory> where file-name is the name the file will be renamed to from the youtube title (no extension, it
                        will be added automatically), and make-
directory is <True|False>. If not specified, defaults to False.
```


### Usage notes
Remember to put quotes ( " ) around command line arg strings, especially for URLs with odd characters. No need to use quotes for anything within a file.

Place this script on your path, add execution permissions, and edit the enviroment tag at the top of the file to your python3 location run as a script. All Examples will show python3 preceding the script as that is the fastest, out of the box run method.

### EXAMPLES

Regular URL run
```
python3 get_audio -u "https://www.youtube.com/watch?v=zK1mLIeXwsQ"
```

Use URL, write to a directory that you want to create
```
python3 get_audio -u "https://www.youtube.com/watch?v=zK1mLIeXwsQ" -l your_directory_name --make-directory
```

Use a named file to read a list
```
python3 get_audio --name-file named_file.csv
```
Where named_file.csv contents look like (remember to leave extension out of file name)
```
https://www.youtube.com/watch?v=zK1mLIeXwsQ,directory_one,file_name_one,True
https://www.youtube.com/watch?v=zK1mLIeXwsQ,directory_two,file_name_two
https://www.youtube.com/watch?v=zK1mLIeXwsQ,directory_three,file_name_three,false
```


##### TODO list
* check that command line arg is surrounded with quotes (or throw accurate error)
* Give naming options for single URL
* specify quality of sound? or make better. Look at sound quality arg, and make it an argument with best default if possible.
* Playlist option and arg

* ##### COMPLETED
* DONE give naming convention options in file
* DONE naming conventions for files.
* DONE arg to specify the target directory.
* DONE arg to CREATE a target directory.


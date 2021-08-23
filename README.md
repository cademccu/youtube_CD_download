# youtube_CD_download
This repository contains python3 scripts designed to fetch and download mp3's from youtube video URL's and playlist URL's.

### WARNING
This code is designed to occasially make custom CD's formyself, and no download of any music is sold or used in any way other than personal
enjoyment. This should only be used for the occasional creation of a custom CD, and should not replace streaming services. This script should **NOT**
be used to redistrubute, sell, or profit off other's works in any way. The technology for actually downloading the videos is provided by outside 
libraries and sources, and I only manage the files once they are created. This code serves as a command line utility for those libraries.

### Intent of this project
The intent of this project was to write a program to fit my music dowload needs. Using a YouTube-mp3 converter for one URL at a time,
that often failed to get the final product, then manually move each video from the Downloads directory to a specific, nested directory 
made creating a custom CD or downlaoding an entire album a 20 plus minute process. 

What I wanted is a portable script that I can place on my path, that gives me the ability to do a few things:
* Give a URL, or a file containing a URL(s) and download to my current place in the filesystem.
* Provide a file with a list of URLs, perhaps individual videos of a custom playlist, to all be downloaded to the same location.
* Provide a location to be created or written to.


### Features
```
-u | --url            <STRING>            Provide the URL to a playlist or individual video. 
-f | --file           <PATH_TO_FILE>      Give a file with a URL for video or playlist on each line.
-l | --location       <DIRECTORY>         For either the -f or -u option, provide a directory location 
                                          relative to where script is being run, or absolute to write to.
--make-directory                          If providing a -l location, using this flag will make the 
                                          directory given. Will throw error if location already exists.
--c | --clear                             Clear youtube-dl's cache. Helpful when a download fails.
--location-file       <PATH_TO_FILE>      Provide a comma seperated (CSV) file of the format:
                                          <URL>,<LOCATION>,<MKDIRS> 
                                          <URL> - The Url of a video or playlist
                                          <LOCATION> - the location where this URL should write to.
                                          <MKDIRS> either <True|False> defaults to false if not present.
                                          Creates the directory provided in <LOCATION>. If fails, or 
                                          directory already exists, continues to next line of file.

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


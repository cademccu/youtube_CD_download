from __future__ import unicode_literals
import youtube_dl
import sys


# This is the first working version of the downloader I got. 
# will function, but want to make a more robust script.





# options for youtube downloader to convert
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}



def download(URL):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([URL])



def main():
    if sys.argv[1] == "--file" or sys.argv[1] == "-f":
        with open(sys.argv[2], "r") as f:
            line = f.readline()
            while True:
                if not line:
                    break
                download(line)
                line = f.readline()
    elif sys.argv[1] == "--help" or sys.argv[1] == "-h":
        print("[ USAGE ] \n")
        print("--file | -f   <ARG>       Provide a text file with a youtube URL on every line.")
        print("<ARG.                     Download the video or playlist at the youtube URL to mp3.")
        print("--help | -h               This menu")
    else: # single URL
        download(sys.argv[1])


if __name__ == "__main__":
    main()

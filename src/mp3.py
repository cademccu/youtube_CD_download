from __future__ import unicode_literals
import youtube_dl
import sys
import subprocess
import argparse


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


# uses argparser to get arguments
def get_arguments():
    #parser = argparse.ArgumentParser(description="Downlad MP3's from YouTube videos.")
    parser = argparse.ArgumentParser()

    parser.add_argument("-u", "--url", help="Specify the URL of a video or playlist.", action="store", dest="URL")
    parser.add_argument("-f", "--file", help="Specify a file name/path of a textfile with a single URL on each line.", action="store", dest="FILE")
    parser.add_argument("-c", "--clear", help="Clear youtube-dl's cache", action="store_true")


    return parser.parse_args()

def main():
    # TODO better arg management either in loop or dictionary
    # need to check for argv length before indexing.

    args = get_arguments()

    if args.clear:
        subprocess.run(["youtube-dl", "--rm-cache-dir"])


    # main decision section
    if args.URL:
        print("Using a URL from the command line.")
        download(args.URL)
    elif args.FILE:
        print("Using URL values from the file:", args.FILE)
        with open(sys.argv[2], "r") as f:
            line = f.readline()
            while True:
                if not line:
                    break
                download(line)
                line = f.readline()

    sys.exit(0)


if __name__ == "__main__":
    main()

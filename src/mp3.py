from __future__ import unicode_literals
import youtube_dl
import sys
import subprocess
import argparse
import os


OUTTMPL_STR = "%(title)s.%(ext)s"
# options for youtube downloader to convert
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': OUTTMPL_STR,
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
    parser.add_argument("-l", "--location", help="Specify a location for the files to download to.", action="store", dest="LOCATION")
    parser.add_argument("--make-directory", help="If location is specified, make the directory with the specified path.", action="store_true", dest="MAKE_DIRECTORY")
    parser.add_argument("-f", "--file", help="Specify a file name/path of a textfile with a single URL on each line.", action="store", dest="FILE")
    parser.add_argument("-c", "--clear", help="Clear youtube-dl's cache", action="store_true")
    

    return parser.parse_args()

def main():
    args = get_arguments()

    if args.clear:
        subprocess.run(["youtube-dl", "--rm-cache-dir"])
    if args.LOCATION != None:
        if args.FILE == None and args.URL == None:
            print("[ERROR] Must specify a url or a file containing URLS. -h for help.")
            sys.exit(-1)
        if args.MAKE_DIRECTORY:
            try:
                os.mkdir(args.LOCATION)
            except OSError as error:
                print("[ERROR] OSError occurred while trying to make new directory. Exiting...")
                print(error) 
                sys.exit()
        # sanatize the filepath if path seperator not provided.
        ydl_opts["outtmpl"] = os.path.join(args.LOCATION, OUTTMPL_STR)



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

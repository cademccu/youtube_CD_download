from __future__ import unicode_literals
import youtube_dl
import sys
import subprocess



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


def help():
    print("[ USAGE ] \n")
    print("<URL>                     Download the video or playlist at the youtube URL to mp3.")
    print("--file | -f   <FILE>      Provide a text file with a youtube URL on every line.")
    print("--help | -h               This help menu.")
    print("--clear | -c              Clears youtube-dl's cache, can help if a download fails.")
    sys.exit(0)


def main():
    # TODO better arg management either in loop or dictionary
    # need to check for argv length before indexing.
    if len(sys.argv) == 1:
        help()
        sys.exit(0)
    elif sys.argv[1] == "--file" or sys.argv[1] == "-f":
        with open(sys.argv[2], "r") as f:
            line = f.readline()
            while True:
                if not line:
                    break
                download(line)
                line = f.readline()
    elif sys.argv[1] == "--help" or sys.argv[1] == "-h":
        help()
        
    elif sys.argv[1] == "--clear" or sys.argv[1] == "-c":
        subprocess.run(["youtube-dl", "--rm-cache-dir"])
    else: # single URL
        download(sys.argv[1])


if __name__ == "__main__":
    main()

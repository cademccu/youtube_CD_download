import youtube_dl # Youtube_dl is used for download the video

ydl_opt = {"f": "mp3"} # Here we give some advanced settings. outtmpl is used to define the path of the video that we are going to download
#ydl_opt = {"outtmpl" : "/videos/%(title)s.%(ext)s", "format": "bestaudio/best"} # Here we give some advanced settings. outtmpl is used to define the path of the video that we are going to download

def operation(link):
    """
    Start the download operation
    """
    try:
        with youtube_dl.YoutubeDL(ydl_opt) as yd: # The method YoutubeDL() take one argument which is a dictionary for changing default settings
            video = yd.download([link]) # Start the download
            print("\n[DOWNLOAD SUCCESS]\n")
    except Exception:
        print("[ERROR] video failed to complete the download process.")
        print("Link: " + link)

#operation("https://www.youtube.com/watch?v=HMKkbco7UFE")
operation("https://www.youtube.com/watch?v=8QmPCrC7uXw&list=PLaVHibd49QFKxvoBVXiySuBLmchLY7cq5&index=1")

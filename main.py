"""
    This small GUI Application should be able to download
    videos or playlists in the mp3 or mp4 format. Please
    use this application to download at your own risk, 
    the owner is not responsible for copyright infractions 
    one may create. It is unknown if it will work on other
    computers due to some of the modules not working properly,
    testing will commence soon.
"""

##  Dependencies Note:                                     ##
##      You will have to install pytube and moviepy        ##
##      Pytube is to download the youtube video as an mp4  ##
##      while moviepy converts it into an mp3 if wanted    ##

#imports:
from tkinter import filedialog, Label, Button, Tk, StringVar, Place, mainloop, Entry, Radiobutton
from pytube import YouTube, Playlist
import pytube, os, glob, re
from moviepy.editor import VideoFileClip
import threading

##Convert input path and youtube link to video/audio
def convert(x, path='', format='mp3'):
    ##Try downloading, if fail, assumed as a playlist
    try:
        yt = YouTube(x).streams.first()
        yt.download(path)
    except pytube.exceptions.RegexMatchError:
        try:
            playlist = Playlist(x)
            playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
            for url in playlist.video_urls:
                yt = YouTube(url).streams.first()
                yt.download(path)
        except:
            #To be added in future versions
            pass
    if format == 'mp3':
        for num in glob.glob(path+"\\*.mp4"):
            video = VideoFileClip(num)
            video.audio.write_audiofile(num[0:-4]+'.mp3')
            video.close()
        for num in glob.glob(path+"\\*.mp4"):
            os.remove(num)

##GUI TKinter##
def browse_button():
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)

#Placeholder, TKinter cannot easily take arguments into functions under button clicks
def sendtoconvert():
    convert(videopath.get(), folder_path.get(), v.get())

#Creates a new thread so that downloading is faster and the GUI is stable
def threader():
    threading.Thread(target=sendtoconvert).start()

#Distinguish between running the program, or having the functions imported
if __name__ == "__main__":
    ##GUI Initialize##
    root, v, folder_path = Tk(), StringVar(), StringVar()
    root.title('Youtube to mp3 converter'), root.geometry("300x300")
    button2 = Button(text="Download Folder", command=browse_button).place(relx=0.35, rely=0.3)
    videopath = Entry(root, width=22)
    videopath.place(relx=0.3, rely=0.2)
    button3 = Button(text="Convert!", command=threader).place(relx=0.4, rely=0.7)
    for text, value, relx, rely in [['Video (mp4)', 'mp4', 0.4, 0.45], ['Audio (mp3)', 'mp3', 0.4, 0.55]]:
        Radiobutton(root, text=text, variable = v, value=value,indicatoron=0).place(relx=relx, rely=rely)
    mainloop()
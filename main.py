'''
    This small GUI Application should be able to download videos or playlists in the mp3 or mp4 format
    Please use this application to download at your own risk, the owner is not responsible for copyright
    infractions one may create.
'''


from tkinter import filedialog, Label, Button, Tk, StringVar, Place, mainloop, Entry, Radiobutton
from pytube import YouTube, Playlist
import pytube, os, glob, re
from moviepy.editor import VideoFileClip

##Convert input path and youtube link to video/audio
def convert(x, path, format):
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

##GUI Initialize##
if __name__ == "__main__":
    root, v, folder_path = Tk(), StringVar(), StringVar()
    root.title('Youtube to mp3 converter'), root.geometry("300x300")
    button2 = Button(text="Download Folder", command=browse_button).place(relx=0.35, rely=0.3)
    videopath = Entry(root, width=22)
    videopath.place(relx=0.3, rely=0.2)
    button3 = Button(text="Convert!", command=sendtoconvert).place(relx=0.4, rely=0.7)
    for text, value, relx, rely in [['Video (mp4)', 'mp4', 0.4, 0.45], ['Audio (mp3)', 'mp3', 0.4, 0.55]]:
        Radiobutton(root, text=text, variable = v, value=value,indicatoron=0).place(relx=relx, rely=rely)
    mainloop()
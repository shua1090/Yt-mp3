# Yt-mp3
## Output
This program, when run properly, creates a TKinter application allowing the user to download youtube videos as *mp4s* or *mp3s* to a certain folder
## Dependencies
This **Python 3.8** program requires the following dependencies:
```python
import pytube #Download Youtube video
import glob
import moviepy #Mp4 -> Mp3

```
along with the built-in modules: 
```python
import RegEx
import TKinter #GUI
import os #File Management
```

## Use
The python file can be run normally, or its functions used in a import format. I recommend changing the name of the python file or copying parts of the code if it is necessary to use it 
similar to a module. For example:
```python
from main import convert
```
is not very feasible. The reason the file is named main is because this was meant to be stand-alone only, as referenced by the GUI.

## 2020.7 alpha update 1: Threading
Using the threading module, the Graphical Interface no longer freezes when downloading.
Furthermore, one can now download multiple videos or multiple playlists while only running
one instance of this program. This allows for quick throughput and a faster average download time:
 instead of downloading 10 files a minute, it creates a new thread so that it can do as many requested files
 as possible at the same time. Theoretically, it can do all requested videos in a time less than 30 seconds, but due to the implementation
 of the playlist feature, this ability cannot be demonstrated feasibly. The threading function will be further implemented in the next minor update
 to allow the downloading of multiple parts of a playlist at the same time - proof that the above concept can be demonstrated realistically.
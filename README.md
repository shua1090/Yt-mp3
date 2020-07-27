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

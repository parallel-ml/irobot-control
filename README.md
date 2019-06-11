# We are not using this repos anymore. Please use [pycreate2](https://github.com/parallel-ml/pycreate2) library instead.


## Control with Keyboard
Make sure Pi is connected to power and serial  

```bash
ssh -X pi@192.168.1.2 
sudo chmod o+rw /dev/ttyUSB0  
gtkterm
```

Configure port to USB0  
Change baud rate to 115200  

```bash
python create2_cmds.py  
```

Click connect and type /dev/ttyUSB0 (the above)  
Press 'p' then 'f'  
The robot is now controllable  

To see data from sensors (power):
 - View -> Hexadecimal  
 - Log -> to somelogfile.txt  
 - Go to python and press 'z' to begin log stream  
 - Do whatever (ML stuff)  
 - Stop logging from log menu when done  
 - translatorStream.py -> change file read name to somelogfile.txt (whatever name)  
 - python translatorStream.py  
 - done.txt contains voltage and current values  


## Capture Video/Image
Install streamer:
```bash
sudo apt-get install streamer
```

Record video or capture 
```bash
streamer -q -c /dev/video0 -r 10 -t 00:00:20 -s 640x480 -o ~/test0000.jpeg
streamer -q -c /dev/video0 -f rgb24 -t 00:01:30 -r 10 -s 640x480 -o ~/outfile.avi
ffmpeg -i outfile.avi -acodec libmp3lame -ab 192 output.mov
```

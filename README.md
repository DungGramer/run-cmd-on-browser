<p align="center">
  <a href="https://github.com/DungGramer/run-cmd-on-browser/releases/"><img src="images/preview.png" alt="run-cmd-on-browser" width="400px"></a>
</p>

## Usage
1. Download [command.exe](https://github.com/DungGramer/run-cmd-on-browser/releases/download/1.0/command.exe) and move to path `C:\command.exe`.  
2. After that, run `setup.reg`.  

Note: 
+ If you want change file name or path, you need edit path inside `setup.reg` before run.
+ Maybe window define is virus. Don't worry! Just allow on your device.
  
  
Command: `cmd:// + cmd-command`  
Example:
```bash
cmd://winver
cmd://md "D:\\new folder"
```

## Build
```bash
pyinstaller -F --onefile --icon="./icon.ico" ./command.py
```

## Idea
My project extend idea of Enderman:  
[https://www.youtube.com/watch?v=46pBeyHKQuQ&t=200s](https://www.youtube.com/watch?v=46pBeyHKQuQ&t=200s)

## Usage
Download `command.exe` and move to path `C:\command.exe`. After that, run `setup.reg`.
If you want change file name or path, you need edit path inside `setup.reg` before run.

`cmd:// + command`
```bash
cmd://winver
cmd://md "D:\\new folder"
```

## Build
```bash
pyinstaller -F --onefile --icon="./icon.ico" ./command.py
```
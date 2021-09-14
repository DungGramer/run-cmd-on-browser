## Usage
`cmd:// + command`
```bash
cmd://winver
cmd://md "D:\\new folder"
```

## Build
```bash
pyinstaller -F --onefile --icon="./icon.ico" ./command.py
```
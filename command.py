from urllib.parse import unquote
import os
import sys

# Decode URL to string
def decode(url):
    url = url.replace('cmd://', '')
    url = url[:-1]
    return unquote(url)


url = decode(sys.argv[1])

print(url)
os.system(url + ' &echo Press enter to exit &pause >nul')

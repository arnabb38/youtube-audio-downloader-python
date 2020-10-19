# Author : Arnab Basak

import pafy

url = input("Enter the URL: ")
video = pafy.new(url)

audiostream = video.audiostreams

for i in audiostream:
    print(i.get_filesize())

print(video.title)


# Author : Arnab Basak

import pafy

url = input("Enter the URL: ")
video = pafy.new(url)

audiostream = video.getbestaudio()

# for a in audiostream:
#     print(a.bitrate, a.extension, a.get_filesize())

print("\n" + video.title)
print("\nStart Downloading Audio...")

audiostream.download(quiet=False)

print("\nDownload Successful. Please check in the current directory")

import pafy

videoUrl = raw_input("Enter URL: ")

video = pafy.new(videoUrl)

audiostreams = video.audiostreams

print("Available Audio Formats: ")

for a in audiostreams:
    print(a.extension,a.get_filesize())

b = int(raw_input("Choose from above format. Enter from 1-5: "))
if b == 1:
    audiostreams[0].download()
    print("Download Complete!")
elif b == 2:
    audiostreams[1].download()
    print("Download Complete!")
elif b == 3:
    audiostreams[2].download()
    print("Download Complete!")
elif b == 4:
    audiostreams[3].download()
    print("Download Complete!")
elif b == 5:
    audiostreams[4].download()
    print("Download Complete!")
else:
    print("Wrong input!")

import pafy

videoUrl = raw_input("Enter URL: ")

video = pafy.new(videoUrl)

audiostreams = video.audiostreams

print("Available Audio Formats: ")

for a in audiostreams:
    print(a.extension,a.get_filesize())

b = int(raw_input("Choose from above format. Enter from 1-5: "))
if b == 1:
    audiostreams[0].download(filepath="/home/usama/Desktop")
    print("Download Complete!")
elif b == 2:
    audiostreams[1].download(filepath="/home/usama/Desktop")
    print("Download Complete!")
elif b == 3:
    audiostreams[2].download(filepath="/home/usama/Desktop")
    print("Download Complete!")
elif b == 4:
    audiostreams[3].download(filepath="/home/usama/Desktop")
    print("Download Complete!")
elif b == 5:
    audiostreams[4].download(filepath="/home/usama/Desktop")
    print("Download Complete!")
else:
    print("Wrong input!")

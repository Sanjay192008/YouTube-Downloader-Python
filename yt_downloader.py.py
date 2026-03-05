from pytubefix import YouTube

link = input("Enter YouTube video link: ")

yt = YouTube(link)

print("Title:", yt.title)
print("Length:", yt.length)

streams = yt.streams.filter(progressive=True)

print("Available Resolutions:")

i = 0
for stream in streams:
    print(i, ":", stream.resolution)
    i = i + 1

choice = int(input("Select resolution number: "))

video = streams[choice]

print("Downloading...")
video.download()

print("Download Completed!")
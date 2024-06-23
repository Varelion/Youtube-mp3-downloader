import yt_dlp
import sys

def download_audio(url):
	ydl_opts = {
		'format': 'bestaudio/best',
		'postprocessors': [{
			'key': 'FFmpegExtractAudio',
			'preferredcodec': 'mp3',
			'preferredquality': '192',
		}],
		'outtmpl': r'./yt_dlp_downloads/%(title)s.%(ext)s',
		'ffmpeg_location': r'C:\ffmpeg\bin'  # Adjust this path to where your FFmpeg is actually installed
	}

	with yt_dlp.YoutubeDL(ydl_opts) as ydl:
		ydl.download([url])

# Example usage
videos_to_download = [
]

if len(sys.argv) > 1:
	for argument in sys.argv[1:]:
		download_audio(argument)

elif len(videos_to_download) > 0:
	for video_url in videos_to_download:
		download_audio(video_url)

else:
	print("You can either put in a single YT playlist, \n and it will download the entire playlist. Or, multiple videos to download.\n Type 'exit' or 0 or enter on an empty line to stop inputting videos")

	videos_to_download = []

	while True:
		if len(videos_to_download)>0:
			print(f'Last download link was: {videos_to_download[-1]}')
		inp = input("Enter video url:\n")
		if inp == 'exit' or inp == '0' or inp =="":
			break
		videos_to_download.append(inp)

	for video_url in videos_to_download:
		download_audio(video_url)



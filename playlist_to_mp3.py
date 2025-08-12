# Install yt-dlp first:
# pip install yt-dlp
# Make sure FFmpeg is installed and in PATH

import yt_dlp

# Paste your playlist link here
playlist_url = "https://youtube.com/playlist?list=PLYJE_nhe9DTIdBe552HBveRGZh4xpI68A&si=5wgEunxcDltQrbN3"

# List to store unavailable or failed videos
missing_videos = []

# Hook to track download status
def my_hook(d):
    if d['status'] == 'error':
        title = d.get('title') or d.get('id') or 'Unknown video'
        missing_videos.append(title)

# Download settings
ydl_opts = {
    'format': 'bestaudio/best',                # Best audio quality
    'outtmpl': '%(playlist_index)s - %(title)s.%(ext)s',  # Number + title
    'noplaylist': False,                       # Download whole playlist
    'ignoreerrors': True,                      # Skip errors, continue
    'download_archive': 'downloaded.txt',      # Avoid re-downloading
    'progress_hooks': [my_hook],               # Track errors
    'quiet': False,                            # Show progress
    'postprocessors': [
        {   # Convert to MP3
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',         # 192 kbps
        }
    ]
}

# Run downloader
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])

# Save missing videos to a file
if missing_videos:
    with open("missing_videos.txt", "w", encoding="utf-8") as f:
        for vid in missing_videos:
            f.write(vid + "\n")
    print("\n⚠ Missing videos saved to missing_videos.txt")
else:
    print("\n✅ All videos downloaded successfully!")

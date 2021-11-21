from pathlib import Path
import tempfile


def upload_videos(video):
    with tempfile.TemporaryDirectory() as videos:
        temp_video = Path(videos) / 'uploaded_video'
        video.save(temp_video)
        if video.file_name:
            return [temp_video, video.file_name]
    return [temp_video, 'noname']

import cv2
from capable_video.video_app.data import CapturedVideo


def process_videos(temp_video):
    video = cv2.VideoCapture(temp_video[0])
    captured_video = CapturedVideo()
    while video.isOpened():
        key = cv2.waitKey(10)
        captured_video.name = temp_video[1]
        captured_video.width = video.get('CAP_PROP_FRAME_WIDTH')
        captured_video.height = video.get('CAP_PROP_FRAME_HEIGHT')
        captured_video.resolution = int(captured_video.width) * int(captured_video.height)
        captured_video.frame_rate = video.get('CAP_PROP_FPS')
        captured_video.number_of_frames = video.get('CAP_PROP_FRAME_COUNT')
        if cv2.waitKey(1) & key == ord('q'):
            break

    return captured_video

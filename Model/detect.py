from .video1 import detect_video1
from .video2 import detect_video2
    
def detect_video(video_path, video_type, csv_path, skipped=10):
    video_type=video_type  #UI input

    # video_path = '/home/zongyi/Desktop/ocr_lzy/Screen_Recording_20210123-110020_WeChat.mp4'# UI input
    video_path=video_path
    if video_type==1:
        detect_video1(video_path, csv_path, skipped)
    elif video_type==2:
        detect_video2(video_path, csv_path, skipped)
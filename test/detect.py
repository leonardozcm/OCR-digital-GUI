from video1 import detect_video1
from video2 import detect_video2
    
def detect_video(video_path):
    video_type=2   #UI input
    key_items=[]    #UI input 待定，问有哪些key
    # video_path = '/home/zongyi/Desktop/ocr_lzy/Screen_Recording_20210123-110020_WeChat.mp4'# UI input
    video_path=video_path
    if video_type==1:
        detect_video1(video_path, key_items)
    elif video_type==2:
        detect_video2(video_path, key_items)

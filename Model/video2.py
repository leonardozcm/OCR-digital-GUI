from paddleocr import PaddleOCR, draw_ocr
from PIL import Image
import numpy as np
from collections import defaultdict
import cv2
import os
import csv
import re
import copy
import time
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    return False


def contain_hz(contents):
    Pattern = re.compile(u'[\u4e00-\u9fa5]+')
    match = Pattern.search(contents)
    if match:
        return True
    else:
        return False
def is_content(content):
    flag = False
    patter1 = re.compile('^(\-|\+)?\d+(\.\d+)?$')
    patter2 = re.compile('^(\-|\+)?\d+(\:\d+)?$')
    key_item = ["km", "kwh", "hr", "kW", "%", "分钟", "时", "min"]

    if len(content)>5:
        return False
    result1 = patter1.match(content)
    result2 = patter1.match(content)
    if result1 or result2:
        return True
    for end_str in key_item:
        if(content.endswith(end_str) and content.strip()!=end_str):
            return True
    return False
# os.environ["CUDA_VISIBLE_DEVICES"] = "0"

def cal_iou(boxes, box1):
    #boxes [n, 4,2]   box1 [4,2]
    boxes = np.array(boxes)
    box1 = np.array(box1)
    # print(boxes.shape, box1.shape)
    box1=box1[[0,2],:]#, box1[3]] #[2,2]
    boxes=boxes[:,[0,2],:], #boxes[:,3]] #[n,2,2]
    boxes = np.array(boxes)[0]
    # box1 = np.array(box1)
    S_rec1=(box1[1][0]-box1[0][0])*(box1[1][1]-box1[0][1])
    # print(boxes[:,1,0].shape)
    S_rec2=(boxes[:,1,0]-boxes[:,0,0])*(boxes[:,1,1]-boxes[:,0,1])
    # print(S_rec1,S_rec2)
    sum_area = S_rec1 + S_rec2
    # print(sum_area)
    # find the each edge of intersect rectangle
    left_line = np.maximum(box1[0][1], boxes[:,0,1])  #max(rec1[1], rec2[1])
    right_line = np.minimum(box1[1][1], boxes[:,1,1]) #min(rec1[3], rec2[3])
    top_line = np.maximum(box1[0][0], boxes[:,0,0])   #max(rec1[0], rec2[0])
    bottom_line = np.minimum(box1[1][0], boxes[:,1,0])#min(rec1[2], rec2[2])
    # print(top_line, left_line, right_line, bottom_line)
    # print(left_line -right_line, top_line - bottom_line)
    # judge if there is an intersect area
    if np.min(left_line -right_line)>=0 or np.min(top_line-bottom_line)>=0:
        # print("=====")
        return 0
    else:
        x=right_line - left_line
        x=np.where(x > 0, x, 0)
        y=bottom_line - top_line
        y=np.where(y > 0, y, 0)
        intersect = x * y
        return (intersect / (sum_area - intersect)) * 1.0
def detect_video2(video_path, csv_path, skipped):
    csv_path = csv_path
    cap = cv2.VideoCapture(video_path)
    ocr = PaddleOCR()  # need to run only once to download and load model into memory #det_east_score_thresh=0.7
    skip_frames = skipped
    fps = int(round(cap.get(cv2.CAP_PROP_FPS)))
    index_dic = defaultdict(list)
    i=0
    init_str=[]
    capacity = 30
    for ii in range(capacity):
        init_str.append("{0:10}".format("***"))
    f = open(csv_path,'w')  #,encoding='utf-8'
    csv_writer = csv.writer(f)
    csv_writer.writerow(init_str)
    box_list=[]
    
    max_num=1
    while (cap.isOpened()):
        ret, frame = cap.read()
        i+=1

        if not ret:
            break
        #每隔ｎ帧检测
        if i%10!=0:
            continue
        content=copy.deepcopy(init_str)
        result = ocr.ocr(frame)
        count = 0
        duration = str(int(i/fps))+" s"
        content[0]="{0:10}".format(duration)
        for line in result:
            if is_content(line[1][0]):
                info="{0:10}".format(line[1][0])
                # print(line[0])
                if len(box_list)==0:

                    box_list.append(line[0])
                    content[max_num]=info
                    max_num+=1
                    continue
                ious = cal_iou(box_list,line[0])
                if np.max(ious)<=0:
                    if max_num==capacity-1:
                        continue
                    box_list.append(line[0])
                    content[max_num]=info
                    max_num+=1
                    continue
                else:
                    content[np.argmax(ious)+1]=info
        csv_writer.writerow(content)

        print("video current time", int(i/fps),"==================",content)
        # 显示检测图片,并保存到result目录
        # image = Image.fromarray(frame).convert('RGB')
        # boxes = [line[0] for line in result]
        # txts = [line[1][0] for line in result]
        # scores = [line[1][1] for line in result]
        # im_show = draw_ocr(image, boxes, txts, scores, font_path='./simfang.ttf')#
        # im_show = Image.fromarray(im_show)
        # im_show.save('result/'+'result'+str(i)+'.jpg')
    f.close()
    cap.release()
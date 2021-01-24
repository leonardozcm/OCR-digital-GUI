from paddleocr import PaddleOCR, draw_ocr
from PIL import Image

from collections import defaultdict
import cv2
import os
import csv
import time


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    return False


# os.environ["CUDA_VISIBLE_DEVICES"] = "0"
def detect_video2(video_path, key_items):
    csv_path = video_path.split("/")[-1][:-4] + ".csv"
    cap = cv2.VideoCapture(video_path)
    ocr = PaddleOCR()  # need to run only once to download and load model into memory
    fps = int(round(cap.get(cv2.CAP_PROP_FPS)))
    index_dic = defaultdict(list)
    i = 0
    drive_time = ""
    kw = ""
    km_h = ""
    km_1 = ""
    km_2 = ""
    percentage = ""

    f = open(csv_path, 'w')  # ,encoding='utf-8'
    csv_writer = csv.writer(f)
    csv_writer.writerow(["{0:10}".format("时间"), "{0:10}".format("行驶时间"), "{0:10}".format("kw"), "{0:10}".format("kw_h"),
                         "{0:10}".format("km_1"), "{0:10}".format("km_2"), "{0:10}".format("％")])
    while (cap.isOpened()):
        ret, frame = cap.read()
        i += 1
        if not ret:
            break
        # 每隔ｎ帧检测
        if i % 10 != 0:
            continue
        drive_time, kw, km_h, km_1, km_2, percentage = "***", "***", "***", "***", "***", "***"

        result = ocr.ocr(frame)
        count = 0
        for line in result:
            print(line[1][0])
            if (line[1][0].endswith("km") or line[1][0].endswith("kwh")):
                count += 1
                if (line[1][0].startswith('+')):
                    # index_dic("km_1").append(line[1][0])
                    km_1 = line[1][0]
                else:
                    # index_dic("km_2").append(line[1][0])
                    km_2 = line[1][0]
            if (line[1][0].endswith("hr")):
                count += 1
                # index_dic("km_2").append(line[1][0])
                km_h = line[1][0]
            if (line[1][0].endswith("kW")):
                count += 1
                kw = line[1][0]
            if (line[1][0].endswith("%")):
                count += 1
                percentage = line[1][0]
            if ((line[1][0].endswith("分钟") or line[1][0].endswith("时") or line[1][0].endswith("min")) and len(
                    line[1][0]) < 10):
                count += 1
                drive_time = line[1][0]
        duration = str(int(i / fps)) + " s"
        csv_writer.writerow(
            ["{0:10}".format(duration), "{0:10}".format(drive_time), "{0:10}".format(kw), "{0:10}".format(km_h),
             "{0:10}".format(km_2), "{0:10}".format(km_1), "{0:10}".format(percentage)])
        print("video current time", int(i / fps))
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

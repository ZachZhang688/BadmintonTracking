import cv2
import numpy as np

# 调用 correlation filter 跟踪算法
#tracker = cv2.Tracker_create("CSRT")
tracker = cv2.TrackerCSRT_create()
# 读取视频并初始
video = cv2.VideoCapture("222.mp4")
ok, frame = video.read()
bbox = cv2.selectROI(frame, False)
tracker.init(frame, bbox)
filename = "coordinates.txt"  # 要写入的文件名
filename_v = "speed_pixel.txt"
f= open(filename, "w")
f_p = open(filename_v, "w")
# 进行跟踪
while True:
    ok, frame = video.read()
    if not ok:
        break
    
    # 更新跟踪器
    ok, bbox = tracker.update(frame)
    
    # 画出矩形框
    if ok:
        # 跟踪成功
        x, y = ((int(bbox[0]+0.5*bbox[2]), int(bbox[1]+0.5*bbox[3])))
        f.write(str(x) + " " + str(y) + "\n")  # 将坐标写入文件，以空格分隔 x 和 y，以换行符分隔每个坐标

        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        dis=np.sqrt(bbox[2]*bbox[2] + bbox[3]*bbox[3])
        f_p.write(str(dis) + "\n")
        print(dis)
        cv2.circle(frame, (int(bbox[0]+0.5*bbox[2]), int(bbox[1]+0.5*bbox[3])),3, (0,0,255), 2)
        cv2.rectangle(frame, p1, p2, (0, 255, 0), 2, 1)
    else:
        # 跟踪失败
        cv2.putText(frame, "Tracking failed", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
    
    # 显示当前帧
    cv2.imshow("Tracking", frame)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

# 释放资源
video.release()
cv2.destroyAllWindows()


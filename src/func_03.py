import cv2
import pytesseract

# 读取视频
video = cv2.VideoCapture("video.mp4")

# 逐帧读取视频，并对每一帧进行 OCR 处理
while video.isOpened():
    ret, frame = video.read()
    if ret:
        # 将帧转换为灰度图像
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # 对图像进行二值化处理，以便更容易识别文本
        threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        
        # 识别文本
        text = pytesseract.image_to_string(threshold)
        
        # 打印文本
        print(text)
        
        # 显示帧
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# 释放资源
video.release()
cv2.destroyAllWindows()

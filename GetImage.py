import cv2
import time
import imutils

def main():
    cap = cv2.VideoCapture('./video/CaBaSa/CaBaSa.mp4')
    time.sleep(1)
    if cap is None or not cap.isOpened():
        print('Khong the mo file video')
        return
    cv2.namedWindow('Image', cv2.WINDOW_AUTOSIZE);
    n = 1
    dem =1
    while True:
        [success, img] = cap.read()
        ch = cv2.waitKey(30)
        if success:
            #img = imutils.rotate(img, 90)  
            #img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
            imgROI = img[70:(40+480),:]
            imgROI = cv2.resize(imgROI,(640,480))
            cv2.imshow('Image', imgROI)
        else:
            break
        if n%4 == 0:
            filename = './image/CaBaSa/CaBaSa_%04d.jpg'%(dem)
            cv2.imwrite(filename,imgROI)
            dem = dem + 1
        n = n + 1
    return
if __name__ == "__main__":
    main()

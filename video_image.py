import cv2
vidcap = cv2.VideoCapture('./output.mp4')
count = 0
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        name ='./data/frame' + str(count) + '.jpg'
        cv2.imwrite(name, image)    
    return hasFrames
sec = 0
frameRate = 0.5 
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
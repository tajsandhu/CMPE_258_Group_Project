import cv2
import time

start_time = time.time()
proto = './model/pose_deploy_linevec.prototxt'
weights = './model/pose_iter_440000.caffemodel'

dnn = cv2.dnn.readNetFromCaffe(proto, weights)

end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))

start_time = time.time()
frame = cv2.imread('./test.jpg')

blob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (368, 368), (0,0,0), swapRB=False, crop=False)

dnn.setInput(blob)

output = dnn.forward()
height, width = output.shape[2], output.shape[3]
frameWidth, frameHeight = frame.shape[0], frame.shape[1]
for i in range(18):
    probMap = output[0, i, :, :]
    minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)

    x = (frameWidth * point[0]) / width
    y = (frameHeight * point[1]) / height

    cv2.circle(frame, (int(x), int(y)), 15, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)

end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))

cv2.imshow('Trout', frame)
cv2.waitKey(0)
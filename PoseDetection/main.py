import cv2

# start_time = time.time()
proto = './model/pose_deploy_linevec.prototxt'
weights = './model/pose_iter_440000.caffemodel'

dnn = cv2.dnn.readNetFromCaffe(proto, weights)

# end_time = time.time()
# print("--- %s seconds ---" % (end_time - start_time))

frame = cv2.imread('./test2.jpg')
frame_height, frame_width = frame.shape[0], frame.shape[1]
frame_ratio = frame_height / frame_width
dimesions = None
if (frame_height > frame_width):
    new_height = 500
    new_width = int(500 / frame_ratio)
    dimesions = (new_width, new_height)
else:
    new_width = 500
    new_height = int(500 * frame_ratio)
    dimesions = (new_width, new_height)
frame = cv2.resize(frame, dimesions, interpolation=cv2.INTER_AREA)

blob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (368, 368), (0,0,0), swapRB=False, crop=False)

# # start_time = time.time()
dnn.setInput(blob)

output = dnn.forward()
height, width = output.shape[2], output.shape[3]
frame_height, frame_width = frame.shape[0], frame.shape[1]
print(frame.shape)
for i in range(18):
    probMap = output[0, i, :, :]
    minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)

    x = (frame_width * point[0]) / width
    y = (frame_height * point[1]) / height

    cv2.circle(frame, (int(x), int(y)), 15, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)

# # end_time = time.time()
# # print("--- %s seconds ---" % (end_time - start_time))

cv2.imshow('Trout', frame)
cv2.waitKey(0)

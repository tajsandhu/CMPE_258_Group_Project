# CMPE_258_Group_Project

### Instructions
Use readme to download and run yolov4 in tensorflow-yolov4-tflite-master:
https://github.com/hualili/opencv/blob/master/deep-learning-2020S/20-2021S-7c-%23README-yolo4-v2-yy-hl-2021-4-5%20(copy).txt

Follow instructions to setup Anaconda environment, 
download yolov4.weights, and convert the weights from DarkNet to TensorFlow.
Need to save and convert weights on local computer since the yolov4.weights and checkpoint folder are over 200MB, too large to push. 

More info:
- changed `tensorflow-yolov4-tflite-master/core/utils.py` to get bounding box images of person class only
- example Colab detecting person, getting box images, and running pose detector to label poses:
https://colab.research.google.com/drive/1w-97X3vivhkl-bLhTFRI4b56ACK-G9Ui?usp=sharing

### Run
```
cd tensorflow-yolov4-tflite-master/
conda activate yolov4-cpu
python detect.py --weights ./checkpoints/yolov4-416 --size 416 --model yolov4 --images ./data/images/frame0000.jpg
```
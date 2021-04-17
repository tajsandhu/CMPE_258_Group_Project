# CMPE_258_Group_Project

### Development Instructions
##### YOLOv4 object detector
Use linked README to setup and run pre-trained YOLOv4 in `tensorflow-yolov4-tflite-master`:
https://github.com/hualili/opencv/blob/master/deep-learning-2020S/20-2021S-7c-%23README-yolo4-v2-yy-hl-2021-4-5%20(copy).txt

Follow instructions to setup Anaconda environment, 
download yolov4.weights, 
and convert the weights from DarkNet to TensorFlow.
Need to save and convert weights on local computer since the yolov4.weights and checkpoint folder are over 200MB, too large to push. 

##### YOLOv3 pose detector
Then follow subfolder README to setup and run YOLOv3 in `TrainYourOwnYOLO`.
For example, used conda to create virtual environment `yolov3-env` and `pip install` in the environment to install requirements:
```
cd TrainYourOwnYOLO
conda create --name yolov3-env
conda activate yolov3-env
pip install -r requirements.txt
python Minimal_Example.py
```

Training YOLOv3. Activate virtual environment first:
```
cd 1_Image_Annotation
python Convert_to_YOLO_format.py

cd ..
cd 2_Training
python Download_and_Convert_YOLO_weights.py
python Train_YOLO.py 
cd ..
cd 3_Inference
python Detector.py
```

More info:
- changed `tensorflow-yolov4-tflite-master/core/utils.py` to get bounding box images of person class only
- example Colab detecting person, getting box images, and running pose detector to label poses:
https://colab.research.google.com/drive/1w-97X3vivhkl-bLhTFRI4b56ACK-G9Ui?usp=sharing

### Run
Assuming virtual environments are named `yolov4-cpu` and `yolov3-env`.
```
cd tensorflow-yolov4-tflite-master/
conda activate yolov4-cpu
python detect.py --weights ./checkpoints/yolov4-416 --size 416 --model yolov4 --images ./data/images/frame0000.jpg

cd TrainYourOwnYOLO
conda activate yolov3-env
cd 3_Inference
python Detector.py
python create_video_from_images.py
```
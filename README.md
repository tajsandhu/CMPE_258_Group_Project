# CMPE_258_Group_Project

### Run
Assuming virtual environments are named `yolov4-cpu` and `yolov3-env`.
Label poses of people in `tensorflow-yolov4-tflite-master/data/images/frame0000.jpg`
```
# run YOLOv4 to get person bounding boxes
cd tensorflow-yolov4-tflite-master/
conda activate yolov4-cpu
python detect.py --weights ./checkpoints/yolov4-416 --size 416 --model yolov4 --images ./data/images/frame0000.jpg

# run YOLOv3 to get images with pose labels
cd ../TrainYourOwnYOLO
conda activate yolov3-env
cd 3_Inference
python Detector.py
# combine images into a video and show it
python create_video_from_images.py
```

### Results
Graph, video, and detected image results can be found in `results` folder.

View graphs in TensorBoard.dev:
- [YOLOv3 training on images in human-pose-dataset](https://tensorboard.dev/experiment/sJyULVIYTXqtNboXkLK2Ag/)

### Development Instructions
##### YOLOv4 object detector
Use [this linked README](https://github.com/hualili/opencv/blob/master/deep-learning-2020S/20-2021S-7c-%23README-yolo4-v2-yy-hl-2021-4-5%20(copy).txt) to setup and run pre-trained YOLOv4 in `tensorflow-yolov4-tflite-master`.

Follow instructions to setup Anaconda environment, 
download yolov4.weights, 
and convert the weights from DarkNet to TensorFlow.
Need to save and convert weights on local computer since the yolov4.weights and checkpoint folder are over 200MB, too large to push. 

##### YOLOv3 pose detector
Then follow [subfolder README](https://github.com/tajsandhu/CMPE_258_Group_Project/tree/yolo-to-get-pose/TrainYourOwnYOLO) to setup and run YOLOv3 in `TrainYourOwnYOLO`.
For example, used conda to create virtual environment `yolov3-env` and `pip install` in the environment to install requirements:
```
cd TrainYourOwnYOLO
conda create --name yolov3-env
conda activate yolov3-env
pip install -r requirements.txt
python Minimal_Example.py
```
###### Download dataset
The folder `human-pose-dataset` has 100 thumbnail images of size 100x150px.
These are very small and were used to initially train YOLOv3 and check the model could be run successfully.

Download the folder `activities-dataset`, which is manually annotated with bounding boxes and used to train YOLOv3. 
This has more images than `human-pose-dataset` but is over 130MB, too large to push.
Unzip [this folder](https://drive.google.com/file/d/17bsXYzBf6PhBrvgWAe0m-vhhBApgE8ys/view?usp=sharing) and place in main folder of this repo.
So the path should be `CMPE_258_Group_Project/activities-dataset`.

###### Copy YOLOv3 training CSV file and images
Copy folder `vott-csv-export` from dataset and paste in `TrainYourOwnYOLO/Data/Source_Images/Training_Images`.

###### Training YOLOv3.
```
# make sure in right folder and activate virtual environment first
cd TrainYourOwnYOLO
conda activate yolov3-env

# convert the VoTT csv format to the YOLOv3 format
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

###### More info:
- changed `tensorflow-yolov4-tflite-master/core/utils.py` to get bounding box images of person class only
- example Colab detecting person, getting box images, and running pose detector to label poses:
https://colab.research.google.com/drive/1w-97X3vivhkl-bLhTFRI4b56ACK-G9Ui?usp=sharing

### Architecture
![architecture diagram](https://github.com/tajsandhu/CMPE_258_Group_Project/blob/yolo-to-get-pose/architecture-draft-pedestrian-behavior-analysis.png)
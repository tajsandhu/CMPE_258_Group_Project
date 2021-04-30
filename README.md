# CMPE_258_Group_Project

## Setup
#### YOLOv3 pose detector
Follow [subfolder README](TrainYourOwnYOLO) to setup and run YOLOv3 in `TrainYourOwnYOLO`.
For example, used conda to create virtual environment `yolov3-env` and `pip install` in the environment to install requirements:
```
cd TrainYourOwnYOLO
conda create --name yolov3-env
conda activate yolov3-env
pip install -r requirements.txt
python Minimal_Example.py
```

##### Download trained YOLOv3 model
Download the folder with trained YOLOv3 model from link below, unzip, and replace `TrainYourOwnYOLO/Data/Model_Weights` with it.
- [trained on Activities.v4-activitiesset2.0.yolokeras](https://drive.google.com/file/d/1a4IKpRl0rWFes_2PTynfUuweXAc5w8Ex/view?usp=sharing)

##### Dataset
The folder [Activities.v4-activitiesset2.0.yolokeras](Activities.v4-activitiesset2.0.yolokeras) is from the [MPII human pose dataset](http://human-pose.mpi-inf.mpg.de/#overview). 
It is labeled with bounding boxes using [Roboflow exported as Keras YOLO txt format](https://roboflow.com/formats/yolo-keras-txt) 

Copy-paste test folder images into `CMPE_258_Group_Project/TrainYourOwnYOLO/Data/Source_Images/Test_Images`.

## Run
Assuming virtual environment was created named `yolov3-env`.
Label poses of people in `TrainYourOwnYOLO/Data/Source_Images/Test_Images`.
```
# run YOLOv3 to get images with pose labels
cd ../TrainYourOwnYOLO
conda activate yolov3-env
cd 3_Inference
python Detector.py
# combine images into a video and show it
python create_video_from_images.py
```
## Output
You should get the following output:
- detection results in `TrainYourOwnYOLO/Data/Source_Images/Test_Image_Detection_Results`
- results combined in a video in `TrainYourOwnYOLO/video.avi`

## Results
Graph, video, and detected image results can be found in [results](results) folder.

View graphs in TensorBoard.dev:
- [YOLOv3 training on images in Activities.v4-activitiesset2.0.yolokeras](https://tensorboard.dev/experiment/OZ1Do5lxQ3ODDwD4Jduzmw/)

## Development Instructions
Follow setup instructions and run.

#### Training
The dataset [Activities.v4-activitiesset2.0.yolokeras](Activities.v4-activitiesset2.0.yolokeras) is used to train YOLOv3.
If want to train manually, follow below steps:
##### Copy train files and images to YOLOv3 folder
1. Copy-paste `train` folder into `TrainYourOwnYOLO/Data/Source_Images/Training_Images`
2. Rename the `train` folder to `vott-csv-export`.
3. Rename `_classes.txt` to `data_classes.txt` and move into the folder `TrainYourOwnYOLO/Data/Model_Weights`.
4. Edit the script `prepend-absolute-path-to-data-train`, replacing `ABSOLUTE_PATH` with your test images folder absolute path.
Run the script.
This creates a new file `data_train.txt` and prepends the absolute path of the train images folder to each line of the file.
5. Delete `_annotations.txt` since it's no longer needed.

Then follow [training instructions](yolov3-training.txt)

##### More info:
- changed `tensorflow-yolov4-tflite-master/core/utils.py` to get bounding box images of person class only
- [example Colab](https://colab.research.google.com/drive/1w-97X3vivhkl-bLhTFRI4b56ACK-G9Ui?usp=sharing) detecting person, getting box images, and running pose detector to label poses.

## Architecture
![architecture diagram](architecture-pedestrian-behavior-analysis.png)
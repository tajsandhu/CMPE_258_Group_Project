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
- [trained on Activities.v5-activitiessetyolo.yolokeras](https://drive.google.com/file/d/1sjlxVz6CDxbP3Sqz5k41UNIL-tAiVE-I/view?usp=sharing)

##### Dataset
The folder [Activities.v5-activitiessetyolo.yolokeras](Activities.v5-activitiessetyolo.yolokeras) is from the [MPII human pose dataset](http://human-pose.mpi-inf.mpg.de/#overview). 
It is labeled with bounding boxes using [Roboflow exported as Keras YOLO txt format](https://roboflow.com/formats/yolo-keras-txt).

Create a new folder `TrainYourOwnYOLO/Data/Source_Images/Test_Images`.
Copy-paste `test` folder images into it.

## Run
Assuming virtual environment was created named `yolov3-env`.
Label poses of people in `TrainYourOwnYOLO/Data/Source_Images/Test_Images`.
```
# run YOLOv3 to get images with pose labels
cd TrainYourOwnYOLO
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
Graphs, video, and detected image results can be found in [results](results) folder.

View graphs in TensorBoard.dev:
- [YOLOv3 training on images in Activities.v5-activitiessetyolo.yolokeras](https://tensorboard.dev/experiment/Lz6ELxUnSey4cYvxl8kU4w/)

---

## Development Instructions
Follow setup instructions and run.

#### Training
The dataset [Activities.v5-activitiessetyolo.yolokeras](Activities.v5-activitiessetyolo.yolokeras) is used to train YOLOv3.
If want to train manually, follow below steps:
##### Copy train files and images to YOLOv3 folder
1. Copy-paste `train` folder into `TrainYourOwnYOLO/Data/Source_Images/Training_Images`
2. Rename the `train` folder to `vott-csv-export`.
3. Rename `_classes.txt` to `data_classes.txt` and move into the folder `TrainYourOwnYOLO/Data/Model_Weights`.
4. Edit the script `prepend-absolute-path-to-data-train`, replacing `ABSOLUTE_PATH` with your test images folder absolute path.
Run the script.
This creates a new file `data_train.txt` and prepends the absolute path of the train images folder to each line of the file.
5. Delete `_annotations.txt` since it's no longer needed.

Then follow [these training instructions](yolov3-training.txt).

### Calculate mAP:
These were the steps used to calculate Mean Average Precision on test images using [this library](https://github.com/Cartucho/mAP).
1. Copied `_annotations.txt` from `Activities.v5-activitiessetyolo.yolokeras/test` folder
2. Copied `Detection_Results.csv` from `TrainYourOwnYOLO/Data/Source_Images/Test_Image_Detection_Results` into `mAP/script/extras`

`cd mAP/script/extras`

3. Replaced all text in `mAP/script/extras/class_list` with `Activities.v5-activitiessetyolo.yolokeras/test/_classes.txt`

4. To create ground truth mAP library format, ran script:
```
python convert_keras-yolo3.py --gt _annotations.txt
```
Output files were created in `mAP/scripts/extra/from_kerasyolo3/version_20210506002504`

Copied these files into `input/ground-truth/`

5. To create detection result mAP library format, ran script:
```
python create-detection-results-txt-from-csv.py
```
This created a text file using Detection_Results.csv in YOLO Keras format: `detection_results.txt`
Then ran script:
```
python convert_keras-yolo3.py --dr detection_results.txt
```
Output files were created in `mAP/scripts/extra/from_kerasyolo3/version_20210506001906`

Copied these files into `input/detection-results/`

6. Ran script to intersect ground-truth and detection-results files,
in case YOLO misses some images entirely:
```
python intersect-gt-and-dr.py
```

7. Then ran mAP main script:
```
cd mAP
python main.py
```

Copied output folder to [results](results) folder.

##### More info:
- [example Colab](https://colab.research.google.com/drive/1w-97X3vivhkl-bLhTFRI4b56ACK-G9Ui?usp=sharing) detecting person, getting box images, and running pose detector to label poses.

## Architecture
![architecture diagram](architecture-pedestrian-behavior-analysis.png)

## References
- [TrainYourOwnYOLO](https://github.com/AntonMu/TrainYourOwnYOLO)
- [YOLO](https://arxiv.org/abs/1506.02640)
# Converts detection results CSV file to YOLO Keras txt format,
# so mAP library can run script to convert results to its own format

import csv
# open new text file which has results in YOLO keras format
with open("detection_results.txt", "w") as f_out:
    # read from detection results CSV created from detection script in TrainYourOwnYOLO
    with open('Detection_Results.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                # lines written to text file follows format of:
                # https://github.com/gustavovaliati/keras-yolo3
                # Prediction format: x_min,y_min,x_max,y_max,class_id,confidence_score (no space).
                txt_line = row[0] + " " + row[2] + "," + row[3] + "," + row[4] + "," + row[5] + "," + row[6] + "," + row[7] + "\n"
                f_out.write(txt_line)
                print(txt_line)
                line_count += 1
        print(f'Processed {line_count} lines.')

# Create a copy of _annotations.txt named data_train.txt
# Prepend user's absolute path to each line of data_train.txt

import os

ABSOLUTE_PATH = 'C:/Users/mdhsi/OneDrive/Documents/Github/CMPE_258_Group_Project/TrainYourOwnYOLO/Data/Source_Images/Training_Images/vott-csv-export/'

# original file
annotation_file = os.path.join(ABSOLUTE_PATH, '_annotations.txt')
# new file named data_train.txt which uses absolute path of images
data_train_file = os.path.join(ABSOLUTE_PATH, 'data_train.txt')

f = open(annotation_file,'r')
newf = open(data_train_file,'w')
lines = f.readlines() # read old content
for line in lines: # write old content after new
    newf.write(ABSOLUTE_PATH) # write new content at the beginning
    newf.write(line)
newf.close()
f.close()

print("finished creating data_train.txt")
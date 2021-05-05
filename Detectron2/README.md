# Detectron2

## How To Run
* Import Detectron2Train.ipynb into Google Colab.
* Click the **Runtime** tab and select **Change runtime type**.
  * Then change the hardware accelerator to **GPU** and click **SAVE**.
* Find the content folder in the Colab.
  * Create a folder named 'test', 'train', and 'valid'.
  * Extract all the contents of the 'test' folder found in the ActivitesDataset.zip into the newly created 'test' folder.
  * Then, extract all the contents of the 'train' folder found in the ActivitesDataset.zip into the newly created 'train' folder.
  * Finally, extract all the contents of the 'valid' folder found in the ActivitesDataset.zip into the newly created 'valid' folder.
* Next, run the first cell to install Detectron2. By default, Colab has the wrong version of **pyyaml** installed. The runtime must be restarted and the first line must then be run again.
* Finally, run the rest of the file in order. Training should take a little over 30 minutes.

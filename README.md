This is a multi-task learning based on YOLOv5 algorithm. We added counting regression head to replace the original detection head of YOLOv5.
Below is the overview of teh architecture:
                 from  n    params  module                                  arguments                     
  0                -1  1      3520  models.common.Conv                      [3, 32, 6, 2, 2]              
  1                -1  1     18560  models.common.Conv                      [32, 64, 3, 2]                
  2                -1  1     18816  models.common.C3                        [64, 64, 1]                   
  3                -1  1     73984  models.common.Conv                      [64, 128, 3, 2]               
  4                -1  2    115712  models.common.C3                        [128, 128, 2]                 
  5                -1  1    295424  models.common.Conv                      [128, 256, 3, 2]              
  6                -1  3    625152  models.common.C3                        [256, 256, 3]                 
  7                -1  1   1180672  models.common.Conv                      [256, 512, 3, 2]              
  8                -1  1   1182720  models.common.C3                        [512, 512, 1]                 
  9                -1  1    656896  models.common.SPPF                      [512, 512, 5]                 
 10                -1  1    524289  torch.nn.modules.linear.Linear          [524288, 1]                   
Model Summary: 152 layers, 4695745 parameters, 4695745 gradients

We flattened the output of SPPF module and added linear layer after SPPF module. 
Then we used MSEloss to find the loss of the counting number of objects.


To use the code, some changes are needed as shown below:
1. In the file yolo_linear/data/wheat.yaml, users need to change the paths after "train" and "validation". This is the configuration file which contains the path to the train and validation dataset. "nc" means number of classes. "names" means the names of classes. Users should changes this two info as needed.
2. The dataset used for training and validation should be added in yolo_linear/in_data/. User must use this folder structure in order to train the model:
in_data/images/train/  --- This folder contains all images for training.
in_data/images/validation/  --- This folder contains all images for validation.
in_data/labels/train/  --- This folder contains all .txt label files for training.
in_data/labels/validation/  --- This folder contains all .txt label files for validation.

After these setup step, it is ready to train the model. Here is an example of the command:
python train.py --img 1024 --batch 1 --epochs 10 --data wheat.yaml --cfg models/yolov5s.yaml --name wm
All arguments after "python train.py" are optional to use. Users should change some of the parameters if needed. 
"--img" is used to set the image size if all images are uniformaly sized. It is not neccessary to use this argument if images have different sizes.
"--batch" and "--epoch" indicates batch size and epoch size. "--data file_name.yaml" should be changed with the correct configuration file for dataset.
"--cfg config_file.yaml" indicates the configuration file of the model architecture. 

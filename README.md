# PCa_tutorial
Tutorial for the [3D Prostate Cancer Classifier Algorithm](https://github.com/pereaanamaria/prostate_cancer_classifier) repository.

More information about the repository can be found at:
- **3D Prostate Cancer Classifier Algorithm** [README.md](https://github.com/pereaanamaria/prostate_cancer_classifier#readme) file
- **1st Workshop on Deep Learning Algorithms for Space Research and Data Imaging** presentation: [[06/02/2023] Classification Algorithm for Prostate Cancer Lesions using Tridimensional MRI Scans](https://www.youtube.com/watch?v=kJOXOUf10iU).

## Purpose
The purpose of this repository is to serve as a strating point for a better understanding for the Machine Learning workshop organised by The Machine Learning and Data Applications Group in Solar Physics at the School of Mathematics and the Monash Data Futures Institute at Monash University.

**[1st Workshop on Deep Learning Algorithms for Space Research and Data Imaging](https://www.monash.edu/science/schools/school-of-mathematics/events/dl4sr)**
- 6 February 2023 and 23 February 2023

# Setup

## Virtual Environment (Optional)
This step is useful for creating a virtual environment for installing the required Python packages and frameworks, instead of installing them on locally. <br>
Recommended: [Anaconda Distribuition](https://www.anaconda.com/products/distribution)

**If you do not wish to create any virtual environment, just install your preffered Python version and skip to the next step.**
- Python version used: **3.10**

### Create a new conda virtual environment
````
conda create --name pca310 python==3.10
````

### Activate the virtual environment
````
conda activate pca310
````

### Deactivate the virtual environment
````
conda deactivate
````

## PyTorch and Python Packages
Install the [PyTorch framework](https://pytorch.org/) using the command suggested based on your hardware configurations. 
Run the command in your terminal and then install the requiered Python packages:
````
pip install -r requirements.txt
````

## Jupyter Notebook
Change directories until you reach the root folder of your git repository, then run ````jupyter notebook```` in order to launch the platform. You can now run the [tutorial](Classification_Algorithm_PCa.ipynb).


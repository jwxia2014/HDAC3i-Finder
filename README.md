# HDAC3i-Finder

Introduction
-----------------------------------
HDAC3i-Finder is a python GUI application for virtually screening for HDAC3 inhibitors with a thoroughly validated machine-learning model, i.e. a model built with XGBoost as the algorithm and Morgan2 fingerprints as features. It was designed to run on any Windows-based machine.

Availability
-----------------------------------
HDAC3i-Finder and its source code and test case (screening a PubChem library) are available from here: 
https://github.com/jwxia2014/HDAC3i-Finder

Implementation
-----------------------------------
* Dependency

  RDKit 2019.09.3  
  joblib 0.13.2  
  numpy 1.16.5  
  pandas 0.25.1  
  scikit-learn 0.21.3  
  xgboost 1.0.2

* Installation

1. Download and install anaconda--python 3.7--windows 64-Bit from https://www.anaconda.com/products/individual
2. run 'Anaconda Prompt' and run the following commands:
  (1) conda create -n HDAC3 python==3.7 (HDAC3 is an environment set by users)
  (2) conda activate HDAC3
  conda install pandas==0.25.1
  conda install numpy==1.16.5
  conda install joblib==0.13.2
  conda install scikit-learn==0.21.3
  conda install rdkit==2019.09.3
3) Download 'xgboost-1.0.2-cp37-cp37m-win_amd64.whl' from https://www.lfd.uci.edu/~gohlke/pythonlibs/#xgboost
4) Create a new directory, e.g. D:/HDAC3i-Finder and put the file 'xgboost-1.0.2-cp37-cp37m-win_amd64.whl' in D:/HDAC3i-Finder  
5) Run 'Anaconda Prompt' and run the following commands:
   $ conda activate HDAC3
   $ pip install D:/HDAC3i-Finder/xgboost-1.0.2-cp37-cp37m-win_amd64.whl
   $ pip list | findstr xgboost   
   if 'xgboost 1.0.2' returns, xgboost is installed successfully. 

  
Usage
-----------------------------------

## Single Compound mode
This mode is used for predicting a single compound  to be an active or not.
Model need to be loaded before predicting.

## A Set of Compound mode
This mode is used for predicting a set of compounds.
Model need to be loaded before predicting.
Compounds should be save in a csv file, and two columns named 'IDNUMBER' and 'SMILES' are essential.
The output is a CSV file with bioactivity predicted by model of each compound. 


Documentation
-----------------------------------

* The manual for the Python GUI application and the files for the case study are available at this website, i.e. 'manual.for.MUBD-Decoymaker2.0.pdf' and 'Case-ACM4-Agonists.zip'.


Installation
-----------------------------------

* We recommend the users to run the Python GUI application on Windows-based machines, as all the dependencies have been included. Please note we used the machine with Intel Core(TM) i7-7700 CPU@3.60GHz and RAM of 16 GB for testing the tool. The computation time for the test case of ACM Agonists was 1882 seconds. 

Dependency 
-----------------------------------
RDKit (Version 2019.9)

joblib 0.13.2

numpy 1.16.5

pandas 0.25.1

References
-----------------------------------
If you find it useful, please cite: 
Li, S., Ding Y., Chen, M., Chen Y., Kirchmair J., Zhu Z., Wu, S., Xia, J.*, HDAC3i-Finder: A Machine Learning-based Computational Tool to Screen for HDAC3 Inhibitors. Mol. Inf.,2020, submitted. 

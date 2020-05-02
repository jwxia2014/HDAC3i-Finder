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
    $ conda create -n HDAC3 python==3.7 (HDAC3 is an environment set by users)
  
    $ conda activate HDAC3
  
    $ conda install pandas==0.25.1
  
    $ conda install numpy==1.16.5
  
    $ conda install joblib==0.13.2
  
    $ conda install scikit-learn==0.21.3
  
    $ conda install rdkit==2019.09.3
  
3. Download 'xgboost-1.0.2-cp37-cp37m-win_amd64.whl' from https://www.lfd.uci.edu/~gohlke/pythonlibs/#xgboost
4. Create a new directory, e.g. D:/HDAC3i-Finder and put the file 'xgboost-1.0.2-cp37-cp37m-win_amd64.whl' in D:/HDAC3i-Finder  
5. Run 'Anaconda Prompt' and run the following commands:

   $ conda activate HDAC3
   
   $ pip install D:/HDAC3i-Finder/xgboost-1.0.2-cp37-cp37m-win_amd64.whl
   
   $ pip list | findstr xgboost (if 'xgboost 1.0.2' returns, xgboost is installed successfully) 

* Run HDAC3i-Finder
1. download HDAC3i-Finder.py and put it in a directory, e.g. D:/HDAC3i-Finder  
2. Run 'Anaconda Prompt' and run the following commands:

    $ conda activate HDAC3
  
    $ python D:/HDAC3i-Finder/HDAC3i-Finder.py (The GUI application will be shown)

Usage
-----------------------------------
* Single Compound mode

  This mode is used for predicting whether a single compound is active for HDAC3 or not.  
  1. click the 'load a model' to load the machine-learning model and paste SMILES of a compound to predict. 
  2. click the 'Classify' button and the activity class of the compound is shown in the textbox along with the probability of the activity class. 

* A Set of Compounds mode (virtual screening)

  This mode is used for virtual screening of a large chemical library.  
  1. click the 'load a model' to load the machine-learning model and provide a csv file with 'IDNUMBER' and 'SMILES' of the compounds to predict. 
  2. click the 'Classify' button and a csv file that contains activity classes with probability values of "being ACITVE" in a descending order returns.  

References
-----------------------------------
If you find HDAC3i-Finder useful, please cite: 

Li, S., Ding Y., Chen, M., Chen Y., Kirchmair J., Zhu Z., Wu, S., Xia, J.*, HDAC3i-Finder: A Machine Learning-based Computational Tool to Screen for HDAC3 Inhibitors. Mol. Inf.,2020, submitted. 

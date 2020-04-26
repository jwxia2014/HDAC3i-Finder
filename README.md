# HDAC3i-Finder

Introduction
-----------------------------------
HDAC3i-Finder is a python GUI application for classify compounds into HDAC3 inhibitors or non-inhibitors based on a machine-learning approach, i.e. XGBoost algorithm with Morgan2 fingerprints as features. It provides two modes, "a single compound" or "a set of compounds" (virtual screening) and can run on Windows-based machine and has no dependency.
  
Availability & Implementation
-----------------------------------

* Due to the large size, the Python GUI application has been uploaded to the cloud drives and is accessible from there：
  https://www.dropbox.com/s/dfa35t2jb0fnarx/MUBD-DecoyMaker2.0.exe?dl=0     (Outside China) or
  https://pan.baidu.com/s/110FJY6YHxcaUmI7fSyUSkw  (China)


Documentation
-----------------------------------

* The manual for the Python GUI application and the files for the case study are available at this website, i.e. 'manual.for.MUBD-Decoymaker2.0.pdf' and 'Case-ACM4-Agonists.zip'.


Installation
-----------------------------------

* We recommend the users to run the Python GUI application on Windows-based machines, as all the dependencies have been included. Please note we used the machine with Intel Core(TM) i7-7700 CPU@3.60GHz and RAM of 16 GB for testing the tool. The computation time for the test case of ACM Agonists was 1882 seconds. 
 


References
-----------------------------------
Computational tool, Methodology and Datasets:
1. Li, S., Ding Y., Chen, M., Chen Y., Kirchmair J., Wu, S., Xia, J.*, HDAC3i-Finder: A Machine Learning-based Computational Tool to Screen for HDAC3 Inhibitors. Mol. Inf.,2020, submitted. 
https://doi.org/10.1002/minf.201900151 (Tool)


# Usage

## Single Compound mode

This mode is used for predicting a single compound  to be an active or not.

Model need to be loaded before predicting.

## A Set of Compound mode

This mode is used for predicting a set of compounds.

Model need to be loaded before predicting.

Compounds should be save in a csv file, and two columns named 'IDNUMBER' and 'SMILES' are essential.

The output is a CSV file with bioactivity predicted by model of each compound. 

# Dependency
RDKit (Version 2019.9)

joblib 0.13.2

numpy 1.16.5

pandas 0.25.1

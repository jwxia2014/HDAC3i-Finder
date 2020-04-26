### The HDAC3i-Finder is a python a python GUI application on windows for easily screeming HDAC3 inhibitors

# Usage

## Single Compound mode

This mode is used for predicting a single compound  to be an active or not.

Model need to be loaded before predicting.

## A Set of Compound mode

This mode is used for predicting a set of compounds.

Model need to be loaded before predicting.

Compounds should be save in a csv file, and two columns named 'IDNUMBER' and 'SMILES' are essential.

The output is a CSV file with bioactivity predicted by model of each compound. 

# Dependence
RDKit (Version 2019.9)

joblib 0.13.2

numpy 1.16.5

pandas 0.25.1

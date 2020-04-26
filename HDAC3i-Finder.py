import os
import joblib
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import Label
from tkinter import Entry
from tkinter import messagebox
from datetime import datetime
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import MolFromSmiles
from rdkit.Chem.AllChem import GetMorganFingerprintAsBitVect
import threading


#=================================================================================
win = tk.Tk()       
win.title("HDAC3i-Finder")
win.geometry('575x400')
tabControl = ttk.Notebook(win) 

lf1 = tk.LabelFrame(win,text = 'A Single Compound' ,font = ('Times',13))
lf1.pack(expand=1, fill="both")
tabControl.add(lf1, text='A Compound')

lf2 = tk.LabelFrame(win,text = 'A Set of Compounds' ,font = ('Times',13))
lf2.pack(expand=1, fill="both")
tabControl.add(lf2, text='A Set of Compounds')

tabControl.pack(expand=1, fill="both")
#====================================================================================
#page 1
#load model
label0 = Label(lf1,text = 'Model File Directory').grid(row=0,column=0,padx = 10)
entry0 = Entry(lf1)
entry0.grid(row=0,column=1, ipadx=50,padx = 50,pady = 10)

def model_load():
    try:
        model_path = str(entry0.get()).replace("\n","")
        global model
        model = joblib.load(model_path)
        messagebox.showinfo('Info','Model Loaded!')
    except IOError:
        messagebox.showinfo('Info','Invalid Path!')

#load button
load_button = tk.Button(lf1,text='Load a model',width=10,command=model_load)
load_button.grid(row=1,column=1,ipadx=5,padx = 20,pady = 10)

#input SMILES
label1 = Label(lf1,text = 'SMILES').grid(row=2,column=0,padx = 20)
entry_in = Entry(lf1)
entry_in.grid(row=2,column=1, ipadx=50,padx = 50,pady = 20)

label2 = Label(lf1,text = 'Activity Class').grid(row=4,column=0)
class_type = tk.Text(lf1,width=20,height=2)
class_type.grid(row=4,column=1,padx=20,pady = 4)
label3 = Label(lf1,text = ' Activity Class Probability').grid(row=5,column=0)
pro_value = tk.Text(lf1,width=20,height=2)
pro_value.grid(row=5,column=1,padx=20,pady = 4)

def compute(smi):
    mol_target = MolFromSmiles(smi)
    fps_morgan2 = GetMorganFingerprintAsBitVect(mol_target, 2, 1024)
    fps_morgan2 = np.array(fps_morgan2).reshape(1,-1)
    class_pre = model.predict(fps_morgan2)
    probability = max(model.predict_proba(fps_morgan2.reshape(1,-1))[0])
    return (class_pre,probability)

def ml_classifier():
    if class_type.get('0.0','end') != None:
        class_type.delete('1.0','end')
    if pro_value.get('0.0','end') != None:
        pro_value.delete('1.0','end')
    Smi_entry = entry_in.get()
    class_type_ = 'INACTIVE'
    class_pre = compute(Smi_entry)[0]
    probability = round(compute(Smi_entry)[1],4)
    if class_pre == 1:
        class_type_ = 'ACTIVE'
    class_type.insert('0.0',class_type_)
    pro_value.insert('0.0',probability)

#compute button
ml_compute = tk.Button(lf1,text='Classify',width=10,command=ml_classifier)
ml_compute.grid(row=3,column=1,ipadx=5,padx = 20,pady = 10)

def reset():
    class_type.delete('1.0','end')
    pro_value.delete('1.0','end')
    entry_in.delete(0,'end')

#reset button
reset_button = tk.Button(lf1,text='Reset',width=10,command=reset)
reset_button.grid(row=6,column=1,ipadx=5,padx = 20,pady = 20)

#=================================================================================================
#page2
#compute morgan2 fingerprints

def Fingerprint_compute(Smi):
    try:
        mol = Chem.MolFromSmiles(Smi)
        fp_hash = AllChem.GetMorganFingerprintAsBitVect(mol,2,nBits=1024)
        fp = fp_hash.ToBitString()
        return fp
    except:
        return ('error')

def Compute(df):
    length = len(df)
    List_smiles = df['SMILES']
    List_type = df['IDNUMBER']

    List_fp = []
    for i in range(0,length):
        smi = List_smiles[i]
        if smi == 'error':
            continue
        else:
            fp = Fingerprint_compute(smi)
            fp_split = list(str(fp))
            List_fp.append(fp_split)
    df_fp = pd.DataFrame(List_fp)
    return df_fp

#transform class type form 1 to active
def class_type2(class_pre):
    flag = 'Inactive'
    if class_pre == 1:
        flag = 'Active'
    return flag

pd.set_option('mode.chained_assignment', None)
#predict
def predict_class(df_data,model_pre,out_path):
    df_pre = Compute(df_data)
    X = np.array(df_pre)
    class_pre = model_pre.predict(X)
    proba_pre = model_pre.predict_proba(X)
    list_active   = [x[1] for x in proba_pre]
    list_inactive = [x[0] for x in proba_pre]
    df_pre.insert(0,'IDNUMBER',df_data['IDNUMBER'])
    df_pre.insert(1,'SMILES',df_data['SMILES'])
    df_pre.insert(2,'class_pre',class_pre)
    df_pre.insert(3,'Probability_active',list_active)
    df_pre.insert(4,'Probability_inactive',list_inactive)

    df_pre['Bioactivity_pre'] = df_pre['class_pre'].apply(class_type2)

    df_pre = df_pre[['IDNUMBER','SMILES','Bioactivity_pre','Probability_active']]
    df_pre_final = df_pre.sort_values(by="Probability_active",ascending= False)  
    df_pre_final.to_csv(out_path,index=None)

#load model
label20 = Label(lf2,text = 'Model File Directory').grid(row=0,column=0,padx = 10)
entry20 = Entry(lf2)
entry20.grid(row=0,column=1, ipadx=50,padx = 10,pady = 10)

def model_load2():
    try:
        model_path = str(entry20.get()).replace("\n","")
        global model2
        model2 = joblib.load(model_path)
        messagebox.showinfo('Info','Model Loaded!')
    except IOError:
        messagebox.showinfo('Info','Invalid Path!')

#load model button
load_button2 = tk.Button(lf2,text='Load a model',width=10,command=model_load2)
load_button2.grid(row=0,column=2,ipadx=15,padx = 10,pady = 10)

#load SMILES label
label21 = Label(lf2,text = 'Compounds File Directory').grid(row=1,column=0,padx = 10)
entry21 = Entry(lf2)
entry21.grid(row=1,column=1, ipadx=50,padx = 10,pady = 20)

#load SMILES
def molecules_load():
    try:
        molecule_path = str(entry21.get()).replace("\n","")
        global out_path
        out_path = os.path.splitext(molecule_path)[0] + '_pre.csv'
        global df_SMILES
        df_SMILES = pd.read_csv(molecule_path)
        messagebox.showinfo('Info','Molecules Loaded!')
    except IOError:
        messagebox.showinfo('Info','Invalid Path!')

#load SMILES button
smi_button = tk.Button(lf2,text='Load compounds',width=10,command=molecules_load)
smi_button.grid(row=1,column=2,ipadx=15,padx = 10,pady = 20)

def molecule_classify():
    print ('Start Time : ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    starttime = datetime.now()
    print('Predicting, Waite please~')

    predict_class(df_SMILES,model2,out_path)

    print('Predicted!')
    print ('End Time : ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    endtime = datetime.now()
    print ('total time: ' + str((endtime - starttime).seconds) + ' seconds')


def th_molecule_classify():
    thread = threading.Thread(target = molecule_classify)
    thread.start()

classify_button = tk.Button(lf2,text='Classify',width=10,command=th_molecule_classify)
classify_button.grid(row=2,column=1,ipadx=5,ipady = 5,padx = 10,pady = 20)

def reset():
    entry20.delete(0,'end')
    entry21.delete(0,'end')

#reset button
reset_button = tk.Button(lf2,text='Reset',width=10,command=reset)
reset_button.grid(row=2,column=2,ipadx=5,padx = 10,pady = 20)

win.mainloop()

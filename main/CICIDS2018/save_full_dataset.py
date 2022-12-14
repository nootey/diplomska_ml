# imports
import sys
import os
sys.path.append('../..')
from vardata import *

import numpy as np 
import pandas as pd 
import pickle

#helper functions
def clean_column(column):
    column = column.strip(' ')
    column = column.replace('/', '_')
    column = column.replace(' ', '_')
    column = column.lower()
    return column

#define paths
paths = [
    
    os.path.join(DATASET_DIR, DATASET_NAME, '02-14-2018.csv'),
    os.path.join(DATASET_DIR, DATASET_NAME, '02-15-2018.csv'), #Benign, Bruteforce, Dos
    os.path.join(DATASET_DIR, DATASET_NAME, '02-16-2018_0.csv'),
    os.path.join(DATASET_DIR, DATASET_NAME, '02-16-2018_1.csv'),
    os.path.join(DATASET_DIR, DATASET_NAME, '02-21-2018.csv'), #Benign, DDOS attack-HOIC, DoS attacks-Hulk, DoS attacks-SlowHTTPTest, DDOS attack-LOIC-UDP
    os.path.join(DATASET_DIR, DATASET_NAME, '02-22-2018.csv'),
    os.path.join(DATASET_DIR, DATASET_NAME, '02-23-2018.csv'), #Benign, Brute Force -Web, Brute Force -XSS, SQL Injection
    os.path.join(DATASET_DIR, DATASET_NAME, '02-28-2018.csv'),    
    os.path.join(DATASET_DIR, DATASET_NAME, '/03-01-2018.csv'), #Benign, Infilteration
    # os.path.join(DATASET_DIR, DATASET_NAME, '/02-20-2018.csv'), #big chungus
]

# optimize datatypes for easier processing
dtypes = np.dtype([
    ('Dst Port', np.int32),
    ('Protocol', np.int8),
    ('Timestamp', object),
    ('Flow Duration', np.int64),
    ('Tot Fwd Pkts', np.int16),
    ('Tot Bwd Pkts', np.int16),
    ('TotLen Fwd Pkts', np.int32),
    ('TotLen Bwd Pkts', np.int32),
    ('Fwd Pkt Len Max', np.int32),
    ('Fwd Pkt Len Min', np.int32),
    ('Fwd Pkt Len Mean', np.float64),
    ('Fwd Pkt Len Std', np.float64),
    ('Bwd Pkt Len Max', np.int16),
    ('Bwd Pkt Len Min', np.int16),
    ('Bwd Pkt Len Mean', np.float64),
    ('Bwd Pkt Len Std', np.float64),
    ('Flow Byts/s', np.float64),
    ('Flow Pkts/s', np.float64),
    ('Flow IAT Mean', np.float64),
    ('Flow IAT Std', np.float64),
    ('Flow IAT Max', np.int64),
    ('Flow IAT Min', np.int32),
    ('Fwd IAT Tot', np.int32),
    ('Fwd IAT Mean', np.float32),
    ('Fwd IAT Std', np.float64),
    ('Fwd IAT Max', np.int32), 
    ('Fwd IAT Min', np.int32),
    ('Bwd IAT Tot', np.int32),
    ('Bwd IAT Mean', np.float64),
    ('Bwd IAT Std', np.float64),
    ('Bwd IAT Max', np.int64),
    ('Bwd IAT Min', np.int64),
    ('Fwd PSH Flags', np.int8),
    ('Bwd PSH Flags', np.int8),
    ('Fwd URG Flags', np.int8),
    ('Bwd URG Flags', np.int8),
    ('Fwd Header Len', np.int32),
    ('Bwd Header Len', np.int32),
    ('Fwd Pkts/s', np.float64),
    ('Bwd Pkts/s', np.float64),
    ('Pkt Len Min', np.int16),
    ('Pkt Len Max', np.int32),
    ('Pkt Len Mean', np.float64),
    ('Pkt Len Std', np.float64),
    ('Pkt Len Var', np.float64),
    ('FIN Flag Cnt', np.int8),
    ('SYN Flag Cnt', np.int8),
    ('RST Flag Cnt', np.int8),
    ('PSH Flag Cnt', np.int8),
    ('ACK Flag Cnt', np.int8),
    ('URG Flag Cnt', np.int8),
    ('CWE Flag Count', np.int8),
    ('ECE Flag Cnt', np.int8),
    ('Down/Up Ratio', np.int64),
    ('Pkt Size Avg', np.float32),
    ('Fwd Seg Size Avg', np.float32),
    ('Bwd Seg Size Avg', np.float32),
    ('Fwd Byts/b Avg', np.int8),
    ('Fwd Pkts/b Avg', np.int8),
    ('Fwd Blk Rate Avg', np.int8),
    ('Bwd Byts/b Avg', np.int8),
    ('Bwd Pkts/b Avg', np.int8),
    ('Bwd Blk Rate Avg', np.int8),
    ('Subflow Fwd Pkts', np.int16),
    ('Subflow Fwd Byts', np.int32),
    ('Subflow Bwd Pkts', np.int16),
    ('Subflow Bwd Byts', np.int32),
    ('Init Fwd Win Byts', np.int32), 
    ('Init Bwd Win Byts', np.int32),
    ('Fwd Act Data Pkts', np.int16),
    ('Fwd Seg Size Min', np.int8),
    ('Active Mean', np.float64),
    ('Active Std', np.float64),
    ('Active Max', np.int32),
    ('Active Min', np.int32),
    ('Idle Mean', np.float64),
    ('Idle Std', np.float64),
    ('Idle Max', np.int64),
    ('Idle Min', np.int64),
    ('Label', object)
])

# fetch the training file
print(bcolors.WARNING + "Reading files" + bcolors.ENDC)

df1 = pd.read_csv(paths[0], dtype=dtypes) #bruteforce
df2 = pd.read_csv(paths[1], dtype=dtypes) #dos
#df3 = pd.read_csv(paths[2], dtype=dtypes) #dos
#df4 = pd.read_csv(paths[3], dtype=dtypes) #dos /
df5 = pd.read_csv(paths[4], dtype=dtypes) #ddos hoic
df6 = pd.read_csv(paths[5], dtype=dtypes) #brute web /
df7 = pd.read_csv(paths[6], dtype=dtypes) #brute web /
df8 = pd.read_csv(paths[7], dtype=dtypes) #infilteration /

# print(bcolors.WARNING + "DF1" + bcolors.ENDC)
# print(df1['Label'].value_counts())
# print(len(df1))
# print(bcolors.WARNING + "DF2" + bcolors.ENDC)
# print(df2['Label'].value_counts())
# print(len(df2))
# print(bcolors.WARNING + "DF3" + bcolors.ENDC)
# print(df3['Label'].value_counts())
# print(len(df3))
# print(bcolors.WARNING + "DF4" + bcolors.ENDC)
# print(df4['Label'].value_counts())
# print(len(df4))
# print(bcolors.WARNING + "DF5" + bcolors.ENDC)
# print(df5['Label'].value_counts())
# print(len(df5))
# print(bcolors.WARNING + "DF6" + bcolors.ENDC)
# print(df6['Label'].value_counts())
# print(len(df6))
# print(bcolors.WARNING + "DF7" + bcolors.ENDC)
# print(df7['Label'].value_counts())
# print(len(df7))
# print(bcolors.WARNING + "DF8" + bcolors.ENDC)
# print(df8['Label'].value_counts())
# print(len(df8))

merge = [
    df1, 
    df2,
    #df3,
    #df4, 
    df5, 
    df6, 
    df7, 
    df8, 
]
df = pd.concat(merge)
del merge

print(df.info())

print(df['Label'].value_counts())

df = df.drop(["Timestamp", "Down/Up Ratio"], axis=1)

#save full dataset
# print(bcolors.WARNING + "Saving as pickle" + bcolors.ENDC)
# with open(PICKLE_DIR + DATASET_NAME + '_full.pkl', 'wb') as f:
#     pickle.dump(df, f)

#save dataset
print(bcolors.WARNING + "Saving as pickle" + bcolors.ENDC)
with open(os.path.join(DATASET_DIR, DATASET_NAME, DATASET_NAME + '_base.pkl'), 'wb') as f:
    pickle.dump(df, f)

print(bcolors.OKGREEN + "Done" + bcolors.ENDC)
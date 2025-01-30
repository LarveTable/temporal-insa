from pyts.classification import LearningShapelets
import time
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# load data from UCR archive

import numpy as np

print(f"Loading data".ljust(80 - 5, "."), end = "", flush = True)

training_data = np.loadtxt("UCRArchive_2018/Adiac/Adiac_TRAIN.tsv")
cleaned_data = np.nan_to_num(training_data[:, 1:], nan=0.0).astype(np.float32) #Cleaned data from NaN values to 0.0
Y_training, X_training = training_data[:, 0].astype(np.int32), cleaned_data

test_data = np.loadtxt("UCRArchive_2018/Adiac/Adiac_TEST.tsv")
cleaned_data = np.nan_to_num(test_data[:, 1:], nan=0.0).astype(np.float32) #Cleaned data from NaN values to 0.0
Y_test, X_test = test_data[:, 0].astype(np.int32), cleaned_data

print("Done.")

# Normalisation des données
scaler = StandardScaler()

time_a_trans = time.perf_counter()
X_training = scaler.fit_transform(X_training)
time_b_trans = time.perf_counter()
time_trans = time_b_trans - time_a_trans

time_a_trans = time.perf_counter()
X_test = scaler.transform(X_test)
time_b_trans = time.perf_counter()
time_trans_test = time_b_trans - time_a_trans

time_a = time.perf_counter()
# Création du transformateur LearningShapelets
ls = LearningShapelets()
ls.fit(X_training, Y_training)
time_b = time.perf_counter()
time_training = time_b - time_a

time_a = time.perf_counter()
score = ls.score(X_test, Y_test)
time_b = time.perf_counter()
time_testing = time_b - time_a

print("transform training data :" + str(time_trans) + ",\n" + 
      "transform test data :" + str(time_trans_test) + ",\n" + 
      "training :" + str(time_training) + ",\n" + 
      "testing :" + str(time_testing) + ",\n" + 
      "score :" + str(score))
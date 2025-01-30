from pyts.transformation import BOSS
from sklearn.svm import SVC
import time

# load data from UCR archive

import numpy as np

print(f"Loading data".ljust(80 - 5, "."), end = "", flush = True)

training_data = np.loadtxt("UCRArchive_2018/BME/BME_TRAIN.tsv")
cleaned_data = np.nan_to_num(training_data[:, 1:], nan=0.0).astype(np.float32) #Cleaned data from NaN values to 0.0
Y_training, X_training = training_data[:, 0].astype(np.int32), cleaned_data

test_data = np.loadtxt("UCRArchive_2018/BME/BME_TEST.tsv")
cleaned_data = np.nan_to_num(test_data[:, 1:], nan=0.0).astype(np.float32) #Cleaned data from NaN values to 0.0
Y_test, X_test = test_data[:, 0].astype(np.int32), cleaned_data

print("Done.")

# Création du transformateur BOSS
boss = BOSS(word_size=4, n_bins=4, window_size=32, sparse=True)

time_a_trans = time.perf_counter()
X_training_transform = boss.fit_transform(X_training).toarray()
time_b_trans = time.perf_counter()
time_trans = time_b_trans - time_a_trans

time_a_trans = time.perf_counter()
X_test_transform = boss.transform(X_test).toarray()
time_b_trans = time.perf_counter()
time_trans_test = time_b_trans - time_a_trans


time_a = time.perf_counter()
# SVM
classifier = SVC()
classifier.fit(X_training_transform, Y_training)
time_b = time.perf_counter()
time_training = time_b - time_a

time_a = time.perf_counter()
score = classifier.score(X_test_transform, Y_test)
time_b = time.perf_counter()
time_testing = time_b - time_a

print("transform training data :" + str(time_trans) + ",\n" + 
      "transform test data :" + str(time_trans_test) + ",\n" + 
      "training :" + str(time_training) + ",\n" + 
      "testing :" + str(time_testing) + ",\n" + 
      "score :" + str(score))

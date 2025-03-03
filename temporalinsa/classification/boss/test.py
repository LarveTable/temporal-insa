from pyts.transformation import BOSS
from sklearn.svm import SVC
import time
import matplotlib.pyplot as plt

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

# Création du transformateur BOSS
boss = BOSS(word_size=4, n_bins=4, window_size=32, sparse=True)

time_a_trans = time.perf_counter()
X_training_transform = boss.fit_transform(X_training)
time_b_trans = time.perf_counter()
time_trans = time_b_trans - time_a_trans

time_a_trans = time.perf_counter()
X_test_transform = boss.transform(X_test)
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

# Visualize
# Visualize the transformation for the first time series
"""plt.figure(figsize=(6, 4))
vocabulary_length = len(boss.vocabulary_)
width = 0.3
plt.bar(np.arange(vocabulary_length) - width / 2, X_training_transform[Y_training == 1][0],
        width=width, label='First time series in class 1')
plt.bar(np.arange(vocabulary_length) + width / 2, X_training_transform[Y_training == 2][0],
        width=width, label='First time series in class 2')
plt.xticks(np.arange(vocabulary_length),
           np.vectorize(boss.vocabulary_.get)(np.arange(X_training_transform[0].size)),
           fontsize=12)
y_max = np.max(np.concatenate([X_training_transform[Y_training == 1][0],
                               X_training_transform[Y_training == 2][0]]))
plt.yticks(np.arange(y_max + 1), fontsize=12)
plt.xlabel("Words", fontsize=14)
plt.ylabel("Frequencies", fontsize=14)
plt.title("BOSS transformation", fontsize=16)
plt.legend(loc='best', fontsize=10)
plt.tight_layout()
plt.show()"""

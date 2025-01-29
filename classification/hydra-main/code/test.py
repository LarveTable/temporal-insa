from hydra import Hydra, SparseScaler
from sklearn.linear_model import RidgeClassifierCV
import torch
import time

# load data from UCR archive

import numpy as np

print(f"Loading data".ljust(80 - 5, "."), end = "", flush = True)

training_data = np.loadtxt("UCRArchive_2018/BME/BME_TRAIN.tsv")
cleaned_data = np.nan_to_num(training_data[:, 1:], nan=0.0).astype(np.float32) #Cleaned data from NaN values to 0.0
Y_training, X_training = training_data[:, 0].astype(np.int32), cleaned_data

# Convert X_training to torch.FloatTensor, shape = (num_examples, 1, length)
X_training = torch.FloatTensor(X_training).unsqueeze(1)

test_data = np.loadtxt("UCRArchive_2018/BME/BME_TEST.tsv")
cleaned_data = np.nan_to_num(test_data[:, 1:], nan=0.0).astype(np.float32) #Cleaned data from NaN values to 0.0
Y_test, X_test = test_data[:, 0].astype(np.int32), cleaned_data

# Convert X_test to torch.FloatTensor, shape = (num_examples, 1, length)
X_test = torch.FloatTensor(X_test).unsqueeze(1)

print("Done.")

transform = Hydra(X_training.shape[-1])
scaler = SparseScaler()

time_a_trans = time.perf_counter()
X_training_transform = transform(X_training)
X_training_transform = scaler.fit_transform(X_training_transform)
time_b_trans = time.perf_counter()
time_trans = time_b_trans - time_a_trans

time_a_trans = time.perf_counter()
X_test_transform = transform(X_test)
X_test_transform = scaler.transform(X_test_transform)
time_b_trans = time.perf_counter()
time_trans_test = time_b_trans - time_a_trans


time_a = time.perf_counter()
classifier = RidgeClassifierCV(alphas = np.logspace(-3, 3, 10))
classifier.fit(X_training_transform, Y_training)
time_b = time.perf_counter()
time_training = time_b - time_a

#predictions = classifier.predict(X_test_transform)

# Save predictions in a txt file
#np.savetxt("predictions.txt", predictions, fmt = "%d")

time_a = time.perf_counter()
score = classifier.score(X_test_transform, Y_test)
time_b = time.perf_counter()
time_testing = time_b - time_a

print("transform training data :" + str(time_trans) + ",\n" + 
      "transform test data :" + str(time_trans_test) + ",\n" + 
      "training :" + str(time_training) + ",\n" + 
      "testing :" + str(time_testing) + ",\n" + 
      "score :" + str(score))
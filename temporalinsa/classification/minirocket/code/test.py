from minirocket import transform, fit
from sklearn.linear_model import RidgeClassifierCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import time

# load data from UCR archive

import numpy as np

print(f"Loading data".ljust(80 - 5, "."), end = "", flush = True)

training_data = np.loadtxt("temporalinsa/UCRArchive_2018/Adiac/Adiac_TRAIN.tsv")
cleaned_data = np.nan_to_num(training_data[:, 1:], nan=0.0).astype(np.float32) #Cleaned data from NaN values to 0.0
Y_training, X_training = training_data[:, 0].astype(np.int32), cleaned_data

test_data = np.loadtxt("temporalinsa/UCRArchive_2018/Adiac/Adiac_TEST.tsv")
cleaned_data = np.nan_to_num(test_data[:, 1:], nan=0.0).astype(np.float32) #Cleaned data from NaN values to 0.0
Y_test, X_test = test_data[:, 0].astype(np.int32), cleaned_data

print("Done.")

# note:
# * input time series do *not* need to be normalised
# * input data should be np.float32

print(X_training.shape)

time_a_trans = time.perf_counter()
parameters = fit(X_training)
X_training_transform = transform(X_training, parameters)
time_b_trans = time.perf_counter()
time_trans = time_b_trans - time_a_trans

time_a_trans = time.perf_counter()
X_test_transform = transform(X_test, parameters)
time_b_trans = time.perf_counter()
time_trans_test = time_b_trans - time_a_trans

time_a = time.perf_counter()
model = make_pipeline(
    StandardScaler(with_mean=False), RidgeClassifierCV(alphas = np.logspace(-3, 3, 10)))
model.fit(X_training_transform, Y_training)
time_b = time.perf_counter()
time_training = time_b - time_a

#predictions = model.predict(X_test_transform)

time_a = time.perf_counter()
score = model.score(X_test_transform, Y_test)
time_b = time.perf_counter()
time_testing = time_b - time_a

print("transform training data :" + str(time_trans) + ",\n" + 
      "transform test data :" + str(time_trans_test) + ",\n" + 
      "training :" + str(time_training) + ",\n" + 
      "testing :" + str(time_testing) + ",\n" + 
      "score :" + str(score))
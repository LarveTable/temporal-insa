from minirocket_dv import fit_transform
from minirocket import transform
from sklearn.linear_model import RidgeClassifierCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

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

# note:
# * input time series do *not* need to be normalised
# * input data should be np.float32

parameters, X_training_transform = fit_transform(X_training)

model = make_pipeline(
    StandardScaler(with_mean=False), RidgeClassifierCV(alphas = np.logspace(-3, 3, 10)))
model.fit(X_training_transform, Y_training)

model.fit(X_training_transform, Y_training)

X_test_transform = transform(X_test, parameters)

predictions = model.predict(X_test_transform)

print(model.score(X_test_transform, Y_test))
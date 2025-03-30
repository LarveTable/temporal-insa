import numpy as np
# available scalers
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import MaxAbsScaler
from sklearn.preprocessing import Normalizer
import os

class Processing:
    def __init__(self, dataset):
        self.dataset = dataset
    
    def extract(self):
        # process the dataset
        print(f"Loading data".ljust(80 - 5, "."), end = "", flush = True)

        # extract training data
        training_data = np.loadtxt("temporalinsa/UCRArchive_2018/Adiac/Adiac_TRAIN.tsv")
        cleaned_data = np.nan_to_num(training_data[:, 1:], nan=0.0).astype(np.float64) #Cleaned data from NaN values to 0.0
        Y_training, X_training = training_data[:, 0].astype(np.int32), cleaned_data

        # extract test data
        test_data = np.loadtxt("temporalinsa/UCRArchive_2018/Adiac/Adiac_TEST.tsv")
        cleaned_data = np.nan_to_num(test_data[:, 1:], nan=0.0).astype(np.float64) #Cleaned data from NaN values to 0.0
        Y_test, X_test = test_data[:, 0].astype(np.int32), cleaned_data

        print("Done.")

        return X_training, Y_training, X_test, Y_test
    
    def scale(self, scaler="StandardScaler"):
        # scale the dataset
        X_training, Y_training, X_test, Y_test = self.extract()
        
        # apply desired scaler
        match scaler:
            case "StandardScaler":
                scaler = StandardScaler()
            case "MinMaxScaler":
                scaler = MinMaxScaler()
            case "RobustScaler":
                scaler = RobustScaler()
            case "MaxAbsScaler":
                scaler = MaxAbsScaler()
            case "Normalizer":
                scaler = Normalizer()
            case _:
                raise ValueError("Invalid scaler")
            
        X_training_scaled = scaler.fit_transform(X_training)
        X_test_scaled = scaler.transform(X_test)

        return X_training_scaled, X_test_scaled, Y_training, Y_test
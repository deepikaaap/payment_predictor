import sys
import numpy as np
import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LinearRegression


data = pd.read_csv('final_query_result.csv')
inFile = sys.argv[1]
outFile = sys.argv[2]

file = open(inFile,'r')
print file.read

input_for_charge = data[['APPNAME','SPECNAME','AGE', 'SEX','PROVIDERID','PRINTPROCEDURECODE']]
input_for_charge = pd.get_dummies(input_for_charge)
charge_features = input_for_charge.columns
output_for_charge = dataset_charge[['AMOUNT']]
charge_ip_train, charge_ip_test, charge_op_train, charge_op_test = model_selection.train_test_split(input_for_charge, output_for_charge,test_size=0.25,random_state=2) 
linreg = LinearRegression()
linreg.fit(charge_ip_train, charge_op_train)
charge_pred= linreg.predict(charge_ip_test)


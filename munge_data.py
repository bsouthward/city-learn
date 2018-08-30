##########
# Munger #
##########
# This takes a reference to a CSV file and prepares the data to train the model

import pandas as pd
import numpy as np

from sklearn_pandas import CategoricalImputer

def clean_impute(df):
	# This function consumes a dataframe and spits out a stripped, imputed dataframe
	data = df
	data = data.fillna(data.mean())
	imputer = CategoricalImputer()
	imp = imputer.fit_transform(data.values)
	return imp

def clean_csv(csv_path):
	# This function consumes the path to CSV file aand spits out cleaned data
	city_data = pd.read_csv(csv_path)
	city_data_t = city_data.set_index('Metric').T
	city_data_t.index.names = ['index']
	return city_data_t

def munge(csv_path, p):
	# Consumes path to CSV and set of predictors, spits out imputed dataframe
	clean_data = clean_csv(csv_path)
	c = clean_data[p]
	return clean_impute(c)

def make_pred_df(p, i):
	# Create pandas dataframe that's indexed by city name
	return pd.DataFrame({'x': range(p.size), 'y': p, 'indices': i})
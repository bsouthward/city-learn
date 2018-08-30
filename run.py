###############
# Main script #
###############

import sys

# Local module for cleaning up the data
import munge_data as md

# Local module for doing the ML stuff
import regressor as rg

# Local graphing module
import graph as gr

# For measuring error
from sklearn.metrics import mean_absolute_error

# Still need to import some Bokeh stuff to plot properly
from bokeh.plotting import show, output_file

# Grab the path to the CSV from the command line and create cleaned version
city_data_path = sys.argv[1]
data = md.clean_csv(city_data_path)

# Choose prediction target and predictors, also number of runs
y = data.DeveloperSalary
X = md.clean_impute(data)
n = 5

# Do the thing, make the prediction
pred = rg.train_model_avg(X, y, n)

# Turn the results back into a dataframe with the approproate indices
indices = data.index.tolist()
prediction_df = md.make_pred_df(pred, indices)

# Print prediction results and mean absolute error
print(prediction_df)
print(mean_absolute_error(pred, y.values))

# Graph the stuff
p = gr.plot_data(prediction_df)
show(p)
output_file("city_plot.html")
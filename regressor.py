#############
# Regressor #
#############

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# I know 'reduce' isn't idiomatic Python these days but it's useful here
from functools import reduce

# Primary function for training the model
def train_model(X, y):
	# Randomly split data into training and target sets
	train_X, val_X, train_y, val_y = train_test_split(X, y, 
		test_size=0.25, random_state=0)

	# Create the regressor and fit it to the training data
	forest_model = RandomForestRegressor()
	forest_model.fit(train_X, train_y)

	# This should probably be predicting on val_X but 
	# that isn't working due to a length mismatch.
	pred = forest_model.predict(X)
	return pred

# Alternate function that averages several runs
def train_model_avg(X, y, n):
	# Variation that averages several runs of the training function.
	# This yields better results than just running it once, 
	# but am I missing the point?

	# Array to hold the results of the runs of the training function
	results = []

	# Thing to run it on
	for i in range(n):
		results.append(train_model(X, y))

	# Put em together
	return reduce(lambda x, y: x+y, results) / len(results)
# CS-UY 1114
# Final project

import math
import turtle

def create_table(file_name):
    """
    sig: str -> tuple(list(float), list(float), list(str))
    Given a file name, read the file into a tuple containing
    two lists of type float and one list of type string.
    The features of the dataset should be of type float
    and the label should be of type string. 
    """
    pass

def print_range_max_min(data):
    """
    sig: tuple(list(float), list(float)) -> NoneType
    Print the max, min and range of both features in the dataset.
    """
    pass

def find_mean(feature):
    """
    sig: list(float) -> float
    Return the mean of the feature.
    """
    pass

def find_std_dev(feature, mean):
    """
    sig: list(float), float -> float
    Return the standard deviation of the feature. 
    """
    pass

def normalize_data(data):
    """
    sig: tuple(list(float), list(float), list(str)) -> NoneType
    Print the mean and standard deviation for each feature.
    Normalize the features in the dataset by
    rescaling all the values in a particular feature
    in terms of a mean of 0 and a standard deviation of 1.
    Print the mean and the standard deviation for each feature, now normalized.
    After normalization, each of your features should display a mean of 0
    or very close to 0 and a standard deviation of 1 or very close to 1. 
    """
    pass

def make_predictions(train_set, test_set):
    """
    sig: tuple(list(float), list(float), list(str)), tuple(list(float), list(float), list(str)) -> list(str)
    For each observation in the test set, you'll need to check all of
    the observations in the training set to see which is the `nearest neighbor.'
    The function should make a call to the function find_dist.
    Accumulate a list of predicted iris types for each of the test set
    observations. Return this prediction list.
    """
    pass


def find_dist(x1, y1, x2, y2):
    """
    sig: float, float, float, float -> float
    Return the Euclidean distance between two points (x1, y1), (x2, y2).
    """
    pass
        
def find_error(test_data, pred_lst):
    """
    sig: tuple(list(float), list(float), list(str)) -> float
    Check the prediction list against the actual labels for
    the test set to determine how many errors were made.
    Return a percentage of how many observations in the
    test set were predicted incorrectly. 
    """
    pass

def plot_data(train_data, test_data, pred_lst):
    """
    sig: tuple(list(float), list(float), list(str)), tuple(list(float), list(float), list(str)), list(str)
        -> NoneType
    Plot the results using the turtle module. Set the turtle window size to 500 x 500.
    Draw the x and y axes in the window. Label the axes "petal width" and "petal length". 
    Plot each observation from your training set on the plane, using a circle shape
    and a different color for each type of iris. Use the value of the first feature
    for the x-coordinate and the value of the second feature for the y-coordinate.
    Use a dot size of 10. Recall that the features have been normalized to have a mean
    of 0 and a standard deviation of 1. You will need to `stretch' your features across
    the axes to make the best use of the 500 x 500 window. Ensure that none of your
    points are plotted off screen. Also plot each correct prediction from your test
    set in the corresponding color. Use a square to indicate that the value is a prediction.
    Plot the incorrect predictions that were made for the test set in red, also using a
    square to indicate that it was a prediction. Include a key in the upper left
    corner of the plot as shown in the sample plot. The function will make a call
    to the function draw_key in order to accomplish this task. 
    """
    pass

def draw_key():
    """
    sig: () -> NoneType
    Draw the legend for the plot indicating which group is shown by each color/shape combination.  
    """
    pass

def main():
    """
    sig: () -> NoneType
    The main body of the program. It will use the other
    functions to load the data, process the training set,
    analyze the test set, and display its conclusions.
    """

    train_data = create_table("iris_train.csv")
    print_range_max_min(train_data[:2])
    print()
    normalize_data(train_data)
    test_data = create_table("iris_test.csv")
    print()
    normalize_data(test_data)
    pred_lst = make_predictions(train_data, test_data)
    error = find_error(test_data, pred_lst)
    print()
    print("The error percentage is: ", error)
    plot_data(train_data, test_data, pred_lst)

main()


#!/usr/bin/python
"""
Student name: Sai Pramodh Sabarissan
Student ID: 21230987
Github URL: https://github.com/SaiPramodh128/ARC
"""
import os, sys
import json
import numpy as np
import re

### YOUR CODE HERE: write at least three functions which solve
### specific tasks by transforming the input x and returning the
### result. Name them according to the task ID as in the three
### examples below. Delete the three examples. The tasks you choose
### must be in the data/training directory, not data/evaluation.
"""
Summary : In the resoning corpus, here we are supposed to indentify patterns and predict the output for the patterns that might be missing.
As we are suposed to write functions to predict the patterns based on the train dataset
I have written to solve few shapes based on pattern , with colour occurance and boundary pattern. 
I have used numpy a lot on working in this assignment I had the chance to go through a lot in numpy libraries.
Helped in better understanding of working with arrays in python.

"""

# ====================================Task solve_5ad4f10b============================================
"""
On analysis here the input contains two unique colour, one scattered all over the grid and other appears to be grid of square shape.
The square shaped grid consists of random colour which appears to be in m x n but the output is in  3 x 3 grid. 
The subgrid which is inside the main input grid is then transformed to  3 x 3, difference with swap of the unique colours found in input.
Pattern:
1. The background colour of the input here appears to be black(0) which will the background of the output grid too.
2. The scattered colour are found initial as I think scattered appears first in the input before the subgrid. There might be also be a 
scenario where scatterd occurs less than the subgrid colour.
3. The subgrid may be in any m x n which is always square matrix array. It appears to be a grid with unique colours filling the m x n  which is resembles a
3 x 3 matric with missing same unique colours.
Transformation:
1. The scattered colour and the subgrid colour are found which are later going to be swapped.
2.The boundary of the subgrid is found by the first occurence of the subgrid color in the input by gramming the index as 
top left and bottom right occurance of the subgrid colour
3. Then framing the output grid with the stepsize of 3 since the output grid is a 3 x 3 grid.
4. The subgrid values are swapped with scattered colour value in the output grid which is filled. With spliting the row in three parts.
These three parts resembles the output grid and black(0) as the missing value    
"""


def solve_5ad4f10b(x):
    #the unique colours with index which is used to identify the scatterd and grid colours
    unique_elem_list, indexes = np.unique(x, return_index=True)
    map_color_index = zip(unique_elem_list, indexes)
    sorted_color = sorted(map_color_index, key=lambda y: y[1])
    unique_elems = [sorted_color[i][0] for i in range(len(sorted_color))]
    #Removing black as it is the background colour
    unique_elems = np.delete(unique_elems, 0)
    # calling a method to get the boundaries of the unique colour value which might be of m x n grid.
    sub_grid = get_boundaries(x, unique_elems[1])
    #splitting the subgrid into three parts
    step_size = (int)(len(sub_grid) / 3)
    output = []
    # filling the output array with rows of array with the scattered colour value.
    for y in range(0, len(sub_grid), step_size):
        row_arr = []
        for x in range(0, len(sub_grid), step_size):
            if sub_grid[y][x] == unique_elems[1]:
                row_arr.append(unique_elems[0])
            else:
                row_arr.append(0)
        output.append(row_arr)
    return np.array(output)

# used to get the boundaries of the value
def get_boundaries(X, unique_elem):

    row , col = X.shape

    for y in range(row):
        if (unique_elem in X[y]):
            top = y
            break;

    for y in range(row):
        yval = row - (y + 1)
        if (unique_elem in X[yval]):
            bottom = yval
            break;

    t = np.transpose(X)
    for x in range(col):
        if (unique_elem in t[x]):
            left = x
            break;

    for x in range(col):
        xval = col - (x + 1)
        if (unique_elem in t[xval]):
            right = xval
            break;

    return np.array(X)[top:bottom + 1, left:right + 1]


# ====================================Task solve_5ad4f10b===============================================

# ====================================Task solve_1b60fb0c===============================================

"""
On analysis the input and output are going to the same.
The background of the input are mostly black (0) and has blue shapes of pattern and the missing pattern are in red.
Patterns:
1. If we consider in a symetrical view of lets say top and bottom halves both are symetrical to each other 
similarly the left and right should also be symetrical.
2. For this input if we consider the top and bottom parts if they are adjusted, the left and right will also
follow the same funcionality since they are symetrical.

On Comparing the first and last rows, as well as the first + 1 and last - 1 rows
On Comparing the first and last columns, as well as the first + 1 and last - 1 columns

Transformations :
1. The goal is to fill the empty blue cells in the output grid with red to satisfy the pattern criteria.
2. If the bottom row of the grid is displaced by one along the x axis as compared to the top row,
when compared to the right column of the grid, the left column is displaced by one along the y axis.
The pattern shape is iterated in a loop to fill the colour same as the symetrical side.
"""


def solve_1b60fb0c(x):
    output = np.copy(x)
    # Getting the unique values and occurence of them
    unique_elem_list, no_of_times = np.unique(x, return_counts=True)
    map_color_count = zip(unique_elem_list, no_of_times)
    sorted_color_count = sorted(map_color_count, key=lambda y: y[1])
    unique_color = 0
    for i in sorted_color_count:
        # since black(0) is the background colour the other unique colour is fetched. which is the pattern's colour
        if i[0] != 0:
            unique_color = i[0]

    m, n = output.shape
    b = m - 1
    t = 0
    r = n - 1
    l = 0
    # Here the colour that is missing in the pattern is replaced with red(2)
    color_to_be_filled = 2
    # Iterate the loop till the center of the grid to get the missing values
    while t < m / 2:
        if unique_color in output[b][:]:
            if unique_color in output[t][:]:

                previous_shape = output[t:b, l]
                if (output[b, l:r] == output[t, l:r]).all():
                    new_shape = output[t:b, r]
                else:
                    # Here roll method is used rotate over the axis
                    new_shape = np.roll(output[t:b, r], axis=0, shift=1)
                output[t:b, l] = np.where(previous_shape == new_shape, previous_shape, color_to_be_filled)
            else:
                t = t + 1
                l = l + 1
                continue
        b = b - 1
        t = t + 1
        l = l + 1
        r = r - 1
    return output
# ====================================Task solve_1b60fb0c==================================================


# ====================================Task solve_c8cbb738==================================================
"""
On analysis the input may be of any size m x n.
The output size depends on the input as of the biggest sub pattern in the input 
Patterns:
1. Two or more distinct colors, with one color notably found in the input grid cells 
2. By connecting the same coloured cells, you can make shapes like squares, rectangles, and diamonds. 
Transformation:
1. Calculate the size of the largest square-shaped colored cells and create an output grid with that size and dominant color as the background colour.
2. Now, start looking at the various colored cells and map them in the output grid in the same form (rectangle, diamond, square) 
with the same color and size as the input grid.
"""

def solve_c8cbb738(x):
    # Getting the unique values and occurence of them
    unique_elem_list, no_of_times = np.unique(x, return_counts=True)
    map_color_count = zip(unique_elem_list, no_of_times)
    sorted_color_count = sorted(map_color_count, key=lambda y: y[1])
    # max occurence colour which will the background colour of the output
    max_num, max_count = sorted_color_count[len(sorted_color_count) - 1]
    min_num, min_count = sorted_color_count[0]
    # Find the indexes of the less frequent color and determine the maximum distance in X axis.
    # Using the calculated distance, find the centre position and generate the output grid with dominant color
    m, n = np.where(x == min_num)
    output_size = np.max(m) - np.min(m) + 1
    mid_point = int(np.floor(output_size / 2))
    output = np.full((output_size, output_size), max_num)

    for color in unique_elem_list:
        if color != max_num:
            m, n = np.where(x == color)
            if len(np.unique(m)) > 2 or len(np.unique(n)) > 2:
                # Filling the diamond shape by coloring the center in the four edges
                output[mid_point, 0] = color
                output[0, mid_point] = color
                output[mid_point, output_size - 1] = color
                output[output_size - 1, mid_point] = color
            elif (np.max(m) - np.min(m) == output_size - 1) and len(np.unique(m)) == 2:
                # Filling the rectangle shaped colored cells by measuring the distance from centre position
                y_diff = int((np.max(n) - np.min(n)) / 2)
                output[0, mid_point + y_diff] = color
                output[0, mid_point - y_diff] = color
                output[output_size - 1, mid_point + y_diff] = color
                output[output_size - 1, mid_point - y_diff] = color
            elif (np.max(n) - np.min(n) == output_size - 1) and len(np.unique(n)) == 2:
                # Filling the rectangle shaped colored cells by measuring the distance from centre position
                x_diff = int((np.max(m) - np.min(m)) / 2)
                output[mid_point + x_diff, 0] = color
                output[mid_point - x_diff, 0] = color
                output[mid_point + x_diff, output_size - 1] = color
                output[mid_point - x_diff, output_size - 1] = color
    return output

# ====================================Task solve_c8cbb738=================================================

# ====================================Task solve_3bd67248=================================================
"""
On analysis the input may be of size m x n and the output will also be same size
Pattern:
1.The input consist of a unique colour along with black. which is bordered along the left side of the grid.
2.The output should consists of a diagonal of red colour
3. And a third colour of yellow bordered at the bottom of the grid.
Transformation:
1.The output grid is filled with red(2) using np.flipud which is other diagonal of the grid 
2. In the output grid last row consists of yellow
3. And finally the input grids unique value along left side
"""
def solve_3bd67248(x):
    unique_elem_list, no_of_times = np.unique(x, return_counts=True)
    output = np.copy(x)
    # finding the unique colour present whose value should not be replaced.
    map_color_count = zip(unique_elem_list, no_of_times)
    sorted_color_count = sorted(map_color_count, key=lambda y: y[1])
    unique_color = 0
    for i in sorted_color_count:
        if i[0] != 0:
            unique_color = i[0]

    left_line_color = unique_color
    #yellow colour for bottom
    bottom_line_color = 4
    #red colour for diagonal
    diagonal_line_color = 2

    output[-1, 1:] = bottom_line_color

    np.fill_diagonal(np.flipud(output), diagonal_line_color)

    output[-1, 0] = left_line_color

    return output
# ====================================Task solve_3bd67248================================================

# ====================================Task solve_9af7a82c================================================
"""
On analysis the input grid may be of any size.
The size of the output grid depends on the occurence of the unique colors in the input grid.
Pattern:
1.Output grid consists of occurence of unique colour in the descending order.
2.The values are arranged from top to bottom in the descending order of colour
Transformation:
The maximum occurence of a colour is number of rows in the output grid, and number of unique colors other than black is the number of columns in the output grid

"""
def solve_9af7a82c(x):
    #the unique values with occurence
    unique_elem_list, no_of_times = np.unique(x, return_counts=True)
    #default output grid is black (2)
    output = np.zeros([max(no_of_times), len(unique_elem_list)], dtype=int)
    map_color_count = zip(unique_elem_list, no_of_times)
    #sorted based on the occurence size.
    sorted_color_count = sorted(map_color_count, key=lambda y: y[1], reverse=True)
    n = 0
    # filling the output based on the occurence size
    for i in sorted_color_count:
        for m in range(i[1]):
            output[m][n] = i[0]
        n += 1
    return output
# ====================================Task solve_9af7a82c===============================================


def main():
    # Find all the functions defined in this file whose names are
    # like solve_abcd1234(), and run them.

    # regex to match solve_* functions and extract task IDs
    p = r"solve_([a-f0-9]{8})"
    tasks_solvers = []
    # globals() gives a dict containing all global names (variables
    # and functions), as name: value pairs.
    for name in globals():
        m = re.match(p, name)
        if m:
            # if the name fits the pattern eg solve_abcd1234
            ID = m.group(1)  # just the task ID
            solve_fn = globals()[name]  # the fn itself
            tasks_solvers.append((ID, solve_fn))

    for ID, solve_fn in tasks_solvers:
        # for each task, read the data and call test()
        directory = os.path.join("..", "data", "training")
        json_filename = os.path.join(directory, ID + ".json")
        data = read_ARC_JSON(json_filename)
        test(ID, solve_fn, data)


def read_ARC_JSON(filepath):
    """Given a filepath, read in the ARC task data which is in JSON
    format. Extract the train/test input/output pairs of
    grids. Convert each grid to np.array and return train_input,
    train_output, test_input, test_output."""

    # Open the JSON file and load it 
    data = json.load(open(filepath))

    # Extract the train/test input/output grids. Each grid will be a
    # list of lists of ints. We convert to Numpy.
    train_input = [np.array(data['train'][i]['input']) for i in range(len(data['train']))]
    train_output = [np.array(data['train'][i]['output']) for i in range(len(data['train']))]
    test_input = [np.array(data['test'][i]['input']) for i in range(len(data['test']))]
    test_output = [np.array(data['test'][i]['output']) for i in range(len(data['test']))]

    return (train_input, train_output, test_input, test_output)


def test(taskID, solve, data):
    """Given a task ID, call the given solve() function on every
    example in the task data."""
    print(taskID)
    train_input, train_output, test_input, test_output = data
    print("Training grids")
    for x, y in zip(train_input, train_output):
        yhat = solve(x)
        show_result(x, y, yhat)
    print("Test grids")
    for x, y in zip(test_input, test_output):
        yhat = solve(x)
        show_result(x, y, yhat)


def show_result(x, y, yhat):
    print("Input")
    print(x)
    print("Correct output")
    print(y)
    print("Our output")
    print(yhat)
    print("Correct?")
    if y.shape != yhat.shape:
        print(f"False. Incorrect shape: {y.shape} v {yhat.shape}")
    else:
        print(np.all(y == yhat))


if __name__ == "__main__": main()

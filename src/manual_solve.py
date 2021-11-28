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
# def solve_6a1e5592(x):
#     return x
#
def solve_1b60fb0c(x):
    output = np.copy(x)
    unique_elem_list, no_of_times = np.unique(x, return_counts=True)
    map_color_count = zip(unique_elem_list, no_of_times)
    sorted_color_count = sorted(map_color_count, key=lambda y: y[1])
    unique_color = 0
    for i in sorted_color_count:
        if i[0] != 0:
            unique_color = i[0]

    m, n = output.shape
    b = m - 1
    t = 0
    r = n - 1
    l = 0
    color_to_be_filled = 2

    while t < m / 2:
        if unique_color in output[b][:]:
            if unique_color in output[t][:]:

                previous_shape = output[t:b, l]
                if (output[b, l:r] == output[t, l:r]).all():
                    new_shape = output[t:b, r]
                else:
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

def solve_9af7a82c(x):
    unique_elem_list,no_of_times=np.unique(x, return_counts=True)
    output=np.zeros([max(no_of_times), len(unique_elem_list)],dtype=int)
    map_color_count = zip(unique_elem_list, no_of_times)
    sorted_color_count = sorted(map_color_count, key=lambda y: y[1], reverse=True)
    n=0
    for i in sorted_color_count:
        for m in range(i[1]):
            output[m][n] = i[0]
        n += 1
    return output

def solve_3bd67248(x):

    unique_elem_list, no_of_times = np.unique(x, return_counts=True)
    output = np.copy(x)

    map_color_count = zip(unique_elem_list, no_of_times)
    sorted_color_count = sorted(map_color_count, key=lambda y: y[1])
    unique_color = 0
    for i in sorted_color_count:
        if i[0] != 0:
            unique_color = i[0]

    left_line_color = unique_color

    bottom_line_color=4
    diagonal_line_color=2
    output[-1,1:] = bottom_line_color

    np.fill_diagonal(np.flipud(output), diagonal_line_color)

    output[-1,0] = left_line_color

    return output

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
            ID = m.group(1) # just the task ID
            solve_fn = globals()[name] # the fn itself
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


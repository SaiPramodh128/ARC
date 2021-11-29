# The Abstraction and Reasoning Corpus (ARC)

This repository contains the ARC task data, as well as a browser-based interface for humans to try their hand at solving the tasks manually.

*"ARC can be seen as a general artificial intelligence benchmark, as a program synthesis benchmark, or as a psychometric intelligence test. It is targeted at both humans and artificially intelligent systems that aim at emulating a human-like form of general fluid intelligence."*

A complete description of the dataset, its goals, and its underlying logic, can be found in: [The Measure of Intelligence](https://arxiv.org/abs/1911.01547).

As a reminder, a test-taker is said to solve a task when, upon seeing the task for the first time, they are able to produce the correct output grid for *all* test inputs in the task (this includes picking the dimensions of the output grid). For each test input, the test-taker is allowed 3 trials (this holds for all test-takers, either humans or AI).


## Task file format

The `data` directory contains two subdirectories:

- `data/training`: contains the task files for training (400 tasks). Use these to prototype your algorithm or to train your algorithm to acquire ARC-relevant cognitive priors.
- `data/evaluation`: contains the task files for evaluation (400 tasks). Use these to evaluate your final algorithm. To ensure fair evaluation results, do not leak information from the evaluation set into your algorithm (e.g. by looking at the evaluation tasks yourself during development, or by repeatedly modifying an algorithm while using its evaluation score as feedback).

The tasks are stored in JSON format. Each task JSON file contains a dictionary with two fields:

- `"train"`: demonstration input/output pairs. It is a list of "pairs" (typically 3 pairs).
- `"test"`: test input/output pairs. It is a list of "pairs" (typically 1 pair).

A "pair" is a dictionary with two fields:

- `"input"`: the input "grid" for the pair.
- `"output"`: the output "grid" for the pair.

A "grid" is a rectangular matrix (list of lists) of integers between 0 and 9 (inclusive). The smallest possible grid size is 1x1 and the largest is 30x30.

When looking at a task, a test-taker has access to inputs & outputs of the demonstration pairs, plus the input(s) of the test pair(s). The goal is to construct the output grid(s) corresponding to the test input grid(s), using 3 trials for each test input. "Constructing the output grid" involves picking the height and width of the output grid, then filling each cell in the grid with a symbol (integer between 0 and 9, which are visualized as colors). Only *exact* solutions (all cells match the expected answer) can be said to be correct.

## Task solved
### solve_5ad4f10b
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
### solve_1b60fb0c
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
### solve_c8cbb738
On analysis the input may be of any size m x n.
The output size depends on the input as of the biggest sub pattern in the input 
Patterns:
1. Two or more distinct colors, with one color notably found in the input grid cells 
2. By connecting the same coloured cells, you can make shapes like squares, rectangles, and diamonds. 
Transformation:
1. Calculate the size of the largest square-shaped colored cells and create an output grid with that size and dominant color as the background colour.
2. Now, start looking at the various colored cells and map them in the output grid in the same form (rectangle, diamond, square) 
with the same color and size as the input grid.
### solve_3bd67248
On analysis the input may be of size m x n and the output will also be same size
Pattern:
1.The input consist of a unique colour along with black. which is bordered along the left side of the grid.
2.The output should consists of a diagonal of red colour
3. And a third colour of yellow bordered at the bottom of the grid.
Transformation:
1.The output grid is filled with red(2) using np.flipud which is other diagonal of the grid 
2. In the output grid last row consists of yellow
3. And finally the input grids unique value along left side
### solve_9af7a82c
On analysis the input grid may be of any size.
The size of the output grid depends on the occurence of the unique colors in the input grid.
Pattern:
1.Output grid consists of occurence of unique colour in the descending order.
2.The values are arranged from top to bottom in the descending order of colour
Transformation:
The maximum occurence of a colour is number of rows in the output grid, and number of unique colors other than black is the number of columns in the output grid

## Usage of the testing interface

The testing interface is located at `apps/testing_interface.html`. Open it in a web browser (Chrome recommended). It will prompt you to select a task JSON file.

After loading a task, you will enter the test space, which looks like this:

![test space](https://arc-benchmark.s3.amazonaws.com/figs/arc_test_space.png)

On the left, you will see the input/output pairs demonstrating the nature of the task. In the middle, you will see the current test input grid. On the right, you will see the controls you can use to construct the corresponding output grid.

You have access to the following tools:

### Grid controls

- Resize: input a grid size (e.g. "10x20" or "4x4") and click "Resize". This preserves existing grid content (in the top left corner).
- Copy from input: copy the input grid to the output grid. This is useful for tasks where the output consists of some modification of the input.
- Reset grid: fill the grid with 0s.

### Symbol controls

- Edit: select a color (symbol) from the color picking bar, then click on a cell to set its color.
- Select: click and drag on either the output grid or the input grid to select cells.
    - After selecting cells on the output grid, you can select a color from the color picking to set the color of the selected cells. This is useful to draw solid rectangles or lines.
    - After selecting cells on either the input grid or the output grid, you can press C to copy their content. After copying, you can select a cell on the output grid and press "V" to paste the copied content. You should select the cell in the top left corner of the zone you want to paste into.
- Floodfill: click on a cell from the output grid to color all connected cells to the selected color. "Connected cells" are contiguous cells with the same color.

### Answer validation

When your output grid is ready, click the green "Submit!" button to check your answer. We do not enforce the 3-trials rule.

After you've obtained the correct answer for the current test input grid, you can switch to the next test input grid for the task using the "Next test input" button (if there is any available; most tasks only have one test input).

When you're done with a task, use the "load task" button to open a new task.

# Mu-Niu-Pandas-Descriptive-Statistics-Project Summary Report

[![CI/CD run](https://github.com/nogibjj/Mu-Niu-Pandas-Descriptive-Statistics-Script/actions/workflows/hello.yml/badge.svg)](https://github.com/nogibjj/Mu-Niu-Pandas-Descriptive-Statistics-Script/actions/workflows/hello.yml)

# Student Performance Analysis and Descriptive Statistics

## Project Overview

This project is designed to analyze student performance using the dataset `student_performance.csv`. The goal is to implement a Python script that calculates statistical metrics (mean, median, and standard deviation) for various numeric columns in the dataset. Additionally, the project provides visual insights using histograms for specified columns.

The project incorporates best practices for code quality and testing, leveraging Python tools like Pylint for linting, pytest for testing, and matplotlib for visualization.

## Files Overview

- **`hello.py`**: Contains the main logic for calculating the mean, median, and standard deviation of a specified column in the dataset. It also includes functionality to draw histograms for data visualization.
- **`test_hello.py`**: Includes test cases for the functions in `hello.py`. The tests validate the correctness of the statistical calculations and check for proper handling of non-numeric columns.
- **`student_performance.csv`**: The dataset used for analysis, containing student performance data with various attributes.
- **`Makefile`**: Automates the process of installation, linting, formatting, and testing the codebase.
- **`requirements.txt`**: Specifies the Python dependencies required for this project. This includes tools like `pytest`, `pylint`, `pandas`, and `matplotlib`.

## Functionality

The primary functionality of the project is to compute descriptive statistics for numerical columns of the dataset and to visualize the distribution of these columns using histograms.

### Key Functions in `hello.py`:

1. **`calc_mean(df, colname)`**: Calculates the mean of the specified column. Returns a message if the column is not numeric or doesn't exist.
2. **`calc_median(df, colname)`**: Computes the median of the specified column.
3. **`calc_sd(df, colname)`**: Computes the standard deviation for the given column.
4. **`draw(df, colname)`**: Generates a histogram for the specified column using `matplotlib`.

Here is an example of the draw() function plotting the histogram for the Attendance Rate column:

![Attendance Rate Histogram](AttendanceRate.png)


### Testing

Testing is an important part of this project. The test suite in `test_hello.py` ensures that:

- Mean, median, and standard deviation calculations are correct for numerical columns.
- Non-numeric columns are handled appropriately with informative messages.
- Histograms are generated without errors.

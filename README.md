# Introduction
Please try to address the following questions as much as possible, different solutions can lead to good results. Feel free to use resources from the internet (stackoverflow etc.) that may help you in answering the questions. 

The following questions assume that you have Python and Git installed on your system.

# 1.)
- Clone the following repo into your local environment: https://benjaminbluhm@dev.azure.com/benjaminbluhm/Training/_git/Training 
- Create a new git branch (with a name of your choice), later you will Git commit and push you code changes using this branch 
- Create two new Python files called `my_functions.py` and `my_classes.py`

# 2.) 
Consider the following example pandas dataframe:

```Python
>>> df = pd.DataFrame([[9, 16]] * 3, columns=['A', 'B'])
>>> df
   A  B
0  9  16
1  9  16
2  9  16
```
Write a new function called `transform` in `my_functions.py` that takes this dataframe as an input and returns 3 dataframes with the following result:

- `df1`: the square root of each element in `df`
- `df2`: the column sums of each column in `df`
- `df3`: the row sums of each row in `df`

# 3.)

# 4.)

# 5.)

Write a new class called `Transformer` in `my_classes.py` that takes a dataframe as an input argument. Add a new class method using your previously defined `transform` function. 

Instantiate the class and call the class method where you provide the example dataframe from Question 2.)

# 6.)

Add docstrings to your class following one of the standard Python docstring formats of your choice.

# 7.)

Write a new class `ChildTransformer` in `my_classes.py` that inherets from `Transformer` class in Question 5.). Override `transform` so that it returns 1 dataframe with the following result:

- `df1`: the square root of each element in `df`

# 8.)
Consider the following function:

The code in this function violates some of python's coding best practices (for example PEP8). Modify the code to improve on coding best practice   

# 9.)
- Git commit your code changes 
- Git push your code changes  

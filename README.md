# Introduction
Please try to address the following questions as much as possible, different solutions can lead to correct results. Feel free to use any resources from the internet (for example stackoverflow etc.) that may help you in answering the questions. 

The following questions assume that you have Python and Git installed on your system. If you do not have Git installed on your system you can download it for your operating system via this link: https://git-scm.com/downloads

# 1.)
Note: If you have not used Git before you can find numerous resources on the internet that will help you to complete the below steps.

- Clone the following repo into your local environment: https://benjaminbluhm@dev.azure.com/benjaminbluhm/Training/_git/Training. When you clone the repo you will be asked to enter a Username and Password, to get this follow these steps:
  - Follow this link: https://dev.azure.com/benjaminbluhm/Training/_git/Training
  - Click on the `Clone` button in the top right 
  - Next click on `Generate Git Credentials` which will show you the Username and Password that you can use for Git authentication
  - Please reach out to `bbluhm.consulting@gmail.com` in case you are experiencing any troubles in the above step
- Create a new git branch (with a name of your choice - later you will Git commit and push you code changes using this branch) 
- Create three new empty Python files called `my_functions.py`, `my_pandas_operations.py` and `my_classes.py`

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
Add a new function called `transform` to `my_functions.py` that takes this dataframe as an input and returns 3 dataframes with the following result:

- `df1`: the square root of each element in `df`
- `df2`: the column sums of each column in `df`
- `df3`: the row sums of each row in `df`

# 3.)
Consider the following two example dataframes:

```Python
>>> df1 = pd.DataFrame({'a': ['fff', 'brr'], 'b': [10, 20]})
>>> df2 = pd.DataFrame({'a': ['fff', 'bzz'], 'c': [30, 40]})
>>> df1
      a  b
0   fff  10
1   brr  20
>>> df2
      a  c
0   fff  30
1   bzz  40
```

Add a Python statement to `my_pandas_operations.py` that joins the two dataframes on column `a` such that the resulting dataframe contains all records from `df1`, and the matching records from `df2`.

# 4.)

- Add a new class called `Transformer` to `my_classes.py` that takes a dataframe as an input argument
- Add `transform` function from Question 2.) as a new class method to `Transformer`
- Instantiate the class where you provide the example dataframe from Question 2.) as an input
- Call `transform` method on the instantiated class object

# 5.)

Add docstrings to your `Transformer` class following one of the standard Python docstring formats of your choice.

# 6.)

- Write a new class `ChildTransformer` in `my_classes.py` that inherets from `Transformer` class in Question 5.)
- Override `transform` so that it returns only one dataframe with the following result:
  - `df1`: the square root of each element in `df`
- Instantiate the `ChildTransformer` class where you provide the example dataframe from Question 2.) as an input
- Call `transform` method on the instantiated class object

# 7.)

Create a new markdown file `explanations.md` and briefly describe what your think are the main benefits of object oriented programming

# 8.)
Consider the following example code:

```Python
def Train(run_prediction: bool = True):

   from sklearn import datasets, linear_model

   # Load the diabetes dataset
   X_Train, y_Train = datasets.load_diabetes(return_X_y = True)

   # Create linear regression object
   regr = linear_model.LinearRegression()

   # Train the model
   regr.fit(X_Train,y_Train)

   if run_prediction == True:

      # Make predictions
      y_Pred = regr.predict(X_Train)
```

The above code violates some of Python's PEP8 Code Style Guide recommendations. Modify the code to make it more consistent with PEP8 style guide recommendations.   

# 9.)
- Git commit all your newly added code 
- Git push your code 

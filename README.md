# Introduction
Please try to address the following questions as much as possible, different solutions can lead to correct results. Feel free to use any resources from the internet (for example stackoverflow etc.) that may help you in answering the questions. 

The following questions assume that you have Python and Git installed on your system. If you do not have Git installed on your system you can download it for your operating system via this link: https://git-scm.com/downloads

# 1.)
- Clone the following repo into your local environment: https://benjaminbluhm@dev.azure.com/benjaminbluhm/Training/_git/Training 
- Create a new git branch (with a name of your choice), later you will Git commit and push you code changes using this branch 
- Create two new empty Python files called `my_functions.py` and `my_classes.py`

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

# 4.)

# 5.)

Add a new class called `Transformer` to `my_classes.py` that takes a dataframe as an input argument. Add `transform` function from Question 2.) as a new class method to `Transformer`. 

Instantiate the class and call the class method where you provide the example dataframe from Question 2.)

# 6.)

Add docstrings to your class following one of the standard Python docstring formats of your choice.

# 7.)

Write a new class `ChildTransformer` in `my_classes.py` that inherets from `Transformer` class in Question 5.). Override `transform` so that it returns 1 dataframe with the following result:

- `df1`: the square root of each element in `df`

Instantiate the `ChildTransformer` and call the class method where you provide the example dataframe from Question 2.)

# 8.)

Create a new markdown file `explanations.md` and describe what are in your view the main benefits of object oriented programming

# 9.)
Consider the following example function:

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

The above function violates some of Python's PEP8 Code Style Guide recommendations. Modify the code to be consistent with PEP8 style guide recommendations.   

# 10.)
- Git commit your code changes 
- Git push your code changes  

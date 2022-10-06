#%% Task 8

def Train(run_prediction: bool = True):
    """
    
    Parameters
    ----------
    run_prediction : bool, optional
        DESCRIPTION. The default is True.

    Returns
    -------
    Arry of float 64 for True and string for False
        run a regression if input is true and return value is "predicted values".
        Otherwise, print "Boolean Input Argument is False"

    """
    # we need docstring
    
    
    #error tracing
    try:
        from sklearn import datasets, linear_model
    except ImportError:
        print("Need to Chcek Library Argument")
    # 4 spaces indentation
    # Load the diabetes dataset
    X_Train, y_Train = datasets.load_diabetes(return_X_y = True)

    # Create linear regression object
    regr = linear_model.LinearRegression()

    # Train the model
    regr.fit(X_Train,y_Train)

    #if run_prediction == True: run_prediction is already boolean 
    if run_prediction: 
        
        # Make predictions
        y_Pred = regr.predict(X_Train)
        return y_Pred
    else:
        output = "Boolean Input Argument is False"
        return print(output)
     # we need a return arg in this case for True and False in the input arg


d1 = Train(True)
d1
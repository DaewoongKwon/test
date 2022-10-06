#%% Task 2
import pandas as pd
import numpy as np

#%%
df = pd.DataFrame([[9, 16]] * 3, columns=['A', 'B'])
def transform (df):
    """

    Parameters
    ----------
    df : Dataframe
        Input Argument.

    Returns
    -------
    df1 : Dataframe
        square root of each element in original data frame.
    df2 : Dataframe
        column-wise sum of original data frame.
    df3 : Dataframe
        row-wise sum of original dataframe.

    """
    df1 = np.sqrt(df)
    df2 = df.sum()
    df2 = df2.to_frame()
    df2 = df2.T
    df3 = df.sum(axis=1)
    df3 = df3.to_frame()
    return df1,df2,df3

df1,df2,df3 = transform (df)
import pandas as pd
import numpy as np
df = pd.DataFrame([[9, 16]] * 3, columns=['A', 'B'])

#%% Task 4 & 5
class Transformer:
    """ Class Transformer transforms dataframe into square root, column-wise, and row-wise sum of the original.
    """

    def __init__(self, dataframe):
        self.dataframe = dataframe
    
    def transform (self):
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
        df1 = np.sqrt(self.dataframe)
        df2 = self.dataframe.sum()
        df2 = df2.to_frame()
        df2 = df2.T
        df3 = self.dataframe.sum(axis=1)
        df3 = df3.to_frame()
        self.dataframe = [df1,df2,df3]
        return self.dataframe

df_test = Transformer(df)
print(df_test.__doc__)
df_get = df_test.transform()
df_get

#%% Task 6

class ChildTransformer(Transformer):
    """ Creats Child Class for Transformer
    """
    
    
    def __init__(self, dataframe):
        super().__init__(dataframe)
        
        
    def override_transform(self, index):
        """
        

        Parameters
        ----------
        index : Int
            give index argument to get a certain data frame.

        Returns
        -------
        newdf : Dataframe
            Choose data frame given the index argument.

        """
        self.index=index
        newdf =self.dataframe[self.index]
         
        return newdf

df_test1 = ChildTransformer(df)
df_test1.transform()
index=0
df_get1=df_test1.override_transform(index)
df_get1
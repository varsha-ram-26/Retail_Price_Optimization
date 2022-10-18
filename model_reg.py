import pandas as pd
import numpy as np
import statsmodels.api as sm

def model_building(df,indep_cols,dep_cols,index):
    df.index = df[index]
    X = df[indep_cols]
    y = df[dep_cols]
    X = sm.add_constant(X)
    result = sm.OLS(y, X).fit()
    return result
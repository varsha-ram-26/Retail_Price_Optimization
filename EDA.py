import pandas as pd
import numpy as np
import datetime as dt

def columns(df,cols_to_use):
    df_new = df[cols_to_use]
    return df_new

def Preprocessing(df):
    df_new = df.copy()
    # df_new['total_freight_price'] = df_new['total_price'] + df_new['freight_price']
    df_new['month_year'] = pd.to_datetime(df_new['month_year'])
    df_new['Day_Of_Week'] = df_new['month_year'].dt.dayofweek
    df_new['IsWeekend'] = np.where(df_new['Day_Of_Week']>=5,1,0)
    return df_new

def sales_info(data,by):
    data_grouped = data.groupby(by).agg({'qty':'sum','total_price':'sum','freight_price':'sum'}).reset_index()
    return data_grouped
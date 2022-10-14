import pandas as pd
import numpy as np

def EDA(df,cols,by):
    df_new = df[cols]
    df_new['total_freight_price'] = df_new['total_price'] + df_new['freight_price']
    how = by
    df_sales = sales_info(df_new,how)
    return df_sales

def sales_info(data,by):
    if(by=='category'):
        data_grouped = data.groupby('product_category_name').agg({'qty':'sum','total_price':'sum','freight_price':'sum','total_freight_price':'sum'}).reset_index()
    if(by=='product_code'):
        data_grouped = data.groupby('product_id').agg({'qty':'sum','total_price':'sum','freight_price':'sum','total_freight_price':'sum'}).reset_index()
    if(by=='time'):
        data['month_year'] = pd.to_datetime(data['month_year'])
        data_grouped = data.groupby('month_year').agg({'qty':'sum','total_price':'sum','freight_price':'sum','total_freight_price':'sum'}).reset_index()
    return data_grouped
from fileinput import filename
import pandas as pd
import numpy as np
import read_data
import model_reg
import os
import EDA
# print(os.getcwd())

# Import Dataframe
file = read_data.import_data()

# Preprocessing Data
df = EDA.Preprocessing(file)

# Filtering columns to use
cols_to_use = ['product_id', 'product_category_name','month_year','qty','total_price', 'freight_price', 'unit_price','product_name_length',
       'product_description_length', 'product_photos_qty', 'product_weight_g','product_score', 'customers','seasonality','IsWeekend',
       'holiday']
df_v1 = EDA.columns(df, cols_to_use)

# Sales by Column
print(cols_to_use)
group_by = 'product_id'
# group_by = input('Sales by Category / Time: ')
eda = EDA.sales_info(df_v1,group_by)

# Model
indep_cols = ['qty', 'freight_price', 'unit_price','product_name_length',
       'product_description_length', 'product_photos_qty', 'product_weight_g','product_score', 'customers','seasonality','IsWeekend',
       'holiday']
dep_cols = ['total_price']
index = ['product_id', 'product_category_name','month_year']
model_result = model_reg.model_building(df_v1, indep_cols, dep_cols, index)

print("hello")

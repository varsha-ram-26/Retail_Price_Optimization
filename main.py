from fileinput import filename
import pandas as pd
import numpy as np
import read_data
import os
import EDA
# print(os.getcwd())


file = read_data.import_data()

cols_to_use = ['product_id', 'product_category_name','month_year','qty','total_price', 'freight_price', 'unit_price','product_name_length',
       'product_description_length', 'product_photos_qty', 'product_weight_g','product_score', 'customers','volume']
group_by = 'category'
final_EDA = EDA.EDA(file, cols_to_use, by=group_by)
print("hello")
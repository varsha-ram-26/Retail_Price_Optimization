import pandas as pd

def import_data():
    main_df = pd.read_csv("Retail_Price_Data.csv")
    return main_df
import pandas as pd

df = pd.read_csv ('base_val.csv', header = None, names =["Base_val"], index_col = 0)
print(df)

deck = {}
deck["Apple"] = (1, df.loc["Apple", "Base_val"])

if(len(deck) < 20):
    deck["Empty"] = (20 - len(deck), df.loc["Empty", "Base_val"])

    
print(deck)